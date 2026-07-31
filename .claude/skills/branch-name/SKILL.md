---
name: branch-name
description: 用 repository 既定的命名慣例建立或重新命名 Git branch，搭配安全的 conventional 降級。當開始隔離工作、命名 feature/fix branch，或準備 pull request 或 worktree 用的分支時使用。
---

# Branch Name

從工作推導名稱，不從組織特定 tracker。

## 工作流

1. 檢查 `git status`、目前分支、remote default branch 與最近的分支名稱（如有）。
2. 保留已文件化的 repository 慣例。若無，使用：

   ```text
   <type>/<optional-issue-id>-<short-outcome>
   ```

3. 根據使用者可見的意圖選 `feat`、`fix`、`refactor`、`docs`、`test`、`perf`、`build`、`ci` 或 `chore`。
4. 只在使用者或 repository 提供時加 issue identifier。絕不自行發明。
5. 寫 2–6 字小寫 kebab-case 結果。描述什麼改變，不是實作技巧。
6. 檢查分支在本地或遠端都不存在。
7. 只在使用者要求建立/重新命名分支時才建立；否則回報提議的名稱。

建立時優先使用 `git switch -c <name> <base>`。在確認變更屬於新分支前，不切換離開未提交的工作。

## 範例

```text
feat/add-export-filters
fix/gh-248-retry-timeouts
refactor/simplify-auth-boundary
docs/document-local-setup
```
