# 沒有訂閱怎麼上這堂課

## 結論卡

| | |
|---|---|
| **建議** | 先用**官方免費額度**跑。真的不夠再走第三方路由 |
| **機制** | 兩個環境變數：`ANTHROPIC_BASE_URL` + 憑證變數 |
| **代價** | 官方**不背書也不支援**第三方 gateway；部分功能會失效 |
| **課堂能不能跑** | 能。**S5 完全不需要 API 額度** |
| **下一步** | 先跑第一節的「先確認你真的需要」 |

---

## 先確認你真的需要

**這堂課 8 小時的實際 token 用量不大。** 大部分時間在：
- 寫決策卡、寫考卷（人在想）
- 改 hook、寫 command（人在打字）
- 跑測試、看報告（本機執行）

真正吃 API 的只有 S4 的 TDD 與迴圈。

**先用官方免費額度試試看。** 不夠再往下讀。

---

## 三條路，依「風險由低到高」排

| 路線 | 是什麼 | 誰適合 | 主要風險 |
|---|---|---|---|
| ① **cc-switch** | 桌面 App，管理多組帳號 / 供應商設定並一鍵切換 | 有多個來源要切換的人 | 第三方軟體，要自己審 |
| ② **claude-code-router** | 本機跑的路由 gateway | 想接自己的 API key 或其他模型 | 官方不支援，功能可能壞 |
| ③ **模型聚合服務** | 用第三方平台的 API key | 完全沒有 Claude 帳號 | **可能整堂課功能不完整** |

---

## ⚠️ 先講清楚代價（這節不要跳）

**已確認**（來源：Claude Code 官方 gateway 文件）：

> Anthropic 不背書、不維護、也不稽核第三方 gateway 產品，
> **且不支援透過任何 gateway 把 Claude Code 導向非 Claude 模型**。

實際會遇到的：

| 會壞的 | 為什麼 |
|---|---|
| **Remote Control** | 需要 claude.ai 身份；`ANTHROPIC_BASE_URL` 指向非 Anthropic 主機時會停用 |
| **語音輸入** | 同上 |
| **`/fast` 快速模式** | 可用性檢查直接打 `api.anthropic.com`，不走 gateway |
| **部分新功能** | gateway 沒轉發新欄位時，會回 `400 Extra inputs are not permitted` |
| **訂閱額度** | 設了憑證變數後，claude.ai 訂閱**不會被使用**，改成按 token 計費給憑證擁有者 |

**課程本身不依賴上面任何一項。** 但你要知道自己在換什麼。

---

## 機制：只有兩個變數

不管走哪條路，Claude Code 這端都是同兩個變數。

```bash
export ANTHROPIC_BASE_URL=https://your-gateway.example.com
export ANTHROPIC_AUTH_TOKEN=your-token
```

**憑證變數選哪個**：

| 變數 | 什麼時候用 | 送到哪個 header |
|---|---|---|
| `ANTHROPIC_AUTH_TOKEN` | 對方說「bearer token」或不確定時 | `Authorization: Bearer` |
| `ANTHROPIC_API_KEY` | 對方說「API key」或「x-api-key」 | `x-api-key` |

**猜錯會拿到 401。** 換另一個再試。

### 驗證（開 claude 之前先做這步）

```bash
curl -X POST "$ANTHROPIC_BASE_URL/v1/messages" \
  -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-4-6","max_tokens":1,"messages":[{"role":"user","content":"."}]}'
```

| 回什麼 | 意思 |
|---|---|
| `{"id":"msg_...` | ✅ 通了 |
| 說模型不認得 | ✅ **也算通了**（它認證過才拒絕模型名） |
| `401` | 憑證變數選錯或 key 無效 → 換另一個變數 |
| 連不上 | URL 錯或網路擋住 |

**先 curl 通了再開 `claude`。** 這樣失敗時你知道是哪一層的問題。

### 讓它持久生效

```bash
# ~/.claude/settings.json —— 對你所有專案生效
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://your-gateway.example.com",
    "ANTHROPIC_AUTH_TOKEN": "your-token"
  }
}
```

