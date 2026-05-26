# Skills（Agent Skills）入門 — Antigravity CLI 版

> Skill 是 Antigravity CLI 的核心擴充原語：放在 `.agents/skills/` 的 markdown 檔，
> 既是 AI 可以「自動觸發」的程序性知識，也是你可以「手動打 `/xxx` 」的 slash command。
> 不會用基本對話之前**先跳過這份**，把 AGENTS.md + MCP 用熟再回來。

---

## 一句話講白

**Skill = 把「程序性知識」封裝成 markdown 檔案 + 資料夾，Antigravity CLI 啟動時掃描載入。**

舉例：你每次寫完 code 都會手動講「請檢查命名一致性、檢查有沒有硬編碼、列出改了哪些檔案」——這個審查流程寫成 Skill 後，AI 看你說「我寫完了」會**自動翻到這份食譜**照做。

**重要變化（vs Gemini CLI）**：
Antigravity 把舊版 Gemini CLI 的 `commands/.toml` 與 `skills/SKILL.md` **合併成單一原語**。同一個 markdown 檔，AI 看 description 會自動觸發，使用者也能手動打 `/<檔名>`。一個 Skill 兩種觸發方式。

---

## Skill vs MCP 對照

| 維度 | MCP | Skill |
|---|---|---|
| **角色** | 外部能力通道 | 知識封裝 + slash command |
| **觸發** | AI 判斷該不該叫 | AI 看 description 自動匹配 / 使用者打 `/<name>` 手動觸發 |
| **檔案** | `settings.json` 內設定 + npx 啟動 server | `.agents/skills/<name>.md` 或 `.agents/skills/<name>/SKILL.md` |
| **適合** | 連網路 / 開瀏覽器 / 操作 GitHub | 多步驟流程、審查 checklist、固定 prompt |
| **比喻** | 烤箱（硬體） | 食譜本（知識） |

**判斷練習**：

- 「我想要 AI 能截圖驗證頁面」→ **MCP**（playwright）
- 「我想要 AI 寫完 code 自動審查」→ **Skill**（pre-commit-review）
- 「我想要打一句 `/test` 自動跑測試」→ **Skill**（test.md，手動觸發版）

---

## Skill 從哪裡來？兩個來源

Antigravity CLI 啟動時會掃描以下位置：

| 來源 | 路徑 | 適合放 |
|---|---|---|
| **User**（全域） | `~/.gemini/antigravity-cli/skills/` | 你個人習慣的審查 / 思考流程 |
| **Workspace**（專案） | `<project>/.agents/skills/` | 專案專屬的流程，**會跟 git 走** |

> 過渡期說明：Antigravity CLI 的全域目錄仍然落在 `~/.gemini/antigravity-cli/`（Google 把 Gemini CLI 的舊家底沿用過來方便 `agy plugin import gemini` 一鍵搬遷）。專案目錄則統一用 `.agents/`（對齊 AGENTS.md 業界規範）。

**初學者只要管 Workspace skill**：放在 `.agents/skills/` 下，跟著專案進 git，未來團隊或下個專案都能複用。

---

## 兩種 Skill 結構

### 結構 A：單檔 Skill（簡單版，等同 slash command）

```
.agents/skills/test.md
```

打 `/test` 會把整份 `test.md` 當 prompt 跑。AI 也會在你問「跑測試」時自動匹配。

### 結構 B：資料夾 Skill（進階版，可附參考檔）

```
.agents/skills/explain-code/
├── SKILL.md              ← 主檔（必須）
├── examples/
│   ├── good-example.md
│   └── bad-example.md
└── checklist.md
```

打 `/explain-code` 觸發；資料夾名 = slash command 名。

**鐵則**：
- 資料夾名 = Skill 名（小寫 kebab-case，例：`pre-commit-review`）
- 資料夾內必須有 `SKILL.md`
- 開頭必須有 `name` + `description` 的 YAML frontmatter
- 附件用相對路徑引用

---

## 第一個 Skill：寫一個 `explain-code`

我們做一個會在「使用者問『這段 code 在幹嘛』時自動觸發」的 Skill。

