---
name: worktree-strategy
description: 規劃、建立、協調、整合與清理 Git worktrees 以進行隔離並行工作。當多個實作需要獨立 working trees、保留 dirty primary tree，或實驗與 reviews 不能共享分支 state 時使用。
---

# Worktree Strategy

每個 worktree 用一個分支，一個明確的整合 owner。worktree 隔離檔案與 index state；它不隔離外部服務、caches、ports、databases 或 credentials。

## 1. Preflight

1. 檢查 `git status`、repository/common-dir、目前 worktrees、remotes、default branch 與候選 base commit。
2. 在其目前 worktree 保留 dirty changes。除非使用者明確選擇那個動作，否則絕不移動、stash、reset 或 clean 它們。
3. 定義每個 workstream 的分支、路徑、base、檔案/寫入 scope、驗證、ports、database/schema 與整合順序。
4. 確認分支與目標路徑都不已存在。使用明確的兄弟姐妹或設定的 worktree 目錄，絕不廣闊或模糊路徑。

## 2. 建立

當 host agent 的原生 worktree 功能提供生命週期追蹤時優先使用。否則使用明確命令如：

```bash
git fetch origin
git worktree add ../<repo>-<slug> -b <type>/<slug> <base-ref>
```

只在目前 remote state 重要且網路存取授權時 fetch。不複製 `.env`、credentials、依賴目錄或建立輸出。只在 package manager 支援並行存取安全時共享 package caches。

為並行 worktrees 指派唯一的 ports、Compose project names、臨時目錄與測試 databases。

## 3. 工作與整合

- 只在其自己的分支上 commit 每個 worktree 的邊界內改動。
- 在 rebase 或 merge 更新 base 後重驗。
- 根據 repository policy 透過 PRs、merge 或 cherry-pick 整合；一個 owner 解決 cross-workstream 設計衝突。
- 在依賴前 merge 阻擋者。在整合分支執行組合 typecheck/tests/build，因為隔離綠燈結果不證明組合是綠燈。
- 絕不在多個 worktrees 檢出一個分支或從目前的改變另一個 worktree 的檔案。

## 4. 安全清理

只在確認其改動已 committed/pushed 或刻意可丟棄且分支已整合或保留後才移除 worktree。顯示目標的 `git status`，再在適當時使用 `git worktree remove <exact-path>` 與 `git worktree prune`。

未經明確核准，絕不強制移除或直接刪除目錄。清理後報告保留的分支/worktrees 與復原參考。
