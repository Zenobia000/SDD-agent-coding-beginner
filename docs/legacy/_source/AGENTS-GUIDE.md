# 怎麼寫好 CLAUDE.md — 研究實證版

> 這份是「**怎麼寫**站立規則」的方法論；本專案實際的站立規則在根目錄 [`CLAUDE.md`](../CLAUDE.md)。
> 想擴充能力先讀 [`SKILLS.md`](./SKILLS.md) / [`MCP.md`](./MCP.md) / [`SUBCLAUDE.md`](./SUBCLAUDE.md)，這份是回頭優化主檔時看的。

---

## 一句話講白

**CLAUDE.md = 為一個「每次失憶、但完全信任文件」的 agent 做記憶植入。**

它是業界開放標準（Anthropic / Google / Microsoft / OpenAI 共同捐給 Linux Foundation 的 Agentic AI Foundation，約 6 萬個 repo 在用）。Claude Code / Claude Code / Cursor / Codex / Copilot 都讀它，所以**寫一份、跨工具通用**。

---

## 第一準則:能從 code 讀到的，就不要寫

> **"If the agent can discover it by reading the code, don't write it down."**

這是整份方法論的地基。Agent 會讀 `package.json`、`pyproject.toml`、目錄結構、README——這些它自己看得到的，寫進 CLAUDE.md 是**純浪費上下文**。

只記錄 agent **推不出來**的東西：

- 非預期的工具選擇（用 `uv` 不用 pip、用 `bun` 不用 npm）
- 歷史技術債、為什麼當初這樣決定
- 團隊共識、外部約束
- **已經踩過的坑**（最高價值）

---

## WHAT / WHY / HOW 框架

| 類別 | 寫什麼 | 重點 |
|---|---|---|
| **WHAT** | 技術棧、專案結構、各部分功能 | 只在 **monorepo**（agent 難自動推斷邊界）時才值得詳寫 |
| **WHY** | 專案目的、關鍵元件的理由 | 讓 agent 懂**意圖**，不只懂結構——這是文件最不可取代的部分 |
| **HOW** | 建置 / 測試 / 驗證流程 | 重點是**非預期的工具鏈**；標準流程 agent 自己會 |

---

## GitHub 的 5 條原則（觀察 2,500+ 實裝）

1. **可執行指令置前** — `npm test`、`pytest -v` 放最上面，不要埋在散文裡
2. **程式碼範例 > 長篇解釋** — 給一段對的 code，勝過三段描述
3. **明確邊界** — 永遠做 / 先問 / 絕對不做（DO / ASK FIRST / NEVER）
4. **具體技術棧 + 版本號** — 「用 React 18」不是「用現代前端框架」
5. **6 核心領域** — 指令、測試、結構、風格、git 工作流、邊界

---

## 反模式:研究證實「寫了反而更糟」

蘇黎世聯邦理工（ETH Zürich）在 SWE-bench Lite + AgentBench（138 任務）實測：

> **自動 `/init` 生出來不修的 CLAUDE.md，平均降低 3% 成功率、增加 20% 推論成本。**

| 反模式 | 為什麼無效甚至有害 |
|---|---|
| 重述 README / 既有文件 | agent 讀 code 自動發現，純複述只吃 context |
| 大段架構概覽 / 目錄列表 | 100% 自動生成檔都有，對「找檔案速度」零改善 |
| 看得見的技術細節 | `package.json` / `pyproject.toml` 已記錄 |
| 程式風格規定 | linter / formatter 更便宜、更確定、不吃 context |
| 空泛標語（"Clean code"、"Good naming"） | 訓練資料裡已充分，寫了等於沒寫 |
| 詳細 API 文件 | 用連結引外部即可 |
| 情境專用指令塞主檔 | 「部署前須 X」應放條件區塊，不是常駐 |

**作者澄清（Thibaud Gloaguen）**：論文反對的是「LLM 自動產生」的 CLAUDE.md，**不是反對這個檔案**。核心提問：

> 「如果你決定每次互動前都加上某些指令，先問自己——這些指令對你**大多數**任務真的需要嗎？」

---

## 你必須知道的容量數字

| 項目 | 數字 | 意義 |
|---|---|---|
| 模型指令順從上限 | **150–200 條** | 超過就開始忽略 |
| 系統提示已佔用 | 約 50 條 | 你能用的更少 |
| 實際可用空間 | **100–150 條** | 預算很緊，每條都要值錢 |
| 提及工具的使用機率 | 比未提及高 **160×** | 想要 agent 用某工具，就明寫——超有效 |
| 規則順從率 | 約 **70%** | 代表 **30% 風險**：真要強制的別靠文件 |

> **Linus 註解**：70% 順從率是這整件事的殘酷真相。
> 「絕對不能 commit secret」寫進 CLAUDE.md，有 30% 機率被無視。
> 真正不可破的規則→寫成 **hook**，讓機械層執行，不是對 agent 許願。但**選對 hook 的層**：
> - 規則攔的是 **git 操作**（commit / push secret、force-push）→ **git hook**（`.githooks/`）。對人和 agent 一律生效、跨工具通用。
> - 規則攔的是 **agent 工具生命週期**（某類工具呼叫前先檢查）→ **agent-settings hook**（`.claude/settings.json` 的 `before_tool_call` 等 / Claude `.claude/settings.json`）。只攔 agent，攔不到你手敲的指令。
>
> 本模板的 secret / force-push 守門就是用 **git hook**（[`.githooks/`](../.githooks/README.md)）——因為威脅是 git 操作。

---

## 推薦結構（目標 ≤ 300 行，理想 60–80 行）

