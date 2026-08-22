#!/usr/bin/env bash
# 檢查一個專案的 Claude Code 技能目錄與它的路由表是否同步。
#
# 這支腳本刻意不綁任何一個專案 —— 複製到別的 repo 直接能跑。專案特有的東西
# 全部走環境變數，而且都有能自己找到的預設：
#
#   SKILLS_DIRS  技能目錄，空白分隔。預設 .claude/skills
#   ROUTE_DOCS   路由表，空白分隔。留空則從候選清單裡挑存在的：
#                  <技能目錄>/compass/SKILL.md、docs/SKILL-MAP.md、SKILL-MAP.md
#                一份都找不到 → 只跑 frontmatter 檢查，不算失敗（很多專案
#                根本不維護路由表，那不是錯）。
#   BUILTINS     不是技能的斜線指令，空白分隔。預設是 Claude Code 內建指令。
#
# 擋三類「不會噴錯、只會靜默壞掉」的漂移：
#
#   1. 漏路由    技能存在，但路由表沒提它。使用者觸發的技能
#                （disable-model-invocation: true）沒有 description 在模型
#                context 裡 —— 表沒提到，就等於只剩人的記憶能觸發它。
#
#   2. 死路由    表裡寫了 `/xxx`，但沒有這個技能。改名或刪除留下的路標。
#
#   3. 壞 frontmatter
#                SKILL.md 開頭不是 `---`（前面多一個空行，Claude Code 會靜默
#                略過整個技能，而且不會告訴你），或 `name:` 不等於資料夾名。
#
# 判定「有提到」用反引號包住的完整寫法 `/技能名`；順便讓 /implement 不會誤配
# 到 /implement-all。一個技能不必在自己的 SKILL.md 裡自我登錄 —— 那是規則，
# 不是替某個路由器開的例外。
#
# 無輸出 = 全部同步。有輸出時 exit 1。
# 自我檢查：bash scripts/test-check-skill-map.sh

set -uo pipefail

# 專案根目錄：在 git repo 裡用 toplevel，否則就用當前目錄（非 git 也能跑）
root=$(git rev-parse --show-toplevel 2>/dev/null) || root=$PWD
cd "$root" || exit 1

SKILLS_DIRS=${SKILLS_DIRS:-.claude/skills}
BUILTINS=${BUILTINS:-clear compact help init config model review agents mcp memory cost doctor login logout status permissions hooks export resume add-dir bug vim terminal-setup pr-comments release-notes}

# --- 技能盤點 --------------------------------------------------------------
# 每列：<技能名> <TAB> <SKILL.md 路徑>
skills=$(
  for dir in $SKILLS_DIRS; do
    [ -d "$dir" ] || continue
    for d in "$dir"/*/; do
      [ -f "${d}SKILL.md" ] && printf '%s\t%s\n' "$(basename "$d")" "${d}SKILL.md"
    done
  done | sort -u
)

if [ -z "$skills" ]; then
  echo "找不到任何技能（找過：$SKILLS_DIRS）。用 SKILLS_DIRS 指定位置。" >&2
  exit 1
fi

# --- 路由表：沒指定就自己找 -------------------------------------------------
if [ -z "${ROUTE_DOCS:-}" ]; then
  cands=""
  for dir in $SKILLS_DIRS; do cands="$cands $dir/compass/SKILL.md"; done
  cands="$cands docs/SKILL-MAP.md SKILL-MAP.md"
  ROUTE_DOCS=""
  for c in $cands; do
    [ -f "$c" ] && ROUTE_DOCS="$ROUTE_DOCS $c"
  done
fi

found=0

# --- 1. 漏路由 --------------------------------------------------------------
# 技能不必在自己的 SKILL.md 裡自我登錄，所以先算出每份路由表的「擁有者」。
for doc in $ROUTE_DOCS; do
  if [ ! -f "$doc" ]; then
    echo "缺路由表  $doc" >&2
    found=1
    continue
  fi
  owner=""
  case "$doc" in
    */SKILL.md) owner=$(basename "$(dirname "$doc")") ;;
  esac

  while IFS=$'\t' read -r name _; do
    [ "$name" = "$owner" ] && continue
    grep -qF "\`/$name\`" "$doc" || {
      echo "漏路由  $name  →  $doc 沒提到"
      found=1
    }
  done <<< "$skills"
done

# --- 2. 死路由 --------------------------------------------------------------
if [ -n "$ROUTE_DOCS" ]; then
  known=$(printf '%s\n' "$skills" | cut -f1; printf '%s\n' $BUILTINS)
  while IFS= read -r name; do
    [ -n "$name" ] || continue
    printf '%s\n' "$known" | grep -qxF "$name" || {
      echo "死路由  \`/$name\`  →  沒有這個技能"
      found=1
    }
  done < <(grep -ohE '`/[a-z0-9][a-z0-9-]*`' $ROUTE_DOCS 2>/dev/null | sed 's/[`/]//g' | sort -u)
fi

# --- 3. 壞 frontmatter ------------------------------------------------------
while IFS=$'\t' read -r name file; do
  if [ "$(head -c 3 "$file")" != "---" ]; then
    echo "壞 frontmatter  $file  →  開頭不是 ---（前置空行會讓 Claude Code 靜默略過整個技能）"
    found=1
    continue
  fi
  declared=$(sed -n '2,20{ /^name:/ { s/^name:[[:space:]]*//; s/[[:space:]]*$//; p; q; } }' "$file")
  if [ "$declared" != "$name" ]; then
    echo "name 不符  $file  →  name: '$declared'，資料夾是 '$name'"
    found=1
  fi
done <<< "$skills"

exit $found
