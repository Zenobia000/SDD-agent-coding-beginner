# 課程設計總覽｜SDD × AI Coding Agent 實戰營

> 這個資料夾是**講師備課用**：投影片逐頁內容、講稿、Demo 腳本、備課清單，以及上課 repo 要怎麼改。
> 學員看的是 [`handbook/`](../handbook/README.md)；學員動手的是 [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)。
> 三者的分工：**投影片講問題與觀念、講義放完整步驟與提示詞、上課 repo 放模板與可以接手的 checkpoint**。

| 檔案 | 內容 |
|---|---|
| [`day1-slides.md`](./day1-slides.md) | D1 30 張投影片：每張的標題、畫面內容、講稿、互動、時間 |
| [`day2-slides.md`](./day2-slides.md) | D2 14 張任務導航投影片：INPUT／ACTION／OUTPUT／GATE、對應提示詞卡與 checkpoint |
| [`instructor-prep.md`](./instructor-prep.md) | 備課清單、Demo 腳本、彩排步驟、現場卡關怎麼處理 |
| [`leavebot-redesign.md`](./leavebot-redesign.md) | 上課 repo 要改什麼，才能接上這份課程設計 |

---

## 一條教學主線

| | 問題 | 落在哪 |
|---|---|---|
| **01 WHY** | 為什麼開發模式正在改變 | D1 單元 1–2 |
| **02 WHAT** | 現代軟體工程怎麼運作：Plan → Build → Verify → Ship | D1 單元 3 |
| **03 HOW** | 怎麼駕馭 Claude Code：操作、Context、Skills、Hooks | D1 單元 4–7 |
| **04 DO** | 一個請假功能，從需求走到測試驗收 | D2 單元 8–14 |

**D1 理解與探索**：觀念 50%、Demo 與操作 50%。上午講觀念，下午先讓學員看到 AI 做得到什麼，再教怎麼控制它。
**D2 專案實作**：講解 20%、操作 80%。同一個專案從頭做到尾。

**心法**：第一天認識圖紙、工具與施工方法；第二天一起蓋好一間能開門、能使用的小房間，不是整棟大樓。
**口訣**：先理解再操作；做一條完整流程；能測試才算完成。

---

## 已定案的設計決策（2026-10-24）

| 決策 | 定案 | 為什麼 |
|---|---|---|
| D2 主線 | **表單請假的垂直切片**：填表 → 驗證日期與必填 → API 存檔 → 畫面顯示狀態 → 測試通過 | D2 同時要寫規格又要做 TDD，7 小時只容得下一條確定性的流程 |
| 一句話 AI 解析 | 列入**進階挑戰**，保留解析合約、eval 句子集與注入測試 | 這是 LeaveBot 最有記憶點的部分，但它不能成為全班的完成門檻 |
| 上課 repo 起點 | **維持空地**，加上 checkpoint 分支 | 骨架由 agent 現場生成，學員看得到「從 0 開始」；卡住的組切到 checkpoint 分支接著做 |
| 前端 | **FastAPI 直接送出靜態 HTML/JS**，拿掉 Next.js | 學員的 app 不需要 Node，公司網路擋 npm 也不影響主線 |
| 工具 | **以 Claude Code 為主**，Codex 保留相容 | 教材以 `CLAUDE.md`、`.claude/skills/`、`.claude/settings.json` 為主，Codex 設定照留不教 |
| 規格文件 | 沿用上課 repo 既有的六份模板與編號 `01-brief` … `06-test-plan` | 模板與範例已經寫好、彩排過，不必改名重做 |
| 文件與圖的分工 | **Claude Code ＋ 模板**寫文件；**Archify** 畫流程、架構、ERD | Archify 是畫圖工具，不會產生 PRD、SRS。沒有另外做 `spec-authoring` skill，因為 `/grilling`、`/to-architecture` 加上模板已經在做這件事 |

⚠️ Archify 執行時需要 **Node 18 以上**（不用 `npm install`）。沒有 Node 的學員改用 Mermaid，畫在 Markdown 裡，用 VS Code 或 GitHub 預覽。

---

## 課表

每天 09:00–17:30。休息時間 10:30–10:45、12:30–13:30、15:00–15:15，不算在授課時數內，每天淨授課 7 小時。

### D1｜AI 時代軟體工程與 Coding Agent

| 時間 | 單元 | 投影片 | 學員產出 |
|---|---|---|---|
| 09:00–09:45 | 1. AI 時代的軟體開發典範轉移 | 01–03 | — |
| 09:45–10:30 | 2. 從傳統開發走向 AI 協作 | 04–07 | — |
| 10:45–12:30 | 3. AI 時代的軟體工程與規格治理 | 08–15 | 一句模糊需求改寫成的驗收條件（紙本或 Markdown） |
| 13:30–14:15 | 4. Claude Code 基礎操作 | 16–18 | 讓 agent 解釋上課 repo；看過一次 diff |
| 14:15–15:00 | 5. Context Engineering 與 Agent Harness | 19–22 | `git add -A` 被 hook 擋下，說得出是哪個檔案擋的 |
| 15:15–16:30 | 6. Coding Agent 能力體驗 Demo | 23–27 | 觀察紀錄：AI 做對了什麼、做錯了什麼 |
| 16:30–17:30 | 7. 使用 Archify 建立專案規格 | 28–30 | `playground/` 裡的 PRD 草稿與一張流程圖 |