### 步驟 1：建資料夾與檔案

```bash
mkdir -p .agents/skills/explain-code
touch .agents/skills/explain-code/SKILL.md
```

### 步驟 2：寫 SKILL.md 的 frontmatter

打開 `.agents/skills/explain-code/SKILL.md`，第一段寫：

```markdown
---
name: explain-code
description: Use when the user asks "what does this do", "explain this code", or 想要白話解釋一段程式碼. Pulls the file, walks through it section by section in plain language.
---
```

**`description` 是觸發關鍵**——Antigravity 會用它跟你的問題做語意比對。三個秘訣：

1. **寫具體場景**，不是「helper」「utility」這種空泛詞
2. **中英混寫無妨**——使用者可能任一語言發問
3. **列觸發詞** "Use when..." 起手，明確告訴 AI 什麼時候該翻到這頁

### 步驟 3：寫 SKILL.md 的 body

繼續往下寫，告訴 AI **這個 skill 該執行什麼步驟**：

```markdown
# Explain Code Skill

當使用者要你「解釋一段 code」時，照以下流程：

## 1. 確認範圍

問使用者：
- 要解釋哪個檔案 / 哪幾行？
- 解釋深度：初學者白話 / 中等技術 / 深入到 implementation 細節？

## 2. 讀檔

用 `read_file` 工具讀完整檔案。**不要憑記憶**。

## 3. 分段講解

- 每段用 1-2 句白話講「這段在幹嘛」
- 標出 file:line 讓使用者可以跳過去看
- 點出 1 個「值得注意的設計決策」

## 4. 收尾 checklist

- 整個檔案在生態系中扮演什麼角色
- 跟其他哪些檔案有耦合
- 建議的「閱讀順序」
```

### 步驟 4：重啟 CLI 觸發測試

```bash
agy
```

進對話打：

```
你能解釋一下 index.html 在做什麼嗎？
```

或直接手動觸發：

```
/explain-code
```

如果 skill 設定正確，AI 會匹配到 `explain-code` skill 並照流程走。

---

## 進階：附加資源（reference files、scripts）

Skill 不只能放 SKILL.md，整個資料夾的內容都可以用：

```
.agents/skills/explain-code/
├── SKILL.md              ← 主檔（必須）
├── examples/
│   ├── good-example.md   ← 好的解釋範例
│   └── bad-example.md    ← 不好的解釋範例
└── checklist.md          ← 收尾用的 checklist
```

在 SKILL.md 內用**相對路徑**引用：

```markdown
## 4. 收尾 checklist

依照 ./checklist.md 走完每一項。如果使用者要看好的解釋範例，
給他看 ./examples/good-example.md。
```

AI 會在執行 skill 時讀這些附件。

**注意**：附件路徑用相對於 SKILL.md 的相對路徑，不要寫絕對路徑（會綁定到你的機器）。

---

## description 怎麼寫得讓 Antigravity 找得到

`description` 是 Skill 被觸發的關鍵。寫得好 = 自動觸發；寫得糊 = 永遠不會被選到。

**好的 description**（具體、有觸發詞、寫清楚場景）：

```yaml
description: >
  Use when the user requests a security audit, OWASP review, or
  pre-launch check on authentication / input validation / secrets
  handling. Performs a 10-point checklist and outputs prioritized
  findings.
```

**差的 description**（空泛、沒場景）：

```yaml
description: Helper for security stuff.   # ❌ 沒人會被觸發到
description: 安全相關。                    # ❌ 同上
description: Code quality.                # ❌ 範圍太大，永遠被誤觸
```

**檢查點**：寫完 description 後，自問「我會怎麼問這件事？」把問句的關鍵字塞進 description。

---

## 與 Vibe Coding 五步流程的搭配

Skill 最強的地方是**把重複出現的審查 / 設計流程包起來**。建議的初學者 Skill 清單：

| Skill 名 | 觸發場景 | 對應 Vibe Coding 步驟 |
|---|---|---|
| `explain-code` | 「解釋這段」 | 任何步驟（debug 用） |
| `prd-rewrite` | 「我要寫 PRD」 | 第 1 步重述需求 |
| `vibe-plan` | 「我要做 ___」 | 第 2 步列計畫 |
| `pre-commit-review` | 「我寫完了」 | 第 3 步寫完後 |
| `test` | 「跑測試」 | 第 4 步帶測試 |

