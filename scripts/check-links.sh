#!/usr/bin/env bash
# 檢查所有 tracked markdown 的相對連結，目標檔案是否存在。
#
# 以「連結所在檔案的目錄」解析相對路徑 —— 不是以 repo root。
# 略過三類非本地目標，否則會誤報：
#   http(s)://…          外部連結
#   #anchor              同頁錨點
#   ../../tree/<branch>  GitHub 分支連結（本 repo 三條線互指用）
#
# 無輸出 = 全部有效。有輸出時 exit 1。

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

found=0
while IFS= read -r f; do
  d=$(dirname "$f")
  while IFS= read -r target; do
    case "$target" in
      http://*|https://*|'#'*|*/tree/*) continue ;;
    esac
    # 去掉錨點後再檢查，例如 ./BUILD.md#關-1
    path=${target%%#*}
    [ -z "$path" ] && continue
    if [ ! -e "$d/$path" ]; then
      echo "死連結  $f  →  $target"
      found=1
    fi
  done < <(grep -oE '\]\([^)]+\)' "$f" 2>/dev/null | sed 's/^](//;s/)$//')
done < <(git ls-files '*.md')

exit $found