### D2｜請假系統從 0 到 1

| 時間 | 單元 | 投影片 | 提示詞卡 | 學員產出 | checkpoint |
|---|---|---|---|---|---|
| 09:00–09:45 | 8. 專案啟動與需求探索 | 31–32 | — | `docs/01-brief.md`（需求簡報卡） | |
| 09:45–10:30 | 9. AI 輔助需求分析 | 33–34 | A、B | 需求問答紀錄、`docs/02-prd.md` | `cp1-requirements` |
| 10:45–12:30 | 10. 規格驅動的系統分析與設計 | 35–37 | C、D、E | `docs/03-srs.md`、`diagrams/`、`docs/04-sad.md`、`docs/05-sds.md` | `cp2-design` |
| 13:30–14:15 | 11. 任務拆解與 TDD 測試先行 | 38–39 | F、G | `docs/06-test-plan.md`、`issues/`、骨架起得來 | `cp3-tests` |
| 14:15–15:00 | 12. 垂直切片開發 | 40 | H | 新增請假的切片，測試由紅轉綠 | `cp4-working-feature` |
| 15:15–16:30 | 13. AI 除錯、重構與驗證 | 41–42 | I、J | 破壞測試紀錄、需求變更的影響分析與回歸結果 | |
| 16:30–17:30 | 14. 版本交付與企業導入 | 43–44 | K | commit、交付檢查表、成果發表 | `cp5-delivered` |

---

## 對照表：投影片 ↔ 講義 ↔ 上課 repo

| 投影片 | 講義段落 | 上課 repo 用到的東西 |
|---|---|---|
| 01–15 | [`02-day1.md`](../handbook/02-day1.md) 單元 1–3 | — （純觀念；單元 3 的例子用 `course/LEAVEBOT.md` 的請假情境） |
| 16–18 | 單元 4 | 整個 repo（唯讀探索）、`git status`、`git diff` |
| 19–22 | 單元 5 | `CLAUDE.md`、`AGENTS.md`、`.claude/skills/`、`.claude/hooks/`、`.claude/settings.json`、`.mcp.json`、`course/HARNESS.md` |
| 23–27 | 單元 6 | 講師在自己的 `playground/` 現場 Demo；學員可以跟著做 |
| 28–30 | 單元 7 | `playground/`、`course/templates/02-prd.md`、`.claude/skills/archify/` |
| 31–32 | [`03-day2.md`](../handbook/03-day2.md) 單元 8 | `course/LEAVEBOT.md`、`course/templates/01-brief.md` |
| 33–34 | 單元 9 | `/grilling`、`course/templates/02-prd.md`、`course/examples/it-asset/02-prd.md` |
| 35–37 | 單元 10 | `course/templates/03-srs.md`～`05-sds.md`、Archify、`/to-architecture`、`course/STACK.md` |
| 38–39 | 單元 11 | `course/templates/06-test-plan.md`、`/to-tickets`、`course/STACK.md` 的骨架步驟 |
| 40 | 單元 12 | `/tdd`、`issues/001-*.md` |
| 41–42 | 單元 13 | `/diagnosing-bugs`、`docs/LESSONS.md` |
| 43–44 | 單元 14 | `/code-review`、`git`、`gh`（講師示範 PR 與 CI） |

完整提示詞在 [`handbook/appendix/prompt-book.md`](../handbook/appendix/prompt-book.md)。投影片只放卡號和一行摘要。

---

## Checkpoint 分支

上課 repo 的 `main` 是空地。講師彩排時把 D2 從頭到尾跑一次，每過一個關卡就推一個分支。

| 分支 | 時間 | 裡面有什麼 |
|---|---|---|
| `cp1-requirements` | 10:30 | `docs/01-brief.md`、`docs/02-prd.md` |
| `cp2-design` | 12:30 | 再加 `docs/03-srs.md`、`04-sad.md`、`05-sds.md`、`diagrams/` |
| `cp3-tests` | 14:15 | 再加 `docs/06-test-plan.md`、`issues/`、骨架（`GET /api/health` 與首頁）。測試全綠，還沒有任何業務測試；紅燈在單元 12 由各組自己寫出來 |
| `cp4-working-feature` | 15:00 | 新增請假的垂直切片，測試全綠 |
| `cp5-delivered` | 17:00 | 需求變更已處理、回歸測試全綠、交付檢查表 |
| `advanced-ai-parse` | — | 進階挑戰的參考解：一句話解析、eval、注入測試 |

學員怎麼切過去，寫在講義 D2 開頭。原則：**落後超過 15 分鐘就切，不要硬撐。** 這是教學進度的檢查點，不要求每一組都同步。

---

## 投影片的編排原則

- **D1**：每個單元走同一個節奏：提出問題 → 建立觀念 → 示範工具 → 學員操作 → 檢查產出。每 30–40 分鐘至少一次互動。
- **D2**：任務導航式。每張只放四格：**INPUT**（本次輸入）、**ACTION**（操作與卡號）、**OUTPUT**（預期產出路徑）、**GATE**（完成條件）。
- **一頁只做一件事；每一步都有完成標準；卡住就切 checkpoint。**
- 正式備課的順序：**先把 D2 完整彩排一次，再做投影片。** 流程能在 7 小時內穩定跑完，每頁要講到哪裡、停在哪裡自然就清楚了。
