#!/usr/bin/env bash
# PreToolUse(Bash) — 擋下不可逆的破壞性指令。
#
# 為什麼要用 hook 而不是寫進 CLAUDE.md：
#   寫進 CLAUDE.md 的規則大約有 ~70% 順從率。真正不可逆的操作不能賭那 30%。
#   hook 對人和 agent 一律生效，是「機械層」。
#
# 契約（見 docs/authoring/04-write-a-hook.md）：
#   stdin  : JSON，含 .tool_input.command
#   exit 0 : 放行（無輸出）或輸出 permissionDecision JSON
#   exit 2 : 阻擋，stderr 內容會回饋給 Claude
set -uo pipefail

INPUT=$(cat)
CMD=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')
[ -z "$CMD" ] && exit 0

deny() {
  jq -n --arg reason "$1" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: $reason
    }
  }'
  exit 0
}

# ① 遞迴刪除
if printf '%s' "$CMD" | grep -Eq '\brm\b[^|;&]*-[a-zA-Z]*[rR][a-zA-Z]*f|\brm\b[^|;&]*-[a-zA-Z]*f[a-zA-Z]*[rR]'; then
  deny "已擋下遞迴強制刪除。要刪請逐一指名檔案，或先讓使用者確認。"
fi

# ② 對保護分支 force push
if printf '%s' "$CMD" | grep -Eq 'git[^|;&]*push[^|;&]*(--force|--force-with-lease|-f)\b'; then
  deny "已擋下 force push。歷史重寫是不可逆操作，需要使用者明確同意。"
fi

# ③ 硬重置 / 清空工作區
if printf '%s' "$CMD" | grep -Eq 'git[^|;&]*reset[^|;&]*--hard|git[^|;&]*clean[^|;&]*-[a-zA-Z]*f'; then
  deny "已擋下 git reset --hard / git clean -f。這會丟掉未提交的修改。"
fi

# ④ 直接 commit 到保護分支
BRANCH=$(git -C "${CLAUDE_PROJECT_DIR:-.}" branch --show-current 2>/dev/null || echo "")
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
  if printf '%s' "$CMD" | grep -Eq 'git[^|;&]*commit\b'; then
    deny "目前在保護分支 $BRANCH。請先開分支：git checkout -b <type>/<描述>"
  fi
fi

exit 0
