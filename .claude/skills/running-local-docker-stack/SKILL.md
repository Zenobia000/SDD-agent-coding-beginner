---
name: running-local-docker-stack
description: 探索、啟動、rebuild、migrate、診斷與驗證 repository 的本地 Docker Compose stack，不假設 service names、ports、environment files 或 project-specific topology。用於本地 container stack 操作與準備檢查。
---

# 執行本地 Docker Stack

在改變 stack 前先探索。絕不重用另一個 repository 的指示。

## 1. 檢查

讀 project contract 與 container docs，再定位 Compose 檔案、overrides、profiles、Dockerfiles、environment templates、health checks、volumes、migration jobs 與 package scripts。在支援處使用 `docker compose config --services`、`--profiles` 與 `docker compose ps -a`。

不從 `docker compose config` 列印已解決的 secrets。不讀或建立真實 `.env` 檔案而未明確許可；從 committed examples 工作並只報告遺漏的變數名。

## 2. 選最小動作

- 已 healthy：只驗證。
- 僅設定變更：recreate 受影響的 services。
- Source/Dockerfile/dependency 變更：只 build 受影響的 images。
- Schema 變更：如所文件化地在啟動前或啟動中執行 repository 的 documented migration job。
- 首次啟動：pull/build 與依其必要順序啟動依賴。

啟動前，檢查佔用的 host ports、既存 project names/containers、必要 networks、disk capacity 與是否真的需要破壞性 volume recreation。未經明確確認與復原計畫，絕不加 `-v`、刪除 volumes 或重設 databases。

## 3. 啟動與觀察

有 repository documented command 時使用；否則用發現的檔案/profiles/services 組合最小 `docker compose up -d` 命令。預設避免 rebuild 全部。

觀察 service state 與 health 直到每個必要 service healthy、成功 exit 如 job，或失敗並有有用 logs。診斷第一個因果失敗而非級聯依賴錯誤。

## 4. 在兩層驗證

1. Shallow：預期 containers、health status、ports、migration exit status、沒有 restart loops。
2. Deep：一個真實本地端到端動作透過公開 entrypoint，從 project docs 或 acceptance criteria 選擇。

報告命令、Compose 檔案/profiles、可達 URLs、unhealthy services、相關遮罩 log excerpts 與確切 stop/restart 指示。不意圖地留下連結的 log streams 或臨時 containers 執行。
