#!/usr/bin/env bash
# 探測一支 YouTube 影片是否符合 fixture 特徵。只抓 metadata 與字幕，不下載影片。
#
#   bash scripts/probe-fixture.sh <video_id_or_url>
#
# 需要 yt-dlp。沒裝的話：uvx yt-dlp（uv 已裝時免安裝）或 pip install yt-dlp。
# 注意：YouTube 會對頻繁的字幕請求限流，字幕字數突然變 0 通常是限流不是影片變了。
set -uo pipefail
ID="$1"
D=$(mktemp -d)
trap 'rm -rf "$D"' EXIT

META=$(timeout 120 uvx yt-dlp --skip-download --no-warnings \
  --print "%(id)s@@%(duration)s@@%(channel).30s@@%(title).70s" "$ID" 2>/dev/null | tail -1)
[ -z "$META" ] && { echo "❌ $ID 取不到（下架／私人／地區限制）"; exit 1; }

IFS='@@' read -r vid _ dur _ chan _ title <<< "$META"
mins=$(( ${dur:-0} / 60 ))

# 字幕清單：分辨人工字幕與自動字幕
SUBS=$(timeout 120 uvx yt-dlp --skip-download --no-warnings --list-subs "$ID" 2>/dev/null)
has_manual=$(echo "$SUBS" | awk '/Available subtitles/{f=1;next}/^\[/{f=0}f' | grep -cE '^(zh|en)' || true)
has_auto=$(echo "$SUBS"   | awk '/automatic captions/{f=1;next}/Available subtitles/{f=0}f' | grep -cE '^(zh|en)' || true)

# 抓字幕文字（優先人工，退回自動）
timeout 180 uvx yt-dlp --skip-download --no-warnings \
  --write-subs --write-auto-subs --sub-langs "zh.*,en.*" --sub-format vtt \
  -o "$D/s" "$ID" >/dev/null 2>&1
TXT=$(cat "$D"/s*.vtt 2>/dev/null | grep -vE '^(WEBVTT|NOTE|Kind:|Language:|[0-9]{2}:|$)' | sed 's/<[^>]*>//g' | sort -u)

if [ -z "$TXT" ]; then
  qty=0; vague=0; words=0
else
  words=$(echo "$TXT" | wc -w)
  # 份量訊號：數字＋單位（中英）
  # 阿拉伯數字＋單位
  qty_num=$(echo "$TXT" | grep -coiE '[0-9]+ *(g|ml|kg|公克|克|毫升|大匙|小匙|茶匙|湯匙|杯|瓣|顆|條|片|斤|兩|tbsp|tsp|cups?|oz|pounds?|lb|cloves?|grams?)' || true)
  # 英文拼寫數字＋單位（auto caption 常這樣寫）
  qty_word=$(echo "$TXT" | grep -coiE '(one|two|three|four|five|six|seven|eight|nine|ten|half|quarter) +(and +a +half +)?(tbsp|tsp|tablespoons?|teaspoons?|cups?|ounces?|oz|pounds?|lbs?|cloves?|grams?|sticks?)' || true)
  # 中文數字＋單位
  qty_zh=$(echo "$TXT" | grep -coE '[一二三四五六七八九十兩半]+ *(公克|克|毫升|大匙|小匙|茶匙|湯匙|杯|瓣|顆|條|片|斤|兩)' || true)
  qty=$(( qty_num + qty_word + qty_zh ))
  # 模糊量詞
  vague=$(echo "$TXT" | grep -coE '適量|少許|酌量|依個人口味|隨意|to taste|a pinch|a dash|as needed|as desired' || true)
fi

printf '%s\n' "─────────────────────────────────────────────"
printf '  %s\n' "$title"
printf '  id=%s  長度=%d 分  頻道=%s\n' "$vid" "$mins" "$chan"
printf '  人工字幕=%s  自動字幕=%s  字幕字數=%s\n' "$has_manual" "$has_auto" "$words"
printf '  份量訊號=%-4s 模糊量詞=%s\n' "$qty" "$vague"
printf '  → https://www.youtube.com/watch?v=%s\n' "$vid"
