#!/usr/bin/env python3
"""Ask before destructive shell actions and deny catastrophic recursive deletes."""

from __future__ import annotations

import json
import re
import shlex
import sys
from pathlib import PurePath


def decision(kind: str, reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": kind,
                    "permissionDecisionReason": reason,
                }
            },
            ensure_ascii=False,
        )
    )


try:
    payload = json.load(sys.stdin)
except (json.JSONDecodeError, OSError):
    raise SystemExit(0)

command = str(payload.get("tool_input", {}).get("command", ""))
if not command:
    raise SystemExit(0)

try:
    command_tokens = shlex.split(re.sub(r"(?:&&|\|\||[;|&])", " ", command))
except ValueError:
    command_tokens = command.split()

for token in command_tokens:
    candidate = token.strip("'\",:()[]{}")
    if not candidate or candidate.startswith("-"):
        continue
    path = PurePath(candidate)
    name = path.name.lower()
    safe_env = name.endswith((".example", ".sample", ".template"))
    is_env = (name == ".env" or name.startswith(".env.")) and not safe_env
    is_private_key = name.endswith(".pem") or name.startswith("id_rsa")
    is_secret_dir = "secrets" in {part.lower() for part in path.parts}
    if is_env or is_private_key or is_secret_dir:
        decision("deny", f"已擋下透過 Bash 讀取敏感路徑 {candidate}。請使用明確不含真實秘密的範例檔。")
        raise SystemExit(0)

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
    targets = [arg for arg in args if not arg.startswith("-")]
    catastrophic_targets = {
        "/",
        "/*",
        "~",
        "~/",
        "~/*",
        "$HOME",
        "${HOME}",
        "$HOME/",
        "${HOME}/",
        ".",
        "./",
        "./*",
        "..",
        "../",
        "../*",
        "$CLAUDE_PROJECT_DIR",
        "${CLAUDE_PROJECT_DIR}",
    }
    if any(target in catastrophic_targets for target in targets):
        decision("deny", "已擋下可能刪除系統、家目錄或整個工作區的遞迴強制刪除。請改成明確且狹窄的目標。")
        raise SystemExit(0)

ask_patterns = (
    (r"\bgit\s+(?:reset\s+--hard|clean\s+-[a-zA-Z]*f|checkout\s+--|restore\b)", "這個 Git 指令可能丟棄未提交變更。"),
    (r"\bgit\s+push\b[^\n;&|]*(?:--force(?:-with-lease)?|-f)\b", "force push 會改寫遠端歷史。"),
    (r"\bgit\s+(?:stash\s+(?:drop|clear)|branch\s+-D)\b", "這個 Git 指令會刪除可復原資訊。"),
    (r"\b(?:DROP\s+(?:DATABASE|TABLE)|TRUNCATE\s+TABLE)\b", "這個資料庫操作具有破壞性。"),
)

if recursive_delete:
    decision("ask", "遞迴強制刪除會讓資料難以復原。請確認精確目標與復原方式後再執行。")
    raise SystemExit(0)

for pattern, reason in ask_patterns:
    if re.search(pattern, command, flags=re.IGNORECASE):
        decision("ask", f"{reason} 請確認目標、影響範圍與復原方式後再執行。")
        break
