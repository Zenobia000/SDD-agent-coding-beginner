# 安裝 Claude Code

## 結論卡

| | |
|---|---|
| **做什麼** | 裝好 `claude`，能在終端機跑起來 |
| **要多久** | 5–20 分鐘（看你有沒有裝過 Node） |
| **有訂閱嗎** | 有 → 這篇就夠。沒有 → 讀完這篇再去 [`02-free-routes.md`](./02-free-routes.md) |
| **驗收** | `claude --version` 有輸出，且能送出一句話得到回覆 |
| **下一步** | 回 [`../../BUILD.md`](../../BUILD.md) |

---

## 一、安裝

### macOS / Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows（PowerShell）

```powershell
irm https://claude.ai/install.ps1 | iex
```

### 已經有 Node.js（任何平台）

```bash
npm install -g @anthropic-ai/claude-code
```

**確認裝好了**：
```bash
claude --version
```

沒有輸出 → 跳到下方「三、裝不起來」。

---

## 二、第一次啟動

```bash
cd <你的專案目錄>
claude
```

第一次會問你登入。三種身份擇一：

| 身份 | 適合 | 計費 |
|---|---|---|
| **claude.ai 訂閱** | 個人開發 | 訂閱額度 |
| **Console API key** | 要精算成本 | 按 token |
| **公司 gateway** | 公司有統一 proxy | 公司帳 |

**沒有以上任何一種** → [`02-free-routes.md`](./02-free-routes.md)。

### 確認能用

進去之後隨便打一句話，有回覆就是好了。

```
> 你好，這是測試
```

再打 `/status` 看目前的登入方式與模型。

---

## 三、裝不起來

依序試，**不要跳**：

### ① `claude: command not found`

安裝成功但 PATH 沒更新。

```bash
# 先重開終端機。還是不行的話：
echo $PATH | tr ':' '\n' | grep -i claude    # 看有沒有在 PATH 裡

# 通常裝在這裡，把它加進 PATH
export PATH="$HOME/.local/bin:$PATH"
# 要永久生效就加進 ~/.zshrc 或 ~/.bashrc
```

### ② 權限錯誤（`EACCES`）

**不要用 `sudo npm install -g`。** 那會製造更多權限問題。

```bash
# 改用官方安裝腳本（裝在使用者目錄，不需要 sudo）
curl -fsSL https://claude.ai/install.sh | bash
```

### ③ 公司網路擋住

```bash
# 設 proxy
export HTTPS_PROXY=http://your-proxy:8080

# 公司有 TLS 檢查（自簽憑證）時
export NODE_EXTRA_CA_CERTS=/path/to/company-ca.pem
```

### ④ 都試過還是不行

```bash
claude doctor
```

它會診斷環境並指出問題。把輸出貼給助教。

**課堂上卡超過 5 分鐘 → 先用參照專案跟跑**，環境午休再修。
不要卡住整個上午。

---

## 四、常用指令（今天會用到的）

| 指令 | 做什麼 |
|---|---|
| `/status` | 看登入方式、模型、base URL |
| `/config` | 改設定，包含**切換 output style** |
| `/context` | 看目前載入了哪些規則與 skill |
| `/mcp` | 看接了哪些 MCP |
| `/help` | 列出所有可用指令 |

> **注意**：`/output-style` 這個指令在 v2.1.91 已移除。
> 切換輸出風格改用 `/config` → Output style。

---

## 五、設定檔在哪

| 檔案 | 範圍 | 進版控嗎 |
|---|---|---|
| `~/.claude/settings.json` | 你所有的專案 | ❌ 個人的 |
| `<專案>/.claude/settings.json` | 這個專案，**團隊共用** | ✅ 會 |
| `<專案>/.claude/settings.local.json` | 這個專案，只有你 | ❌ 已在 gitignore |

**憑證絕對不要寫進 `<專案>/.claude/settings.json`** —— 那個檔案會被 commit。

---

## 下一步

回 [`../../BUILD.md`](../../BUILD.md) 的動手第 2 步。
