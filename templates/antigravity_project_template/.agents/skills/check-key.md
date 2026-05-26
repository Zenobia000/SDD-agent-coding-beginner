---
name: check-key
description: Use when the user asks to check API key setup, audit secrets, 檢查金鑰, or before pushing to git. Scans for unfilled placeholders, hard-coded keys, missing env vars, and `.gitignore` coverage.
---

# Check API Key Skill

當使用者要你檢查金鑰設定或打 `/check-key` 時，照以下流程：

1. 跑 `grep -rn "請貼上你的金鑰" .` 看是否還有未填的佔位符
2. 跑 `grep -rEn "AIza[0-9A-Za-z_-]{35}" --include="*.html" --include="*.js" .` 掃描檔案內有沒有真的 key 被寫死（這會洩漏到 git）
3. 跑 `echo $GEMINI_API_KEY | head -c 10` 確認環境變數有設（只顯示前 10 字避免完整外洩）
4. 看 `.gitignore` 有沒有把 `.env` 排除

如果有任何問題，告訴使用者：
- 哪個檔案 / 哪一行有問題
- 該怎麼修（具體指令）
- 已經 commit 過的話要不要 rotate key

如果都 OK，回一句「金鑰設定 OK」就好。
