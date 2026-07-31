# Project Backlog

> 整個專案的未來任務總清單。
> 大廠對標：Linear / Jira 的 backlog grooming 格式。
> 維護方式：每個 sprint 開始時跑 `內建 plan 模式` 從這裡挑任務、結束時跑 `/ship` 加新任務。

---

## P0 — Critical（不做專案不完整）

- [ ] [US-001](../docs/PRD.md#us-001) 摘要主流程 [M] [Sprint 1]
- [ ] [US-004](../docs/PRD.md#us-004) 多語言輸出 [M] [Sprint 2]

## P1 — Important（核心體驗）

- [ ] [US-002](../docs/PRD.md#us-002) 批次摘要 [L] [Sprint 2-3]
- [ ] [US-005](../docs/PRD.md#us-005) 錯誤訊息友善化 [S] [Sprint 2]

## P2 — Nice to have（不做也能上線）

- [ ] [US-003](../docs/PRD.md#us-003) 歷史記錄 [M] [Later]
- [ ] [US-006](../docs/PRD.md#us-006) 主題標籤 [L] [Later]

## 🧪 Ideas（未進 PRD，尚未驗證）

- 個人化摘要長度設定
- 摘要 + 翻譯雙模式
- 匯出成 PDF / Markdown
- 分享連結

---

## Size 參考

| Size | 估時 | 範例 |
|---|---|---|
| XS | < 2 小時 | 改文字、調樣式、加按鈕 |
| S | 半天 | 一個小元件、一個 API endpoint |
| M | 1 天 | 一個完整 feature 含測試 |
| L | 2-3 天 | 跨模組功能，需要先設計 |
| XL | > 3 天 | **過大，必須拆** |

## 標記說明

- `[Sprint N]` — 預計排入哪個 sprint
- `[Later]` — 暫不排程，等其他條件滿足
- `[Blocked: <reason>]` — 被什麼擋住
- `[P0 / P1 / P2]` — Priority

---

## 維護鐵律

1. 每個條目必須對應 PRD 的 user story（除了 Ideas 區）
2. 每個條目必須有 Size 估算
3. 已完成的條目移到 `tasks/done.md`（archive），不留在 backlog
4. Backlog 條目超過 30 條 → 整理 / 砍 Ideas / 重新審視 P2
