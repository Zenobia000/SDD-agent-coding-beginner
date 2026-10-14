# 課前環境檢核表

> **開課前一週完成。** 上課時間不處理安裝問題 —— 環境卡住的人，會錯過整個上午。
>
> 每一項都有「確認方式」。打得出那個結果，才算完成。

---

## 1. 帳號

| 項目 | 說明 | 確認方式 |
|---|---|---|
| GitHub 帳號 | 用來 fork 課程 repo | 能登入 github.com |
| Claude 或 ChatGPT 付費方案 | Claude Code 需要 Claude Pro / Max 或 Anthropic API；Codex 需要 ChatGPT 付費方案或 OpenAI API。**兩個選一個就好** | 下面第 2 步能登入 |
| LLM API key | Day 4 的 eval 要呼叫真的模型。Starter 內建 Anthropic（Claude）；用 OpenAI 的話，要在 Day 4 前讓 agent 照 `LLMClient` 介面補一個實作 | 拿到一串 key，**存在密碼管理器，不要貼在任何聊天室** |

> 公司電腦常擋安裝或擋連線。**先用公司電腦試一次**，不行就改帶個人電腦，並提前和 IT 確認。

---

## 2. 工具

### 必裝

| 工具 | 安裝 | 確認方式 |
|---|---|---|
| Git | [git-scm.com](https://git-scm.com/downloads) | `git --version` 印出版本號 |
| Python 3.11 以上 | [python.org](https://www.python.org/downloads/) | `python3 --version`（Windows：`python --version`） |
| 編輯器 | VS Code 或任何你習慣的 | 打得開 Markdown 檔，看得到 Mermaid 預覽更好 |

### AI coding agent（二選一）

| | Claude Code | Codex |
|---|---|---|
| 官方說明 | [docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code/overview) | [developers.openai.com/codex](https://developers.openai.com/codex/cli) |
| 啟動 | `claude` | `codex` |
| 確認方式 | 啟動後能登入，打 `hello` 有回應 | 啟動後能登入，打 `hello` 有回應 |

安裝指令會隨版本更新，**以官方說明頁為準**。

---

## 3. 上課 repo

上課用的是 [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)，不是這份講義所在的 repo。

```bash
# 先在 GitHub 上 fork 上課 repo，再 clone 你們組的那一份
git clone https://github.com/<你的帳號>/leavebot-bootcamp.git
cd leavebot-bootcamp
```

### Windows 使用者先做這一步

這個 repo 用 symlink 讓 Codex 讀到技能。Windows 預設不建立 symlink，要先：

1. 開啟「開發人員模式」（設定 → 系統 → 開發人員專用）
2. clone **之前**執行：`git config --global core.symlinks true`

已經 clone 過的，刪掉重新 clone。

---

## 4. 最後確認

在 repo 根目錄啟動 agent：

| 你用的是 | 打這個 | 通過的樣子 |
|---|---|---|
| Claude Code | `/compass` | 列出技能清單 |
| Codex | `$compass` | 列出技能清單 |

再請它做一件事：

```text
只讀 README.md，告訴我這個 repo 是做什麼的，三句話以內。
```

它回答得出來，你的環境就完成了。

---

## 卡住了

| 狀況 | 處理 |
|---|---|
| `claude` / `codex` 找不到指令 | 重開終端機。還是不行，照官方說明確認安裝路徑有加進 PATH |
| 公司網路連不上 | 換手機熱點試一次。能連 → 是公司防火牆，找 IT |
| `/compass` 或 `$compass` 沒反應 | 確認是在 repo 根目錄啟動；Windows 確認上面的 symlink 步驟 |
| 以上都試過 | 把**完整錯誤訊息**截圖，開課前三天寄給講師 |
