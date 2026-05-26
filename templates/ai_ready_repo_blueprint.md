# AI-Ready Repo 藍圖：給 Coding Agent CLI 的設定教學範例

> 用途：教初學者怎麼把一個專案「升級成 AI Agent 看得懂、會遵守規則的工作環境」。
> 對象：要開始用 Claude Code / Antigravity CLI / OpenAI Codex / GitHub Copilot 協作的開發者。
> 設計原則：**README 給人看，`AGENTS.md / CLAUDE.md` 給 Agent 工作。**

> ⚠️ **2026-05-26 重要更新**：Google I/O 2026（5/19）宣布把 Gemini CLI 統一到 Antigravity 平台，命令從 `gemini` 改為 `agy`、用 Go 重寫。**個人版 Gemini CLI 將於 2026-06-18 停止服務**（企業版 Gemini Code Assist Standard/Enterprise 不受影響）。Antigravity CLI 直接採用 `AGENTS.md` 業界規範，**不再使用 `GEMINI.md`**。下方文件保留三份檔名分離論述供歷史/相容性參考；新專案建議只寫 `AGENTS.md` + 視需要補 `CLAUDE.md`。Gemini CLI 舊有設定可一鍵搬遷：`agy plugin import gemini`。

---

## 一句話先講白

**2026 年不要再把 `AGENTS.md`、`CLAUDE.md` 當成「提示詞筆記本」；它們應該被設計成 AI Agent 的「專案操作手冊 + 治理邊界 + 可執行 SOP」。**

換句話說：你寫文件的對象變了。
以前我們寫文件是給新人 onboarding。
現在我們寫文件，是給 AI 員工 onboarding。

---

## 第 0 步：先理解這些 `.md` 在系統裡的角色

主流 AI coding agent 都已支援「專案上下文文件」：

- **OpenAI Codex** 工作前讀取 `AGENTS.md`，可由全域指引 + 專案層級覆蓋。
- **Google Gemini CLI** 用 `GEMINI.md` 作為預設 context file，可放專案指令、persona、coding style。
- **Anthropic Claude Code** 讀取分層 `CLAUDE.md` 作為工作記憶。
- **GitHub Copilot** 讀取 `.github/copilot-instructions.md`。

它們的本質都不是「文件」，而是：

> **Agent Runtime 的靜態上下文入口。**

它會直接影響 AI 怎麼理解你的 repo、怎麼改程式、怎麼跑測試、什麼不能碰、什麼要先問。

---

## 為什麼不能把三份合成一份？

學員最常問的問題：「都是規範文件，內容差不多，為什麼要寫三份？」

**因為檔名是給工具看的協議，不是給人看的標籤。**

| 面向         | AGENTS.md       | CLAUDE.md                  | GEMINI.md                |
| ---------- | --------------- | -------------------------- | ------------------------ |
| **誰會自動讀**  | Codex、Cursor 等多家 | 只有 Claude Code             | 只有 Gemini CLI            |
| **載入機制**   | 整檔注入            | 分層 merge（global + project） | 單檔 + memory tool 動態加     |
| **失效時的行為** | Codex 直接忽略      | Claude 仍會工作但少了 guardrail   | Gemini 不會自動 fallback     |
| **慣用語法**   | 偏 README 風      | 指令式 / forbidden list 風     | 偏 memory bullet 風        |

就算內容 100% 相同，Claude Code **不會去讀** `GEMINI.md`，反之亦然。

### 正確心法：80/20 原則

```text
共用 80%  ──→ AGENTS.md（單一真相來源）
              │
              ├─ CLAUDE.md  只寫 Claude 特有的 20% + 引用 AGENTS.md
              │
              └─ GEMINI.md  只寫 Gemini 特有的 20% + 引用 AGENTS.md
```

如果你的專案規則很少、團隊很小，也可以直接 symlink：

```bash
ln -s AGENTS.md CLAUDE.md
ln -s AGENTS.md GEMINI.md
```

什麼時候**不該** symlink？當你想針對某個 Agent 寫專屬規則時（例如：「Claude 修改前一定要先 plan」這條對 Gemini 沒意義）。

---

## 第 1 步：先看「最小但完整」的目錄藍圖（推薦初學者從這版開始）

