# 自訂 Slash Command（進階，可以先跳過）

> 初學者可以先不管這個資料夾，等用熟基本對話再來看。

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
