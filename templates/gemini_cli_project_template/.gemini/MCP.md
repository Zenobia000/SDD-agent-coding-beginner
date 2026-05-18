# MCP（Model Context Protocol）入門

> 給 Gemini CLI 學員：MCP 是讓你的 AI「長出新工具」的標準介面。
> 範例設定都已在 `.gemini/settings.json` 寫好，預設 `enabled: false`，按需打開即可。

---

## 一句話講白

**Gemini 預設只會「讀檔、寫檔、跑 shell、搜檔案」這 4 招。**
裝 MCP 之後，它可以**多會一招**：

- 連 GitHub API → 自動建 PR、留言、看 issue
- 開瀏覽器 → 截圖驗證你的 index.html 真的長對
- 查官方文件 → 不再腦補 API、不再寫過期語法
- 連 SQLite / PostgreSQL → 直接幫你 query 資料

每個 MCP server 就是一個「外掛工具箱」。

---

## 怎麼啟用？三步驟

### 步驟 1：打開 `.gemini/settings.json`

找到你想要的 MCP，把 `enabled: false` 改成 `enabled: true`：

```json
"github": {
  "enabled": true,
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github"],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

### 步驟 2：補上需要的環境變數

例如 GitHub MCP 需要：

```bash
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxxx"
```

寫到 `~/.zshrc` 或 `~/.bashrc` 永久生效。

### 步驟 3：重啟 CLI，確認工具有載入

```bash
gemini
```

進入後打：

```
/mcp
```

會列出目前載入的 MCP server 與它們提供的工具。看到 `github` 在列就成功了。

---

## 各 MCP 用途速查

| MCP server                  | 什麼時候要打開                            | 範例 prompt                                       |
| --------------------------- | ---------------------------------- | ----------------------------------------------- |
| **filesystem**              | 想限制 Gemini 只能動特定資料夾，避免它亂改別處        | "幫我整理 ./src 內的檔案"                               |
| **fetch**                   | 想讓 Gemini 讀網頁、API 文件               | "幫我看 https://example.com/docs 然後依此實作"          |
| **github**                  | 要管 PR、issue、repo                   | "把這個 bug 開成 issue 並 assign 給我"                  |
| **context7**                | 用了某個套件，想查最新 API（避免 AI 用過期語法）       | "use context7" 加在 prompt 結尾，會自動查最新文件             |
| **puppeteer / playwright**  | 想讓 AI 自動開瀏覽器測 index.html、截圖、跑 E2E | "打開 index.html，截圖給我看畫面長對不對"                     |
| **sqlite**                  | 小專案要存資料但不想架 server                 | "查 data.db 內 users table 有幾筆"                   |

---

## 初學者該打開哪幾個？

| 你的階段           | 建議打開                                    |
| -------------- | --------------------------------------- |
| 第 1-3 個專案      | **全部關閉**。Gemini 內建工具夠用，多開 MCP 只是浪費 token |
| 開始接 API        | 打開 `fetch`、`context7`                   |
| 想自動化 git       | 打開 `github`                             |
| 做有 UI 的東西要驗證   | 打開 `puppeteer`                          |
| 進到「真的會存資料」階段   | 打開 `sqlite` 或自己接其他 DB MCP                |

---

## ⚠️ 安全警告

MCP 是**讓 AI 多一個權限通道**，不是「裝飾」。每打開一個就要想：

| MCP                | 風險                            | 緩解                                     |
| ------------------ | ----------------------------- | -------------------------------------- |
| `filesystem`       | AI 可能誤刪你限制範圍內的檔案              | 把 path 限制到專案資料夾，**不要**指到 `~/` 或 `/`   |
| `github`           | Token 外洩會被人代你發 PR / 刪 repo    | Token 只給最小權限（`repo` scope，不要給 `delete_repo`）|
| `fetch`            | AI 可能被 prompt injection 引導去抓壞網址 | 對來源不明的 URL 一律先問使用者                     |
| `puppeteer`        | 自動瀏覽可能洩漏 cookie / session     | 只用在本機 localhost，不要登入正式帳號              |
| `sqlite` / DB MCP   | AI 可能誤 DROP TABLE              | 開啟 read-only 模式；或用測試用的副本             |

**口訣：用之前先問「最壞情況是什麼」，能接受才打開。**

---

## 常見問題

### Q：MCP server 跑不起來怎麼辦？

在 CLI 內打 `/mcp`，看狀態：

- `connected` → 沒問題
- `disconnected` → 重啟 CLI，或檢查 `command` 路徑對不對
- `error` → 看錯誤訊息，常見是缺環境變數或 npx 版本太舊

### Q：可以自己寫 MCP server 嗎？

可以。MCP 是公開協定，用 Python / TypeScript 都能寫。
但**初學者不建議**——先用社群現成的，等熟了再自己做。

社群清單：[github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

### Q：MCP 的設定可以給整台機器共用嗎？

可以。把 `mcpServers` 區塊放到 `~/.gemini/settings.json`（全域），所有專案都會繼承。
專案內的 `.gemini/settings.json` 可以覆蓋全域設定。

**建議**：個人偏好的 MCP（如 context7、fetch）放全域；專案專屬的（如指定資料夾的 filesystem）放專案。

---

## 五歲小孩版理解

- Gemini 預設像「只會看書寫字的小朋友」
- 裝 MCP = 給他**新玩具**：望遠鏡（fetch）、瀏覽器（puppeteer）、GitHub 遙控器（github）
- 每個玩具都有可能闖禍，所以**沒在用的玩具收起來**（`enabled: false`）
- 用前要先教他「這玩具的安全守則」（看本檔的安全警告表）
