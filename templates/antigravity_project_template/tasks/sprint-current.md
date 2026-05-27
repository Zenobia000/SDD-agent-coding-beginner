# Sprint Current — <YYYY-MM-DD> ~ <YYYY-MM-DD>

> 當前 sprint 的執行清單。Solo dev 的「日曆 + 待辦」結合版。
> 大廠對標：Linear active sprint view。

---

## Sprint Goal

**一句話描述**：sprint 結束時，外人能看到什麼？

> 範例：「使用者能貼一篇英文文章、點按鈕得到 100 字中文摘要。」

---

## Now（這 2 小時要做的，只能 1-2 個）

- [ ] T-101 [S] 建立輸入框 UI + 按鈕

> **規則**：Now 區最多 2 個。避免 context switch。

---

## Next（這個 sprint 內要做）

- [ ] T-102 [S] 寫 Summarizer class 骨架 + 測試
- [ ] T-103 [M] 接 Gemini API + 處理 success case
- [ ] T-104 [S] 處理失敗 case（API 錯 / network 斷）
- [ ] T-105 [S] 加字數驗證（80-120 字）

---

## Later（下個 sprint 候選）

- [ ] T-201 [L] US-002 批次摘要
- [ ] T-202 [M] US-005 錯誤訊息友善化

---

## 🚫 Blocked

- (無)

> 如果有 blocked 條目，**寫明原因 + 解鎖條件**：
> - [ ] T-XXX [M] 接 OAuth → **Blocked**: 等 Google Cloud 專案審核 / **解鎖**：5/30 拿到 client_id

---

## ✅ Done（本 sprint 已完成）

- [x] T-100 [S] 環境 setup + .env 設定

---

## 📝 Sprint Notes

- 對應 PRD：[`docs/PRD.md`](../docs/PRD.md)
- 對應 BDD：[`tests/features/summarize.feature`](../tests/features/summarize.feature)
- 主要 risk：Gemini API 配額（先測 50 次內必須完成）
- 主要決策：[ADR-0002](../adr/ADR-0002-llm-provider.md)

---

## Daily Check-in（Solo 版 standup）

每天開始工作前，自問 3 題：

1. **昨天我完成了什麼？**（看 git log）
2. **今天我要完成什麼？**（看 Now 區）
3. **有什麼會卡住我？**（潛在的 Blocked）

寫不出 → 表示沒方向。先停下，回頭看 Sprint Goal。

---

## Sprint 結束 Checklist

Sprint 結尾跑 `/retro` 前，確認：

- [ ] Now / Next 區都已清空（移到 Done 或 Later）
- [ ] Blocked 條目有後續處理計畫
- [ ] 所有 done 條目對應的 commit 已 push
- [ ] `docs/` 與 code 沒有 critical drift（跑 `/sync-it` 確認）
