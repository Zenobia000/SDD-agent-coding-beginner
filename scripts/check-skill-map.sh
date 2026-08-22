#!/usr/bin/env bash
# 檢查 .claude/skills/ 與兩張路由表是否同步。
#
# 擋三類「不會噴錯、只會靜默壞掉」的漂移：
#
#   1. 漏路由    技能存在，但 compass/SKILL.md 或 docs/SKILL-MAP.md 沒提它。
#                使用者觸發的技能（disable-model-invocation: true）沒有
#                description 在模型 context 裡 —— 表沒提到，就等於只剩
#                人的記憶能觸發它。
#
#   2. 死路由    表裡寫了 `/xxx`，但 .claude/skills/xxx/ 不存在。
#                技能改名或刪掉時會留下這種指向空氣的路標。
#
#   3. 壞 frontmatter
#                SKILL.md 開頭不是 `---`（前面多一個空行，Claude Code 會
#                靜默略過整個技能，而且不會告訴你），或 `name:` 不等於
#                資料夾名。
#
# 判定「有提到」用反引號包住的完整寫法 `/技能名`，那也是兩張表的既有慣例；
# 順便讓 /implement 不會誤配到 /implement-all。
#
# 無輸出 = 全部同步。有輸出時 exit 1。

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

SKILLS_DIR=.claude/skills
COMPASS=$SKILLS_DIR/compass/SKILL.md
MAP=docs/SKILL-MAP.md

# Claude Code 內建指令，不是本 repo 的技能
BUILTINS=" clear compact "

found=0

for f in "$COMPASS" "$MAP"; do
  if [ ! -f "$f" ]; then
    echo "缺檔案  $f"
    exit 1
  fi
done

# --- 1. 漏路由 --------------------------------------------------------------
for d in "$SKILLS_DIR"/*/; do
  s=$(basename "$d")
  [ -f "${d}SKILL.md" ] || continue

  # compass 是那張表本身，不必自我登錄
  if [ "$s" != compass ] && ! grep -qF "\`/$s\`" "$COMPASS"; then
    echo "漏路由  $s  →  $COMPASS 沒提到"
    found=1
  fi
  if ! grep -qF "\`/$s\`" "$MAP"; then
    echo "漏路由  $s  →  $MAP 沒提到"
    found=1
  fi
done

# --- 2. 死路由 --------------------------------------------------------------
while IFS= read -r name; do
  [ -n "$name" ] || continue
  case "$BUILTINS" in
    *" $name "*) continue ;;
  esac
  if [ ! -f "$SKILLS_DIR/$name/SKILL.md" ]; then
    echo "死路由  \`/$name\`  →  $SKILLS_DIR/$name/SKILL.md 不存在"
    found=1
  fi
done < <(grep -ohE '`/[a-z0-9-]+`' "$COMPASS" "$MAP" | sed 's/[`/]//g' | sort -u)

# --- 3. 壞 frontmatter ------------------------------------------------------
for d in "$SKILLS_DIR"/*/; do
  s=$(basename "$d")
  f=${d}SKILL.md
  [ -f "$f" ] || continue

  if [ "$(head -c 3 "$f")" != "---" ]; then
    echo "壞 frontmatter  $f  →  開頭不是 ---（前置空行會讓 Claude Code 靜默略過整個技能）"
    found=1
    continue
  fi

  declared=$(sed -n '2,20{ /^name:/ { s/^name:[[:space:]]*//; s/[[:space:]]*$//; p; q; } }' "$f")
  if [ "$declared" != "$s" ]; then
    echo "name 不符  $f  →  name: '$declared'，資料夾是 '$s'"
    found=1
  fi
done

exit $found
