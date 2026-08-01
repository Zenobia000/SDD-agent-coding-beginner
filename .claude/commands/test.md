---
name: test
description: 跑目前專案的測試；不帶參數跑 Full test，帶參數當作 Focused test 目標。命令一律從專案契約讀，不假設任何框架。
argument-hint: [focused test target]
---

# Test

跟其他 skill 一樣，先照優先序取得 Quality commands 的 Focused test 與 Full test：`docs/agents/project.md`（存在才用）→ `CLAUDE.md`〈專案契約〉節 → 從 repo 探索（CI 設定、manifest、既有 script）。

- 沒有 $ARGUMENTS：執行 Full test 命令。
- 有 $ARGUMENTS：把它當成 Focused test 的目標（測試模組、檔名或測試名稱），代入 Focused test 命令執行。
- 三個來源都沒有對應命令：回報「Quality commands 未定義，尚未驗證」，不得猜測或捏造指令。
- 只回報實際執行的指令與結果（pass/fail、exit code）；未跑的部分明講原因，不能寫成已通過。
