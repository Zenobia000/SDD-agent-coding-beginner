# Subagents 入門 — Claude Code 平台特性

> Subagents 是 Claude Code 2026 新增的**平行任務原語**。
> 跟 [MCP](./MCP.md) / [Skills](./SKILLS.md) 並列為「平台特有、模型本能彌補不了」的三大擴充原語。
> 不會用基本對話之前**先跳過這份**，把 CLAUDE.md + Skills 用熟再回來。

---

## 一句話講白

**Subagent = 主 agent 派出去的「平行助手」**，有自己的 context window、自己的工作目標、跑完回報結果給主 agent。

過去 Gemini CLI 時代，一個 agent = 一個對話 = 一條線跑到底，遇到大型任務 context 會爆、跑很久。Claude Code 2026 內建多代理調度（**無須 tmux**），主 agent 可以動態派 N 個 subagent 並行處理。

---

## 官方架構：Technical Director（2026-05-19 I/O 確認）

Claude Code 2.0 把多代理調度做成**平台級原語**，架構名稱叫 **Technical Director**：

| 維度 | 內容 |
|---|---|
| **誰主導** | **Orchestrator（主 agent）自己決定**要不要分解、派幾個、何時收斂 |
| **使用者角色** | 描述目標就好，**不手動配置 subagent** |
| **Subagent 型態** | **Dynamic subagents** — on-the-fly 創建，每個有獨立 context window |
| **內建程度** | 平台原生，**不用 tmux、不用寫 orchestrator code、不用外掛** |
| **CLI 入口** | `claude`（取代 Gemini CLI；個人版 Gemini CLI 2026-06-18 EOL） |
| **相關 slash command** | `/goal`、`/schedule`（2.0 新增） |

→ **設計含義**：寫 skill 時，**不要把「派 subagent」當成 skill body 的硬指令**。
應該描述「任務的範圍與獨立性」，讓 orchestrator 自己判斷要不要平行展開。
這跟舊式「手動 orchestrator」（例如 LangGraph / CrewAI 的人工編排）哲學相反。

---

## 三大擴充原語對照（MCP / Skill / Subagent）

| 維度 | MCP | Skill | Subagent |
|---|---|---|---|
| **角色** | 外部能力通道 | 程序知識 + slash command | 平行任務分派 |
| **比喻** | 烤箱、攪拌機（硬體） | 食譜本 + hot key（知識） | 派出去的工人（人力） |
| **解決問題** | AI 不會做的事 | AI 該怎麼做 | AI 一次做不完的事 |
| **觸發** | AI 自己判斷該叫 | AI 看 description 自動 / 手動 `/xxx` | 主 agent 主動派 / Skill 內宣告 |
| **檔案** | `settings.json` 內 `mcpServers` | `.claude/skills/<name>.md` | 對話中宣告 / Skill body 內宣告 |
| **context** | 共享主 agent | 共享主 agent | **獨立 window**（隔離） |
| **適合** | 連 GitHub / 開瀏覽器 / 查資料庫 | 多步驟流程、固定 prompt | 大型 refactor、跨檔案分析、平行調查 |

**判斷練習**：

- 「我想要 AI 能截圖驗證頁面」→ **MCP**（playwright）
- 「我想要 AI 寫完 code 自動審查」→ **Skill**（pre-commit-review）
- 「重構整個 src/ 目錄、20 個檔案要同時改」→ **Subagents**（每模組派一個）

---

## 何時用 vs 何時不用

### ✅ 該用 subagent

| 場景 | 為什麼 |
|---|---|
| 大型 refactor（> 10 檔案） | 一條線跑會超過 context window |
| 跨模組調查（auth / api / db 各看一遍） | 平行跑省時間 |
| 平行驗證假設（同題派 3 個 agent 跑、比結果） | 多視角避免單一偏見 |
| 超長任務（爬一份 100 頁 PDF + 100 個網頁） | 拆塊並行 |
| Map-Reduce 工作（對 1000 筆資料各跑一次分析） | 平行加速 |

### ❌ 不該用 subagent

| 場景 | 為什麼 |
|---|---|
| MVP 階段、單檔小專案 | **殺雞用牛刀**，主 agent 一條線就夠 |
| 任務有強依賴順序（A → B → C） | 平行省不到時間，反而難協調 |
| 任務需要使用者中途確認 | subagent 失去人類在迴圈內控制 |
| 不確定能不能拆 | 拆錯反而更亂；先用主 agent 跑、真的卡了再拆 |

**Linus 原則**：能用主 agent 一條線跑完，就**絕對不要拆**。subagent 是用來解決真實 context / 時間問題，不是用來顯擺架構。

---

## 怎麼觸發 subagent

### 方法 A：對話中直接派（最常用）

