# AI-Ready Repo 藍圖：給 Antigravity CLI 的設定教學

> 用途：教初學者怎麼把一個專案「升級成 Google Antigravity 看得懂、會遵守規則的工作環境」。
> 對象：要開始用 Antigravity 桌面版 / Antigravity CLI（`agy`）協作的開發者。
> 設計原則：**README 給人看，`AGENTS.md` + `.agents/` 給 Agent 工作。**

---

## 一句話先講白

**2026 年不要再把 `AGENTS.md` 當成「提示詞筆記本」；它應該被設計成 Antigravity Agent 的「專案操作手冊 + 治理邊界 + 可執行 SOP」。**

換句話說：你寫文件的對象變了。
以前我們寫文件是給新人 onboarding。
現在我們寫文件，是給 AI 員工 onboarding。

---

## 第 0 步：先理解 `AGENTS.md` 在 Antigravity 系統裡的角色

當你用 `agy` CLI 或 Antigravity 桌面版開啟一個資料夾，平台會**自動掃描並注入** `AGENTS.md` 到 system instruction。它不是「文件」，而是：

> **Antigravity Runtime 的靜態上下文入口。**

它會直接影響 Antigravity 怎麼理解你的 repo、怎麼改程式、怎麼跑測試、什麼不能碰、什麼要先問。

`AGENTS.md` 是 Antigravity 平台採用的標準入口格式。**站立規則寫一份，Antigravity 桌面版與 CLI（`agy`）都吃**。

> **想直接動手？** 本檔所有設計都已實作在 `templates/antigravity_project_template/`，整包複製即可。對應的「實際操作手冊」是 `templates/antigravity_project_template/USAGE.md`（A 模式 / B 模式選擇器）。

---

## 第 1 步：先看「最小但完整」的目錄藍圖

