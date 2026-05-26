---
name: explain-code
description: Use when the user asks "what does this do", "explain this code", "解釋這段", "白話講一下這個檔案", or 想要白話解釋一段程式碼. Pulls the file, walks through it section by section in plain language, marks file:line for jumping, calls out non-obvious design decisions.
---

# Explain Code Skill

當使用者要你「解釋一段 code」時，照以下流程，**不要憑記憶**。

## 1. 確認範圍

問使用者：

- 要解釋哪個檔案 / 哪幾行？
- 解釋深度：
  - **初學者白話**（零術語，比喻為主）
  - **中等技術**（保留必要術語但解釋）
  - **深入到 implementation 細節**（呼叫鏈、邊界條件、效能考量）

如果使用者只說「解釋這個」沒指明檔案，**先列出最近改動的 3 個檔案**讓他選（用 `!git diff --name-only HEAD~3 HEAD` 或 `!ls -t` 看時間）。

## 2. 讀檔

用 `read_file` 工具讀**完整檔案**。

❌ 不要憑記憶 — AI 對程式碼的記憶常常有偏差（變數名錯、行號錯、條件反了）
❌ 不要只讀 diff — 沒有完整 context 會誤判用途

## 3. 分段講解

把檔案切成邏輯段（function / class / 區塊），**每段**：

- 用 1-2 句白話講「這段在幹嘛」
- 標出 `file:line` 讓使用者可以跳過去看
- 點出 **1 個值得注意的設計決策**（為什麼這樣寫而不是另一種）

範例格式：

> **`utils/validate.ts:14-32` — `validateEmail` function**
>
> 這段在檢查 email 格式對不對，用的是 regex 而不是呼叫外部 API。
>
> 💡 設計決策：選 regex 是因為不想為了驗證 email 引入網路請求（會慢、會失敗、會洩漏個資給第三方）。代價是只能驗格式不能驗「真的存在」。

## 4. 收尾 checklist

最後一段總結：

- 整個檔案在生態系中扮演什麼角色（是 helper / entry point / 領域模型 / API layer）
- 跟其他哪些檔案有耦合（import / export 關係）
- 建議的「閱讀順序」（如果使用者要繼續看下去，下一個該看哪個檔案）

## 禁止行為

- ❌ 不要直接貼原始碼當解釋（使用者自己會看，重複沒價值）
- ❌ 不要用 jargon 不解釋（CORS、middleware、polyfill、closure 都要白話一遍）
- ❌ 不要超出檔案範圍幫他重構（這是 explain，不是 refactor — 使用者沒要求改）
- ❌ 不要在「初學者白話」模式下用技術詞（即使加註解也不行 — 直接換比喻）

## 觸發此 skill 時的開場白

執行此 skill 時請先告訴使用者：

> 我正在用 `explain-code` skill 走解釋流程。請先告訴我：
>
> 1. 要解釋哪個檔案？（沒指定的話我列最近改動的給你選）
> 2. 深度：白話 / 中等 / 深入？

這樣使用者知道你在跑哪個 skill，方便對照行為是否正確。
