#!/usr/bin/env python3
"""風險判定核心：只回答「該不該擋」，不知道自己跑在哪個 agent 上。

這一層刻意**不含任何輸出格式**。它回傳工具中立的 `(decision, reason)`，
由 `guard.py` 負責翻成 Antigravity 的 hook 協定。
分層的理由：hook 協定的欄位名會隨 host 改變，
但「什麼叫不可逆操作」不會變。

`decision` 只有三種可能：
- `"deny"`  —— 硬擋，不給使用者放行的機會
- `"ask"`   —— 交回使用者確認
- `""`      —— 沒有意見，交回上層原本的 permission 流程（**不是 allow**）
"""

from __future__ import annotations

import re
import shlex
from pathlib import PurePath
from typing import Iterable, Sequence

NO_OPINION: tuple[str, str] = ("", "")

# 這些直譯器會把 heredoc 內容當指令執行，內容照樣要掃。
SHELL_INTERPRETERS = {"bash", "sh", "zsh", "ksh", "dash", "eval", "source"}

# 不帶路徑資訊的字面目標。展開成絕對路徑的 workspace root 由呼叫端另外餵進來。
BASE_CATASTROPHIC_TARGETS = frozenset(
    {
        "/",
        "/*",
        "~",
        "~/",
        "~/*",
        "$HOME",
        "${HOME}",
        "$HOME/",
        "${HOME}/",
        "$PWD",
        "${PWD}",
        "$PWD/",
        "${PWD}/",
        "$PWD/*",
        ".",
        "./",
        "./*",
        "..",
        "../",
        "../*",
    }
)

SAFE_ENV_SUFFIXES = (".example", ".sample", ".template")

SECRET_PATTERNS = (
    r"sk-[A-Za-z0-9_-]{20,}",
    r"sk-ant-[A-Za-z0-9_-]{20,}",
    r"ghp_[A-Za-z0-9]{30,}",
    r"AIza[A-Za-z0-9_-]{30,}",
    r"AKIA[A-Z0-9]{16}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
)

ASK_PATTERNS = (
    (
        r"\bgit\s+(?:reset\s+--hard|clean\s+-[a-zA-Z]*f|checkout\s+--|restore\b)",
        "這個 Git 指令可能丟棄未提交變更。",
    ),
    (r"\bgit\s+push\b[^\n;&|]*(?:--force(?:-with-lease)?|-f)\b", "force push 會改寫遠端歷史。"),
    (r"\bgit\s+(?:stash\s+(?:drop|clear)|branch\s+-D)\b", "這個 Git 指令會刪除可復原資訊。"),
    (r"\b(?:DROP\s+(?:DATABASE|TABLE)|TRUNCATE\s+TABLE)\b", "這個資料庫操作具有破壞性。"),
)


def is_sensitive_path(candidate: str) -> bool:
    """`.env`、私鑰、`secrets/` 底下的任何東西都算敏感。範例檔不算。"""
    path = PurePath(candidate)
    name = path.name.lower()
    if name.endswith(SAFE_ENV_SUFFIXES):
        return False
    is_env = name == ".env" or name.startswith(".env.")
    is_private_key = name.endswith(".pem") or name.startswith("id_rsa")
    is_secret_dir = "secrets" in {part.lower() for part in path.parts}
    return is_env or is_private_key or is_secret_dir


def contains_credential(text: str) -> bool:
    return bool(text) and any(re.search(pattern, text) for pattern in SECRET_PATTERNS)


def catastrophic_targets(workspace_roots: Sequence[str] = ()) -> frozenset[str]:
    """字面 catastrophic 目標 + 每個 workspace root 的三種寫法。

    Antigravity 的 hook stdin 直接帶 `workspacePaths`，沒有等價的
    「專案根目錄」環境變數，所以這裡改由呼叫端把已展開的絕對路徑餵進來。
    """
    extra: set[str] = set()
    for root in workspace_roots:
        trimmed = root.rstrip("/")
        if not trimmed:
            continue
        extra.update({trimmed, trimmed + "/", trimmed + "/*"})
    return BASE_CATASTROPHIC_TARGETS | frozenset(extra)


def strip_heredoc_bodies(text: str) -> str:
    """移除 heredoc 內容。那是餵給程式的資料，不是這條指令要碰的路徑。

    沒有這一步，`git commit -F - <<'MSG'` 的訊息裡只要提到敏感檔名，
    整條指令就會被誤判成存取。
    """
    lines = text.split("\n")
    kept: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        kept.append(line)
        index += 1

        marker = re.search(r"<<-?\s*(['\"]?)(?P<tag>[A-Za-z_][A-Za-z0-9_]*)\1", line)
        if not marker:
            continue
        try:
            leading = shlex.split(line)[0] if line.strip() else ""
        except ValueError:
            leading = line.split()[0] if line.split() else ""
        if PurePath(leading).name in SHELL_INTERPRETERS:
            continue

        tag = marker.group("tag")
        while index < len(lines) and lines[index].strip() != tag:
            index += 1
        index += 1  # 跳過結束標記
    return "\n".join(kept)


