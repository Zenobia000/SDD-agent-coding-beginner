# 02 — 寫一個 skill

## 這是什麼

**一套按需載入的流程說明。你打 `/name` 觸發，或 AI 依 description 自動載入。**

---

## 什麼時候用它而不是別的

| 條件 | 用 skill |
|---|---|
| 是多步驟流程 | ✅ |
| 需要帶附件（範本、腳本） | ✅ **只有 skill 能** |
| 想讓 AI 自己判斷何時該用 | ✅ **只有 skill 能** |
| 想限制它能用哪些工具 | ✅ **只有 skill 能** |
| 只是一段固定動作、沒附件 | ❌ 用 command 就好 |
| 需要獨立 context / 獨立視角 | ❌ 用 subagent |
| 需要「AI 沒得選」 | ❌ 用 hook |

> **skill 和 command 都產生 `/name`，行為一樣。**
> 差別在上面那四個「只有 skill 能」。完整比較 → [`07-choose-which.md`](./07-choose-which.md)

---

## 最小可跑範例

`.claude/skills/daily-check/SKILL.md`：

```markdown
---
name: daily-check
description: 檢查專案的每日健康狀態 —— 測試、依賴漏洞、待辦數量。用在每天開工前。
---

# /daily-check

## 步驟

1. 跑 `pytest -q`，記錄通過數
2. 跑 `pip-audit`，只回報 high / critical
3. 數 `tasks/sprint-current.md` 的 Now 有幾條

## 輸出

| 項目 | 狀態 |
|---|---|
| 測試 | <N passed> |
| 漏洞 | <數量或「無」> |
| 今日 Now | <N 條> |

下一步：<恰好一個動作>

## 硬規則

- ❌ 不准自動修任何東西 —— 只回報
- ❌ 不准超過 10 行輸出
```

存檔 → **重開 `claude`** → 打 `/daily-check`。

---

## 目錄形式（要帶附件時）

```
.claude/skills/spec/
├── SKILL.md
└── templates/
    ├── PRD-template.md
    ├── api-contract-template.md
    └── bdd-scenarios-template.md
```

在 SKILL.md 裡用 `${CLAUDE_SKILL_DIR}` 指向自己的目錄：

```markdown
用 `${CLAUDE_SKILL_DIR}/templates/PRD-template.md` 當範本。
```

**目錄名 = 指令名。** `skills/spec/` → `/spec`。

---

## Frontmatter 常用欄位

| 欄位 | 做什麼 | 什麼時候需要 |
|---|---|---|
| `name` | 顯示名稱 | 想跟目錄名不同時 |
| `description` | **AI 判斷何時載入的依據** | **一定要寫** |
| `when_to_use` | 補充觸發情境、範例說法 | description 塞不下時 |
| `argument-hint` | `/` 選單的參數提示 | 有參數時 |
| `arguments` | 具名參數，供 `$name` 代換 | 有多個參數時 |
| `allowed-tools` | 這輪免問就能用的工具 | 想減少中斷時 |
| `disallowed-tools` | 這輪不准用的工具 | **唯讀 skill 必用** |
| `disable-model-invocation` | `true` = 只有你能打，AI 不會自動載入 | 危險或昂貴的流程 |
| `user-invocable` | `false` = 不出現在 `/` 選單 | 純背景知識 |
| `model` / `effort` | 這輪換模型 / 換思考深度 | 特別難或特別簡單的任務 |
| `context: fork` | 在獨立 context 跑 | 會產生大量中間資訊 |
| `paths` | 只在處理符合的檔案時自動載入 | 特定語言 / 目錄的流程 |

**唯讀 skill 的寫法**（很重要）：
```yaml
allowed-tools: Read, Glob, Grep
disallowed-tools: Write, Edit, NotebookEdit
```
本模板的 `lesson-check` 就是這樣 —— **審查工具不該能改檔案。**

---

## 參數代換

| 寫法 | 拿到什麼 |
|---|---|
| `$ARGUMENTS` | 全部參數 |
| `$0` / `$1` | 第 1 / 第 2 個 |
| `$name` | 具名參數（要先在 `arguments` 宣告） |
| `${CLAUDE_SKILL_DIR}` | 這個 skill 的目錄 |
| `${CLAUDE_PROJECT_DIR}` | 專案根目錄 |