```text
repo-root/
├── README.md                 # 給人看的入口
├── AGENTS.md                 # 多 Agent 共用主入口：專案總規則
├── CLAUDE.md                 # Claude Code 專屬規則
├── GEMINI.md                 # Gemini CLI 專屬規則
├── .github/
│   └── copilot-instructions.md  # GitHub Copilot 專屬規則
├── docs/
│   ├── architecture.md       # 系統架構真相來源
│   ├── domain-model.md       # 領域模型與核心概念
│   ├── api-contract.md       # API 契約
│   ├── testing-strategy.md   # 測試策略
│   ├── security.md           # 安全與權限邊界
│   └── deployment.md         # 部署與環境
└── adr/
    ├── ADR-0001-tech-stack.md
    ├── ADR-0002-architecture-boundary.md
    └── ADR-0003-agent-governance.md
```

這樣已經可以支撐：Claude Code、Gemini CLI、Codex、GitHub Copilot、Cursor / Windsurf、團隊開發、CI/CD、Agentic coding 工作流。

---

## 第 2 步：搞懂文件分層 —— 誰看哪一份？

| 文件                            | 主要對象             | 用途                              |
| ----------------------------- | ---------------- | ------------------------------- |
| `README.md`                   | 人類新人             | 安裝、介紹、Quick Start               |
| `AGENTS.md`                   | 所有 coding agents | 共用工作規則、跨模型一致                    |
| `CLAUDE.md`                   | Claude Code      | Claude 專屬偏好、工作流程、工具限制           |
| `GEMINI.md`                   | Gemini CLI       | Gemini 專屬 context / memory / 指令 |
| `.github/copilot-instructions.md` | GitHub Copilot   | IDE 補全與 GitHub 工作流              |
| `docs/architecture.md`        | 人類 + Agent       | 系統結構真相來源                        |
| `adr/*.md`                    | 人類 + Agent       | 技術決策歷史                          |
| `docs/testing-strategy.md`    | Agent + QA       | 測試邊界與驗證流程                       |
| `docs/security.md`            | Agent + DevOps   | 權限、資料、危險操作邊界                    |

關鍵心法：

- **共用規則放 `AGENTS.md`**
- **模型個性放 `CLAUDE.md` / `GEMINI.md`**
- **系統真相放 `docs/` 與 `adr/`**

---

## 第 3 步：`AGENTS.md` 怎麼寫？（共用 80%，這份是主檔）

### 定位

`AGENTS.md` 是**跨模型共用的總規則**，也是**單一真相來源**。
其他兩份（`CLAUDE.md` / `GEMINI.md`）只負責補充各自工具的特殊行為。

不要塞模型專屬語法，否則 Claude、Gemini、Codex、Copilot 讀起來都會混亂。
官方與社群把它視為「給 coding agent 的 README」，適合放 setup、test command、code style、project structure。

### 建議綱要（複製到專案後改成你的內容）

```markdown
# AGENTS.md

## 1. Project Mission
- 本專案要解決什麼問題
- 最重要的產品目標
- 不要偏離的核心價值

## 2. System Overview
- 前端 / 後端 / DB / Queue / AI Service 的關係
- 關鍵資料流
- 外部系統依賴

## 3. Repository Structure
- 每個資料夾負責什麼
- 哪些資料夾不可任意修改
- 新功能應放在哪裡

## 4. Development Workflow
- 安裝依賴
- 啟動服務
- lint / format / test 指令
- migration 指令

## 5. Coding Standards
- 命名規則
- TypeScript / Python / SQL 寫法
- Error handling pattern
- Logging pattern

## 6. Testing Rules
- 單元測試怎麼寫
- 整合測試怎麼跑
- E2E 測試何時需要
- 修改功能後必跑哪些測試

## 7. Security & Privacy Rules
- 不可 hardcode secrets
- 不可輸出敏感資料
- 不可直接修改 production config
- 測試資料需脫敏

## 8. Agent Behavior Rules
- 先讀文件再改 code
- 大改動前先提出 plan
- 不確定 API contract 時先查 docs
- 修改後必須說明影響範圍

## 9. Definition of Done
- build pass
- test pass
- lint pass
- migration checked
- docs updated if behavior changed
```

---

## 第 4 步：`CLAUDE.md` 怎麼寫？（只寫 Claude 特有的 20%）

### 定位

