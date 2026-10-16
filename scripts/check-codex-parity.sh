#!/usr/bin/env bash
# Claude Code 的專案能力在 .claude/。Codex 不讀 settings.json，也不讀 output-styles。
# 這支檢查兩邊有沒有接上：
#   1. settings.json 裡的兩支 Bash guard，hooks.json 也登記了，腳本檔還在。
#   2. 兩個輸出風格各有一支使用者觸發技能，指向原本那份 markdown。
#
# 無輸出 = 接上了。有輸出時 exit 1。

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

found=0

python3 -c 'import json; json.load(open(".codex/hooks.json"))' 2>/dev/null || {
  echo ".codex/hooks.json 不是合法 JSON"
  found=1
}

for s in guard-git.sh guard-secrets.sh; do
  [ -f ".claude/hooks/$s" ] || { echo "缺腳本  .claude/hooks/$s"; found=1; }
  grep -q "$s" .claude/settings.json || { echo "Claude 沒登記  $s"; found=1; }
  grep -q "$s" .codex/hooks.json || { echo "Codex 沒登記  $s"; found=1; }
done

if [ -d .codex/skills ]; then
  echo "舊目錄還在  .codex/skills（Codex 的專案技能位置是 .agents/skills）"
  found=1
fi

for name in roast seduce; do
  skill=".claude/skills/$name/SKILL.md"
  yaml=".claude/skills/$name/agents/openai.yaml"
  style=".claude/output-styles/$name.md"
  [ -f "$style" ] || { echo "缺輸出風格  $style"; found=1; }
  [ -f "$skill" ] || { echo "缺技能  $skill"; found=1; continue; }
  [ "$(head -c 3 "$skill")" = "---" ] || { echo "壞 frontmatter  $skill"; found=1; }
  [ -f ".agents/skills/$name/SKILL.md" ] || { echo "Codex 路徑看不到  .agents/skills/$name"; found=1; }
  grep -q "$style" "$skill" || { echo "$skill 沒指向 $style"; found=1; }
  grep -qE '^[[:space:]]+allow_implicit_invocation:[[:space:]]*false' "$yaml" || {
    echo "$yaml 沒關掉自動觸發"
    found=1
  }
done

exit $found