def _path_like_tokens(command: str) -> Iterable[str]:
    """把指令拆成「看起來像路徑」的 token，跳過 git 的訊息參數。

    git 的訊息參數是文字不是路徑：commit message 提到 .env 或私鑰不算存取。
    只在 git 的訊息型子指令生效，才不會放過 `grep -m`、`sort -m` 之類的檔案參數。
    """
    scannable = strip_heredoc_bodies(command)
    try:
        tokens = shlex.split(re.sub(r"(?:&&|\|\||[;|&])", " ", scannable))
    except ValueError:
        tokens = scannable.split()

    writes_message = re.search(
        r"\bgit\s+(?:commit|tag|merge|revert|cherry-pick|stash\s+push)\b", command
    )
    skip_next = False
    for token in tokens:
        if skip_next:
            skip_next = False
            continue
        if writes_message and (token == "--message" or re.fullmatch(r"-[A-Za-z]*m", token)):
            skip_next = True
            continue
        candidate = token.strip("'\",:()[]{}")
        if not candidate or candidate.startswith("-"):
            continue
        yield candidate


def evaluate_shell(command: str, workspace_roots: Sequence[str] = ()) -> tuple[str, str]:
    """判定一條 shell 指令。空指令一律沒有意見。"""
    if not command.strip():
        return NO_OPINION

    for candidate in _path_like_tokens(command):
        if is_sensitive_path(candidate):
            return (
                "deny",
                f"已擋下透過 shell 存取敏感路徑 {candidate}。請使用明確不含真實秘密的範例檔。",
            )

    fatal = catastrophic_targets(workspace_roots)
    recursive_delete = False
    for rm_match in re.finditer(r"\brm\b(?P<args>[^\n;&|]*)", command):
        try:
            args = shlex.split(rm_match.group("args"))
        except ValueError:
            args = rm_match.group("args").split()

        short_flags = "".join(arg[1:] for arg in args if re.fullmatch(r"-[A-Za-z]+", arg))
        is_recursive = "r" in short_flags.lower() or "--recursive" in args
        is_forced = "f" in short_flags.lower() or "--force" in args
        if not (is_recursive and is_forced):
            continue

        recursive_delete = True
        if any(arg in fatal for arg in args if not arg.startswith("-")):
            return (
                "deny",
                "已擋下可能刪除系統、家目錄或整個工作區的遞迴強制刪除。請改成明確且狹窄的目標。",
            )

    if recursive_delete:
        return ("ask", "遞迴強制刪除會讓資料難以復原。請確認精確目標與復原方式後再執行。")

    for pattern, reason in ASK_PATTERNS:
        if re.search(pattern, command, flags=re.IGNORECASE):
            return ("ask", f"{reason} 請確認目標、影響範圍與復原方式後再執行。")

    return NO_OPINION


def evaluate_write(file_path: str, body: str) -> tuple[str, str]:
    """判定一次檔案寫入。路徑與內容各擋一半。"""
    name = PurePath(file_path).name.lower() if file_path else ""
    safe_env = name.endswith(SAFE_ENV_SUFFIXES)

    if file_path and (name == ".env" or name.startswith(".env.")) and not safe_env:
        return (
            "deny",
            f"已擋下寫入 {file_path}。請改寫明確使用假值的 .env.example，真實值由使用者在本機注入。",
        )

    # 與 shell 分支同一組判斷：讀不到的路徑也不該寫得進去。
    if file_path and is_sensitive_path(file_path):
        return (
            "deny",
            f"已擋下寫入敏感路徑 {file_path}。私鑰與 secrets/ 不進版控；"
            "請改用明確假值的範例檔，真實金鑰由使用者在本機注入。",
        )

    if contains_credential(body):
        return (
            "deny",
            "偵測到疑似真實憑證或私鑰。請改用環境變數或 secret manager，範例檔只能放明確假值。",
        )

    return NO_OPINION


def evaluate_delete(
    directory_path: str, force: bool = False, workspace_roots: Sequence[str] = ()
) -> tuple[str, str]:
    """判定一次目錄刪除。

    `delete_directory` 本質上就是遞迴刪除，而且不像 `rm -r` 會停下來問，
    所以基準線是 `ask`；碰到 workspace root 或敏感目錄才升級成 `deny`。
    """
    if not directory_path.strip():
        return NO_OPINION

    if directory_path.rstrip("/") in {t.rstrip("/") for t in catastrophic_targets(workspace_roots)}:
        return ("deny", f"已擋下刪除 {directory_path}。這會清掉整個工作區或家目錄，請改成明確且狹窄的目標。")

    if is_sensitive_path(directory_path):
        return ("deny", f"已擋下刪除敏感路徑 {directory_path}。請由使用者自行在本機處理秘密檔案。")

    scope = "強制刪除" if force else "刪除"
    return ("ask", f"目錄{scope}難以復原。請確認 {directory_path} 是正確目標，並確認復原方式後再執行。")
