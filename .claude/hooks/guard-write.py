#!/usr/bin/env python3
"""Block writes to secret files and obvious embedded credentials."""

from __future__ import annotations

import json
import re
import sys
from pathlib import PurePath


def deny(reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
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

tool_input = payload.get("tool_input", {})
file_path = str(tool_input.get("file_path", ""))
body = "\n".join(
    str(value)
    for value in (tool_input.get("content"), tool_input.get("new_string"))
    if value is not None
)

path = PurePath(file_path)
name = path.name.lower() if file_path else ""
safe_env_suffixes = (".example", ".sample", ".template")
safe_env = name.endswith(safe_env_suffixes)
if (name == ".env" or name.startswith(".env.")) and not safe_env:
    deny(f"已擋下寫入 {file_path}。請改寫明確使用假值的 .env.example，真實值由使用者在本機注入。")
    raise SystemExit(0)

# 與 guard-bash.py 同一組判斷：讀不到的路徑也不該寫得進去。
is_private_key = name.endswith(".pem") or name.startswith("id_rsa")
is_secret_dir = "secrets" in {part.lower() for part in path.parts}
if is_private_key or is_secret_dir:
    deny(f"已擋下寫入敏感路徑 {file_path}。私鑰與 secrets/ 不進版控；請改用明確假值的範例檔，真實金鑰由使用者在本機注入。")
    raise SystemExit(0)

secret_patterns = (
    r"sk-[A-Za-z0-9_-]{20,}",
    r"sk-ant-[A-Za-z0-9_-]{20,}",
    r"ghp_[A-Za-z0-9]{30,}",
    r"AIza[A-Za-z0-9_-]{30,}",
    r"AKIA[A-Z0-9]{16}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
)
if body and any(re.search(pattern, body) for pattern in secret_patterns):
    deny("偵測到疑似真實憑證或私鑰。請改用環境變數或 secret manager，範例檔只能放明確假值。")