**心法**：每次你跟 AI 講「請每次都先 ___」、「請每次寫完都 ___」這種重複指令時——那就是個 Skill。

---

## 動態子代理（Dynamic Subagents）— Antigravity 2026 新功能

Antigravity CLI 新增的殺手特性：**Skill 內可以宣告子代理（subagents），讓主 agent 平行展開複雜任務**。

範例（在 SKILL.md body 內）：

```markdown
## 4. 分派子任務

對每個受影響的模組，**派一個 subagent 並行處理**：

- subagent A：分析 src/auth/ 的耦合
- subagent B：分析 src/api/ 的耦合
- subagent C：分析 src/db/ 的耦合

各自跑完後彙整成一份報告。
```

效果：大型 refactor / 跨模組調查不用 agent 自己一條線跑到底，主 agent 派 3 個並行跑、自己等結果回來統整。

> 初學者**不用一開始就用**這功能。等你寫過 5+ 個 skill、開始覺得「這 skill 要跑很久」時再考慮拆 subagent。

---

## 安全與品質規則

Skill 是被 AI **當作 system instruction 直接執行的**，所以：

1. **不要放 secret**：API key、token、密碼絕對不能寫在 SKILL.md（如果 skill 進 git，就外洩到全世界）
2. **不要寫絕對路徑**：`/Users/sunny/projects/...` 換台機器就壞了，用相對路徑或 `.` 開頭
3. **不要寫破壞性指令當預設行為**：例如別寫「直接刪掉 .agents/ 重建」，要寫「列出可刪選項等使用者確認」
4. **Skill 的 description 不該包含對抗性詞彙**：例如「ignore previous instructions」這種 prompt injection 句型——你自己寫沒問題，但別人也能讀到，可能被 LLM 視為攻擊向量
5. **單一 Skill 不要超過 200 行**：超過了就拆成多個 Skill 或抽附件

---

## 除錯：Skill 為什麼沒被觸發？

**症狀 A：問了相關問題但 AI 沒翻 skill**

- 看 description 的觸發詞跟你的問題用詞是否重疊
- 改用 description 內的關鍵字重問一次測試
- 直接打 `/skill-name` 手動觸發確認 skill 本身能跑

**症狀 B：CLI 啟動時 skill 沒被掃到**

- 確認資料夾結構：`.agents/skills/<name>/SKILL.md` 或 `.agents/skills/<name>.md`
- 確認 frontmatter 用 `---` 包起來，YAML 格式合法
- 重啟 CLI（skill 在啟動時掃描，不是熱載）

**症狀 C：多個 Skill 互相蓋掉**

- 兩個 skill 的 description 太相似 → 改寫成不同關鍵字
- 不確定當下匹配哪個 → 在 SKILL.md body 開頭加一句「執行此 skill 時請先告訴我『我正在用 explain-code skill』」協助 debug

---

## 延伸閱讀

- [Antigravity CLI Agent Skills 官方文件](https://antigravity.google/docs/skills)
- [Building Custom Skills in Google Antigravity（Medium）](https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d)
- [Antigravity CLI Hands-On Guide（DEV）](https://dev.to/arindam_1729/antigravity-cli-a-hands-on-guide-to-googles-terminal-coding-agent-5bc7)

---

## 五歲小孩版理解

- 一般情況：AI 像個工程師朋友，你問它它就回答
- 裝 Skill：你給它一本「公司 SOP」，他遇到 SOP 涵蓋的情境會自動翻書照做
- SKILL.md 的 description = SOP 目錄索引
- SKILL.md 的 body = SOP 內文
- 附件 = SOP 附錄的範本、checklist
- **重點是 description 寫得讓他「想得到該翻」**——寫太模糊永遠翻不到，寫太死板每個問題都翻
- 同一份 Skill 你也能手動叫：打 `/skill-name` 強制執行（自動匹配失靈時的備案）