```yaml
---
name: fix-issue
arguments: issue branch
argument-hint: <issue 編號> <分支名>
---

處理 issue #$issue，開在 $branch 分支上。
```

---

## 填空模板

```markdown
---
name: <目錄名>
description: <做什麼>。<什麼時候用>。 ← AI 靠這句判斷要不要載入，寫具體場景
when_to_use: 使用者說「<觸發語>」「<觸發語>」，或 <狀態條件>。
argument-hint: [<參數說明>]
---

# /<name> — <一句話定位>

## 🚨 自動觸發訊號

### 強訊號
- 「<使用者會說的話>」
- <專案狀態條件>

### 反訊號（這些不要觸發）
- <什麼情況不該用它>
- <該改用哪個 skill>

---

## 執行步驟

### Step 1：<動作>
<具體到可以照做>

### Step 2：<動作>

---

## 輸出格式

<嚴格規定，否則每次長得不一樣>

---

## 硬規則

- ❌ 不准 <最容易犯的錯>
- ❌ 不准 <第二容易犯的錯>
- ✅ 一定要 <最重要的動作>

---

## 相關

- 前一步 → `/<skill>`
- 下一步 → `/<skill>`
```

---

## 三個常見錯誤

### ① description 太空泛

```yaml
❌ description: 一個好用的測試工具
❌ description: helper for the project
   → AI 判斷不出何時該用，等於沒有自動觸發

✅ description: 為既有的、沒有測試的 code 補上一批特徵測試。
   用在接手 legacy code、或某個模組被標為「沒測試所以不敢改」時。
```

**description 要寫「什麼時候用」，不是「這是什麼」。**

### ② 沒寫反訊號

只寫何時用 → AI 會過度觸發 → 你開始覺得它很煩 → 你關掉所有建議。

**每個 skill 都要有「這些情況不要觸發」那一段。**

### ③ 太長

超過 200 行就該拆，或把細節抽到同目錄的附件。

```
skills/big-thing/
├── SKILL.md          ← 主流程，100 行以內
├── reference.md      ← 細節，需要時才讀
└── templates/
```

---

## 怎麼驗證它真的生效

```bash
claude          # 重開！skill 在啟動時載入
```

**① 出現在選單**
```
/
```
打斜線看你的 skill 在不在清單裡。

**② 手動觸發得了**
```
/your-skill
```

**③ 自動觸發得了**（如果你要這個功能）
說一句 description 裡的觸發情境，看 AI 會不會主動建議。

**④ 載入狀況**
```
/context
```

### 沒反應時

| 症狀 | 檢查 |
|---|---|
| 選單裡沒有 | frontmatter 的 `---` 有沒有成對？目錄名對嗎？ |
| 有但沒反應 | 重開了嗎？ |
| AI 不會自動用 | description 太空泛，改寫成具體場景 |
| 過度觸發 | 補反訊號那一段 |

---

## 安全提醒

Skill 會被當 system instruction 執行，且**跟著 git 走**：

- ❌ 不要放 secret
- ❌ 不要寫絕對路徑
- ❌ 不要把破壞性指令寫成預設行為（「直接刪 ___」改成「列出選項等確認」）
- ✅ 唯讀的 skill 一定要設 `disallowed-tools`

**裝第三方 skill 前先讀它的 `SKILL.md` 和附帶的 scripts。**

---

## 本專案的八個 skill 可以直接讀

想看範例的話，這三個各代表一種型態：

| Skill | 型態 | 學什麼 |
|---|---|---|
| `loop` | 純流程 | 怎麼寫「一步一步跟著走」的流程 |
| `spec-it` | 帶附件 | `templates/` 目錄怎麼用 |
| `lesson-check`（根 `.claude/`） | 唯讀 | `disallowed-tools` 怎麼設 |

---

## 下一步

複製上面的填空模板，把你重複講第 3 次的那件事寫成 skill，然後重開 `claude` 打 `/` 確認它在選單裡。
