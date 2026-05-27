# Rule 04 — Spec First

> **沒寫 spec 就寫 code = vibe coding 災難的開頭。**

## 鐵律

1. **任何新功能**動工前，必須先有 `docs/PRD.md` 對應的 user story + AC
2. **任何 API 變動**前，必須先有 `docs/api-contract.md` 對應的 endpoint 定義
3. **任何 DB schema 變動**前，必須先有 `docs/db-schema.md` 對應的 table / migration 計畫
4. **任何行為改變**都必須有對應的 BDD scenario 或 unit test 描述「正確長怎樣」

## 例外（可以跳過 spec）

- 純樣式 / 文案 / 註解修改
- 純 refactor（無行為改變）
- 修 typo
- 改 hardcoded value（如 timeout 從 5s 改 10s）
- 加 log / debug 訊息

## 觸發 `/spec-it` 的情境

| 使用者說 | 你該做 |
|---|---|
| 「我要做 ___」 | 跑 `/spec-it` |
| 「加一個 ___ 功能」 | 跑 `/spec-it` |
| 「改 ___ 的行為」 | 跑 `/sync-it` 先確認既有 spec，再決定要不要跑 `/spec-it` |
| 「優化 ___」 | 問清楚是 refactor 還是行為改變；行為改變 → `/spec-it` |
| 「修 ___ bug」 | 跑 `/tdd-cycle`，先寫能重現 bug 的失敗測試 |

## 為什麼

- **AI 沒 spec 會自由發揮** — 寫出「看起來合理但不是你要的」程式
- **6 個月後你會忘** — 沒寫下決策理由，未來重訪會把當時的取捨忘光
- **無法驗收** — 沒 AC，無法判斷「做完了」是什麼意思
- **無法 review** — 沒 spec，review 變成主觀感想

## 違反這條規則的後果

AI 會在沒有方向感的情況下：
- 自己加你沒要的功能
- 漏掉你以為理所當然的邊界 case
- 寫出與你心目中「正確」不同的行為
- 把整個 sprint 變成「再改改」「再加點」的無底洞

## 心法

> **Spec 30 分鐘，省你 5 小時返工。**
