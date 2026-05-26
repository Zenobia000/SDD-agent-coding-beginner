# Skills（Agent Skills）入門

> Skill 是 Gemini CLI 較新的擴充原語（2026 年才落地）。
> 如果你的 `gemini --version` 太舊找不到 skill 功能，先 `npm i -g @google/gemini-cli@latest` 升級。
> 不會用基本對話之前**先跳過這份**，把 GEMINI.md + MCP 用熟再回來。

---

## 一句話講白

**Skill = 把「程序性知識」封裝成 AI 可以自動觸發的 markdown 檔案 + 資料夾。**

舉例：你每次寫完 code 都會手動講「請檢查命名一致性、檢查有沒有硬編碼、列出改了哪些檔案」——這個審查流程寫成 Skill 後，AI 看你說「我寫完了」會**自動翻到這份食譜**照做。

---

## Skill vs Command vs MCP 對照

三個原語常被搞混，這張表釘起來看：

| 維度 | MCP | Skill | Command |
|---|---|---|---|
| **角色** | 外部能力通道 | 進階知識封裝 | 快捷 prompt |
| **觸發** | AI 判斷該不該叫 | AI 看 description 自動匹配 | 你手動打 `/xxx` |
| **檔案** | `settings.json` 內設定 + npx 啟動 server | `.gemini/skills/<name>/SKILL.md` + 附件 | `.gemini/commands/<name>.toml` |
| **適合** | 連網路 / 開瀏覽器 / 操作 GitHub | 多步驟流程、審查 checklist | 你常重複的固定指令 |
| **比喻** | 烤箱（硬體） | 食譜本（知識） | hot key（快捷） |

**判斷練習**：

- 「我想要 AI 能截圖驗證頁面」→ **MCP**（playwright）
- 「我想要 AI 寫完 code 自動審查」→ **Skill**（pre-commit-review）
- 「我想要打一句 `/test` 自動跑測試」→ **Command**（test.toml）

---

## Skill 從哪裡來？四個來源

Gemini CLI 啟動時會掃描以下位置：

| 來源 | 路徑 | 適合放 |
|---|---|---|
| Built-in | CLI 內建 | 不用管 |
| Extension | 透過 extension 安裝 | 進階，先跳過 |
| **User** | `~/.gemini/skills/` 或 `~/.agents/skills/` | 你個人習慣的審查 / 思考流程 |
| **Workspace** | `<project>/.gemini/skills/` 或 `<project>/.agents/skills/` | 專案專屬的流程，**會跟 git 走** |

**初學者只要管 Workspace skill**：放在 `.gemini/skills/` 下，跟著專案進 git，未來團隊或下個專案都能複用。

---

## 第一個 Skill：寫一個 `explain-code`

我們做一個會在「使用者問『這段 code 在幹嘛』時自動觸發」的 Skill。

### 步驟 1：建資料夾與檔案

```bash
mkdir -p .gemini/skills/explain-code
touch .gemini/skills/explain-code/SKILL.md
```

> Skill 是「資料夾」不是「單一檔案」。資料夾名 = Skill 名。資料夾內必須有一份 `SKILL.md`。

### 步驟 2：寫 SKILL.md 的 frontmatter

打開 `.gemini/skills/explain-code/SKILL.md`，第一段寫：

```markdown
---
name: explain-code
description: Use when the user asks "what does this do", "explain this code", or 想要白話解釋一段程式碼. Pulls the file, walks through it section by section in plain language.
---
```

**`description` 是觸發關鍵**——Gemini 會用它跟你的問題做語意比對。三個秘訣：

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

如果使用者只說「解釋這個」沒指明檔案，**先列出最近改動的 3 個檔案**讓他選。

## 2. 讀檔

用 `read_file` 工具讀完整檔案。**不要憑記憶**——AI 對程式碼的記憶常常有偏差。

## 3. 分段講解

把檔案切成邏輯段（function / class / 區塊），每段：

- 用 1-2 句白話講「這段在幹嘛」
- 標出 file:line 讓使用者可以跳過去看
- 點出 1 個「值得注意的設計決策」（為什麼這樣寫而不是另一種）

## 4. 收尾 checklist