> 完整目錄樹（含每個 skill / template / rule 檔名與註解）→ [`antigravity_project_template/README.md` §這個資料夾裡有什麼](./antigravity_project_template/README.md#-這個資料夾裡有什麼)（單一 SoT）

**最小骨架**（4 層分區，職責對應第 7 步分工表）：

```text
repo-root/
├── README.md / USAGE.md / AGENTS.md       # 入口三件套（人類 + Agent）
├── .agents/                               # Agent 執行細節（settings / WORKFLOW / SKILL-MAP / MCP / SKILLS / SUBAGENTS / rules / prompts / skills）
├── docs/                                  # 系統真相（PRD / HANDBOOK / templates）
└── tasks/                                 # Sprint 治理（backlog / sprint-current / known-issues / retros）
```

這個結構支撐：Antigravity 桌面版、Antigravity CLI（`agy`）、團隊開發、CI/CD、Agentic coding 工作流。

> **ADR 在哪？** 為了避免初學者一上手就被 8 個 ADR 嚇到，template 把 ADR 範本放在 `.agents/skills/adr/templates/adr-template.md`（跟 `/adr` skill 共置）。需要記錄技術決策時，自行建立 `adr/ADR-0001-<topic>.md` 即可（詳見第 6 步）。

---

## 第 2 步：搞懂文件分層 —— 誰看哪一份？

| 文件                            | 主要對象               | 用途                              |
| ----------------------------- | ------------------ | ------------------------------- |
| `README.md`                   | 人類新人               | 安裝、介紹、Quick Start               |
| `USAGE.md`                    | 人類學員              | SDD Sprint 完整使用說明 + walkthrough + FAQ |
| `AGENTS.md`                   | Antigravity Agent  | 站立規則、跨對話一致的專案總綱                 |
| `.agents/settings.json`       | Antigravity CLI    | model / checkpoint / MCP 等執行設定 |
| `.agents/WORKFLOW.md`         | Antigravity Agent  | 工作流封裝（Sprint 10 站 + 3 層 Spec）  |
| `.agents/rules/*.md`          | Antigravity Agent  | 撰寫 code 時的硬約束（細分主題）             |
| `.agents/skills/*/SKILL.md`   | Antigravity Agent  | 可手動 / 自動觸發的 slash command       |
| `.agents/skills/spec-it/templates/*.md` | 人類 + Agent | Spec 範本（PRD / user-story / API / DB / BDD / test-cases） |
| `.agents/skills/adr/templates/adr-template.md` | 人類 + Agent | ADR 範本 |
| `docs/PRD.md`                 | 人類 + Agent         | 需求規格（單一 source of truth）       |
| `docs/HANDBOOK.md`            | 人類學員              | CLI / harness engineering 學習指引 |
| `tasks/*.md`                  | 人類 + Agent         | Sprint backlog / 已知問題 / retros |
| `adr/*.md`                    | 人類 + Agent         | 技術決策歷史（template 不預設此目錄，自行建立）  |

關鍵心法：

- **站立規則放 `AGENTS.md`**（每次對話都生效）
- **執行細節放 `.agents/`**（settings + WORKFLOW + rules + skills）
- **系統真相放 `docs/` 與 `adr/`**
- **學員指引放 `USAGE.md` + `docs/HANDBOOK.md`**（給人類，不給 AI 讀）

---

## 第 3 步：`AGENTS.md` 怎麼寫？（最核心的一份）

### 定位

`AGENTS.md` 是 Antigravity 啟動時自動讀的**站立規則**。它應該回答這幾個問題：

1. 我是誰、做什麼專案
2. AI 應該扮演什麼角色
3. 必讀哪些補充文件
4. 工作流程是什麼
5. 平台特有的操作合約（Memory / Skills / MCP / Subagents）
6. 什麼絕對不能做

不要塞模型專屬語法，這份應該是「中性、可執行」的指令。

### 建議綱要（複製到專案後改成你的內容）

```markdown
# AGENTS.md

## 1. 你的角色
你是 ___ 領域的工程師，使用者是 ___。

## 2. 必讀文件（依序）
1. docs/PRD.md
2. .agents/rules/01-keep-it-simple.md
3. .agents/rules/02-coding-style.md

## 3. 工作流程
1. 重述需求
2. 列出計畫
3. 寫 code
4. 帶使用者測試
5. 等回報

## 4. Antigravity 平台規範
- Memory：可用 save_memory 記長期慣例，不要記 secrets
- Skills：.agents/skills/ 下的 markdown 是 skill + slash command
- MCP：要呼叫工具前先告知並等使用者確認
- Subagents：MVP / 單檔小專案不要派 subagent

## 5. 預設技術選擇
| 場景 | 用什麼 | 不用什麼 |
| --- | --- | --- |
| ...

## 6. 對話風格
- 講中文（繁體），技術詞保留英文
- 每段 code 配一句白話解釋
- 不要用 jargon

## 7. 絕對禁止
- 不要在未確認下裝套件
- 不要建立超過 PRD 範圍的功能
- 不要 hardcode API Key
```

> **範本完整版**：見 `templates/antigravity_project_template/AGENTS.md`，這份是已驗證可直接複製使用的學員版本。

---

## 第 4 步：`.agents/` 三大擴充原語

Antigravity 把「擴充能力」分成三個原語，分別放在 `.agents/` 下：

| 原語 | 角色 | 教學文件 |
|---|---|---|
| **MCP** | 外部能力通道（連 GitHub / 開瀏覽器 / 查文件） | [`antigravity_project_template/.agents/MCP.md`](./antigravity_project_template/.agents/MCP.md) |
| **Skills + Slash Commands** | 程序知識封裝 + hot key | [`antigravity_project_template/.agents/SKILLS.md`](./antigravity_project_template/.agents/SKILLS.md) |
| **Subagents** | 平行任務分派（大型 refactor / 跨檔案分析） | [`antigravity_project_template/.agents/SUBAGENTS.md`](./antigravity_project_template/.agents/SUBAGENTS.md) |

> 三大原語的**完整對照表 + 判斷練習** → [`SUBAGENTS.md` §三大擴充原語對照](./antigravity_project_template/.agents/SUBAGENTS.md#三大擴充原語對照mcp--skill--subagent)（單一 SoT，避免重複寫三次）

**心法**：
- MCP 是「AI 的 USB-C」，一次寫好就能接所有支援 MCP 的 agent
- Skill 是「該怎麼做的食譜」，AI 看 description 自動翻
- Subagent 是「派出去的工人」，MVP 階段不要派——能一條線跑就一條線

---

## 第 4.5 步：工作流封裝（`.agents/WORKFLOW.md`）

三大原語是「能力」；WORKFLOW.md 是把這些能力**串成可重複的工作流**的入口。

> **完整 10 站工作流（Mermaid 圖 + 每站產出 + 大廠對標）** → [`antigravity_project_template/.agents/WORKFLOW.md`](./antigravity_project_template/.agents/WORKFLOW.md)（單一 SoT）
>
> **Skill 之間的依賴與斷層分析** → [`antigravity_project_template/.agents/SKILL-MAP.md`](./antigravity_project_template/.agents/SKILL-MAP.md)

### 為什麼要把工作流「寫成檔案」？

- **AI 沒有持久記憶**：流程寫成檔案，每次新對話 AI 都會自動讀進來，不需重講
- **3 層 Spec 強迫設計先行**：L1 PRD（意圖）→ L2 API/DB（介面）→ L3 BDD（行為），缺一層 AI 就會自由發揮
- **每站對應一個 skill**：AI 看 WORKFLOW.md 就知道現在該觸發哪個 `/<command>`、要產出什麼

> **與 USAGE.md 的關係**：USAGE.md 是給人看的 SDD Sprint 使用說明（walkthrough + 陷阱 + FAQ）；WORKFLOW.md 是給 AI 看的十站流程定義（每站產出 + skill 對應）。

---

## 第 5 步：系統真相層 —— `docs/` 該放什麼？

> **Template 的取捨**：學員版 template 只放 `docs/PRD.md` + `docs/HANDBOOK.md`，把下面這些「成熟階段才需要」的文件範本改放在對應 skill 的 `templates/` 子資料夾（如 `.agents/skills/spec-it/templates/`）。等專案規模大到需要時，才從 skill 內抄出來填。下面列出的章節是各文件的**建議綱要**，方便你決定要不要加。

### `docs/architecture.md`（最重要的真相來源）

```markdown
# System Architecture

## 1. Architecture Goal
## 2. High-Level Architecture
## 3. Component Diagram
## 4. Data Flow
## 5. Request Flow
## 6. Module Boundaries
## 7. Dependency Rules
## 8. Scaling Strategy
## 9. Failure Modes
## 10. Observability
```

### `docs/domain-model.md`

```markdown
# Domain Model

## 1. Core Concepts
## 2. Entity Definitions
## 3. Aggregate Boundaries
## 4. State Transitions
## 5. Business Rules
## 6. Invariants
## 7. Example Scenarios
```

### `docs/api-contract.md`

```markdown
# API Contract

## 1. API Design Principles
## 2. Authentication
## 3. Common Response Format
## 4. Error Codes
## 5. Endpoint List
## 6. Request / Response Schema
## 7. Backward Compatibility Rules
```

### `docs/testing-strategy.md`

```markdown
# Testing Strategy

## 1. Testing Philosophy
## 2. Test Pyramid
## 3. Unit / Integration / E2E Scope
## 4. Regression Test Rules
## 5. Performance / Security Test Rules
## 6. Required Commands Before Merge
```

### `docs/security.md`

```markdown
# Security Policy for Development Agents

## 1. Secret Handling
## 2. PII / Sensitive Data Rules
## 3. Permission Boundaries
## 4. Dangerous Commands
## 5. Production Access Rules
## 6. Dependency Security
## 7. Prompt Injection Risks
## 8. MCP / Tool Risk Classification
```

### `docs/deployment.md`

```markdown
# Deployment Guide

## 1. Environments
## 2. Environment Variables
## 3. Docker Compose / Kubernetes
## 4. CI/CD Pipeline
## 5. Migration / Rollback Procedure
## 6. Release Checklist
```

---

## 第 6 步：決策治理層 —— `adr/` 為什麼一定要有？

**因為 AI 很容易「看起來合理地推翻歷史決策」。這很危險。**

ADR (Architecture Decision Record) 是避免 AI 亂改架構的關鍵防線。每個重要決策獨立一份，append-only，永不修改已通過的 ADR。

> **Template 的取捨**：學員版 template **不預設 `adr/` 目錄**——避免一開始就要面對 8 個 ADR 的心理負擔。ADR 範本放在 `.agents/skills/adr/templates/adr-template.md`（與 `/adr` skill 共置），需要時自己 `mkdir adr/` 即可。

### ADR 範本

```markdown
# ADR-0001: Use PostgreSQL as Primary Database

## Status
Accepted

## Context
為什麼需要這個決策？現狀有什麼痛點？

## Decision
我們決定採用什麼？

## Consequences
好處是什麼？
代價是什麼？
未來什麼情況要重評估？
```

### 建議至少建立的 ADR

```text
adr/
├── ADR-0001-tech-stack.md
├── ADR-0002-frontend-framework.md
├── ADR-0003-backend-framework.md
├── ADR-0004-database-design.md
├── ADR-0005-authentication.md
├── ADR-0006-deployment-strategy.md
├── ADR-0007-observability.md
└── ADR-0008-ai-agent-governance.md
```

---

## 第 7 步：怎麼切 `AGENTS.md` / `.agents/` / `docs/` / `adr/` 的職責？

### 最佳分工表

| 文件                       | 該放什麼                       | 不該放什麼                |
| ------------------------ | -------------------------- | -------------------- |
| `README.md`              | 給新人看的安裝與介紹                 | 給 Agent 的細碎工作規則      |
| `USAGE.md`               | 模式選擇器（A vs B 路徑）、第一次跑的 walkthrough | 完整工作流細節（那是 WORKFLOW.md 的事） |
| `AGENTS.md`              | 角色、必讀清單、工作流程、平台規範、絕對禁止     | 完整 PRD、完整 ADR、太長的架構細節 |
| `.agents/WORKFLOW.md`    | Sprint 站別、3 層 Spec、每站觸發的 skill | 各 skill 的具體步驟（那是 `.agents/skills/*` 的事） |
| `.agents/rules/*`        | 細分主題的硬約束（命名、錯誤處理、安全）       | 一次性任務指令              |
| `.agents/skills/*`       | 可手動 / 自動觸發的程序流程            | 通用文件全文               |
| `docs/PRD.md`            | 當前產品需求、acceptance criteria | 歷史版本（用 git history）  |
| `docs/HANDBOOK.md`       | CLI / harness engineering 學員指引 | 給 AI 的執行規則（那是 AGENTS.md 的事） |
| `.agents/skills/*/templates/*` | 可複用的文件範本（與 skill 共置）   | 已填好的真實內容             |
| `tasks/*`                | sprint backlog、known-issues、retros | 給 AI 的硬約束（那是 rules/ 的事） |
| `adr/*.md`               | 技術決策歷史                     | 當前操作 SOP            |

---

## 第 8 步：實務上最容易犯的 4 個錯

### 錯誤 1：把所有東西都塞進 `AGENTS.md`

結果上下文爆炸，Agent 反而抓不到重點。
`AGENTS.md` 應該像索引和站立規則，不是百科全書。細節下放到 `.agents/rules/` 與 `docs/`。

### 錯誤 2：把 `.agents/skills/` 寫成空殼

只寫描述、沒有可執行步驟，AI 觸發了也不知道做什麼。
**Skill 必須是「AI 看得懂、做得到」的具體流程**，不是抽象口號。

### 錯誤 3：文件寫得很抽象

❌ `請寫出高品質程式碼。`
✅ `When changing API behavior: 1) Update docs/api-contract.md. 2) Add integration test.`

### 錯誤 4：寫了但從不更新

文件與 code 漂移後比沒寫還糟，因為 AI 會根據過期文件做出錯誤推論。
**Rule of thumb：行為變更必須同步更新 `docs/`，否則 PR 不能合。**

---

## 第 9 步：完整版藍圖（給已經上手的人）

學員版 template 的目錄樹見[第 1 步連結到的 README](./antigravity_project_template/README.md#-這個資料夾裡有什麼)。當專案規模變大，**漸進加入以下檔案**（不要一次全建）：

**`.agents/` 新增**：
- `memory/` — 長期慣例、跨 sprint 學到的 pattern

**`docs/` 漸進加入**：
| 加什麼 | 何時加 |
|---|---|
| `architecture.md` | 系統規模 > 5 模組時 |
| `domain-model.md` | 出現多個 entity 時 |
| `api-contract.md` | 對外 API 多於 5 個時 |
| `testing-strategy.md` | 測試金字塔需要顯式規範時 |
| `quality-gate.md` | 有 CI/CD 時 |
| `security.md` | 處理敏感資料時 |
| `deployment.md` | 上 production 前 |
| `observability.md` | 要監控 SLO 時 |

**`adr/` 首次架構決策時建立**（建議 8 份骨架）：
`ADR-0001-tech-stack` / `0002-frontend-framework` / `0003-backend-framework` / `0004-database-design` / `0005-authentication` / `0006-deployment-strategy` / `0007-observability` / `0008-ai-agent-governance`

**`tasks/` 新增**：
- `release-plan.md` — 開始有 release cadence 時加

額外的任務管理層：

```markdown
# tasks/backlog.md
## Now / Next / Later / Blocked

# tasks/sprint-current.md
## Sprint 目標 / 任務拆解（每個任務半天可完成） / Definition of Done

# tasks/known-issues.md
## Issue / Impact / Workaround / Owner / Target Fix

# tasks/retros/YYYY-MM-DD.md
## 4Ls：Liked / Learned / Lacked / Longed for

# tasks/release-plan.md
## Version / Scope / Risk / Test Plan / Rollback Plan
```

> **升級節奏**：不要一次把所有 `←` 註記的檔案都建出來。每次只在「真的需要」時加一個——例如出現第二個 entity 才加 `domain-model.md`，第一次上線前才加 `deployment.md`。提前加會變成文件腐爛源頭。

---

## 第 10 步：怎麼驗證 Antigravity 真的有讀進去？

| 動作                       | 怎麼做                                                   |
| ------------------------ | ----------------------------------------------------- |
| 確認 `AGENTS.md` 載入        | 在 `agy` CLI 內打 `/memory show`，看內容有沒有列出來              |
| 改完 `AGENTS.md` 不重啟       | 打 `/memory refresh` 強制重讀                              |
| 確認 `.agents/skills/` 註冊  | 打 `/help` 看 slash command 清單有沒有你的 skill              |
| 確認 MCP 工具掛載              | 打 `/mcp` 看當前狀態與已連線的 server                            |
| 測試規則生效                   | 故意給一個違反規則的指令（例如要求 hardcode API Key），看 Antigravity 會不會拒絕 |

**如果它沒讀到，再華麗的規則也是裝飾品。**

---

## 五歲小孩版心法

想像你請一個很聰明但剛進公司的新人幫你改系統。

你不能只說：

> 幫我變好。

你要告訴他：

> 這是廚房，這是客廳，這個抽屜不能打開，這個開關不能亂按，改完要檢查水有沒有漏。

`AGENTS.md` + `.agents/` + `docs/` + `adr/` 就是在做這件事。

---

## 三句口訣（背起來就好）

1. **站立規則放 `AGENTS.md`**
2. **執行細節放 `.agents/`**
3. **系統真相放 `docs/` 與 `adr/`**

---

## 附錄：建議的 onboarding 步驟（給今天就要動手的人）

### 快速路徑（推薦）

1. **整包複製 `templates/antigravity_project_template/`** 到你的 repo 根目錄
2. **打開 `USAGE.md`** 看 SDD Sprint 十站怎麼跑（含完整 walkthrough）
3. **填 `docs/PRD.md`** 第 1-3 節（不會填 → 用 `/spec-it` 讓 AI 問你）
4. **用 `agy` 開啟資料夾**，跑 `/memory show` 確認 `AGENTS.md` 有被讀到
5. **開始用 Antigravity 改 code**

### 從零自建（給想理解每個檔案存在原因的人）

1. **複製第 1 步的「最小但完整」目錄藍圖**
2. **先填 `AGENTS.md` 第 1-3 節**（角色 / 必讀清單 / 工作流程），其他章節先留 TODO
3. **建立 `.agents/settings.json`**（最小設定：model + checkpointing）
4. **建立 `.agents/WORKFLOW.md`**（從 template 複製 Sprint 10 站結構）
5. **建立 `docs/PRD.md` 骨架**（即使只有標題也好）
6. **規模大到需要決策記錄時**，再 `mkdir adr/` + 用 `.agents/skills/adr/templates/adr-template.md` 建第一份 ADR
7. 用 `agy` 開啟資料夾，跑 `/memory show` 確認 `AGENTS.md` 有被讀到
8. 開始用 Antigravity 改 code

這個流程跑兩週，你的 repo 就會變成「Antigravity 進來就上手」的工作環境。

---

## 參考資料

- Antigravity 官方：[antigravity.google](https://antigravity.google/)
- AGENTS.md 社群規範：[agents.md](https://agents.md/)
- OpenAI Codex `AGENTS.md` 規範（同格式）：[developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)
- 本專案的可複製模板：`templates/antigravity_project_template/`
