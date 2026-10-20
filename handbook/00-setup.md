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
| （選用）Claude API key | D2 的 I4 要用真的模型跑 eval。**有 Claude 訂閱就不需要**：上課 repo 的 `LLM_PROVIDER=claude-cli` 會借用已登入的 Claude Code。只有 Codex 訂閱的人，I4 跟講師的示範機一起跑 | 有 key 的話，**存在密碼管理器，不要貼在任何聊天室** |

> 公司電腦常擋安裝或擋連線。**先用公司電腦試一次**，不行就改帶個人電腦，並提前和 IT 確認。

---

## 2. 工具

### 必裝

| 工具 | 安裝 | 確認方式 |
|---|---|---|
| Git | [git-scm.com](https://git-scm.com/downloads) | `git --version` 印出版本號 |
| Python 3.11 以上 | [python.org](https://www.python.org/downloads/) | `python3 --version`（Windows：`python --version`） |
| Node.js 24 | [nodejs.org](https://nodejs.org/) | `node --version` 印出 v24 開頭。講師實測的是 24；更舊的版本能不能跑 Next.js 16 ⚠️ 未驗證 |
| 編輯器 | VS Code 或任何你習慣的 | 打得開 Markdown 檔，看得到 Mermaid 預覽更好 |

> ⚠️ **Python 版本一定要先確認是 3.11 以上。** 版本太舊時，`pip install` 不一定會報錯，
> 可能卡住好幾分鐘不動，看起來像當機。Linux / macOS 內建的 `python3` 常常是 3.10 或更舊。
> 印出來的是 3.10 以下，就照上面的連結裝新版，再用 `python3.12 --version` 這種帶版本號的指令確認。

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

## 4. 預熱：把要下載的東西先下載好

D2 早上 40 個人同時下載套件，教室網路會塞爆。**課前在家先跑一次**，之後就是從快取拿。

```bash
# 在 leavebot-bootcamp 根目錄
python3 -m venv .venv
source .venv/bin/activate          # Windows：.venv\Scripts\activate
pip install -e ".[dev]"
pytest                             # 全綠才算過

# 先把 Next.js 的骨架下載一次（版本要和 STACK.md 一樣），確認能建立之後刪掉
npx --yes create-next-app@16.4.2 warmup --ts --app --eslint --tailwind --no-src-dir --import-alias "@/*" --use-npm --disable-git --yes
rm -rf warmup                      # Windows：rmdir /s /q warmup
```

講師實測：create-next-app 第一次約 40 秒；跑不完或報錯，把完整訊息截圖寄給講師。

---

## 5. 最後確認

在 repo 根目錄啟動 agent：

| 你用的是 | 打這個 | 通過的樣子 |
|---|---|---|
| Claude Code | `/compass` | 列出技能清單 |
| Codex | `$compass` | 列出技能清單 |

再請它做一件事：

```text
只讀 README.md 和 HARNESS.md，告訴我這個 repo 是做什麼的、哪個檔案會擋下危險的 git 指令，三句話以內。
```

D1 的第一個單元會解剖這些設定檔，先有個印象就好。

它回答得出來，你的環境就完成了。

---

## 卡住了

| 狀況 | 處理 |
|---|---|
| `claude` / `codex` 找不到指令 | 重開終端機。還是不行，照官方說明確認安裝路徑有加進 PATH |
| 公司網路連不上 | 換手機熱點試一次。能連 → 是公司防火牆，找 IT |
| `/compass` 或 `$compass` 沒反應 | 確認是在 repo 根目錄啟動；Windows 確認上面的 symlink 步驟 |
| `npx create-next-app` 很慢或失敗 | 換手機熱點試一次；公司網路常擋 npm registry，找 IT 開 `registry.npmjs.org` |
| `pip install` 卡住好幾分鐘不動 | 先按 Ctrl+C，再跑 `python3 --version`。低於 3.11 就是版本問題：裝新版後刪掉 `.venv`，用新版重建 |
| 以上都試過 | 把**完整錯誤訊息**截圖，開課前三天寄給講師 |