```
請開 3 個 subagent 分別處理：
- subagent A：分析 src/auth/ 的耦合，找出循環依賴
- subagent B：分析 src/api/ 的耦合，找出循環依賴
- subagent C：分析 src/db/ 的耦合，找出循環依賴

各自跑完後彙整成一份報告，按嚴重度排序。
```

主 agent 會自己分派、收結果、統整。你不需要管調度。

### 方法 B：在 Skill body 描述「任務範圍與獨立性」

⚠️ **重要觀念**：Skill body 不要寫成「派 subagent A、B、C」的硬指令。
應該描述「**任務的範圍 + 哪些子任務彼此獨立**」，由 orchestrator 自己判斷要不要平行展開。

```markdown
---
name: cross-module-audit
description: Use when the user asks to audit coupling / dependencies across modules. Independent per-module analysis; orchestrator may parallelize.
---

# Cross-Module Audit Skill

## 1. 確認範圍

問使用者：要審查哪些模組？（沒指定就 grep 列出最大的 5 個）

## 2. 對每個模組獨立分析

**每個模組的分析互不相依**（適合 orchestrator 平行展開）：

- 循環依賴
- 跨層存取（UI 直接打 DB）
- god object（單檔超過 500 行）
- 命名一致性

## 3. 彙整

收齊所有模組分析結果後：
- 按嚴重度排序（🔴 緊急 / 🟡 留意 / 🟢 健康）
- 列出 top 3 修復優先項
- 給每項一句白話建議
```

打 `/cross-module-audit` 觸發後，orchestrator 看到「N 個模組獨立分析」自然會 spawn N 個 dynamic subagents 並行（或在小規模時選擇單線跑完），使用者不用管細節。

**反面教材**（不要這樣寫 skill body）：
> ❌「派 subagent A 分析 auth、subagent B 分析 api、subagent C 分析 db」
> — 這是 LangGraph / CrewAI 風格的手動編排，跟 Claude Code 的 Technical Director 哲學衝突。

---

## Context 隔離（最重要的觀念）

**每個 subagent 有獨立的 context window**，跟主 agent 隔離。

```
┌────────────────────────────────┐
│  主 agent（你正在對話的這個）   │
│  context: 完整對話歷史 + 規則    │
└────────────────────────────────┘
         │ 派任務
         ├─ subagent A: 只看自己被交付的 prompt
         ├─ subagent B: 只看自己被交付的 prompt
         └─ subagent C: 只看自己被交付的 prompt
         │ 各自回報結果
         ▼
   主 agent 彙整
```

**優點**：
- **互不污染**：A 跑壞不影響 B
- **token 預算分開**：主 agent context 不會爆
- **平行加速**：3 個同時跑 ≈ 1/3 時間

**陷阱**：
- **subagent 看不到主對話歷史**——派任務時必須把背景塞進 prompt
- 例：派 subagent A 分析 auth 時，要在 prompt 內寫「專案用 Python + Flask、目前在重構登入流程」，不能假設它知道
- 否則 subagent 會問「這專案是什麼？」之類，等於白派

**檢查口訣**：派出去的 prompt 拿給陌生人讀能不能懂？不能 → 補背景。

---

## 三種常見彙整模式

### 1. Map-Reduce（最常見）

```
主 agent (Reduce)
     ▲
     │ 結果彙整
     │
┌────┴────┬────┐
│         │    │
▼         ▼    ▼
subagent  ...  subagent  (Map: 平行做 N 個獨立任務)
```

**範例**：分析 100 個檔案 → 派 10 個 subagent 各分析 10 個 → 主 agent 彙整成一份報告。

### 2. Pipeline（鏈式）

```
主 agent
   │
   ▼
subagent A (擷取原始資料)
   │
   ▼
subagent B (清洗 / 轉換)
   │
   ▼
subagent C (寫入結果)
```

**範例**：爬網頁 → 抽結構化資料 → 寫進 DB。每步 subagent 用前一步的輸出。

### 3. Vote（多視角）

```
主 agent
   │ 同一題派給 3 個 subagent
┌──┼──┐
▼  ▼  ▼
A  B  C  (用不同方法 / 不同 prompt 跑同一題)
└──┼──┘
   ▼
主 agent (比較三個結果，挑最好 / 投票)
```

**範例**：難題派 3 個 subagent 用不同切入點解 → 主 agent 比較、給出最終答案。**避免單一視角偏見**。

---

## 範例：完整工作流

**任務**：審查 50 個檔案的測試覆蓋率，找出缺測試的 hot path。

