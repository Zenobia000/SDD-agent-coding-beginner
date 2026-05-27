---
name: adr
description: 產生 MADR v3.0 格式的 Architecture Decision Record。**主動觸發時機**：對話出現多個技術選項在比較（「X 還是 Y」「___ vs ___」「用 ___ 還是 ___ 比較好」），或使用者要選 LLM provider / DB / 框架 / auth / 部署目標時。注意：PRD 已寫死的技術不需要 ADR。
---

# /adr — Architecture Decision Record 生成器

## 🚨 自動觸發訊號（AI 主動偵測）

依 `rules/07-proactive-skill-trigger.md`，AI 要監測對話、發現訊號主動建議。

### 強訊號（高機率該觸發）

- 「X 還是 Y」「用 ___ 還是 ___」「___ vs ___」
- 「___ 跟 ___ 哪個比較好」「我該選 ___ 還是 ___」
- 「要不要用 ___」（在多選項背景下）
- 使用者列出 2+ 個技術選項並比較利弊

### 中訊號（建議但詢問）

- 「我選 ___」（在沒寫 ADR 的情況下做重大選型）
- 對話中提到 LLM provider / DB / 主要框架 / auth 機制 / 部署目標
- 「___ 適合嗎」「___ 有什麼好處」

### 反訊號（這些不要觸發 adr）

- **PRD 已經寫死**「使用 Gemini API」這類外部約束 → 不需要 ADR（PRD 已捕捉）
- 局部小決定：「用哪個 lodash function」「fetch() 還是 axios」
- 純樣式：「按鈕用藍色」「字體用什麼」
- 還在探索期、沒有具體選項在競爭

### 寫 ADR 的 3 題自檢（給 AI 判斷用）

主動建議前，先檢查 3 題：

1. 影響超出單一 user story 嗎？
2. 有 2+ 個合理選項在競爭嗎？
3. 3 個月後想換會痛嗎？

**3 題都 Yes → 建議寫 ADR。任一 No → 不建議。**

### 主動建議的話術範例

> 我注意到你在比較 Gemini 跟 OpenAI — 這算是 ADR 等級的決策（影響全專案、3 個月後想換很痛、有多個競爭選項）。
>
> 要不要跑 `/adr`？這個 skill 會幫你寫一份 1 頁的決策記錄，3 個月後 AI 看到會自動參考、不會自作主張把 Gemini 改回 OpenAI。
>
> 要 / 不要 / 之後再說？

### Solo dev 實際 ADR 數量參考

| 專案規模 | ADR 數量 |
|---|---|
| 半天 demo | 0-1 個 |
| 一週 MVP | 2-4 個 |
| 一個月專案 | 5-10 個 |

寫太多反而是 over-engineering。Solo 半天~一週專案 **0-3 個就夠用**。

---

## 何時觸發

- 使用者說「我們要選 ___」「用 A 還是 B」「決定一下 ___」
- 使用者打 `/adr`
- 重大技術選型出現（DB / 框架 / 部署 / auth / LLM provider）

## 不要觸發的情況

- **PRD 已涵蓋此決策**（PRD 寫「使用 X」屬於外部約束，不是決策）
- 一次性的局部決定（用哪個 lib function、要不要加 cache）
- 還在探索期、沒有具體選項
- 該決策已有 ADR（這時跑 `/sync-it` 確認沒漂移）

---

## 大廠對標

採 **MADR v3.0**（Markdown ADR，ThoughtWorks Tech Radar 採用 / GitHub 上最廣泛格式）。
範本見 `docs/templates/adr-template.md`。

---

## 執行步驟

### Step 1：確認這是 ADR 等級的決策

問使用者 3 題：

1. 這個決策**影響範圍**有多大？（單一檔案 / 單一模組 / 全專案）
2. 如果**3 個月後想換**，會多痛？（換 import / 改 10 個檔 / 重寫一半）
3. 有沒有**多個合理選項**在競爭？

3 題都「大 / 痛 / 是」→ 寫 ADR。任一條「小 / 不痛 / 只有一個選項」→ 不需要 ADR。

### Step 2：找下一個 ADR 編號

掃描 `adr/` 目錄，找到最大編號 + 1：

```bash
ls adr/ADR-*.md | sort -r | head -1
# adr/ADR-0004-deployment-target.md
# → 下一個是 ADR-0005
```

檔名格式：`adr/ADR-NNNN-kebab-case-title.md`

