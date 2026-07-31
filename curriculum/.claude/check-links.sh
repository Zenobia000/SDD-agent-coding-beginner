#!/usr/bin/env bash
# 連結檢查器 —— 掃出所有指向不存在檔案的相對連結。
#
# 這不是 hook（沒有註冊在 settings.json），是可以手動跑的工具：
#   bash .claude/hooks/check-links.sh              # 掃全 repo
#   bash .claude/hooks/check-links.sh curriculum   # 只掃某個目錄
#
# 為什麼需要它：本 repo 的 doc contract 要求「不重述、用連結」，
# 連結一多就會有斷鏈，而斷鏈是學員最直接的卡關來源。
set -uo pipefail

ROOT="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
SCOPE="${1:-.}"
cd "$ROOT" || exit 1

BROKEN=0
while IFS= read -r md; do
  # 抓出 markdown 相對連結 ](./x) 與 ](../x)，去掉 #anchor
  grep -oE '\]\(\.{1,2}/[^)]+\)' "$md" 2>/dev/null | sed -E 's/^\]\(//; s/\)$//' | while read -r link; do
    target="${link%%#*}"
    [ -z "$target" ] && continue
    resolved="$(cd "$(dirname "$md")" 2>/dev/null && realpath -m "$target" 2>/dev/null)"
    if [ ! -e "$resolved" ]; then
      printf '%s → %s\n' "$md" "$link"
    fi
  done
done < <(find "$SCOPE" -name '*.md' -type f -not -path './.git/*' -not -path './node_modules/*') > /tmp/_broken_links.$$

if [ -s /tmp/_broken_links.$$ ]; then
  BROKEN=$(wc -l < /tmp/_broken_links.$$ | tr -d ' ')
  printf '斷鏈 %s 條：\n\n' "$BROKEN"
  cat /tmp/_broken_links.$$
  rm -f /tmp/_broken_links.$$
  exit 1
fi

rm -f /tmp/_broken_links.$$
echo "連結全部有效。"
exit 0
