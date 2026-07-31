---
name: code-review
description: 對固定基準以來的完整變更集做獨立雙軸審查，涵蓋 commits、staged、unstaged 與 untracked files；Standards 檢查 repo 標準與程式品質，Spec 檢查漏做、做錯與 scope creep。當使用者要 review branch、PR、diff、working tree，或 implement skill 收尾時使用。
---

# Code Review

Standards 與 Spec 必須由隔離 context 的 agents 平行審查，再並列呈現；不要讓其中一軸替另一軸洗掉問題。

## 1. 固定比較基準

使用者指定的 commit、branch、tag 或 merge-base 就是 fixed point。沒有指定時：

- `/implement` 呼叫本 skill 時沿用實作開始前記錄的 fixed point。
- 獨立 review 時先從 upstream branch/merge-base 推斷並展示；若有多個合理基準才問一題。

先執行：

- `git rev-parse <fixed-point>` 固定基準。
- `git status --short` 找出 staged、unstaged 與 untracked files。
- `git diff <fixed-point> --` 取得 fixed point 到目前 working tree 的 tracked changes。
- `git log <fixed-point>..HEAD --oneline` 取得其間 commits。
- `git ls-files --others --exclude-standard` 列出 diff 不包含的 untracked files，交給 reviewers 直接讀取。

只有 tracked diff、commit list 與 untracked files 全部為空時才停止。使用者明確只要求 committed branch/PR diff 時，才改用 `<fixed-point>...<target>`，並說明 working tree 不在審查範圍。ref 不存在就停止，不把錯誤丟給 agents。

## 2. 找規格來源

依序找：使用者指定路徑/URL、implement ticket、commit/branch 對應 issue、project contract 的 specs 位置。讀完整 body 與必要 comments。找不到時 Spec 軸標示「無規格來源」，不要用 code 反推規格。

## 3. 找標準來源

讀 `docs/agents/project.md`、相關 repo rules、CONTRIBUTING、style guide、glossary 與 ADR。工具可機械判斷的 formatter/lint/type 問題交給命令，不要讓 reviewer 重複猜。

## 4. 平行審查

在同一個訊息同時呼叫：

- `standards-reviewer`：提供 fixed point、完整 diff 命令、commit list、untracked paths 與 standards paths。
- `spec-reviewer`：提供相同 fixed point、diff、commits、untracked paths 與 spec path 或內容。沒有 spec 時不啟動。

兩者不能看到對方輸出，也不能修改檔案。若變更涉及認證、授權、付款、上傳、秘密、外部 API 或不可逆資料變更，再獨立呼叫 `security-reviewer`，但不要把 Security 合併進前兩軸。

## 5. 聚合

依序輸出 `## Standards`、`## Spec`，必要時加 `## Security`。保留各軸自己的嚴重度與排序，不跨軸選出單一總冠軍。

最後只總結：各軸 finding 數、每軸最嚴重項、review 未能驗證的事項。沒有 findings 也要說明讀過哪些來源與跑過哪些命令。