`CLAUDE.md` **不重複** `AGENTS.md` 的內容，只補上 Claude Code 的特殊行為：plan 流程、Claude 容易犯的錯、Claude 專用工具限制。

### 精簡綱要（80/20 版本）

```markdown
# CLAUDE.md

> Read AGENTS.md first for all shared project rules.
> This file only adds Claude-specific behavior.

## Claude Working Mode
- 修改 3+ 檔案時必須先產出 plan，等使用者確認再動手
- 不要只做局部 patch，先確認 call graph / data flow
- 對風險操作（rm、force push、migration drop）一律先問

## Claude-Specific Forbidden Actions
- 不可使用 --no-verify 跳過 hook
- 不可在保護分支（main / master）直接 commit
- 不可在沒有 plan 的情況下做跨模組重構

## Claude 的盲點補強
- 修改 payment flow 前必讀 docs/domain-model.md
- 改 API 時必須同步更新 docs/api-contract.md（Claude 容易漏這條）
- 改完要主動報告影響範圍，不要只說「done」
```

### 心法（很重要）

`CLAUDE.md` 不要寫成這種抽象垃圾：

```markdown
請你是一位資深工程師，幫我寫乾淨程式碼。
```

要寫成這種**有可執行步驟**的版本：

```markdown
When modifying payment flow:
1. Read docs/domain-model.md first.
2. Check tests/payment/.
3. Do not change settlement logic without adding regression tests.
4. Any change to amount calculation must include before/after examples.
```

AI 看得懂，也做得到。

### 何時可以把 `CLAUDE.md` 直接 symlink 成 `AGENTS.md`？

當你還沒發現任何 Claude 專屬的特殊需求時，就先 symlink，等遇到問題再拆出來補規則。
**不要為了「寫滿三份」而硬擠內容**——空的 `CLAUDE.md` 反而會稀釋 `AGENTS.md` 的權威。

---

## 第 5 步：`GEMINI.md` 怎麼寫？（只寫 Gemini 特有的 20%）

### 定位

`GEMINI.md` **不重複** `AGENTS.md` 的內容，只補上 Gemini CLI 的特殊操作：memory 機制、檔案搜尋偏好、輸出格式。

### 精簡綱要（80/20 版本）

```markdown
# GEMINI.md

> Read AGENTS.md first for all shared project rules.
> This file only adds Gemini-CLI-specific behavior.

## Gemini CLI Usage Rules
- 搜尋檔案優先用 ripgrep，不要用 grep
- 修改前先用 read 工具 inspect，不要憑記憶改
- 不要產生不必要的新 script，先找 repo 內既有工具

## Memory Rules
- 可用 save_memory 記住長期專案慣例
- 不要記住 secrets / 個資 / 一次性任務
- 覺得 Gemini「忘了」時，先跑 /memory show 檢查

## Preferred Output Format
- 先列 summary
- 再列 changed files
- 再列 test result
- 最後列 remaining risks
```

### 實務提醒

Gemini CLI 的 memory/context 載入仍有實作細節差異。每次覺得 Gemini 沒遵守規則時，用 `/memory show` 檢查實際載入內容，比猜測有效。

### 一樣的提醒

如果你還沒發現 Gemini 專屬的特殊需求，直接 symlink 即可，不要硬擠內容。

---

## 第 6 步：系統真相層 —— `docs/` 該放什麼？

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

## 第 7 步：決策治理層 —— `adr/` 為什麼一定要有？

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

## 第 8 步：怎麼切 `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` 的職責？

### 最佳分工表

| 文件          | 該放什麼                                       | 不該放什麼                       |
| ----------- | ------------------------------------------ | --------------------------- |
| `AGENTS.md` | 共用專案規則、架構邊界、測試指令                           | 特定模型語氣、Claude/Gemini 專用技巧   |
| `CLAUDE.md` | Claude 的任務拆解、重構規則、大型修改流程                   | 通用文件全文、太長的架構細節              |
| `GEMINI.md` | Gemini CLI 操作習慣、memory、search/navigation hints | 完整 PRD、完整 ADR              |
| `README.md` | 給新人看的安裝與介紹                                 | 給 Agent 的細碎工作規則             |
| `docs/*.md` | 系統真相來源                                     | prompt-style 指令             |
| `adr/*.md`  | 技術決策歷史                                     | 當前操作 SOP                    |

