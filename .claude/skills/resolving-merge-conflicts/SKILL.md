---
name: resolving-merge-conflicts
description: 依兩邊變更的原始意圖逐 hunk 解決進行中的 git merge 或 rebase conflict，並完成驗證。當 repo 已處於 conflict 狀態時使用。
---

# Resolving Merge Conflicts

1. 讀 `git status`、rebase/merge state、conflicting files 與雙方 commits。
2. 對每個 hunk 找 primary intent：commit message、diff、issue/PR/spec、tests 與 ADR。不要只挑語法看起來新的那邊。
3. 逐 hunk 解決。可相容就保留雙方意圖；不相容時選符合當前 merge/rebase 目標與現行 spec 的行為，記錄放棄的 trade-off。不要趁衝突發明新功能。
4. 每組相關 hunks 解完先跑 focused checks；全部解完依 `docs/agents/project.md` 跑 typecheck、tests、lint/build。
5. 搜尋殘留 conflict markers，確認 staged diff 只含解衝突需要的內容。
6. 使用者已明確要求「解決並完成 merge/rebase」時才 stage 並繼續/commit；否則停在已驗證、尚未完成狀態並回報下一個命令。

不要用 `--ours`/`--theirs` 批量覆蓋，不自動 `--abort`，也不丟棄未提交的第三方變更。
