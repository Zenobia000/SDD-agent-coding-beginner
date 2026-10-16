#!/usr/bin/env bash
# 把 curriculum/ 打包成發給學員的講義（放 OneDrive 用）。
#
# 原稿留在 git 裡才有版本紀錄與連結檢查；OneDrive 上的只是某一版的副本。
# instructor/ 是講師手冊，不打包。
#
# 打包後會掃一次：講義裡指向 curriculum/ 以外的相對連結，在 zip 裡一定會斷，
# 列出來並 exit 1，改成 GitHub 網址再打包。
#
# 用法：bash scripts/export-handout.sh   → dist/handout-<日期>-<commit>.zip

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

out_dir=dist
name="handout-$(date +%Y%m%d)-$(git rev-parse --short HEAD)"
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT

mkdir -p "$stage/$name"
git archive HEAD curriculum | tar -x -C "$stage"
rm -rf "$stage/curriculum/instructor"
mv "$stage/curriculum"/* "$stage/$name/"

# 掃描：只看 markdown 連結 ](...)，略過網址、錨點、GitHub 分支連結
found=0
while IFS= read -r f; do
  dir=$(dirname "$f")
  while IFS= read -r target; do
    path=${target%%#*}
    [ -z "$path" ] && continue
    case "$path" in http*|mailto:*|*/tree/*) continue ;; esac
    if [ ! -e "$dir/$path" ]; then
      echo "斷連結  ${f#"$stage/"} → $target"
      found=1
    fi
  done < <(grep -oE '\]\([^) ]+\)' "$f" | sed -E 's/^\]\(//; s/\)$//')
done < <(find "$stage/$name" -name '*.md')

if [ $found -ne 0 ]; then
  echo "講義裡有連到包外的相對連結，打包中止。改成 GitHub 網址後再跑一次。"
  exit 1
fi

if git status --porcelain -- curriculum | grep -q .; then
  echo "注意：curriculum/ 有未 commit 的修改，這份講義用的是 HEAD，不含那些修改。"
fi

mkdir -p "$out_dir"
(cd "$stage" && zip -qr - "$name") > "$out_dir/$name.zip"
echo "$out_dir/$name.zip"
