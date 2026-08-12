---
name: test
description: 執行目前專案的測試並如實回報結果。使用者有指定測試目標時當 Focused test 跑，沒有指定時跑 Full test。命令一律從專案契約的 Quality commands 讀，不假設任何測試框架。當使用者要求跑測試、驗證某個測試檔或測試名稱是否通過，或某個工作收尾需要測試證據時使用。
---
# Test

先照優先序取得 Quality commands 的 Focused test 與 Full test：`docs/agents/project.md`（存在才用）→ `AGENTS.md`〈專案契約〉節 → 從 repo 探索（CI 設定、manifest、既有 script）。

- 使用者沒有指定測試目標：執行 Full test 命令。
- 使用者有指定測試目標（測試模組、檔名或測試名稱）：把它代入 Focused test 命令執行。
- 三個來源都沒有對應命令：回報「Quality commands 未定義，尚未驗證」，不得猜測或捏造指令。
- 只回報實際執行的指令與結果（pass/fail、exit code）；未跑的部分明講原因，不能寫成已通過。