### Step 3：產生 ADR 草稿

依 `docs/templates/adr-template.md` 結構填寫：

```markdown
# ADR-NNNN: <動詞開頭的標題>

## Status
Proposed

## Context and Problem Statement
[從使用者的問題描述展開：為什麼需要這個決策？現狀有什麼痛點？]

## Decision Drivers
- 驅動 1
- 驅動 2
- 驅動 3

## Considered Options
- Option A：___
- Option B：___
- Option C：___

## Decision Outcome
**Chosen option：Option ___**

理由：___

### Consequences
**好處：** ___
**代價：** ___
**未來重評估時機：** ___

## Pros and Cons of the Options

### Option A
- ✅ Pro：___
- ❌ Con：___

### Option B
- ✅ Pro：___
- ❌ Con：___

## References
- 相關 ADR：[[ADR-NNNN]]
- 外部資料：___
- PRD 關聯：[[docs/PRD.md#section-N]]
```

**鐵律：** Options 至少 2 個（只有 1 個叫公告，不叫決策）。

### Step 4：標記為 Proposed，等使用者確認

寫完後：

```
ADR-NNNN 草稿已寫到 adr/ADR-NNNN-xxxxx.md（Status: Proposed）。

請 review：
1. Decision Drivers 列得完整嗎？有沒有漏？
2. Options 完整嗎？有沒有第 4 個方向？
3. Chosen option 與你心中的選擇一致嗎？

你確認後我把 Status 改成 Accepted，並更新相關文件參照。
```

**不要直接 Accepted** — 等使用者明確確認。

### Step 5：使用者確認後

1. 把 ADR Status 從 `Proposed` 改 `Accepted`
2. 加上日期：`Accepted (YYYY-MM-DD)`
3. 在 `docs/PRD.md` 或 `docs/architecture.md` 相關段落加 `→ See ADR-NNNN`
4. 若新 ADR 推翻舊 ADR：
   - 把舊 ADR Status 改成 `Superseded by ADR-NNNN`
   - 在新 ADR 的 References 段加 `Supersedes ADR-MMMM`

---

## ADR 範例（精簡）

```markdown
# ADR-0003: Use localStorage Instead of Backend Database for MVP

## Status
Accepted (2026-05-27)

## Context and Problem Statement
本工作坊學員多為非工程背景，要在 4 小時內做出可運行 demo。後端 DB 會引入：環境設定、auth、CORS、deploy 等多個額外維度，學員很容易卡關。

## Decision Drivers
- 學員 4 小時內必須看到完整 demo
- 不能要求學員會 docker / SQL
- 資料量小（個人筆記等級）

## Considered Options
- Option A：localStorage
- Option B：Firebase
- Option C：Postgres + Hosted (Supabase)

## Decision Outcome
**Chosen option：Option A（localStorage）**

理由：零設定、學員打開 index.html 就能用、與本工作坊「最低門檻」哲學一致。

### Consequences
**好處：** 零設定、學員 100% 能跑、教學摩擦最低
**代價：** 換裝置資料不同步、無法跨人共享
**未來重評估時機：** 學員規模上 100 人、需要跨裝置同步、需要分析使用資料

## References
- PRD：[[docs/PRD.md#section-2-goals]]
- 相關 ADR：[[ADR-0001-tech-stack]]
```

---

## 鐵律

1. **Status 只能往前走**：Proposed → Accepted → Deprecated / Superseded
2. **Accepted 後不可改內容** — 要推翻就寫新 ADR
3. **每份 ADR 只記一個決策**
4. **Considered Options 至少 2 個**
5. **Decision Drivers 至少 3 條**
6. **檔名永久編號** — 即使刪掉也保留空號
7. **檔名 kebab-case** — `ADR-0001-use-postgresql.md` 不是 `ADR-0001-UsePostgreSQL.md`

---

## 觸發範例

使用者：「我們要用 React 還是 Vue？」

AI（你）：
> 這是 ADR 等級的決策（影響全專案、3 個月後換很痛、有多個合理選項），跑 `/adr`。
>
> 動筆前先問 3 題：
>
> 1. 你 / 團隊現有 React vs Vue 經驗是？
> 2. 這專案會接 ___ 生態系（component library / state mgmt）嗎？
> 3. 預期維護年限？（demo / 1 年 / 5 年）
>
> 回答後我寫 ADR-0002-frontend-framework.md 草稿。