最後一段總結：
- 整個檔案在生態系中扮演什麼角色
- 跟其他哪些檔案有耦合
- 建議的「閱讀順序」（如果使用者要繼續看下去）

## 禁止行為

- ❌ 不要直接貼原始碼當解釋（使用者自己會看）
- ❌ 不要用 jargon 不解釋（CORS、middleware、polyfill 都要白話）
- ❌ 不要超出檔案範圍幫他重構（這是 explain，不是 refactor）
```

### 步驟 4：重啟 CLI 觸發測試

```bash
gemini
```

進對話打：

```
你能解釋一下 index.html 在做什麼嗎？
```

如果 skill 設定正確，AI 會**自動匹配**到 `explain-code` skill 並照流程走。觀察它有沒有：

- ✅ 先問你要解釋哪個檔案（如果你沒指明）
- ✅ 用 `read_file` 讀檔
- ✅ 分段講解、標 file:line
- ✅ 給「值得注意的設計決策」

如果沒觸發，看下面除錯段落。

---

## 進階：附加資源（reference files、scripts）

Skill 不只能放 SKILL.md，整個資料夾的內容都可以用：

```
.gemini/skills/explain-code/
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

## description 怎麼寫得讓 Gemini 找得到

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
| `plan-before-code` | 「我要做 ___」 | 第 2 步列計畫 |
| `pre-commit-review` | 「我寫完了」 | 第 3 步寫完後 |
| `test-helper` | 「怎麼測？」 | 第 4 步帶測試 |

**心法**：每次你跟 AI 講「請每次都先 ___」、「請每次寫完都 ___」這種重複指令時——那就是個 Skill。

---

## 安全與品質規則

Skill 是被 AI **當作 system instruction 直接執行的**，所以：

1. **不要放 secret**：API key、token、密碼絕對不能寫在 SKILL.md（如果 skill 進 git，就外洩到全世界）
2. **不要寫絕對路徑**：`/Users/sunny/projects/...` 換台機器就壞了，用相對路徑或 `.` 開頭
3. **不要寫破壞性指令當預設行為**：例如別寫「直接刪掉 .gemini/ 重建」，要寫「列出可刪選項等使用者確認」
4. **Skill 的 description 不該包含對抗性詞彙**：例如「ignore previous instructions」這種 prompt injection 句型——你自己寫沒問題，但別人也能讀到，可能被 LLM 視為攻擊向量
5. **單一 Skill 不要超過 200 行**：超過了就拆成多個 Skill 或抽附件

---

## 除錯：Skill 為什麼沒被觸發？

**症狀 A：問了相關問題但 AI 沒翻 skill**

- 看 description 的觸發詞跟你的問題用詞是否重疊
- 改用 description 內的關鍵字重問一次測試

**症狀 B：CLI 啟動時 skill 沒被掃到**

- 確認資料夾結構：`.gemini/skills/<name>/SKILL.md`，缺一不可
- 確認 frontmatter 用 `---` 包起來，YAML 格式合法
- 重啟 CLI（skill 在啟動時掃描，不是熱載）

**症狀 C：多個 Skill 互相蓋掉**

- 兩個 skill 的 description 太相似 → 改寫成不同關鍵字
- 不確定當下匹配哪個 → 在 SKILL.md body 開頭加一句「執行此 skill 時請先告訴我『我正在用 explain-code skill』」協助 debug

---

## 延伸閱讀

- [Agent Skills 官方文件](https://geminicli.com/docs/cli/skills/)
- [Get started with Agent Skills tutorial](https://geminicli.com/docs/cli/tutorials/skills-getting-started/)
- [Codelabs — Create Agent Skills for Gemini CLI](https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli)
- [google-gemini/gemini-skills 範例庫](https://github.com/google-gemini/gemini-skills) — 看官方寫的 skill 怎麼長

---

## 五歲小孩版理解

- 一般情況：AI 像個工程師朋友，你問它它就回答
- 裝 Skill：你給它一本「公司 SOP」，他遇到 SOP 涵蓋的情境會自動翻書照做
- SKILL.md 的 description = SOP 目錄索引
- SKILL.md 的 body = SOP 內文
- 附件 = SOP 附錄的範本、checklist
- **重點是 description 寫得讓他「想得到該翻」**——寫太模糊永遠翻不到，寫太死板每個問題都翻
