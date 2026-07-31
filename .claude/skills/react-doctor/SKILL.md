---
name: react-doctor
description: 執行並 triage React 專案診斷，不假設特定 repository、package manager 或工具版本。在 React 變更後、commit/PR 前，或被要求檢查 React 正確性、無障礙、效能、安全性或架構回歸時使用。
---

# React Doctor

有 project 固定的診斷工具時使用；不靜默下載或執行變動 remote prompts。

## 工作流

1. 確認 repository 是 React 專案並定位其 workspace/package manager、scripts、lockfile、React 版本、lint/type/test 命令與任何既存 React Doctor 設定。
2. 從目前分支的 merge-base 建立固定比較基準。
3. 依序優先使用：
   - repository script 已執行 React 診斷；
   - 本地安裝的 `react-doctor` binary；
   - 只在使用者核准網路執行後的一次性 package runner。
4. 在使用非固定或陌生 CLI 前，執行其目前 `--help` 並從支援的 flags 組合命令。不假設快取命令語法仍然有效。
5. 先執行變更檔/diff 診斷。只在基準清理或使用者要求時執行完整掃描。
6. 記錄基準輸出或分數、按規則與根因分組 findings，再區分：
   - 目前 diff 引入的回歸；
   - 既存的 findings；
   - 偽陽性或需要設定的規則。
7. 除非使用者要求清理，只修復 scope 內的回歸。每個 cluster 後重跑狹窄掃描；用 repository 的 typecheck、lint、tests 與 build（適用時）結束。

報告確切命令、before/after 結果、未解決的 findings 與是否使用了網路下載的工具。除非另外要求，否則絕不 commit 或開 PR。
