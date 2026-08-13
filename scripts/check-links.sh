#!/usr/bin/env bash
# 檢查本 repo 自己的 markdown 相對連結，目標檔案是否存在。
#
# 以「連結所在檔案的目錄」解析相對路徑 —— 不是以 repo root。
#
# 略過三類非本地目標，否則會誤報：
#   http(s)://…          外部連結
#   #anchor              同頁錨點
#   ../../tree/<branch>  GitHub 分支連結（本 repo 幾條線互指用）
#
# 也略過 .claude/skills/ 底下除了 README.md 以外的檔案：那是 luca-skills 的
# 第三方凍結副本，它們文件裡的 `01-adopt.png`、`docs/adr/0007-….md` 是**範例**
# 不是真連結，我們既不該修也修不了。只檢查我們自己加的那份 README。
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
done < <(git ls-files '*.md' | grep -v '^\.claude/skills/' ; git ls-files '.claude/skills/README.md')

exit $found
