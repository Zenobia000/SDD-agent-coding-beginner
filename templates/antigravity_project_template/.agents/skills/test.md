---
name: test
description: Use when the user asks to run tests, 跑測試, "test it", or wants a summary of test pass/fail status. Executes `npm test`, summarizes pass/fail counts, lists failures, and suggests next step.
---

# Test Skill

當使用者要你「跑測試」或打 `/test` 時，照以下流程：

1. 執行 `npm test`（若專案用其他測試框架，依 `package.json` 的 `scripts.test` 為準）
2. 把通過 / 失敗的數量摘要給我（用一句話）
3. 如果有失敗，列出失敗的測試名稱（不超過 5 個）
4. 給我一句「下一步建議」（修哪個、再跑一次、或繼續開發）

**禁止**：失敗時不要自動嘗試修，先回報讓使用者決定。
