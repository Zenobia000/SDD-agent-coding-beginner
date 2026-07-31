---
name: parallel-work
description: 把工作拆成安全的並行 workstreams 並聚合輸出，不依賴、context 或檔案寫入衝突。當兩個以上的調查、review、tests 或實作可平行執行，或需要決定是否平行實際有益時使用。
---

# 並行工作

只平行獨立工作。在依賴鏈上加更多工人製造協調開銷，不加速。

## 1. 畫出依賴圖

對每個候選 workstream 記錄：

- 它需要的輸入 artifacts 與事實；
- 它產生的決策或交付物；
- 它可能讀寫的檔案/state；
- side effects、外部系統、ports、databases 與 git 操作；
- 阻擋它的 tasks 與它解除阻擋的 tasks。

frontier 包含阻擋者完成的 tasks。只在 write sets 與 side effects 不衝突時並行執行 frontier tasks。

## 2. 選隔離層級

- 相同 working tree：唯讀探索、獨立 reviews 或只建立分離臨時 artifacts 的命令。
- 分離 worktrees：並行實作、migrations、產生的檔案、formatters 或任何可能觸及重疊 repository state 的 tasks。使用 `worktree-strategy`。
- 序列：一個 task 消費另一個的結果、兩者編輯相同概念決策、共享可變 database/port/index，或需要相同人類決策。

不平行 `git add`、commits、rebases、merges、package-lock 產生、針對單一 database 的 schema migrations，或正確設計仍未決的 fixes。

## 3. 給每個 worker 明確邊界的契約

只提供 task-local context：

```text
目標：
輸入與 fixed point：
允許的讀寫範圍：
必要的輸出 artifact：
驗證命令：
停止條件與禁止的 side effects：
```

避免洩漏預期結論給獨立 reviewers。要求證據、路徑、命令、不確定項與一個推薦下一步。

## 4. 刻意地 fan in

等待每個必要結果，再驗證 artifacts 而非信任摘要。根據主要證據協調矛盾。檢查組合 diffs 找重疊假設、一次執行整合檢查、報告失敗/取消的 workstreams。

平行加速受最長依賴鏈限制。優先使用兩個高價值獨立 tasks，而非許多協調成本超過工作量的小 agents。
