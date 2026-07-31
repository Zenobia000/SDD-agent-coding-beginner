---
name: release-notes
description: 從 tag range、branch comparison、milestone 或 release PR 產生 repository-agnostic release notes。當草稿 changelogs 或發布 release notes 時過濾機械 commits 並只保留使用者相關變更時使用。
---

# Release Notes

從主要 repository 證據草稿。只在明確要求時發布。

## 1. 解決 range

從使用者參考、tags、release branch、PR 或 repository 慣例決定目標版本與比較 range。絕不假設 semantic versioning、date versioning、branch names 或 hosting provider。

擷取：

- 範圍內的 commits 與 merge commits；
- 可用時的 linked PRs/issues；
- 前一個 release 的格式與語氣；
- migration、security、deprecation 與 breaking-change 證據；
- 若 repository 包含致謝時的貢獻者名字。

## 2. 過濾與分類

排除 merge noise、conflict-resolution commits、sync-only commits、release bookkeeping、立即重新應用的 reverts 與無可觀察影響的內部 churn。

使用 repository 的類別。無先例時，只用非空 sections 來自：

- Highlights
- Features
- Improvements
- Bug fixes
- Security
- Breaking changes
- Deprecations
- Upgrade notes

Conventional Commit types 是訊號，不是真理。subject 模糊時讀 diff/PR。`refactor` 可以是使用者可見；`feat` 可以是內部基礎設施。

## 3. 為受眾寫作

- 描述可觀察結果與為何重要；不逐字複製 commit subjects。
- 從公開筆記移除內部 ticket IDs，除非 repository 先例保留它們。
- 為安全項目連結 advisories，不暴露超過 project 披露政策的 exploit 細節。
- 把必要動作、相容性限制與不可逆 migrations 放進 Upgrade notes 或 Breaking changes。
- 標記不確定 claims 並識別驗證它們需要的 artifact。

最後一次對比草稿與實際 range，確認每個 bullet 都對應證據且每個主要使用者可見變更都被代表。

## 4. 安全發布

先預覽最終 Markdown 與目的地。發布時，使用暫時 body 檔案或 hosting provider 的結構化 API 以避免 shell 插值。回報 release/PR URL 與列出任何刻意省略或未驗證的項目。