```
1. 專案身分與背景      用途、核心責任（WHY）
2. 技術棧             具體版本（只記 agent 推不出的）
3. 目錄結構           monorepo 才必須
4. 開發流程           建置 / 測試命令置前
5. 編碼約定           給範例，不給標語
6. 邊界與限制         DO / ASK FIRST / NEVER
7. 常見陷阱           踩過的坑（最高價值）
```

---

## 超過 150–200 行就分層

別把所有東西塞一個大檔。分層策略：

| 層 | 放什麼 | 在本模板對應 |
|---|---|---|
| **根 `CLAUDE.md`** | 技術棧、專案身分、路標（指向細節在哪） | [`../CLAUDE.md`](../CLAUDE.md) |
| **子目錄 `CLAUDE.md`** | 該領域特定指引（monorepo 各 package） | 視專案需要新增 |
| **`.claude/` 拆主題** | 規則 / 工作流 / skill 分檔 | [`rules/`](./rules/) `WORKFLOW.md` `skills/` |
| **git hook（git 操作硬規則）** | 機械擋 commit/push 級威脅，跨工具 | [`../.githooks/`](../.githooks/README.md) |
| **agent-settings hook（工具生命週期）** | 攔 agent 工具呼叫，平台限定 | [`settings.json`](./settings.json) |

**條件區塊語法**（HumanLayer 慣例）——情境指令別常駐，用條件包起來：

```xml
<important if="writing or modifying tests">
- Use createTestApp() helper for integration tests
- Mock database with dbMock
</important>
```

---

## 跨工具:一份來源，多檔 symlink

| 檔名 | 工具 | 關係 |
|---|---|---|
| `CLAUDE.md` | 開放標準 | **單一來源** |
| `CLAUDE.md` | Claude Code | symlink → CLAUDE.md |
| `.cursorrules` | Cursor | symlink → CLAUDE.md |
| `.claude/settings.json` | Claude Code | hooks（機械層強制，非文件） |

**多工具團隊**：寫一份 `CLAUDE.md`，其餘用 symlink 指過去，別維護平行版本。

> 補充:Claude Code 會把 `CLAUDE.md` 放進 `<system_reminder>` 並標記「**可能相關**」——
> 意思是它會自己判斷要不要理你的規則。又一個「文件 ≠ 強制」的證據。

---

## 優先順序（記這 5 條就好）

1. **非預期工具鏈 > 寬泛架構圖**
2. **行為偏好 > 技術事實**（事實 agent 自己讀得到）
3. **禁止項目用 hooks，不是用文件許願**
4. **版本與具體細節 > 抽象原則**
5. **層級化結構（主檔 + 子檔 + hooks）> 單一大檔**

---

## 套用回本模板:我們的 CLAUDE.md 自評

對照上面準則，誠實打分本模板的 [`../CLAUDE.md`](../CLAUDE.md)：

| 準則 | 現況 | 判定 |
|---|---|---|
| 明確邊界 DO/ASK/NEVER | §7「絕對禁止」+ §4 MCP「先說再用」 | 🟢 有 |
| 可執行指令置前 | 指令分散在各 skill，主檔較少 | 🟡 靠 `/verify` 等 skill 補 |
| 硬規則用 hooks | secret + force-push 已由 [`../.githooks/`](../.githooks/README.md) 機械強制 | 🟢 已落實（見下方「已動的一件事」） |
| 能讀到的別寫 | §5 技術選擇表多為「預設值」，非複述 | 🟢 OK |
| 行為偏好 > 事實 | §6 對話風格、§3 鐵則順序 | 🟢 對焦在 agent 推不出的紀律 |
| 篇幅 | 主檔含 7 章，偏長但有分層到 `rules/` | 🟡 可再瘦，把範例移進 rules |

**已動的一件事（headline）**：把「不准 commit secret」「不准 `push --force`」從 §7 的**文件許願**，升級成 **git hook 機械強制**：

- [`../.githooks/pre-commit`](../.githooks/README.md) — 擋寫死的 key / 誤加的 `.env`
- [`../.githooks/pre-push`](../.githooks/README.md) — 擋對 `main` 的 force-push
- 補上模板原本**缺的** [`../.gitignore`](../.gitignore) 與 [`../.env.example`](../.env.example)（先前叫使用者「把 `.env` 加進 `.gitignore`」卻沒附檔——這是自評沒抓到的洞）

**為什麼不是 `settings.json` hook**：查證後（[Claude Code Hooks 文件](https://antigravity.google/docs/hooks)）其 hook 點是 agent 工具生命週期，攔不到「人手敲 `git commit`」。secret/force-push 的威脅是 git 操作，**git hook 才是對的層**，且跨工具通用。日常仍搭 [`/sec-scan`](./skills/sec-scan.md)（agent 判斷力）做部署前體檢。

---

## 速查清單（寫 / 改 CLAUDE.md 前過一遍）

- [ ] 每一行都問：agent 讀 code 能不能自己發現？能 → 刪
- [ ] 可執行指令（test / build）放最前面
- [ ] 邊界寫成 DO / ASK FIRST / NEVER 三段
- [ ] 技術棧寫具體版本，不寫「現代框架」
- [ ] 真正不可破的規則 → 寫成 hook，不是寫進文件
- [ ] 情境指令 → 用 `<important if="...">` 條件區塊，不常駐
- [ ] 總行數 ≤ 300（理想 60–80）；超過就分層
- [ ] 沒有空泛標語、沒有複述 README、沒有 linter 管得到的風格條文

---

**資料來源**：本文濃縮自 [blog.aihao.tw《CLAUDE.md 研究與實踐》](https://blog.aihao.tw/2026/05/03/agents-md-research-and-practices/)，
底層研究為 ETH Zürich 在 SWE-bench Lite / AgentBench 的實證，與 GitHub 對 2,500+ 實裝的觀察。
