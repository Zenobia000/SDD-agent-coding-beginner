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

---

## 第 1 步：先看「最小但完整」的目錄藍圖（推薦初學者從這版開始）

```text
repo-root/
├── README.md                    # 給人看的入口
├── AGENTS.md                    # ⭐ Antigravity 一定會讀的「站立規則」
├── .agents/
│   ├── settings.json            # Antigravity CLI 設定（model / checkpoint / MCP）
│   ├── MCP.md                   # 三大擴充原語 ①：MCP 外部工具
│   ├── SKILLS.md                # 三大擴充原語 ②：Skill + Slash Command
│   ├── SUBAGENTS.md             # 三大擴充原語 ③：平行任務分派
│   ├── rules/                   # AI 寫 code 時的硬約束
│   ├── prompts/                 # 常用對話開場白
│   └── skills/                  # 自訂 skill / slash command
├── docs/
│   ├── PRD.md                   # 需求規格
│   ├── architecture.md          # 系統架構真相來源
│   ├── domain-model.md          # 領域模型與核心概念
│   ├── api-contract.md          # API 契約
│   ├── testing-strategy.md      # 測試策略
│   ├── security.md              # 安全與權限邊界
│   └── deployment.md            # 部署與環境
└── adr/
    ├── ADR-0001-tech-stack.md
    ├── ADR-0002-architecture-boundary.md
    └── ADR-0003-agent-governance.md
```

這樣的結構能支撐：Antigravity 桌面版、Antigravity CLI（`agy`）、團隊開發、CI/CD、Agentic coding 工作流。

---

## 第 2 步：搞懂文件分層 —— 誰看哪一份？

| 文件                            | 主要對象               | 用途                              |
| ----------------------------- | ------------------ | ------------------------------- |
| `README.md`                   | 人類新人               | 安裝、介紹、Quick Start               |
| `AGENTS.md`                   | Antigravity Agent  | 站立規則、跨對話一致的專案總綱                 |
| `.agents/settings.json`       | Antigravity CLI    | model / checkpoint / MCP 等執行設定 |
| `.agents/rules/*.md`          | Antigravity Agent  | 撰寫 code 時的硬約束（細分主題）             |
| `.agents/skills/*.md`         | Antigravity Agent  | 可手動 / 自動觸發的 slash command       |
| `docs/architecture.md`        | 人類 + Agent         | 系統結構真相來源                        |
| `adr/*.md`                    | 人類 + Agent         | 技術決策歷史                          |
| `docs/testing-strategy.md`    | Agent + QA         | 測試邊界與驗證流程                       |
| `docs/security.md`            | Agent + DevOps     | 權限、資料、危險操作邊界                    |

關鍵心法：

- **站立規則放 `AGENTS.md`**（每次對話都生效）
- **執行細節放 `.agents/`**（settings + rules + skills）
- **系統真相放 `docs/` 與 `adr/`**

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

### 4.1 MCP（外部能力通道）

- 在 `.agents/settings.json` 的 `mcpServers` 區塊宣告
- 詳細用法與安全警告寫在 `.agents/MCP.md`
- 常見：filesystem / fetch / github / playwright
- 心法：MCP 是「AI 的 USB-C」，**一次寫好就能接所有支援 MCP 的 agent**

### 4.2 Skills + Slash Commands（程序知識封裝）

- `.agents/skills/<name>.md` 同時是 skill 也是 slash command
- AI 可依 description 自動觸發，使用者也能打 `/<name>` 手動觸發
- 詳細結構寫在 `.agents/SKILLS.md`
- 適合放：審查流程、debug SOP、特定領域的撰寫規範

### 4.3 Subagents（平行任務分派）

- 大型 refactor / 跨檔案分析 / 超長任務時可派 subagent 平行處理
- 詳細用法寫在 `.agents/SUBAGENTS.md`
- **MVP 階段不要派**——能一條線跑就一條線

---

## 第 5 步：系統真相層 —— `docs/` 該放什麼？

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

| 文件                  | 該放什麼                       | 不該放什麼                |
| ------------------- | -------------------------- | -------------------- |
| `AGENTS.md`         | 角色、必讀清單、工作流程、平台規範、絕對禁止     | 完整 PRD、完整 ADR、太長的架構細節 |
| `.agents/rules/*`   | 細分主題的硬約束（命名、錯誤處理、安全）       | 一次性任務指令              |
| `.agents/skills/*`  | 可手動 / 自動觸發的程序流程            | 通用文件全文               |
| `README.md`         | 給新人看的安裝與介紹                 | 給 Agent 的細碎工作規則      |
| `docs/*.md`         | 系統真相來源                     | prompt-style 指令     |
| `adr/*.md`          | 技術決策歷史                     | 當前操作 SOP            |

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

當你的專案規模變大，可以擴充成這個樣子：

```text
repo-root/
├── README.md
├── AGENTS.md
├── .agents/
│   ├── settings.json
│   ├── MCP.md
│   ├── SKILLS.md
│   ├── SUBAGENTS.md
│   ├── rules/
│   ├── prompts/
│   ├── skills/
│   └── memory/
├── docs/
│   ├── PRD.md
│   ├── architecture.md
│   ├── domain-model.md
│   ├── api-contract.md
│   ├── testing-strategy.md
│   ├── quality-gate.md
│   ├── security.md
│   ├── deployment.md
│   └── observability.md
├── adr/
│   ├── ADR-0001-tech-stack.md
│   ├── ADR-0002-frontend-framework.md
│   ├── ADR-0003-backend-framework.md
│   ├── ADR-0004-database-design.md
│   ├── ADR-0005-authentication.md
│   ├── ADR-0006-deployment-strategy.md
│   ├── ADR-0007-observability.md
│   └── ADR-0008-ai-agent-governance.md
└── tasks/
    ├── backlog.md
    ├── known-issues.md
    └── release-plan.md
```

額外的任務管理層：

```markdown
# tasks/backlog.md
## Now / Next / Later / Blocked

# tasks/known-issues.md
## Issue / Impact / Workaround / Owner / Target Fix

# tasks/release-plan.md
## Version / Scope / Risk / Test Plan / Rollback Plan
```

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

1. **複製本檔的「最小但完整」目錄藍圖**到你的 repo（或直接用 `templates/antigravity_project_template/` 整包複製）
2. **先填 `AGENTS.md` 第 1-3 節**（角色 / 必讀清單 / 工作流程），其他章節先留 TODO
3. **建立 `.agents/settings.json`**（最小設定：model + checkpointing）
4. **建立 `docs/PRD.md` 與 `docs/architecture.md` 各一份骨架**（即使只有標題也好）
5. **建立 `adr/ADR-0001-tech-stack.md`**（記錄你選用的語言與框架）
6. 用 `agy` 開啟資料夾，跑 `/memory show` 確認 `AGENTS.md` 有被讀到
7. 開始用 Antigravity 改 code

這個流程跑兩週，你的 repo 就會變成「Antigravity 進來就上手」的工作環境。

---

## 參考資料

- Antigravity 官方：[antigravity.google](https://antigravity.google/)
- AGENTS.md 社群規範：[agents.md](https://agents.md/)
- OpenAI Codex `AGENTS.md` 規範（同格式）：[developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)
- 本專案的可複製模板：`templates/antigravity_project_template/`
