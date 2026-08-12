---
name: improve-codebase-architecture
description: 掃描近期常變或指定區域的架構摩擦，提出 deepening candidates，讓使用者選擇後再共同設計。只在使用者明確要求做架構檢視或架構改善時使用，不要在其他情況自行啟動。
---
# Improve Codebase Architecture

這個 skill 只在使用者明確要求時執行。不要在使用者沒要求時自行啟動它。

使用 `codebase-design` 的 module/interface/depth/seam/adapter/leverage/locality 詞彙。目標是找出能增加 locality 與 testability 的 deepening opportunity，不是列通用 clean-code 建議。

## 1. 先定掃描範圍

使用者有指定範圍就採用。否則先看一段近期 git history 與 churn，優先檢查反覆變更的 hot spots；沒有明顯 hot spot 才擴大。讀相關 glossary 與 ADR，避免重提已拒絕的方向。

把探索交給 `.agents/agents/code-explorer/agent.md` 這個只讀 subagent；無法載入時自行只讀探索，這個階段一律不改 code。觀察實際摩擦：理解一個概念需要跳很多 modules、interface 和 implementation 一樣複雜、同一 decision 散在 callers、真正 bug 無法從公開 seam 測到、adapters 洩漏到 core policy。對候選做 deletion test。

## 2. 只交付候選，不先改 code

在對話中呈現最多五張候選卡：

- Files/modules。
- 現在的 friction 與 `path:line` 證據。
- 建議深藏的複雜度與可能 seam；此時不要定死完整 interface。
- locality、leverage 與 tests 如何改善。
- migration risk、ADR conflict。
- `Strong / Worth exploring / Speculative`。

最後推薦一個優先候選與會翻盤的條件，問使用者要探索哪一個。

## 3. 使用者選擇後才設計

對選中的 candidate 使用 `grilling` 逐一決定 constraints、dependencies、seam、interface、migration 與保留的 tests；術語改變時使用 `domain-modeling`。重要 interface 使用 `codebase-design` 的 Design It Twice 比較。

輸出可直接送進 `to-spec` 的決策摘要。不要把 architecture review 與 refactor 實作混在同一 skill。
