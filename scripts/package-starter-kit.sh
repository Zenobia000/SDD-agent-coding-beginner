#!/usr/bin/env bash
# 把企業啟動包打包成一個 zip，發給企業用。
#
# 內容：報告與高層簡報的 HTML（雙擊打開），以及用 Chrome 印好的 PDF（找得到 Chrome 才會產生）。
# 用法：bash scripts/package-starter-kit.sh   → dist/starter-kit-<日期>.zip

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

python3 scripts/build-html.py >/dev/null

name="starter-kit-$(date +%Y%m%d)"
stage=$(mktemp -d)
trap 'rm -rf "$stage"' EXIT
mkdir -p "$stage/$name"
cp dist/starter-kit.html "$stage/$name/AI的回報卡在組織-報告.html"
cp dist/deck.html "$stage/$name/AI的回報卡在組織-高層簡報.html"

chrome=$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)
if [ -n "$chrome" ]; then
  for pair in "starter-kit:報告" "deck:高層簡報"; do
    src=${pair%%:*}; label=${pair#*:}
    timeout 120 "$chrome" --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
      --virtual-time-budget=8000 --print-to-pdf="$stage/$name/AI的回報卡在組織-$label.pdf" \
      "file://$PWD/dist/$src.html" 2>/dev/null || echo "! $label PDF 產生失敗，只打包 HTML" >&2
  done
else
  echo "! 找不到 Chrome，只打包 HTML；PDF 請用瀏覽器列印" >&2
fi

(cd "$stage" && zip -qr "$name.zip" "$name")
mv "$stage/$name.zip" dist/
echo "✓ dist/$name.zip"
