#!/usr/bin/env bash
# UserPromptSubmit — 把「你現在在第幾站、第幾拍」注入每一輪對話。
#
# 這是「狀態外顯」型 hook。人的工作記憶會斷，AI 的 context 會漂；
# 把當前狀態寫成每輪都看得到的一行，兩邊都省力。
#
# 契約（見 docs/authoring/04-write-a-hook.md）：
#   stdin  : JSON，含 .prompt
#   stdout : exit 0 時，輸出會被當成 context 餵給 Claude
#
# 狀態檔：.claude/.station（已被 .gitignore 擋，屬個人進度）
#   格式：一行，例如 `S4 beat3`
#   更新方式：學員自己 `echo "S5 beat1" > .claude/.station`，或由 /gate 寫入
set -uo pipefail

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-.}"
STATION_FILE="$PROJECT_DIR/.claude/.station"

[ -f "$STATION_FILE" ] || exit 0
STATION=$(head -n1 "$STATION_FILE" | tr -d '\r\n')
[ -z "$STATION" ] && exit 0

SID=$(printf '%s' "$STATION" | awk '{print $1}')
BEAT=$(printf '%s' "$STATION" | awk '{print $2}')

case "$SID" in
  S0) NAME="開機";        OBJ="—（暖身站，不跑四拍）" ;;
  S1) NAME="問對問題";    OBJ="題目" ;;
  S2) NAME="定契約";      OBJ="規格" ;;
  S3) NAME="先跑通";      OBJ="—（體感站，不跑四拍）" ;;
  S4) NAME="迴圈開工";    OBJ="程式" ;;
  S5) NAME="方法變資產";  OBJ="資產" ;;
  S6) NAME="積木裝配";    OBJ="積木" ;;
  S7) NAME="守門與交付";  OBJ="交付" ;;
  *)  exit 0 ;;
esac

case "$BEAT" in
  beat1) BEATTXT="① 劃邊界 —— 這輪只准動什麼？評分是什麼？跑幾輪？" ;;
  beat2) BEATTXT="② 放它跑 —— 產候選，中途不要停下來問人" ;;
  beat3) BEATTXT="③ 打分數 —— 用二元判準；程式能判就別問人" ;;
  beat4) BEATTXT="④ 收判斷 —— 看分數、抽查最好的、決定收工或再跑一輪" ;;
  *)     BEATTXT="" ;;
esac

{
  printf '【目前進度】%s %s｜這一站對「%s」跑四拍\n' "$SID" "$NAME" "$OBJ"
  [ -n "$BEATTXT" ] && printf '【當前拍子】%s\n' "$BEATTXT"
  printf '回覆結尾請依 CLAUDE.md §5.1 給出「下一步：<恰好一個動作>」。\n'
}
exit 0
