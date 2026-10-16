#!/usr/bin/env bash
# 確認 Codex 看得到同一套技能，而且「誰能叫」的設定跟 Claude Code 一致。
#
# Codex 從工作目錄往上掃到 repo 根的 .agents/skills/，並跟隨 symlink。
# 本 repo 用 .agents/skills → ../.claude/skills 讓兩邊共用一份技能。
#
# Codex 不認 SKILL.md 的 disable-model-invocation。它的對應設定是
# <技能>/agents/openai.yaml 裡的 policy.allow_implicit_invocation: false。
# 兩邊不同步時不會噴錯 —— 只會讓編排型技能在 Codex 被 agent 自己啟動 ——
# 所以由這支擋。
#
# 無輸出 = 全部一致。有輸出時 exit 1。

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

SKILLS_DIR=${SKILLS_DIR:-.claude/skills}
LINK=${CODEX_LINK:-.agents/skills}

found=0

if [ ! -L "$LINK" ]; then
  echo "$LINK 不是 symlink（Windows 請開啟 git config core.symlinks true 後重新 checkout）"
  found=1
elif [ "$(cd "$LINK" 2>/dev/null && pwd -P)" != "$(cd "$SKILLS_DIR" && pwd -P)" ]; then
  echo "$LINK 沒有指向 $SKILLS_DIR"
  found=1
fi

for skill in "$SKILLS_DIR"/*/SKILL.md; do
  dir=$(dirname "$skill")
  name=$(basename "$dir")
  yaml="$dir/agents/openai.yaml"
  user_only=0
  grep -q '^disable-model-invocation: true' "$skill" && user_only=1
  codex_off=0
  [ -f "$yaml" ] && grep -qE '^[[:space:]]+allow_implicit_invocation:[[:space:]]*false' "$yaml" && codex_off=1

  if [ $user_only -eq 1 ] && [ $codex_off -eq 0 ]; then
    echo "不同步  $name：Claude Code 只准使用者觸發，Codex 卻允許 agent 自己啟動（缺 $yaml）"
    found=1
  elif [ $user_only -eq 0 ] && [ $codex_off -eq 1 ]; then
    echo "不同步  $name：Codex 關掉了自動觸發，Claude Code 卻允許"
    found=1
  fi
done

exit $found
