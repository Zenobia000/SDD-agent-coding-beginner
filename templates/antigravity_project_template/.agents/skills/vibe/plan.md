---
name: vibe-plan
description: Use when the user wants a plan before code, 先列計畫等我確認, 不要直接動手, "show me the plan first", or 打 /vibe:plan. Lists files to add/modify/delete with rationale and risks, then STOPS and waits for confirmation.
---

# Vibe Plan Skill — 先列計畫等我確認

當使用者要你「先列計畫」或打 `/vibe:plan` 時，**先不要動 code**，請：

1. 列出你打算【新增 / 修改 / 刪除】的所有檔案（用清單）
2. 每個檔案說一句「為什麼要這樣做」
3. 列出 1-3 個可能踩到的風險或副作用
4. 列出你不確定、需要使用者先決定的事情（如果有）
5. **停下來等使用者說 "OK" 才開始實作**

不要在這次回覆內就動手寫 code，等使用者看完計畫才決定要不要繼續。

---

**為什麼有這個 skill**：Vibe Coding 第 2 步是「列計畫」。每次都手動跟 AI 說「先列計畫」很煩，打 `/vibe:plan` 三秒搞定。
