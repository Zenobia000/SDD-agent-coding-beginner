---
name: to-tickets
description: 把規格、計畫或目前對話拆成可在單一新 session 完成的 tracer-bullet tickets，標出 blocking edges，確認後發布。
disable-model-invocation: true
argument-hint: "spec 路徑、issue 或目前對話"
---

# To Tickets

## 流程

1. 讀完整來源、`docs/agents/project.md`、相關 glossary 與 ADR。來源是 issue 時也讀相關 comments。
2. 必要時探索 codebase，找出既有 seams 與「先讓改動容易，再做容易的改動」的 prefactor 機會。
3. 拆成窄而完整的垂直切片：每張票穿過需要的資料、邏輯、介面與測試層，完成後可獨立 demo 或驗證，且適合一個乾淨 context 完成。
4. 為每張票列出真正阻擋它的 tickets。沒有 blocker 的票形成目前 frontier。
5. 先展示編號、標題、blocked by 與交付行為；逐一釐清 granularity 與 edges，使用者核准後才發布。

發布前用 `parallel-work` 檢查 frontier：標記哪些 tickets 可以同時執行、哪些共享 write set 或外部 state 而必須序列化。並行實作若會修改 repository，為每張票指定獨立 branch/worktree；具體隔離策略交給 `worktree-strategy`。

不要按 schema、backend、frontend、tests 做水平切片。跨 repo 的單一機械變更無法垂直切時，採 expand → 分批 migrate → contract，每一步維持相容；若個別批次無法綠燈，明確增加最後的整合驗證票。

## Ticket 格式

```markdown
# <NN> — <Title>

## What to build
從使用者角度描述這張票完成的端到端行為。

## Acceptance criteria
- [ ] 可獨立驗證的結果。

## Testing seam
- <公開 interface 與驗證命令>

## Blocked by
- <ticket reference> 或 None — can start immediately

## Out of scope
- 本票刻意不處理的內容。
```

本地 tracker 寫成 `.scratch/<feature>/issues/<NN>-<slug>.md`，一票一檔並依 dependency 排序。外部 tracker 依 project contract 使用原生 blocking 關係；沒有原生能力才把 edges 寫進 body。不要修改或關閉來源 issue。
