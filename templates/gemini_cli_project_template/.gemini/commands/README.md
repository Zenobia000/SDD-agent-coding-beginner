# 自訂 Slash Command（進階，可以先跳過）

> 初學者可以先不管這個資料夾，等用熟基本對話再來看。
> Skill / Command / MCP 三者的差別請看 [`.gemini/SKILLS.md`](../SKILLS.md) 上方對照表。

---

## 什麼是 Slash Command？

在 Gemini CLI 內打 `/help` 會看到內建指令（`/memory`、`/restore`、`/clear`…）。
你也可以加自己的 `/xxx` 指令，讓重複動作變成一句話。

例如：

```bash
/test         # 自動跑 npm test 並回報
/commit       # 自動 git add + commit + 寫 message
/check-key    # 檢查 .env 有沒有 API Key
```

## Command vs Skill 怎麼選？

兩者都能「打包重複任務」，但觸發方式不同：

| 維度 | Command | Skill |
|---|---|---|
| 觸發 | 你**手動**打 `/xxx` | AI **自動匹配** description |
| 適合 | 「我打一句就跑」的固定流程 | 「AI 應該自己判斷該做」的流程 |
| 例子 | `/test`、`/commit`、`/deploy` | 寫完 code 自動審查、安全 audit |
| 優點 | 簡單、確定性高 | 不用記指令，AI 會在對的時候用 |
| 缺點 | 你要記得 `/xxx` 是什麼 | description 寫不好就不會被觸發 |

**判斷練習**：

- 「跑 `npm test` 並摘要結果」→ **Command**（每次你都得手動觸發）
- 「我每次寫完 code 都希望被審查」→ **Skill**（你說「我寫完了」就該自動跑）
- 「把 git diff 翻譯成中文摘要」→ **Command**（明確的一次性動作）

---

## 怎麼建立？

在這個資料夾建立 `<指令名>.toml`：

```toml
# .gemini/commands/test.toml
description = "跑專案測試並回報結果"
prompt = """
請執行以下動作：
1. 用 !npm test 跑測試
2. 把通過 / 失敗的數量摘要給我
3. 如果有失敗，列出失敗的測試名稱
"""
```

存檔後，在 CLI 內打：

```
/test
```

就會自動觸發。

---

## 三個進階語法

寫熟基本 command 後，這三個語法會讓你省非常多時間：

### 1. Namespace（用資料夾分組）

把相關 command 放到子資料夾，路徑分隔符會變成冒號：

```
.gemini/commands/
├── test.toml              → /test
├── git/
│   ├── commit.toml        → /git:commit
│   └── pr.toml            → /git:pr
└── deploy/
    ├── staging.toml       → /deploy:staging
    └── prod.toml          → /deploy:prod
```

避免你的 `/help` 變成 50 個指令的大亂鬥。

### 2. `{{args}}` —— 把使用者輸入塞進 prompt

```toml
# .gemini/commands/translate.toml
description = "把指定文字翻譯成英文"
prompt = """
請把以下文字翻譯成英文，保留原本的語氣：

{{args}}
"""
```

CLI 內使用：

```
/translate 今天天氣真好，我想去散步
```

`今天天氣真好，我想去散步` 會被代入 `{{args}}` 位置。

### 3. `!{shell}` —— 把 shell 結果塞進 prompt

```toml
# .gemini/commands/explain-diff.toml
description = "解釋當前 git diff 在改什麼"
prompt = """
以下是當前的 git diff：

```
!{git diff}
```

請用 5 句話告訴我：
1. 這個 diff 改了什麼
2. 為什麼可能會這樣改
3. 有沒有需要注意的副作用
"""
```

`!{git diff}` 會先在 shell 跑 `git diff`，把輸出塞進 prompt 的對應位置。

**搭配範例**：`!{!ls -la}` 在 prompt 中插入當下目錄結構；`!{cat package.json}` 插入某個檔案內容（不過更建議用 `@package.json` 引用）。

---

## 給初學者的建議

| 你的階段   | 建議               |
| ------ | ---------------- |
| 第一個專案  | 完全不用碰，用對話就好     |
| 第三個專案  | 加 1-2 個你常重複的指令   |
| 多專案後   | 把跨專案通用的指令放到 `~/.gemini/commands/`（全域生效） |

---

## 範例（你可以複製到 toml 檔試試）

### `.gemini/commands/explain.toml`

```toml
description = "用白話解釋這個專案在做什麼"
prompt = """
請讀 @docs/PRD.md 和 @GEMINI.md，
用 5 句話跟一個完全沒寫過程式的人解釋：
1. 這個專案要解決什麼問題
2. 使用者會怎麼操作
3. 技術上大概用了什麼
4. 目前完成到哪
5. 下一步該做什麼
"""
```

### `.gemini/commands/check-key.toml`

```toml
description = "檢查 API Key 設定是否正確"
prompt = """
請：
1. 用 !grep -n API_KEY index.html 看是否還有 "請貼上你的金鑰"
2. 用 !echo $GEMINI_API_KEY 確認環境變數有設
3. 如果有問題，告訴我具體該改哪裡
"""
```

把這些放到對應 `.toml` 檔，重啟 CLI 後 `/explain`、`/check-key` 就可以用了。

### `.gemini/commands/git/commit.toml`（示範 namespace + 雙語法）

```toml
description = "幫我寫一個依照 Conventional Commits 規範的 commit message"
prompt = """
以下是目前的 git diff：

```
!{git diff --staged}
```

使用者額外提示：{{args}}

請：
1. 依 Conventional Commits 格式產生 commit subject（< 72 字）
2. body 用 3 行內說明 WHY（為什麼要這個改動）
3. 如果偵測到 breaking change，加 `BREAKING CHANGE:` footer
4. **不要直接 commit**，把 message 顯示給我，等我確認

可用的 type：feat / fix / refactor / docs / test / chore / perf / ci
"""
```

放到 `.gemini/commands/git/commit.toml`，CLI 內使用：

```
/git:commit 這次主要是改了登入流程的 error handling
```

`!{git diff --staged}` 會自動填入當下 staged diff；`{{args}}` 會被「這次主要是改了登入流程的 error handling」取代。

---

## 安全注意事項

Custom command 也是被 AI 當 prompt 跑的，所以：

- ❌ **不要在 prompt 內塞 secret**：API key、token 一律用環境變數，commit 上 git 會外洩
- ❌ **不要用 `!{shell}` 跑破壞性指令**：例如 `!{rm -rf node_modules}`——使用者不小心打 `/xxx` 會直接執行
- ❌ **不要寫絕對路徑**：commands 會跟著 repo 走，路徑要相對於專案根
- ✅ **危險動作改用「列出建議讓使用者確認」**：commit / deploy / push 這類動作，prompt 結尾加「**不要直接執行，把指令印出來等我確認**」
