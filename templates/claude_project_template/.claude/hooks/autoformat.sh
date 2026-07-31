#!/usr/bin/env bash
# PostToolUse(Write|Edit) — 檔案寫完後自動跑格式化。
#
# 這是「自動化」型 hook：把「每次都要記得跑」的雜事從人腦搬到系統。
# 靜默執行，不干擾對話；formatter 沒裝就跳過，不報錯。
#
# 為什麼是 PostToolUse 不是 Stop：
#   在每次寫檔後立刻格式化，diff 才會乾淨。等到 Stop 才跑，
#   中間 Claude 讀回來的是未格式化的內容，可能造成無謂的來回修改。
#
# 契約（見 docs/authoring/04-write-a-hook.md）：
#   stdin  : JSON，含 .tool_input.file_path
#   exit 0 : 靜默通過
set -uo pipefail

INPUT=$(cat)
FILE=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty')
[ -z "$FILE" ] || [ ! -f "$FILE" ] && exit 0

have() { command -v "$1" >/dev/null 2>&1; }

case "$FILE" in
  *.py)
    have ruff   && ruff format "$FILE" >/dev/null 2>&1
    have ruff   && ruff check --fix "$FILE" >/dev/null 2>&1
    ;;
  *.js|*.jsx|*.ts|*.tsx|*.json|*.css|*.scss|*.html|*.md|*.yml|*.yaml)
    if have prettier; then
      prettier --write "$FILE" >/dev/null 2>&1
    elif have npx && [ -f "${CLAUDE_PROJECT_DIR:-.}/package.json" ]; then
      npx --no-install prettier --write "$FILE" >/dev/null 2>&1
    fi
    ;;
  *.go)
    have gofmt  && gofmt -w "$FILE" >/dev/null 2>&1
    ;;
  *.rs)
    have rustfmt && rustfmt "$FILE" >/dev/null 2>&1
    ;;
  *.sh)
    have shfmt  && shfmt -w "$FILE" >/dev/null 2>&1
    ;;
esac

exit 0
