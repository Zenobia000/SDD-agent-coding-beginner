# 課前環境檢核表

> **開課前一週完成。** 上課時間不處理安裝問題。環境卡住的人，會錯過整個下午的實作。
>
> 每一項都有「確認方式」。打得出那個結果，才算完成。

---

## 1. 帳號

| 項目 | 說明 | 確認方式 |
|---|---|---|
| GitHub 帳號 | 用來 fork 上課 repo | 能登入 github.com |
| Claude 付費方案 | Claude Code 需要 Claude Pro / Max，或 Anthropic API | 下面第 2 步能登入 |
| （選用）Anthropic API key | **只有進階挑戰 C4、C5（一句話 AI 解析、注入測試）才需要**。基本範圍完全不呼叫模型 | 有 key 的話，**存在密碼管理器，不要貼在任何聊天室** |

> 公司電腦常擋安裝或擋連線。**先用公司電腦試一次**，不行就改帶個人電腦，並提前和 IT 確認。

---

## 2. 工具

### 必裝

| 工具 | 安裝 | 確認方式 |
|---|---|---|
| Git | [git-scm.com](https://git-scm.com/downloads) | `git --version` 印出版本號 |
| Python 3.12 | [python.org](https://www.python.org/downloads/) | `python3 --version`（Windows：`python --version`）印出 3.12 |
| Claude Code | [官方說明](https://docs.claude.com/en/docs/claude-code/overview) | 啟動 `claude` 後能登入，打 `hello` 有回應 |
| 編輯器 | VS Code 或任何你習慣的 | 打得開 Markdown 檔，看得到 Mermaid 預覽更好 |

> ⚠️ **Python 版本一定要先確認。** 版本太舊時，`pip install` 不一定會報錯，
> 可能卡住好幾分鐘不動，看起來像當機。Linux / macOS 內建的 `python3` 常常是 3.10 或更舊。
> 印出來不是 3.12，就照上面的連結裝新版，再用 `python3.12 --version` 這種帶版本號的指令確認。

### 建議裝

| 工具 | 用在哪 | 確認方式 |
|---|---|---|
| Node.js 18 以上 | **只給 Archify 畫圖用**（D1 單元 7、D2 投影片 36）。不用 `npm install` 任何東西 | `node --version` 印出 v18 以上 |

**沒裝 Node 也能完成兩天的主線。** 畫圖那兩段改用 Mermaid：圖寫在 Markdown 裡，用 VS Code 或 GitHub 預覽。

### 用 Codex 的人

這門課以 Claude Code 示範。上課 repo 保留了 Codex 的設定（`.codex/`、`.agents/skills`），能用，但講義不逐步說明。

安裝指令會隨版本更新，**以官方說明頁為準**。

---

## 3. 上課 repo

上課用的是 [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)，不是這份講義所在的 repo。

1. 在 GitHub 上按 **Fork**。⚠️ **取消勾選「Copy the `main` branch only」**，否則你的 fork 裡沒有講師準備的 checkpoint 分支。
2. clone 你們組的那一份，並加上講師的 repo 當 `upstream`：

```bash
git clone https://github.com/<你的帳號>/leavebot-bootcamp.git
cd leavebot-bootcamp
git remote add upstream https://github.com/Zenobia000/leavebot-bootcamp.git
git fetch upstream
git branch -r          # 看得到 upstream/cp1-requirements 等分支就對了
```

> ⚠️ 開課前講師可能還在推 checkpoint 分支。現在 `git branch -r` 看不到也沒關係，上課當天再 `git fetch upstream` 一次。

### 只有用 Codex 才需要：Windows symlink

這個 repo 用 symlink 讓 Codex 讀到技能。用 Claude Code 的人跳過這段。

1. 開啟「開發人員模式」（設定 → 系統 → 開發人員專用）
2. clone **之前**執行：`git config --global core.symlinks true`

已經 clone 過的，刪掉重新 clone。

---

## 4. 預熱：把要下載的東西先下載好

D2 下午 40 個人同時下載套件，教室網路會塞爆。**課前在家先跑一次**，之後就是從快取拿。

上課 repo 的 `main` 是空地，還沒有 `pyproject.toml`（D2 才由 agent 生出來）。所以預熱是在一個暫存 venv 裡直接裝同樣的套件，裝完就刪：

```bash
# 在任何資料夾都可以
python3 -m venv warmup-venv
source warmup-venv/bin/activate          # Windows：warmup-venv\Scripts\activate
pip install "fastapi>=0.115" "uvicorn>=0.30" "httpx>=0.27" "pytest>=8.0"
python -c "import fastapi, uvicorn, httpx, pytest; print('ok')"
deactivate
rm -rf warmup-venv                        # Windows：rmdir /s /q warmup-venv
```

印出 `ok` 就算過。跑不完或報錯，把完整訊息截圖寄給講師。

有裝 Node 的人，再確認 Archify 能跑（在上課 repo 根目錄）：

```bash
node .claude/skills/archify/bin/archify.mjs doctor
```

⚠️ 這個指令在乾淨的 Windows 筆電上還沒驗證過。失敗的話截圖寄給講師，上課改用 Mermaid 不影響進度。

---

## 5. 最後確認

**一律在 repo 根目錄啟動 `claude`。** 在子目錄啟動，護欄不會生效。

| 打這個 | 通過的樣子 |
|---|---|
| `/compass` | 列出技能清單 |

第一次啟動會問要不要啟用專案的 MCP，選同意。

再請它做一件事：

```text
只讀 README.md 和 course/HARNESS.md，告訴我這個 repo 是做什麼的、哪個檔案會擋下危險的 git 指令，三句話以內。不要修改任何檔案。
```

它回答得出來，你的環境就完成了。D1 單元 5 會解剖這些設定檔，先有個印象就好。

---

## 卡住了

| 狀況 | 處理 |
|---|---|
| `claude` 找不到指令 | 重開終端機。還是不行，照官方說明確認安裝路徑有加進 PATH |
| 公司網路連不上 | 換手機熱點試一次。能連 → 是公司防火牆，找 IT |
| `/compass` 沒反應 | 確認是在 repo 根目錄啟動 |
| `pip install` 卡住好幾分鐘不動 | 先按 Ctrl+C，再跑 `python3 --version`。不是 3.12 就是版本問題：裝新版後刪掉 venv，用新版重建 |
| `pip install` 很慢或失敗 | 換手機熱點試一次；公司網路常擋 `pypi.org`，找 IT |
| `git branch -r` 看不到 cp 分支 | fork 時勾了「只複製 main」。不用重 fork，有 `upstream` remote 就夠了；上課當天 `git fetch upstream` |
| Archify `doctor` 失敗 | 先確認 `node --version` 是 18 以上。還是失敗就截圖寄講師，上課改用 Mermaid |
| 以上都試過 | 把**完整錯誤訊息**截圖，開課前三天寄給講師 |
