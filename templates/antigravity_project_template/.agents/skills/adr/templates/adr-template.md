# ADR — Architecture Decision Record

> **Layer 1 spec（意圖層）— 記錄「為什麼這樣做」**
> 大廠對標：**MADR v3.0**（Markdown ADR，ThoughtWorks Tech Radar 採用 / 業界最廣泛格式）
> 檔名規範：`adr/ADR-NNNN-kebab-case-title.md`（例：`adr/ADR-0001-use-gemini-api.md`）
> 寫作時機：任何「會影響整個專案、3 個月後想換很痛」的決策。

---

## 為什麼要寫 ADR？

**AI 很會「看起來合理地推翻歷史決策」**。沒寫 ADR，3 個月後 AI 會建議你「重構用 Vue 重寫」而你不記得當初為什麼選了 React。

ADR 是 **append-only 的決策歷史** — 一旦 accepted，**永遠不修改**。要推翻就寫新的 ADR superseded 它。

---

## MADR v3.0 標準格式

```markdown
# ADR-NNNN: [決策標題，動詞開頭]

## Status
[proposed | accepted | deprecated | superseded by ADR-MMMM]

## Context and Problem Statement
為什麼需要這個決策？現狀有什麼痛點？相關的 user / business / technical 因素是什麼？

## Decision Drivers（決策驅動因素）
- 驅動 1（例：學員必須在 5 分鐘內看到第一個輸出）
- 驅動 2（例：成本 / 效能 / 學習曲線）
- 驅動 3

## Considered Options（考慮過的選項）
- Option A：___
- Option B：___
- Option C：___

## Decision Outcome
**Chosen option：Option X**

理由：___

### Consequences
**好處：**
- ___
- ___

**壞處 / 代價：**
- ___
- ___

**未來什麼情況要重評估：**
- ___

## Pros and Cons of the Options（各選項利弊）

### Option A：___
- ✅ Pro：___
- ❌ Con：___

### Option B：___
- ✅ Pro：___
- ❌ Con：___

### Option C：___
- ✅ Pro：___
- ❌ Con：___

## References
- 相關 ADR：[[ADR-0002]]、[[ADR-0005]]
- 外部資料：___
- PRD 關聯：[[docs/PRD.md#section-3]]
```

---

## 範例（精簡版）

```markdown
# ADR-0001: Use Google Gemini API as Primary LLM

## Status
Accepted (2026-05-26)

## Context and Problem Statement
本工作坊需要讓學員在 4 小時內做出能呼叫 LLM 的 demo。選錯 LLM provider 會卡在註冊 / 計費 / 額度。

## Decision Drivers
- 學員必須能 5 分鐘內拿到 API key
- 免費額度要足夠跑 50+ 次測試
- 文件對中文友善
- 與 Antigravity / Gemini CLI 生態原生整合

## Considered Options
- Option A：Google Gemini API（aistudio.google.com）
- Option B：OpenAI API
- Option C：Anthropic Claude API

## Decision Outcome
**Chosen option：Option A（Gemini API）**

理由：Google AI Studio 註冊一鍵搞定（GoogleID 即可），免費額度大，與本工作坊主軸 Antigravity 同生態。

### Consequences
**好處：** 入門摩擦最低、與 Antigravity CLI 零接縫整合
**壞處：** 學員回家若想換 OpenAI，需要改 fetch URL + auth header
**未來重評估時機：** Gemini 免費額度大幅縮減 / 出現更佳教學替代品

## Pros and Cons of the Options
### Option A：Gemini
- ✅ 5 分鐘拿 key、與本工作坊生態一致、免費額度高
- ❌ 鎖在 Google 生態

### Option B：OpenAI
- ✅ 業界最廣泛
- ❌ 信用卡綁定門檻、與 Antigravity 教學軸線無關

### Option C：Claude
- ✅ 程式能力強
- ❌ 台灣信用卡綁定流程曲折、無免費 web key
```

---

## 寫作鐵律

1. **Status 只能往前走**：proposed → accepted → deprecated / superseded。已 accepted 的 ADR **不可修改內容**，要推翻就寫新 ADR 並把舊的標為 `superseded by ADR-NNNN`
2. **每份 ADR 只記一個決策**：「選 React + 選 Tailwind + 選 Vite」是三個決策，三份 ADR
3. **Considered Options 至少 2 個**：只有 1 個叫公告，不叫決策
4. **Decision Drivers 一定要寫**：不寫驅動因素，未來無法判斷情境變了該不該推翻
5. **檔名永久編號**：ADR-0001 一旦發出去就不改編號，即使刪掉也保留空號

---

## 建議至少建立的 ADR

```text
adr/
├── ADR-0001-tech-stack.md           # 主要技術選型
├── ADR-0002-llm-provider.md         # LLM provider
├── ADR-0003-data-storage.md         # 資料儲存（localStorage / DB / 雲）
├── ADR-0004-deployment-target.md    # 部署目標
└── ADR-0005-ai-agent-governance.md  # AI 協作邊界
```

---

## 寫作檢查清單

- [ ] Status 寫了
- [ ] Decision Drivers 至少 3 條
- [ ] Considered Options 至少 2 個
- [ ] Consequences 同時列了好處 + 代價 + 重評估時機
- [ ] Pros / Cons 每個 option 都列了
- [ ] 檔名是 `ADR-NNNN-kebab-case.md`