```
你：「請審查 src/ 下所有檔案的測試覆蓋率。
     檔案太多，請用 subagents 平行處理。」

主 agent：
  好的，我先掃 src/ 目錄結構（找出有 50 檔），決定切 5 組（每組 10 檔）。

  派 5 個 subagent：
  - subagent 1: src/auth/* (10 檔)
  - subagent 2: src/api/* (10 檔)
  - subagent 3: src/db/* (10 檔)
  - subagent 4: src/utils/* (10 檔)
  - subagent 5: src/ui/* (10 檔)

  每個 subagent 收到 prompt：
  「分析這 10 個檔案的測試覆蓋率，列出：
   - 無測試的函式（檔名:行號）
   - 測試覆蓋率 < 50% 的函式
   - 屬於 hot path（被其他模組大量呼叫）的優先項
   背景：專案用 pytest，慣例是 test_<module>.py 對應 <module>.py」

  [5 個 subagent 並行跑，平均每個 30 秒]

  全部回報後，主 agent 彙整：
  📋 整體報告
  - 總覆蓋率：62%
  - 最差模組：src/db/ (28%)
  - Hot path 缺測試 top 5：
    1. src/auth/jwt.py:45 verify_token (被 8 處呼叫)
    2. ...
  建議優先補：top 5 + src/db/ 整體拉到 50%
```

主 agent 花 30 秒（非 50 × 30 秒 = 25 分鐘）。

---

## 安全與限制

| 限制 | 為什麼 |
|---|---|
| **不要無限套娃**（subagent 內再派 subagent） | 容易失控、追蹤困難。Claude Code 預設限制套娃深度 |
| **並行數由 orchestrator 動態決定** | 受 token 預算 / API 計費 / 任務獨立性影響。使用者通常不用手動限制；確切上限與計費見 [Claude Code 官方文件](https://antigravity.google/docs) |
| **subagent 失敗時主 agent 要 fallback** | 不要靜默吞錯。失敗的 subagent 至少要在最終報告列出 |
| **subagent 不要動破壞性指令** | 派 subagent 只給 read-only 任務最安全。要寫檔 / 跑 shell 由主 agent 統一執行 |
| **subagent 不會看到使用者中途新指令** | 派出去後使用者改主意，主 agent 必須 cancel 後重派 |

---

## 除錯

**症狀 A：subagent 跑出來的結果跟你想的不一樣**

- 派出去的 prompt 太精簡 → subagent 沒背景
- **修法**：補背景。把專案用什麼語言、什麼框架、慣例、限制全寫進 prompt

**症狀 B：subagent 跑很久沒回報**

- 任務切得太大 → subagent context 爆 → 它自己也卡
- **修法**：再拆細。把 50 檔分 5 組（10 檔/組）改成 10 組（5 檔/組）

**症狀 C：subagents 結果矛盾**

- 任務不夠獨立 → 各自看到不同資訊做出不同判斷
- **修法**：確保任務真的獨立（例如「分析 src/auth/」跟「分析 src/api/」之間沒共用 state）

**症狀 D：主 agent 彙整不出像樣的報告**

- subagent 回報格式不統一 → 主 agent 不知道怎麼合
- **修法**：派任務時規定回報格式（JSON / Markdown table），主 agent 才能機械化彙整

---

## vs Gemini CLI / Claude Code / Cursor

| 工具 | Subagent 支援度 |
|---|---|
| **Claude Code** | ✅ 原生支援，無須額外配置（2026 殺手特性） |
| **Claude Code** | ✅ 有 `Agent` 工具可 spawn subagent，需手動觸發 |
| **Gemini CLI**（舊） | ❌ 無原生 subagent，要靠 tmux 自己拼 |
| **Cursor** | ⚠️ 部分支援（Composer 多檔案編輯，非完整 subagent） |

**Claude Code 的優勢**：subagent 是平台原語，不是 hack。主 agent 派 / 收 / 彙整全自動，使用者只管講「請用 subagents 處理 X」。

---

## 五歲小孩版理解

- **主 agent** = 包工頭
- **subagent** = 派出去的工人
- 包工頭把工程拆成 3 塊，派 3 個工人並行做
- 工人**各自有自己的工地**（context 隔離），互不干擾
- 工人做完回報包工頭，包工頭統整給你
- 你只管「需求」和「結果」，不需要知道工人是誰

**口訣**：能一個人做就一個人做（主 agent 一條線）；做不完才找幫手（派 subagents）。**先嘗試一條線、真的卡了再拆**。

---

## 延伸閱讀

- [Claude Code Dynamic Subagents 官方文件](https://antigravity.google/docs/subagents)
- [Claude Code Deep Dive — Subagents 段（agentpedia）](https://agentpedia.codes/blog/antigravity-cli-deep-dive)
- [Map-Reduce pattern in agent design（Anthropic）](https://www.anthropic.com/engineering/building-effective-agents)
