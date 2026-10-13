# 範本 hook：把紅線從「建議」變成「做不到」

寫在 `AGENTS.md` 的規則，AI 大部分時候會遵守，但不是每一次。
真正不能破的紅線，要用 hook 擋：**它不是請 AI 不要做，是讓 AI 做不到。**

| Hook | 擋什麼 | 適用 |
|---|---|---|
| [`pytest-on-stop.sh`](./pytest-on-stop.sh) | 改過 `.py` 而測試沒過，agent 不能結束這一輪 | Claude Code |

回歸規格：[`test-pytest-on-stop.sh`](./test-pytest-on-stop.sh)，由 repo 的 `scripts/check.sh` 自動執行。

---

## 裝到你的專案（Claude Code）

1. 複製 hook：

   ```bash
   mkdir -p .claude/hooks
   cp <課程 repo>/2-templates/hooks/pytest-on-stop.sh .claude/hooks/
   ```

2. 在專案的 `.claude/settings.json` 加上：

   ```json
   {
     "hooks": {
       "Stop": [
         {
           "hooks": [
             { "type": "command", "command": "bash .claude/hooks/pytest-on-stop.sh" }
           ]
         }
       ]
     }
   }
   ```

   已經有 `hooks` 區塊的話，把 `Stop` 那一段併進去，不要整個覆蓋。

3. 確認它有作用：故意改壞一行程式碼，請 agent「結束這個任務」。它應該會被擋下，並開始修。

測試指令不是 `pytest -q` 的話，在 settings 的 command 前面加環境變數，例如
`PYTEST_CMD="python -m pytest -q" bash .claude/hooks/pytest-on-stop.sh`。

---

## Codex

Codex 也有 lifecycle hooks（在 Codex 裡打 `/hooks` 查看與管理），但設定格式和 Claude Code 不同。
⚠️ 這支 hook 尚未在 Codex 上驗證。Codex 使用者目前請靠 `AGENTS.tdd.md` 的文字規則，
並在每次 agent 說完成時，**自己跑一次測試**。

---

## 它擋不住什麼

這支 hook 只能保證「結束時測試是綠的」，**擋不住順序**：AI 先寫實作、後補測試，它也會放行。
「先看到紅燈」這件事，目前靠人在對話中盯 —— 也就是 Day 3 單元 11 要你親眼看紅燈的原因。
