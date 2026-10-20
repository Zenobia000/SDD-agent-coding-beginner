#!/usr/bin/env bash
# 把 curriculum/ 建成課程網站，輸出到 site/（不進版控）。
#
# 設定檔放在 scripts/site/zensical.toml，不放根目錄：根目錄只留第一次來就要知道的東西。
# Zensical 要求 docs_dir 在設定檔所在的目錄底下，所以建置時暫時複製一份到根目錄，跑完就刪。
#
# 用法：bash scripts/build-site.sh          建置
#       bash scripts/build-site.sh serve    本機預覽，改檔自動重建

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

if ! command -v zensical >/dev/null 2>&1; then
  echo "找不到 zensical。先裝：pip install -r scripts/site/requirements.txt" >&2
  exit 1
fi

tmp_config=.zensical.build.toml
trap 'rm -f "$tmp_config"' EXIT
cp scripts/site/zensical.toml "$tmp_config"

if [ "${1:-build}" = serve ]; then
  zensical serve -f "$tmp_config"
else
  zensical build --strict -f "$tmp_config"
fi
