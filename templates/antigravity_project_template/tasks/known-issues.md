# Known Issues

> 已知但暫時不修的問題清單。
> 大廠對標：GitHub Issues / Linear 的「Wontfix / Backlog」狀態。
> 維護方式：發現 bug 但 sprint 內不修 → 進這份；每 sprint retro 審視一次。

---

## 為什麼需要這份檔案

**不寫下來的 bug 會在腦中累積、變成焦慮、最後忘記。**

寫下來後：
- AI 進 session 能看到「這些是已知問題，不要 surprise」
- 6 個月後你能客觀評估「哪些變嚴重了、哪些自動消失了」
- 退技術債時有具體清單

---

## 標準格式

```markdown
## ISSUE-NNN: [一句話描述]

| 項目 | 內容 |
|---|---|
| **發現日** | YYYY-MM-DD |
| **影響範圍** | 哪個功能 / user story |
| **嚴重度** | Critical / High / Medium / Low |
| **重現步驟** | 1. ... / 2. ... / 3. ... |
| **預期** | 應該怎樣 |
| **實際** | 實際怎樣 |
| **暫時對策** | 使用者怎麼避開 |
| **修法草案** | 大概要怎麼修 |
| **延後原因** | 為什麼這 sprint 不修 |
| **重評估時機** | 什麼條件下要重排優先 |
```

---

## 範例

## ISSUE-001: Safari 上輸入框字體跑掉

| 項目 | 內容 |
|---|---|
| **發現日** | 2026-05-27 |
| **影響範圍** | US-001 摘要主流程的 UI |
| **嚴重度** | Low |
| **重現步驟** | 1. 用 Safari 18 打開 index.html / 2. 輸入文字 / 3. 觀察 |
| **預期** | 字體為系統字體（San Francisco） |
| **實際** | 變成 Times New Roman |
| **暫時對策** | 加一行 `font-family: -apple-system, ...` 即可 |
| **修法草案** | 在 `<input>` 元素加 `font-family: inherit` |
| **延後原因** | Sprint 1 主目標是功能跑通，UI 微調延後 |
| **重評估時機** | Sprint 2 開始時優先處理（已加入 T-202） |

## ISSUE-002: Gemini API 偶發 503 沒重試

| 項目 | 內容 |
|---|---|
| **發現日** | 2026-05-28 |
| **影響範圍** | US-001 摘要主流程的失敗處理 |
| **嚴重度** | Medium |
| **重現步驟** | 1. 連續送 20 次摘要 / 2. 觀察是否有 503 |
| **預期** | 自動 retry 1 次後才報錯 |
| **實際** | 直接報錯，使用者要手動重試 |
| **暫時對策** | 提示使用者「請點兩次摘要按鈕」 |
| **修法草案** | 寫一個 ADR 決定 retry 策略（exponential backoff / max 2 retries），實作後加 unit test |
| **延後原因** | 需要先寫 ADR-0004-api-retry-policy（已列下 sprint） |
| **重評估時機** | 使用者反饋這是首要痛點時提前處理 |

---

## 嚴重度判斷表

| 嚴重度 | 判斷 | 處理時機 |
|---|---|---|
| **Critical** | 主流程完全壞掉、有資料遺失風險、有安全漏洞 | **立刻修**，不能進這份檔案 |
| **High** | 主流程偶發失敗、無法解決的使用者抱怨來源 | 下個 sprint 必排 |
| **Medium** | 邊界 case 失效、UX 不佳但有 workaround | 2 sprint 內排 |
| **Low** | 美觀問題、罕見情境 | 有空就修，可永遠延後 |

**Critical 永遠不該出現在 Known Issues** — 看到就立刻停下、進入 incident 處理。

---

## 維護鐵律

1. **發現 bug 當下寫下來**（5 分鐘的事，省下重複發現的痛苦）
2. **每個 sprint retro 審視一次**：哪些變嚴重了？哪些可以直接刪？
3. **超過 3 sprint 還沒處理的 Low → 直接刪**（顯然不重要）
4. **使用者直接抱怨同一個 issue 2 次 → 升一級嚴重度**
5. **修完的 issue 移到 `tasks/closed-issues.md` 或直接刪**

---

## Closed Issues（已修復的）

可選擇歸檔到 `tasks/closed-issues.md`，或在 git history 找。

> Solo dev 建議：直接從本檔案刪除，留 commit message 與 git history 即可。