⚠️ **不要寫進 `<專案>/.claude/settings.json`** —— 那個檔案會被 commit。

### 確認 Claude Code 真的走 gateway

```
claude
/status
```

要看到 `Anthropic base URL` 那一行顯示你的 gateway 位址。
沒有那行 = 變數沒傳進去。

---

## 路線 ①：cc-switch

**已確認**：GitHub `farion1231/cc-switch`，官方網站 ccswitch.io。
跨平台桌面 App，管理 Claude Code / Codex 等多種 agent 的供應商設定並一鍵切換。

**適合**：你有多組來源（公司的、自己的、朋友分享的），想快速切換。

**它做的事**：幫你改上面那兩個變數，不用每次手動 export。

**要自己判斷的**：
- 它會讀寫你的憑證設定 → **裝之前看一下它的原始碼或社群評價**
- 第三方桌面軟體，Anthropic 不背書

---

## 路線 ②：claude-code-router

**已確認**：npm `@musistudio/claude-code-router`（查詢時 v3.0.18），
GitHub `musistudio/claude-code-router`。本機跑的路由 gateway，有 CLI 與 web 管理介面。

```bash
npm install -g @musistudio/claude-code-router
```

**適合**：想接自己的 API key，或想在不同模型間路由。

**⚠️ 重要**：官方**不支援**把 Claude Code 導向非 Claude 模型。
你可以這樣做，但：
- 功能可能壞（工具呼叫、thinking、structured output 行為都可能不同）
- 出問題時官方文件幫不了你
- **課堂上出問題，助教也幫不了你**

**課堂建議**：如果你要走這條，**課前就設好並驗證過**。
不要當天現場設定。

---

## 路線 ③：模型聚合服務

**未知**：你提到的「omnirouter」，我查證後沒有找到對應的知名專案
（GitHub 上同名 repo 星數都在 25 以下）。
**推測**你指的可能是 **OpenRouter**（知名的模型聚合平台）。

若要走這類服務：
1. 在該平台取得 API key
2. 找到它的 Anthropic 相容端點（不是所有平台都有）
3. 照上面的兩個變數設定
4. **一定要先跑 curl 驗證**

**風險最高的一條**：
- 速度與穩定性看服務商
- Anthropic 格式相容性看服務商
- 可能整堂課的 skill 行為都不太一樣

---

## 完全沒有任何 API 可用時

**這堂課還是可以上。** 對照表：

| 站 | 需要 API 嗎 | 沒有 API 的做法 |
|---|---|---|
| S0 開機 | ❌ | 照跑，只是最後不能送訊息測試 |
| S1 問對問題 | ⚠️ 需要 | 用紙本 `cards/task-triage.md` 自己填決策卡 |
| S2 定契約 | ⚠️ 需要 | 對照 `labs/reference-project/S2/expected/` 自己寫 |
| S3 先跑通 | ⚠️ 需要 | 用線上平台的免費額度（AI Studio / Replit） |
| S4 迴圈開工 | ✅ 一定要 | 改讀老師的 `loop-log.md` 做紙上推演 |
| **S5 方法變資產** | **❌ 完全不用** | **照跑，這站是編輯本機檔案** |
| S6 積木裝配 | ❌ | 複製 `labs/blocks/` 是本機操作 |
| S7 守門與交付 | ❌ | 資安掃描是 grep + git，維運卡是寫文件 |

**八站裡有四站完全不需要 API。**
而且不需要 API 的那幾站，正好包含最關鍵的 S5。

---

## 建議的決策

```
有 claude.ai 訂閱？
├─ 有 → 直接用，不要折騰
└─ 沒有 ↓
   願意付 Console API 的錢嗎？（這堂課大概幾美金）
   ├─ 願意 → 用 Console API key，最穩
   └─ 不願意 ↓
      課前有時間設定並驗證嗎？
      ├─ 有 → 路線 ① 或 ②，**課前就設好**
      └─ 沒有 → 課堂用「沒有 API 的做法」，S5 照樣完整跑
```

---

## 下一步

先跑一次官方免費額度看夠不夠。真的不夠，選一條路線並**在課前**完成 curl 驗證。
