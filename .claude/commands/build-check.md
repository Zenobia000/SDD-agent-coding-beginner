---
name: build-check
description: 跑目前專案的 build/compile check；命令一律從專案契約的 Quality commands 讀，沒設定就明講 unknown，不猜測。
---

# Build check

先照優先序取得 Quality commands 的 Build 欄位：`docs/agents/project.md`（存在才用）→ `CLAUDE.md`〈專案契約〉節 → 從 repo 探索。

- 有定義：執行該命令，如實回報結果（exit code、有無錯誤輸出）。
- 未定義或標記 `unknown`：直接回報「Build check 未設定，尚未驗證」，不得捏造命令。
