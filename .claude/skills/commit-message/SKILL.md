---
name: commit-message
description: 從 staged diff 與 repository history 草稿或驗證 Git commit message。當準備 commit、拆分混合變更、檢查 Conventional Commit 風格，或解釋為何改動屬於同一 atomic commit 時使用。
---

# Commit Message

如實描述 staged change。當 index 顯示不同內容時，不用對話作為唯一真相源。

## 工作流

1. 讀 `git status --short`、`git diff --cached --stat` 與 `git diff --cached`。若沒有 staged 內容，停止或清楚標示結果為未 staged 變更的草稿。
2. 檢查最近 commit subjects 與任何貢獻指南，學習 repository 既定的語言、大寫、scopes、issue references 與 body 風格。
3. 檢查原子性。若 staged diff 包含獨立意圖，在草稿前建議拆分；一個 message 不能隱藏多個不相關的變更。
4. 使用 repository 風格。無明確先例時，降級到：

   ```text
   <type>(<optional-scope>)<!>: <imperative outcome>
   ```

5. 從意圖選 type：`feat`、`fix`、`refactor`、`perf`、`test`、`docs`、`build`、`ci`、`chore` 或 `revert`。
6. subject 保持具體、祈使句，通常不超過 72 字元。說明什麼可觀察的結果改變了；不寫「updates」或列檔名。
7. 只在保留有用脈絡時加 body：動機、非顯而易見的取捨、migration/相容性影響或為何明顯替代方案被拒。不敘述 diff。
8. 只在有證據支持時加 issue references 與 `BREAKING CHANGE:` footers。

分別回報提議的 subject 與可選的 body。除非使用者明確要求，否則絕不 stage 檔案、commit、amend 或 push。

## 範例

```text
fix(auth): reject expired refresh tokens

Keep refresh-token validation at the session seam so every caller receives
the same expiry behavior.
```

```text
refactor(skills): separate orchestration from engineering disciplines
```
