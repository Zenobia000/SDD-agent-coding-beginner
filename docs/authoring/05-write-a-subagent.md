# 05 — 寫一個 subagent

## 這是什麼

**一個有自己 context 和系統提示的助手。它做完只回報結論，過程不佔用你的主對話。**

---

## 什麼時候用它而不是別的

**兩題，任一「是」就用 subagent**：

1. 這件事會產生一堆**我不想看**的中間資訊嗎？（檔案內容、log、搜尋結果）
2. 這件事需要**不知道我為什麼這樣寫**的視角嗎？

第 2 題最常被忽略，但它是 subagent 最有價值的用途：

> **別讓球員兼裁判。**
> 主對話知道你的意圖，會不自覺地配合你的假設。
> subagent 沒有這個包袱 —— 它只看到 code 說了什麼。

| 情境 | 用 skill | 用 subagent |
|---|---|---|
| 理解一段 code | `/next` | — |
| 在 200 個檔案裡找東西 | — | ✅ |
| 為新功能寫測試 | `/tdd` | — |
| 為既有 code 補一批測試 | — | ✅ |
| 例行品質檢查 | `/review` | — |
| 重要決策要第二意見 | — | ✅ |

---

## 最小可跑範例

`.claude/agents/finder.md`：

```markdown
---
name: finder
description: 在陌生的 code 裡定位東西 —— 「這個功能實作在哪」「誰呼叫了這個」。
  它讀很多檔案但只回報結論。找單一已知檔案時不要派它，直接讀比較快。
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
model: inherit
color: cyan
---

你是程式碼定位員。**你只找，不改，不評論品質。**

## 你存在的理由

主對話的 context 很貴。你的價值是：**讀 30 個檔案，只回報 10 行結論。**

## 輸出格式

## 找到了 / 沒找到

## 位置
- `path/to/file.py:42` — <一句話>

## 沒找到的
<使用者問了但確實不存在的，明講。不要腦補>

## 硬規則

- ❌ 不准回傳超過 20 行
- ❌ 不准說「可能在 ___」—— 要嘛附行號，要嘛明講沒找到
- ❌ 不准改任何檔案
```

存檔 → 重開 → 對 Claude 說「幫我找 ___ 在哪」，它會判斷要不要派。

---

## Frontmatter 常用欄位

| 欄位 | 做什麼 | 建議 |
|---|---|---|
| `name` | 識別名 | **必填** |
| `description` | **AI 判斷何時要派的依據** | **必填**，要寫「什麼時候不要派」 |
| `tools` | 能用哪些工具 | 明確列出，不要全開 |
| `disallowedTools` | 移除哪些工具 | **唯讀 agent 必用** |
| `model` | `sonnet` / `opus` / `haiku` / `inherit` | 預設 `inherit`，多數情況不用改 |
| `color` | 顯示顏色 | 讓你在 task list 一眼分辨 |
| `permissionMode` | 權限模式 | 唯讀 agent 可用 `default` |
| `maxTurns` | 最多跑幾輪 | 防止失控的保險 |
| `skills` | 啟動時預載哪些 skill | 讓它一開始就有流程可循 |
| `isolation: worktree` | 在獨立 git worktree 跑 | 會改檔案且可能衝突時 |

### 唯讀 agent 的標準寫法

```yaml
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit, NotebookEdit
```

**審查類的 agent 一律唯讀。**
理由：發現問題就順手改掉，你會失去 review 的機會，而且改錯了更難查。

---

## 填空模板

```markdown
---
name: <名稱>
description: <做什麼>。<什麼時候派>。<什麼時候不要派 —— 這句很重要>
tools: <列出來，不要全開>
disallowedTools: <唯讀的話一定要寫>
model: inherit
color: <顏色>
---

你是 <角色>。**<一句話定義邊界，例：你只找不改>**

## 你存在的理由

<為什麼這件事需要獨立 context 或獨立視角。寫出來，agent 才知道自己
在扮演什麼角色，而不是變成第二個萬能助手>

## <方法 / 策略>

<依序的檢查步驟。寫得像 checklist，不要寫成散文>

## 輸出格式

<嚴格規定。subagent 的輸出是給主對話讀的，格式亂會抵銷它的價值>

## 硬規則

- ❌ 不准回傳超過 <N> 行 ← 幾乎每個 agent 都需要這條
- ❌ 不准 <越界行為>
- ✅ <查不到 / 做不到時要明講>
```

---

## 三個常見錯誤

### ① 沒限制輸出長度

subagent 的價值是**壓縮**。回傳 200 行就等於沒有省下 context。

```markdown
✅ ❌ 不准回傳超過 20 行 —— 超過表示你在貼檔案內容而不是回報結論
```

**幾乎每個 subagent 都該有這條。**

### ② description 沒寫「什麼時候不要派」

```yaml
❌ description: 幫你找程式碼
   → AI 每次找東西都派它，連讀一個已知檔案都派 → 反而更慢

✅ description: 在陌生的 code 裡定位東西。
   找單一已知檔案時不要派它，直接讀比較快。
```

### ③ 讓審查 agent 能改檔案

```yaml
❌ tools: Read, Write, Edit, Grep
   → 它會「順手」修掉發現的問題，你失去 review 的機會

✅ tools: Read, Glob, Grep, Bash
   disallowedTools: Write, Edit, NotebookEdit
```

---

## 怎麼驗證它真的生效

```bash
claude          # 重開
```

**① 直接指定**
```
> 派 finder 找一下 summarize 函式定義在哪
```

**② 自動判斷**
說一句 description 描述的情境，看它會不會主動派。

**③ 檢查輸出真的被壓縮了**
主對話裡應該只看到結論，不是一堆檔案內容。

| 症狀 | 檢查 |
|---|---|
| 找不到這個 agent | 檔名 / frontmatter `name` 對嗎？重開了嗎？ |
| 啟動失敗 | `tools` 裡有沒有寫錯的工具名？一個都對不上會直接失敗 |
| 回傳一大堆 | 缺「不准超過 N 行」 |
| AI 從不派它 | description 太空泛 |
| AI 太常派它 | description 缺「什麼時候不要派」 |

---

## 進階：獨立視角的組合用法

需要更強的獨立性時，同一件事派**多個視角不同**的 agent：

```
一個發現 → 派三個 agent，各自用不同 lens 檢驗
           ├─ 正確性：這真的會壞嗎？
           ├─ 安全性：這能被利用嗎？
           └─ 重現性：我照著做真的會出現嗎？
         → 兩票以上認定是真的，才當成真的
```

比派三個一模一樣的 agent 有效得多 —— **多樣性抓得到冗餘抓不到的東西。**

---

## 本專案的四個 subagent 可以直接讀

| Agent | 學什麼 |
|---|---|
| `explorer` | 怎麼寫「只回報結論」的壓縮型 agent |
| `reviewer` | 怎麼寫「預設立場是懷疑」的獨立視角 |
| `test-writer` | 唯一會改檔案的那個，看它怎麼限制範圍 |
| `security-auditor` | 怎麼寫「從攻擊者視角走一遍」的方法論 |

路徑：`.claude/agents/`

---

## 下一步

複製 `explorer.md` 改成你領域專用的版本，重開後說一句它 description 裡的情境，看會不會被派出去。
