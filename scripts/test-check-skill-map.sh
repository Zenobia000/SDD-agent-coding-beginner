#!/usr/bin/env bash
# check-skill-map.sh 的回歸規格。每個案例蓋一個臨時的假專案，跑一次腳本，比對判決。
# 行為變更必須先改這張表 —— 沒有檢查的規則不是規則，是願望。
#
# 案例刻意用跟本 repo 不一樣的技能名與目錄佈局：那支腳本要能在任何專案跑，
# 綁死本 repo 的測試證明不了這件事。
#
# 執行：bash scripts/test-check-skill-map.sh
set -u
cd "$(dirname "$0")"
GUARD=$PWD/check-skill-map.sh

tmproot=$(mktemp -d)
trap 'rm -rf "$tmproot"' EXIT
fail=0
proj=""
ENVS=""

# mkskill <專案> <資料夾名> [frontmatter 的 name] [任意值=前置空行]
mkskill() {
  local p=$1 dir=$2 declared=${3:-$2} lead=${4:-} base=${SKILLS_BASE:-.claude/skills}
  mkdir -p "$p/$base/$dir"
  {
    [ -n "$lead" ] && printf '\n'
    printf -- '---\nname: %s\ndescription: x\n---\n\nbody\n' "$declared"
  } > "$p/$base/$dir/SKILL.md"
}

# mkdoc <專案> <相對路徑> <內容>
mkdoc() {
  mkdir -p "$(dirname "$1/$2")"
  printf '%s\n' "$3" > "$1/$2"
}

new() { proj=$tmproot/$1; ENVS=""; SKILLS_BASE=.claude/skills; mkdir -p "$proj"; }

# ---------------------------------------------------------------- 案例定義 --
case_ok() {                       # 兩個技能，表裡都有
  new ok; mkskill "$proj" alpha; mkskill "$proj" beta
  mkdoc "$proj" docs/SKILL-MAP.md '見 `/alpha` 與 `/beta`。'
}
case_missing_route() {            # beta 沒被表提到
  new missing; mkskill "$proj" alpha; mkskill "$proj" beta
  mkdoc "$proj" docs/SKILL-MAP.md '只提了 `/alpha`。'
}
case_dead_route() {               # 表指向不存在的技能
  new dead; mkskill "$proj" alpha
  mkdoc "$proj" docs/SKILL-MAP.md '`/alpha` 還有 `/ghost`。'
}
case_bad_frontmatter() {          # 前置空行 —— Claude Code 會靜默略過
  new badfm; mkskill "$proj" alpha "" LEAD
  mkdoc "$proj" docs/SKILL-MAP.md '`/alpha`'
}
case_name_mismatch() {            # name 不等於資料夾名
  new mismatch; mkskill "$proj" alpha alphabet
  mkdoc "$proj" docs/SKILL-MAP.md '`/alpha`'
}
case_no_route_doc() {             # 完全沒有路由表 → 只跑 frontmatter，不算失敗
  new nodoc; mkskill "$proj" alpha; mkskill "$proj" beta
}
case_no_route_doc_bad_fm() {      # 沒路由表，但 frontmatter 壞了 → 還是要抓
  new nodocbad; mkskill "$proj" alpha "" LEAD
}
case_self_registration() {        # 路由表是 router 自己的 SKILL.md，不必自我登錄
  new selfreg; mkskill "$proj" alpha
  mkdir -p "$proj/.claude/skills/router"
  printf -- '---\nname: router\ndescription: x\n---\n\n見 `/alpha`。\n' \
    > "$proj/.claude/skills/router/SKILL.md"
  ENVS="ROUTE_DOCS=.claude/skills/router/SKILL.md"
}
case_self_registration_strict() { # 同上，但漏了 alpha → 免登錄只赦免自己
  new selfregstrict; mkskill "$proj" alpha
  mkdir -p "$proj/.claude/skills/router"
  printf -- '---\nname: router\ndescription: x\n---\n\n什麼都沒提。\n' \
    > "$proj/.claude/skills/router/SKILL.md"
  ENVS="ROUTE_DOCS=.claude/skills/router/SKILL.md"
}
case_custom_layout() {            # 非標準目錄，靠環境變數指定
  new custom; SKILLS_BASE=tools/skills
  mkskill "$proj" alpha; mkskill "$proj" beta
  mkdoc "$proj" ROUTES.md '`/alpha` `/beta`'
  ENVS="SKILLS_DIRS=tools/skills ROUTE_DOCS=ROUTES.md"
}
case_builtins_ok() {              # 內建斜線指令不算死路由
  new builtins; mkskill "$proj" alpha
  mkdoc "$proj" docs/SKILL-MAP.md '`/alpha`，收工用 `/clear` 或 `/compact`。'
}
case_prefix_strict() {            # /implement-all 不能讓 /implement 蒙混過關
  new prefix; mkskill "$proj" implement; mkskill "$proj" implement-all
  mkdoc "$proj" docs/SKILL-MAP.md '只提了 `/implement-all`。'
}
case_git_subdir() {               # git repo 裡從子目錄執行，要能climb到根
  new gitsub; mkskill "$proj" alpha
  mkdoc "$proj" docs/SKILL-MAP.md '`/alpha`'
  git -C "$proj" init -q 2>/dev/null
  mkdir -p "$proj/deep/nested"
}
case_no_skills() {                # 根本沒有技能目錄 → 明確報錯，不要靜默放行
  new noskills; mkdir -p "$proj/src"
}

# -------------------------------------------------------------------- 執行 --
while IFS=$'\t' read -r want name desc; do
  [ -z "${want:-}" ] && continue
  "case_$name"
  runin=$proj
  [ "$name" = git_subdir ] && runin=$proj/deep/nested
  out=$(cd "$runin" && env $ENVS bash "$GUARD" 2>&1)
  if [ -z "$out" ]; then got=PASS; else got=FAIL; fi
  if [ "$got" = "$want" ]; then
    printf '  ✓ %-4s %-26s %s\n' "$want" "$name" "$desc"
  else
    printf '  ✗ want=%s got=%s  %-26s %s\n' "$want" "$got" "$name" "$desc"
    printf '%s\n' "$out" | sed 's/^/        /'
    fail=1
  fi
done <<'CASES'
PASS	ok	表與技能一致
FAIL	missing_route	技能沒被路由表提到
FAIL	dead_route	路由表指向不存在的技能
FAIL	bad_frontmatter	frontmatter 前有空行
FAIL	name_mismatch	name 不等於資料夾名
PASS	no_route_doc	沒有路由表不算失敗
FAIL	no_route_doc_bad_fm	沒路由表也要驗 frontmatter
PASS	self_registration	技能不必在自己的 SKILL.md 裡登錄
FAIL	self_registration_strict	免登錄只赦免自己，別人照抓
PASS	custom_layout	非標準目錄靠環境變數指定
PASS	builtins_ok	內建斜線指令不算死路由
FAIL	prefix_strict	/implement-all 不讓 /implement 蒙混
PASS	git_subdir	git repo 從子目錄執行
FAIL	no_skills	找不到技能要明確報錯
CASES

exit $fail
