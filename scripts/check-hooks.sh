#!/usr/bin/env bash
# 同一對 Bash guard，Claude Code 登記在 .claude/settings.json，Codex 登記在 .codex/hooks.json。
# Codex 不讀 settings.json，兩邊不同步不會噴錯，只會讓其中一個工具少了護欄 —— 所以由這支擋。
#
# 無輸出 = 接上了。有輸出時 exit 1。

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

found=0

for f in .claude/settings.json .codex/hooks.json; do
  python3 -c 'import json,sys; json.load(open(sys.argv[1]))' "$f" 2>/dev/null || { echo "$f 不是合法 JSON"; found=1; }
done

for s in guard-git.sh guard-secrets.sh; do
  [ -f ".claude/hooks/$s" ] || { echo "缺腳本  .claude/hooks/$s"; found=1; }
  [ -f ".claude/hooks/test-$s" ] || { echo "缺回歸規格  .claude/hooks/test-$s"; found=1; }
  grep -q "$s" .claude/settings.json || { echo "Claude 沒登記  $s"; found=1; }
  grep -q "$s" .codex/hooks.json || { echo "Codex 沒登記  $s"; found=1; }
done

exit $found
