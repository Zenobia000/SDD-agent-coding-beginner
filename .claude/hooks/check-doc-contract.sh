#!/usr/bin/env bash
# PostToolUse(Write|Edit) — 寫入站別教材後，核對七段骨架是否齊全。
#
# 這是「回饋迴圈」型 hook：不阻擋，只把缺漏回灌給 Claude 讓它自己補。
# 對照 rules/00-doc-contract.md §2。
#
# 契約（見 docs/authoring/04-write-a-hook.md）：
#   stdin  : JSON，含 .tool_input.file_path
#   exit 0 + additionalContext : 把訊息餵給 Claude
set -uo pipefail

INPUT=$(cat)
FILE=$(printf '%s' "$INPUT" | jq -r '.tool_input.file_path // empty')
[ -z "$FILE" ] && exit 0

# 只管站別教材
case "$FILE" in
  *curriculum/S[0-9]*.md) ;;
  *) exit 0 ;;
esac
[ -f "$FILE" ] || exit 0

REQUIRED=("## 結論卡" "## 課堂 15 分鐘版" "## 動手" "## 閘門" "## 我做對了嗎" "## 回家展開版" "## 下一步")
MISSING=()
for section in "${REQUIRED[@]}"; do
  grep -qF "$section" "$FILE" || MISSING+=("$section")
done

# 閘門條目數檢查（≤ 5 條）
GATE_ITEMS=$(awk '/^## 閘門/{f=1;next} /^## /{f=0} f && /^- \[ \]/{c++} END{print c+0}' "$FILE")

NOTES=""
[ ${#MISSING[@]} -gt 0 ] && NOTES="缺少段落：${MISSING[*]}。"
[ "$GATE_ITEMS" -gt 5 ] && NOTES="${NOTES}閘門有 ${GATE_ITEMS} 條，規約上限 5 條（rules/00-doc-contract.md §2）。"

[ -z "$NOTES" ] && exit 0

jq -n --arg ctx "教材規約檢查 — $FILE：$NOTES 請依 .claude/rules/00-doc-contract.md 補齊後再繼續。" '{
  hookSpecificOutput: {
    hookEventName: "PostToolUse",
    additionalContext: $ctx
  }
}'
exit 0
