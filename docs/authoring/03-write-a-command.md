# 03 — 寫一個 command

## 這是什麼

**一個 markdown 檔 = 一個 `/指令`。最輕量的資產，五分鐘寫得完。**

---

## 什麼時候用它而不是別的

```
是一段我要跟著走的固定動作？
├─ 是 → 需要附件（範本 / 腳本）嗎？
│        ├─ 需要 → skill
│        └─ 不需要 → command ← 你在這
└─ 否 → 看 07-choose-which.md
```

**command vs skill**：兩者都產生 `/name`、行為一樣。
command 是單檔、好維護；skill 能帶附件、能被 AI 自動載入、能限制工具。

**先寫 command。** 之後真的需要附件再升級成 skill —— 把檔案搬進
`skills/<name>/SKILL.md` 就好。

---

## 最小可跑範例

`.claude/commands/standup.md`：

```markdown
---
description: 產出今天的站立會議摘要
---

# /standup

## 步驟

1. 跑 `git log --oneline --since=yesterday --author="$(git config user.name)"`
2. 讀 `tasks/sprint-current.md` 的 Now 區塊
3. 讀 `tasks/known-issues.md` 標為 blocked 的條目

## 輸出

昨天做了：<條列，最多 3 條>
今天要做：<條列，最多 3 條>
卡住的：<一條，沒有就寫「無」>

## 硬規則

- ❌ 不准超過 9 行
- ❌ 不准把 commit message 原文貼上 —— 要濃縮成人話
```

存檔 → **重開 `claude`** → 打 `/standup`。

---

## Frontmatter

command 的 frontmatter 比 skill 精簡：

| 欄位 | 做什麼 |
|---|---|
| `description` | `/` 選單裡顯示的說明 |
| `argument-hint` | 參數提示，例 `[issue-number]` |
| `arguments` | 具名參數，供 `$name` 代換 |

```yaml
---
description: 修一個 GitHub issue
argument-hint: <issue 編號>
arguments: issue
---

去看 issue #$issue，先寫一個能重現問題的失敗測試。
```

---

## 參數

| 寫法 | 拿到什麼 |
|---|---|
| `$ARGUMENTS` | 全部 |
| `$0` `$1` | 第 1、第 2 個 |
| `$name` | 具名（要先在 `arguments` 宣告） |
| `${CLAUDE_PROJECT_DIR}` | 專案根目錄 |

**沒有用到 `$ARGUMENTS` 時**，參數會自動附加成 `ARGUMENTS: <值>`，
所以不寫也不會弄丟使用者的輸入。

---

## 填空模板

```markdown
---
description: <一句話，會出現在 / 選單>
argument-hint: [<參數說明>]
---

# /<名稱> — <定位>

## 動手前先確認

<要先讀什麼 / 要先有什麼。沒有就刪掉這段>

## 步驟

1. <一步一個動作>
2. <一步一個動作>

## 輸出

<嚴格規定格式，否則每次長得不一樣>

下一步：<恰好一個動作>

## 硬規則

- ❌ 不准 <最容易犯的錯>
- ✅ 一定要 <最重要的動作>
```

---

## 三個常見錯誤

### ① 沒寫輸出格式

```markdown
❌ ## 步驟
   1. 檢查測試
   2. 檢查 lint
   → 每次輸出長得都不一樣，你要重新讀一遍才知道結果

✅ ## 輸出
   | 項目 | 狀態 |
   |---|---|
   | 測試 | <N passed> |
   → 每次一樣，掃一眼就知道
```

**格式固定，你的眼睛才能自動化。**

### ② 沒寫硬規則

沒有「❌ 不准」那段，AI 會自由發揮：
- 自動修東西（你只想看報告）
- 輸出爆長
- 順便做你沒要求的事

**每個 command 至少寫一條 ❌。**

### ③ 步驟寫得太模糊

```markdown
❌ 1. 檢查程式碼品質
✅ 1. 跑 `ruff check .`，只回報 error 等級，忽略 warning
```

**每步要具體到「照做就會得到同樣結果」。**

---

## 怎麼驗證它真的生效

```bash
claude          # 重開
```

```
/               # 看選單裡有沒有你的指令
/your-command   # 打打看
```

| 症狀 | 檢查 |
|---|---|
| 選單裡沒有 | frontmatter 的 `---` 成對嗎？檔名對嗎？ |
| 有但沒反應 | 重開了嗎？ |
| 行為不對 | 步驟太模糊，或缺「硬規則」段 |
| 輸出每次不一樣 | 缺「輸出」段的格式規定 |

---

## 從 command 升級成 skill

需要附件或想讓 AI 自動觸發時：

```bash
mkdir -p .claude/skills/my-command
git mv .claude/commands/my-command.md .claude/skills/my-command/SKILL.md
# 在 frontmatter 補上 name 與更具體的 description
```

指令名不變，使用者無感。

---

## 本專案的四個 command 可以直接讀

| Command | 學什麼 |
|---|---|
| `gate` | 怎麼寫「嚴格照此格式輸出」 |
| `kickoff` | 怎麼寫「一次問一題」的互動流程 |
| `ship` | 怎麼寫「依序執行、紅燈就停」的編排 |
| `blocks` | 怎麼寫「先看現況再給建議」 |

路徑：`templates/claude_project_template/.claude/commands/`

---

## 下一步

想一件你今天跟 AI 講過最多次的話，用上面的模板寫成 command，重開後打 `/` 確認它在選單裡。