---

## 第 9 步：實務上最容易犯的 4 個錯

### 錯誤 1：把所有東西都塞進 `CLAUDE.md`

結果上下文爆炸，Agent 反而抓不到重點。
`CLAUDE.md` 應該像索引和工作規則，不是百科全書。

### 錯誤 2：`CLAUDE.md` 和 `GEMINI.md` 完全複製貼上

很省事，但不好。
Claude Code 的 memory 階層、Gemini CLI 的 `/memory show`、Codex 的 `AGENTS.md` 行為都不一樣。

### 錯誤 3：文件寫得很抽象

❌ `請寫出高品質程式碼。`
✅ `When changing API behavior: 1) Update docs/api-contract.md. 2) Add integration test.`

### 錯誤 4：寫了但從不更新

文件與 code 漂移後比沒寫還糟，因為 AI 會根據過期文件做出錯誤推論。
**Rule of thumb：行為變更必須同步更新 `docs/`，否則 PR 不能合。**

---

## 第 10 步：完整版藍圖（給已經上手的人）

當你的專案規模變大，可以擴充成這個樣子：

```text
repo-root/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── .github/
│   └── copilot-instructions.md
├── docs/
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

## 第 11 步：怎麼驗證 Agent 真的有讀進去？

| Agent          | 驗證方式                                                     |
| -------------- | -------------------------------------------------------- |
| Claude Code    | 在對話中問 "What does CLAUDE.md tell you about testing?"，看回答對不對 |
| Gemini CLI     | 在 CLI 內輸入 `/memory show`，檢查 GEMINI.md 是否在 context 內       |
| OpenAI Codex   | 觀察 Codex 是否遵守 `AGENTS.md` 的指令（例如修改前是否先讀指定資料夾）             |
| GitHub Copilot | 在 IDE 內請它套用「專案命名規則」，看是否真的對齊                              |

**如果它沒讀到，再華麗的規則也是裝飾品。**

---

## 五歲小孩版心法

想像你請一個很聰明但剛進公司的新人幫你改系統。

你不能只說：

> 幫我變好。

你要告訴他：

> 這是廚房，這是客廳，這個抽屜不能打開，這個開關不能亂按，改完要檢查水有沒有漏。

`AGENTS.md`、`CLAUDE.md`、`GEMINI.md` 就是在做這件事。

---

## 三句口訣（背起來就好）

1. **共用規則放 `AGENTS.md`**
2. **模型個性放 `CLAUDE.md` / `GEMINI.md`**
3. **系統真相放 `docs/` 與 `adr/`**

---

## 附錄：建議的 onboarding 步驟（給今天就要動手的人）

1. **複製本檔的「最小但完整」目錄藍圖**到你的 repo
2. **先填 `AGENTS.md` 第 1-3 節**（Mission / System Overview / Repo Structure），其他章節先留 TODO
3. **先 symlink**：`ln -s AGENTS.md CLAUDE.md && ln -s AGENTS.md GEMINI.md`（不要急著拆三份）
4. **建立 `docs/architecture.md` 與 `docs/security.md` 各一份骨架**（即使只有標題也好）
5. **建立 `adr/ADR-0001-tech-stack.md`**（記錄你選用的語言與框架）
6. 開始用 AI Agent 改 code
7. **當你發現某個 Agent 有專屬問題**（例如 Claude 老是漏更新 docs），才把 symlink 拆掉，補上專屬規則

這個流程跑兩週，你的 repo 就會變成「AI 進來就上手」的工作環境。

### 為什麼建議先 symlink，再按需要拆分？

避免「為了寫滿三份而硬擠內容」的反模式。
規則應該從**真實踩到的痛點**長出來，不是憑空想像。

---

## 參考資料

- OpenAI Codex `AGENTS.md` 規範：[developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)
- AGENTS.md 社群規範：[agents.md](https://agents.md/)
- Google Gemini CLI `GEMINI.md`：[github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md)
- Gemini CLI Memory Tool：[google-gemini.github.io/gemini-cli/docs/tools/memory.html](https://google-gemini.github.io/gemini-cli/docs/tools/memory.html)
- Claude Code Memory 機制（社群整理）：[dsebastien.net/claude-code-memory](https://www.dsebastien.net/claude-code-memory/)
