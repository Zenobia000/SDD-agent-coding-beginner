# Rule 05 — TDD Required

> **先寫測試。GREEN 之前不要寫實作。**

## 鐵律

1. **任何新功能**必須先寫測試（紅燈）→ 再寫實作（綠燈）→ 重構（保持綠燈）
2. **任何 bug 修復**必須先寫能重現 bug 的失敗測試 → 再修
3. **任何 refactor** 必須有現存綠燈測試保護（沒測試覆蓋的 code 不允許重構）
4. **Coverage 目標**：unit 80%、integration 主流程 100%、E2E 關鍵 user journey 100%

## 例外（可以跳過 TDD）

- 純樣式 / CSS 調整（無邏輯）
- 純文案修改
- 純 log / debug 訊息
- 一次性 script（會在這個 sprint 內刪掉的）

## 觸發 `/tdd-cycle` 的情境

| 使用者說 | 你該做 |
|---|---|
| 「實作 US-XXX」 | 跑 `/tdd-cycle` |
| 「寫 ___ 功能」 | 跑 `/tdd-cycle` |
| 「我要動手了」 | 跑 `/tdd-cycle` |
| 「修 ___ bug」 | 跑 `/tdd-cycle`（先寫重現 bug 的測試） |
| 「重構 ___」 | 確認有測試覆蓋 → 進行重構（保持綠燈）|

## 為什麼先寫測試

- **強迫你想清楚「正確長怎樣」** — 不寫 AC 就寫不出測試
- **避免 over-engineering** — GREEN 階段只寫剛好夠用的程式
- **重構有靠山** — 測試是 contract，重構過程綠燈代表行為沒變
- **AI 可信度上升** — AI 寫的 code 跑得過你寫的測試 = 它真的懂你要什麼

## 違反這條規則的後果

「先寫 code 再補測試」的問題：

- 測試會傾向確認「現在這樣寫」是對的（confirmation bias）
- 邊界 case 容易漏（因為實作時沒想到）
- 看起來覆蓋率很高，實際品質沒提升
- AI 寫 code 時沒有「對齊目標」，容易發散

## 反例（不要這樣做）

```
❌ 使用者：「實作 US-001」
   AI：「好的我寫⋯⋯」（直接寫 app/summarizer.py 200 行 + 補 5 個測試）
```

```
✅ 使用者：「實作 US-001」
   AI：「跑 /tdd-cycle。Step 1 RED：我寫第一個失敗測試⋯⋯」
       （寫 test_summarize_xxx → 跑 → 紅 → 寫最少實作 → 跑 → 綠 → 重構 → 下一個測試）
```

## 心法

> **GREEN 之前不要寫實作。GREEN 之後才能重構。**

> **沒測試的 code 不存在。**（Michael Feathers, Working Effectively with Legacy Code）
