---
name: spec-it
description: 從一句話需求生成 SDD 三層 spec（PRD / API contract / BDD scenarios）。用於新功能動工前，或既有功能要重新對齊規格時。
---

# /spec-it — Spec-Driven Development 三層生成器

## 何時觸發

- 使用者說「我要做 ___」「新增 ___ 功能」「重新規劃 ___」
- 使用者直接打 `/spec-it`
- 你看到對話進入新功能討論，但沒有對應的 PRD / spec

## 不要觸發的情況

- 改 typo / 樣式 / 註解 → 過度設計
- 修 bug → 改用 /tdd-cycle（先寫測試重現 bug）
- 已經有完整 spec 的功能再次討論 → 改用 /sync-it

---

## 執行步驟

### Step 1：意圖澄清（問 5 題）

不要動手就寫 spec。先問使用者：

1. **這功能解什麼問題？** 誰會用？什麼情境用？
2. **成功長什麼樣？** 一句話描述 demo 情境
3. **這 sprint 不做什麼？**（明確 Non-Goals）
4. **有沒有現有的 PRD / 既存功能要對齊？**
5. **預期 sprint 長度？**（半天 / 一天 / 三天）

等使用者回答後才進入 Step 2。**5 個問題沒問過就動手 = 違反本 skill**。

### Step 2：生 Layer 1 — PRD + User Stories

依 `docs/templates/PRD-template.md` 結構，寫入 `docs/PRD.md`（若已存在則 append 新 section）：

- §1 Problem Statement（從 Q1 答案展開）
- §2 Goals / Non-Goals（從 Q2 + Q3）
- §3 Target User
- §4 User Stories — **依 `docs/templates/user-story-template.md` 寫，至少 3 個 story，每個有 AC**
- §5 Success Metrics（量化）
- §6 Out of Scope
- §7 Open Questions
- §8 Risks

### Step 3：生 Layer 2 — API / DB Schema（如需要）

若功能涉及：
- API → 依 `docs/templates/api-contract-template.md` 寫入 `docs/api-contract.md`
- DB → 依 `docs/templates/db-schema-template.md` 寫入 `docs/db-schema.md`
- 純前端 / 純本地工具 → 跳過 Step 3

### Step 4：生 Layer 3 — BDD Scenarios + Test Cases

針對 Step 2 寫的每個 user story：

- **BDD scenarios**：寫到 `tests/features/<feature>.feature`（依 `docs/templates/bdd-scenarios-template.md` 的 Gherkin 格式）
  - 主流程 1 個
  - 邊界 case 至少 2 個（短輸入 / 長輸入 / 異常）
  - 失敗 case 至少 1 個（API 失敗 / 網路斷）
- **Test case 骨架**：寫到 `tests/unit/test_<module>.py`（依 `docs/templates/test-cases-template.md` 的 AAA pattern）
  - 只寫 `def test_xxx(): pass` 骨架 + docstring，**不寫實作**（留給 /tdd-cycle）

### Step 5：更新 backlog

把每個 user story 寫進 `tasks/backlog.md`，標 Priority + Size + Status。

### Step 6：產出 Sprint Briefing

最後給使用者一段 markdown 總結：

```markdown
# Sprint Briefing — <date>

## 本 sprint 目標
- 一句話：___

## 文件已建立
- docs/PRD.md（§1-§8）
- docs/api-contract.md（如有）
- tests/features/<name>.feature
- tests/unit/test_<module>.py（骨架）
- tasks/backlog.md（新增 N 條）

## 下一步建議
1. 你 review docs/PRD.md，補 §7 Open Questions 的答案
2. 確認 BDD scenarios 符合你的期待
3. 打 `/tdd-cycle` 開始寫第一個 US-001
```

---

## 鐵律

1. **5 個澄清問題沒問完不能動手**
2. **PRD 一定要寫，API/DB 看需要寫，BDD/Test 一定要寫**
3. **User story 一定要有 AC**（Given-When-Then 三段）
4. **Non-Goals 至少寫 2 條**（防後續 AI 加功能）
5. **產出格式對齊 `docs/templates/` 範本**

---

## 與其他 skill 的關係

```
/spec-it（這個）
   │  產出 PRD + spec
   ▼
/plan-sprint  ─→ 把 spec 拆成可執行任務
   │
   ▼
/tdd-cycle    ─→ 對每個任務跑紅綠燈
   │
   ▼
/verify       ─→ 跑 lint + test + coverage
   │
   ▼
/sync-it      ─→ 比對 code 與 spec drift
```

## 範例觸發

使用者：「我想做一個批次摘要新聞的工具」

AI（你）：
> 收到。動工前我需要先澄清 5 件事（這是 /spec-it 的標準流程）：
>
> 1. **解什麼問題？** 你現在每天看新聞 / 工作上要看的內容是什麼？批次是指多少篇？
> 2. **成功長什麼樣？** 用一句話描述：「結束時我能看到 ___」
> 3. **這次不做什麼？** 例如：不做使用者登入、不做存歷史
> 4. **既有 docs/PRD.md 要不要對齊？**
> 5. **預期 sprint 長度？** 半天 / 一天 / 三天
>
> 你回答完，我就生 PRD + API spec + BDD scenarios + 測試骨架。
