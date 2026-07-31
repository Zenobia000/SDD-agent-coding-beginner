#!/usr/bin/env bash
# Stop — 這一輪結束時，如果動了 code 卻沒跑驗證，提醒一次。
#
# 這是「收尾」型 hook。它示範 Stop 事件最有價值的用法：
# 不是阻擋，是在人準備離開時補上一句「你漏了什麼」。
#
# 刻意的設計取捨：
#   - 每個 session 只提醒一次（用旗標檔），避免變成噪音
#   - 只在「有未 commit 的程式碼改動」時才提醒，純文件改動不管
#   - 用 additionalContext 而不是 decision:"block"，讓 Claude 自己決定要不要講
#
# 契約（見 docs/authoring/04-write-a-hook.md）：
#   stdin  : JSON，含 .session_id、.last_assistant_message
#   exit 0 + additionalContext : 把提醒餵給 Claude
set -uo pipefail

INPUT=$(cat)
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-.}"
SID=$(printf '%s' "$INPUT" | jq -r '.session_id // "unknown"')
FLAG="$PROJECT_DIR/.claude/.verify-reminded-$SID"

# 這個 session 已經提醒過就閉嘴
[ -f "$FLAG" ] && exit 0

# 沒有未提交的程式碼改動就不用管
command -v git >/dev/null 2>&1 || exit 0
CHANGED=$(git -C "$PROJECT_DIR" status --porcelain 2>/dev/null \
  | grep -Ev '\.(md|txt)$' \
  | grep -Ev '^\?\? \.claude/\.' \
  | wc -l | tr -d ' ')
[ "${CHANGED:-0}" -eq 0 ] && exit 0

touch "$FLAG" 2>/dev/null || true

jq -n --arg n "$CHANGED" '{
  hookSpecificOutput: {
    hookEventName: "Stop",
    additionalContext: ("目前有 " + $n + " 個未提交的程式碼改動，這個 session 還沒跑過 /verify。若這一輪已經改完，提醒使用者：下一步跑 /verify（五維度驗證），過了才 commit。若還在中途，忽略這則提醒。")
  }
}'
exit 0
