#!/usr/bin/env python3
"""Antigravity PreToolUse guard：單一進入點，依 `toolCall.name` 分流。

協定（來源：Antigravity 內建規格 `agy-customizations/docs/hooks.md`）：

- stdin 是一個 JSON 物件，key 是 camelCase：
  `toolCall.name`、`toolCall.args`、`stepIdx`、`conversationId`、`workspacePaths`。
- stdout 必須是 JSON。有意見時輸出 `{"decision": ..., "reason": ...}`，
  `decision` 的合法值有五個：`allow` / `deny` / `ask` / `force_ask` /
  `deny_unless_prior_grant`（binary schema tag 實證；內建規格漏列第五個）。
  本檔只用 `deny` 與 `ask`。
- working directory 是 `hooks.json` 所在目錄（本 repo 是 `.agents/`），
  所以 `hooks.json` 裡寫 `python3 ./hooks/guard.py`。

**沒有意見時輸出 `{}`，不是 `{"decision":"allow"}`。**
⚠️ 官方規格把 `decision` 列為 required，並未載明省略時的行為；「`{}` = 不表態」
是本 repo 的設計選擇與合理推論，尚未端到端實測。選它的理由是失敗方向較安全：
`allow` 會直接蓋過使用者的 permission 設定，等於把整個授權機制關掉。

本檔只負責協定翻譯，實際判斷全在 `guard_core.py`。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

# hook 的 working directory 是 `.agents/`，不是這支腳本所在的 `.agents/hooks/`。
# 一般情況 Python 會自動把腳本目錄放進 sys.path，但 `PYTHONSAFEPATH` 一開就不會，
# guard 會靜默失效。明確補上，讓它在哪種環境都 import 得到。
sys.path.insert(0, str(Path(__file__).resolve().parent))

import guard_core  # noqa: E402  # 必須在 sys.path 補完之後

# binary 1.1.12 實測的 tool 名稱。`hooks.json` 的 matcher 也要跟這兩組一致。
SHELL_TOOLS = {"run_command", "shell_exec", "send_command_input"}
WRITE_TOOLS = {"file_change", "write_blob", "edit_notebook"}
DELETE_TOOLS = {"delete_directory"}

# args 的欄位名取自 binary 的 proto struct（`CortexStepRunCommand.CommandLine` 等）。
# 官方文件只明載 `run_command` 的 `CommandLine`，其餘是從 binary 推得，
# 所以一律走「不分大小寫 + 多個候選鍵」的容錯查找，欄位名改了也還擋得住。
SHELL_KEYS = ("commandline", "command", "input")
PATH_KEYS = (
    "absolutepathuri",
    "absolutepath",
    "targetpath",
    "directorypathuri",
    "directorypath",
    "filepath",
    "file_path",
    "path",
    "uri",
)

# 憑證掃描要略過的鍵：這些是「被改掉之前的舊內容」。
# 把它們納入掃描，會讓「刪掉已經外洩的金鑰」這個修補動作反而被擋。
IGNORED_BODY_KEYS = {
    "targetcontent",
    "oldstring",
    "old_string",
    "diff",
    "contextlines",
    "targethascarriagereturn",
}


def emit(decision: str, reason: str = "") -> None:
    """有意見才寫 decision；沒有意見輸出空物件。"""
    payload: dict[str, str] = {}
    if decision:
        payload["decision"] = decision
        if reason:
            payload["reason"] = reason
    sys.stdout.write(json.dumps(payload, ensure_ascii=False))


def to_local_path(value: str) -> str:
    """`file:///a/b` → `/a/b`；本來就是路徑就原樣回傳。"""
    if not value.startswith("file://"):
        return value
    parsed = urlparse(value)
    return unquote(parsed.path) or value


def lookup(args: dict[str, Any], keys: tuple[str, ...]) -> str:
    """不分大小寫地找第一個非空字串值。"""
    normalized = {str(key).lower(): value for key, value in args.items()}
    for key in keys:
        value = normalized.get(key)
        if isinstance(value, str) and value.strip():
            return value
    return ""


def collect_text(node: Any, skip: set[str]) -> list[str]:
    """把 args 樹裡所有字串葉節點收出來，跳過 `skip` 裡的鍵。

    用整棵樹而不是固定幾個欄位，是因為 `edit_notebook` 這類 tool 的
    args 形狀官方沒有載明；寧可多掃，也不要因為欄位名沒對上就漏掉憑證。
    """
    if isinstance(node, str):
        return [node]
    if isinstance(node, list):
        return [text for item in node for text in collect_text(item, skip)]
    if isinstance(node, dict):
        return [
            text
            for key, value in node.items()
            if str(key).lower() not in skip
            for text in collect_text(value, skip)
        ]
    return []


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        emit("")  # 讀不懂就不表態，不要因為 guard 自己壞掉而卡住 agent
        return 0

    if not isinstance(payload, dict):
        emit("")
        return 0

    tool_call = payload.get("toolCall") or {}
    name = str(tool_call.get("name", ""))
    args = tool_call.get("args") or {}
    if not isinstance(args, dict):
        args = {}

    roots = [
        to_local_path(str(item))
        for item in (payload.get("workspacePaths") or [])
        if isinstance(item, str)
    ]

    if name in SHELL_TOOLS:
        decision, reason = guard_core.evaluate_shell(lookup(args, SHELL_KEYS), roots)
    elif name in DELETE_TOOLS:
        decision, reason = guard_core.evaluate_delete(
            to_local_path(lookup(args, PATH_KEYS)),
            force=bool(args.get("Force") or args.get("force")),
            workspace_roots=roots,
        )
    elif name in WRITE_TOOLS:
        path = to_local_path(lookup(args, PATH_KEYS))
        skip = IGNORED_BODY_KEYS | set(PATH_KEYS)
        decision, reason = guard_core.evaluate_write(path, "\n".join(collect_text(args, skip)))
    else:
        decision, reason = guard_core.NO_OPINION

    emit(decision, reason)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
