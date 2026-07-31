# 06 — 寫一個 output style

## 這是什麼

**改 system prompt，換掉 AI 講話的形狀。每一句回覆都生效。**

---

## 什麼時候用它而不是別的

| 你想改的是 | 用 |
|---|---|
| **講話的形狀**（語氣、格式、密度） | **output style** |
| 專案的**事實**（用什麼工具鏈、檔案在哪） | CLAUDE.md |
| 一套要跟著走的**流程** | skill |
| 某次的一句話調整 | 直接講就好 |

```
✅ output style：「結論先行」「清單 ≤5」「證據要標級」「選型題先給答案」
✅ CLAUDE.md   ：「這個專案用 pnpm」「測試在 tests/」

❌ 不要把專案慣例寫進 output style —— 換專案就錯了
❌ 不要把講話風格寫進 CLAUDE.md —— 會被專案資訊淹沒
```

---

## 最小可跑範例

`.claude/output-styles/terse.md`：

```markdown
---
name: Terse
description: 極簡輸出 —— 結論先行、不超過 10 行、結尾恰好一個下一步。
keep-coding-instructions: true
---

你的讀者只想知道結論和下一步。

## 永遠遵守

1. **第一句就是結論。** 禁止「讓我們先了解…」這類開場。
2. **回覆不超過 10 行**（code block 不算）。
3. **結尾恰好一個下一步。**
4. 刪掉不改變「建議 / 實作方式 / 風險 / 下一步」的內容。

## 禁止

- 客套開場、結尾寒暄
- 「順便建議你也可以…」
- 最後再把全文重複總結一次
- 敘述例行的工具使用過程
```

切換：`/config` → **Output style** → 選 Terse。

> **注意**：`/output-style` 這個指令在 **v2.1.91 已移除**。改用 `/config`。

---

## Frontmatter

只有四個欄位：

| 欄位 | 做什麼 | 預設 |
|---|---|---|
| `name` | 顯示名稱 | 檔名 |
| `description` | `/config` 選單裡的說明 | 無 |
| **`keep-coding-instructions`** | **保留 Claude Code 內建的軟體工程指示** | `false` |
| `force-for-plugin` | 只給 plugin 用 | `false` |

### `keep-coding-instructions` 是最重要的一個

```yaml
keep-coding-instructions: true     # 還在寫 code，只是改講話方式
keep-coding-instructions: false    # 完全不做軟體工程（寫作助手、資料分析）
```

**寫成 `false` 而人還在 coding**，會失去內建的工程行為
（怎麼界定改動範圍、怎麼寫註解、怎麼驗證工作）。

**開發用的 style 一律寫 `true`。**

---

## 填空模板

```markdown
---
name: <名稱>
description: <一句話。會出現在 /config 選單>
keep-coding-instructions: true
---

<一句話定義你的讀者是誰、他要什麼。這句決定後面所有規則。>

## 永遠遵守

1. **<最重要的一條>**
2. **<第二條>**
3. **<第三條>**

（**最多 5 條。** 超過模型會開始漏掉。）

## 依情境換格式

### <情境 A，例：選型題>
<規定的輸出結構>

### <情境 B，例：debug>
<規定的輸出結構>

## 例外（這些情況放寬）

- 使用者明確要求「詳細解釋」→ 可以完整展開
- <不可逆操作> → **先確認再動手**，這比簡潔重要
- <什麼情況該停下來>

## 禁止

- <具體的壞習慣>
- <具體的壞習慣>
```

---

## 三個常見錯誤

### ① 寫「請簡潔」這種不可執行的指令

```markdown
❌ Be concise.
❌ 請簡潔一點。
❌ 不要浪費 token。
   → 「簡潔」對模型沒有可執行標準
```

```markdown
✅ 回覆不超過 10 行（code block 不算）
✅ 清單最多 5 項
✅ 結尾恰好一個下一步
✅ 刪掉不改變「建議 / 實作 / 風險 / 下一步」的內容
```

**要具體到可以核對。**

### ② 只縮短字數，沒降低決策成本

這是最容易犯的錯：

```markdown
❌ 只寫「講短一點」
   → 得到：「Root cause is a circular dependency caused by
            eager module initialization.」
   → 很短，但你還是不知道要做什麼
```

```markdown
✅ 加上：「選型 / 架構 / 比較題，第一句要是**推薦的選擇**，不是一個動作。」
   → 得到：「建議保留 A，只有在需要 B 時才換。
            下一步：把 config 第 12 行改成 ___」
```

**你要的是「能做決定的輸出」，不是「比較短的輸出」。**

### ③ 規則超過 5 條

模型會開始漏掉後面的。**先寫最重要的 3 條，用一週，不夠再加。**

---

## 怎麼驗證它真的生效

### ① 切換

```
/config    → Output style → 選你的
```

**改完要 `/clear` 或開新 session。**
output style 是 system prompt 的一部分，session 啟動時載入。

### ② 檢查它有在選單裡

沒有的話：
- frontmatter 的 `---` 成對嗎？
- 檔案在 `.claude/output-styles/` 嗎？
- 重開了嗎？

### ③ 實測

用**同一個問題**問兩次，切換前後比對：

```
> Postgres 還是 SQLite？
```

| 沒有 style | 有 dev-decision style |
|---|---|
| 「這取決於你的需求。Postgres 適合…SQLite 適合…你可以考慮…」 | 「建議 SQLite。只有需要多寫入者並行時才換 Postgres。」 |

**看第一句話是不是結論。** 那是最快的判斷方法。

### ④ 確認範圍

output style **只影響主對話**。subagent 有自己的 system prompt，不受影響。
要改 subagent 的講話方式，寫進那個 agent 的 `.md` 裡。

---

## 兩層架構（推薦的組合）

單一 output style 解決不了所有問題。實務上是兩層：

```
output style  = 永遠生效的最低標準（講話的形狀）
     +
skill         = 遇到特定情境才載入的完整協議（決策的方法）
```

本專案的實作：

| 層 | 檔案 | 管什麼 |
|---|---|---|
| 永久 | `output-styles/adhd.md` | 結論先行、清單 ≤5、一個下一步 |
| 永久 | `output-styles/dev-decision.md` | 三種問題三種格式 + 證據分級 |
| 按需 | `skills/decide/SKILL.md` | 遇到選型 / debug 時的完整決策協議 |
| 說明 | `rules/09-evidence-labels.md` | **為什麼**要標級（style 只說怎麼做） |

**style 管形狀，rule 管理由，skill 管流程。**

---

## 本專案的三個 output style 可以直接讀

| Style | 學什麼 |
|---|---|
| `adhd` | 怎麼把「簡潔」寫成可執行的規則 |
| `dev-decision` | 怎麼依問題類型換格式 + 三級證據標記 |
| `teaching` | 怎麼寫「教學」而不是「完成任務」的風格 |

路徑：`templates/claude_project_template/.claude/output-styles/`

---

## 下一步

複製 `adhd.md` 改成你自己的版本，用 `/config` 切換後開新 session，
問一個選型問題看第一句是不是結論。
