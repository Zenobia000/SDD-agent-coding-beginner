---
name: git-commit
description: Use when the user wants to write a Conventional Commits-formatted commit message, 幫我寫 commit message, 或打 /git:commit. Reads staged diff, drafts message in Conventional Commits format, prints for confirmation — does NOT auto-commit.
---

# Git Commit Skill（依 Conventional Commits 格式）

當使用者要你寫 commit message 或打 `/git:commit [額外說明]` 時：

1. 先跑 `git diff --staged` 看當下要 commit 的內容
2. 把使用者的額外說明（slash command 後面的參數）當作補充資訊一起參考
3. 依 Conventional Commits 格式產生 commit subject（< 72 字元，用祈使句）
   - 可用 type：feat / fix / refactor / docs / test / chore / perf / ci
   - 格式：`<type>(<scope>): <subject>`
4. body 用 3 行內說明 **WHY**（為什麼要這個改動，不要重複描述 diff）
5. 如果偵測到 breaking change，加 `BREAKING CHANGE: <說明>` footer
6. **不要直接執行 `git commit`**，把完整 message 印出來等我確認

如果 staged diff 是空的，告訴使用者「沒有 staged 變更，請先 git add」就好，不要硬寫 message。
