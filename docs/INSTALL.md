# 安裝 SOP：Antigravity CLI（`agy`）

> 本文只講 **Antigravity**。本 repo 的 harness（`AGENTS.md` + `.agents/`）是 Antigravity 原生格式，不需要任何其他 AI CLI。

**證據標記**（2026-08-11）—— 本文每個「你應看到」都標了來源等級：
【本機實測】= 在這台機器實跑過，貼的是真實輸出。
【安裝腳本原文】= 用 `curl` 讀過 `install.sh` / `install.ps1` 原始碼，未執行。
【binary 字串】= 從 `agy` 1.1.12 執行檔抽出的訊息字串（該流程未實跑，字串本身為真）。
⚠️ 官方文件未載明 = 查不到，本文不猜。

---

## 0. 先讀這段

### 這台機器的結論

| 目標 | 這台能不能 | 依據 |
|---|---|---|
| **Antigravity CLI（`agy`）** | ✅ **已經裝好了**（版本 `1.1.12`，位於 `~/.local/bin/agy`，認證已完成） | 【本機實測】`agy --version` → `1.1.12` |
| **Antigravity IDE** | ❌ **裝了也開不起來** | 【本機實測】`DISPLAY` 與 `WAYLAND_DISPLAY` 皆未設定、非 WSL、`SSH_CONNECTION` 有值 —— 這是一台**沒有圖形介面的遠端 Linux 主機**。IDE 是 GUI 應用程式 |

這不是「設定沒調好」，是**這台機器沒有畫面可以顯示**。不要花時間修。

### 兩條路線，二選一

- **路線 A（本 repo 預設，推薦）**：Headless / SSH 主機**只裝 `agy` CLI**，全程走終端機。
  本 repo 的 harness 以 CLI 為主，走這條**不會少任何功能**。
- **路線 B**：IDE 裝在你手邊**有桌面**的電腦（Apple Silicon Mac / Windows / 有 X11 或 Wayland 的 Linux），
  遠端主機維持只有 CLI。第 4 節是寫給那台看的。

### 已經裝好了還要看這份嗎

要。**第 3 節（確認裝好了）與第 5 節（接上 harness）**是每次換機器、換 clone 都要重跑的驗收；
第 1、2 節是給還沒裝的機器看的。

---

## 1. 前置檢查

安裝前把下面整段貼進終端機跑一次。

```bash
# 1. 作業系統與架構
grep -o 'PRETTY_NAME="[^"]*"' /etc/os-release
uname -m

# 2. glibc / libstdc++ —— Antigravity 的硬需求
ldd --version | head -1
strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep -o 'GLIBCXX_3\.4\.[0-9]*' | sort -V | tail -1

# 3. ~/.local/bin 在不在 PATH（安裝器預設把 agy 放這裡）
case ":$PATH:" in *":$HOME/.local/bin:"*) echo "PATH OK";; *) echo "PATH MISSING";; esac

# 4. 有沒有圖形介面（決定 IDE 能不能裝在這台）
echo "DISPLAY=[${DISPLAY:-未設定}] WAYLAND_DISPLAY=[${WAYLAND_DISPLAY:-未設定}] WSL=[${WSL_DISTRO_NAME:-否}]"

# 5. 是不是 SSH 連進來的（決定認證走哪條路）
echo "SSH_CONNECTION=[${SSH_CONNECTION:-未設定}]"
```

**【本機實測】輸出（2026-08-11）**

```
PRETTY_NAME="Ubuntu 22.04.5 LTS"
x86_64
ldd (Ubuntu GLIBC 2.35-0ubuntu3.14) 2.35
GLIBCXX_3.4.30
PATH OK
DISPLAY=[未設定] WAYLAND_DISPLAY=[未設定] WSL=[否]
SSH_CONNECTION=[10.136.49.128 65063 10.137.80.64 22]
```

**逐項判讀**

| 檢查 | 通過條件 | 不符合怎麼辦 |
|---|---|---|
| OS / 架構 | 64-bit Linux / macOS / Windows，x86_64 或 aarch64 | 【安裝腳本原文】不符會直接 `Fatal: Unsupported operating system` 或 `Fatal: Unsupported architecture` |
| glibc | `≥ 2.28` | 低於 2.28 不能裝。換一台，或升級發行版 |
| GLIBCXX | `≥ 3.4.25` | 低於不能裝。Ubuntu 20+ / Debian 10+ / Fedora 36+ / RHEL 8+ 一般都達標 |
| `~/.local/bin` in PATH | `PATH OK` | 顯示 `PATH MISSING` 也沒關係 —— 安裝器會自己接手設定（見 2.2）。見第 6 節第 1 項 |
| `DISPLAY` / `WAYLAND` | 有值才有桌面 | 兩者皆未設定 = 沒有 GUI，**跳過第 4 節**，走路線 A |
| `SSH_CONNECTION` | 有值 = 遠端 session | 有值代表認證要走「貼授權碼」流程（見 2.3），不要枯等瀏覽器彈出 |

> `agy` 是 Go 靜態編譯的單一執行檔（【本機實測】193 MB），**不需要 Node.js、不需要 Python、不需要套件管理器**。
> 前置檢查裡沒有 Node 檢查不是漏寫。

---

## 2. 安裝 `agy`

### 2.1 一行安裝

**macOS / Linux**

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

**Windows（PowerShell）**

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

【安裝腳本原文】腳本實際做的事，依序是：

1. 偵測 OS 與架構 → 印 `✓ Platform detected: <platform>`
2. 查詢 release manifest → 印 `✓ Latest available version: <version>`
3. 下載並**驗證 checksum** → 印 `✓ Download complete and checksum verified.`
   （checksum 不符會 `Security Halt: ... Installation aborted.` 並中止 —— 這是好事，不要繞過）
4. 把執行檔寫到 **`$HOME/.local/bin/agy`**（Windows 是 `%LOCALAPPDATA%\agy\bin\agy.exe`）
5. 印 `⠋ Configuring shell environment...`，然後**呼叫 `agy install` 自己設定 shell 環境**

**已經裝過會怎樣**：【安裝腳本原文】偵測到檔案已存在就不覆蓋，改印
`Notice: 'agy' is already installed at ...` 與
`The Antigravity CLI automatically self-updates in the background during regular runs.`，
並提示要重裝就先 `rm` 掉執行檔。也就是說 **`agy` 平常會自己在背景更新**，不需要定期重跑安裝腳本。

### 2.2 `--skip-aliases` / `--skip-path` 是給 `agy install` 用的，不是給 curl 那行

這一點很多教學寫錯，這裡講清楚。

【安裝腳本原文】`install.sh` **只接受兩個旗標**：

```
Usage: install.sh [options]

Options:
  -d, --dir <path>    Specify a custom directory to install the binary
  -h, --help          Display this help menu
```

【本機實測】`--skip-aliases` / `--skip-path` 屬於 **`agy install` 子命令**（`agy help install`
原文：`Configure environment paths and shell settings`）：

| 旗標 | 官方原文 | 什麼時候用 |
|---|---|---|
| `--skip-path` | `Bypasses shell profile PATH appending` | 你自己管理 PATH（例如 `~/.local/bin` 早就在裡面），不想被安裝器再加一行 |
| `--skip-aliases` | `Bypasses shell profile alias purging` | 你自己在 `.bashrc` / `.zshrc` 定義過 `agy` 或 `antigravity` 同名 alias |
| `--dir <path>` | `Custom directory target to configure PATH for` | 執行檔不在預設位置 |

**正確用法是分兩步**（不是把旗標塞進 curl 那行）：

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash   # 這步無論如何都會跑一次 agy install
agy install --skip-path --skip-aliases                        # 想改設定就事後自己重跑
```

裝到別的目錄用 `-d`：

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash -s -- --dir "$HOME/bin"
```

【安裝腳本原文】帶 `--dir` 時腳本最後會呼叫 `agy install --dir "<你指定的目錄>"`。

### 2.3 認證：SSH / 無 GUI 走「貼授權碼」

裝完直接啟動：

```bash
agy
```

**有桌面的機器**會走：【binary 字串】`Opening browser to authenticate with %s...` —— 自動開瀏覽器完成 OAuth。

**這台（SSH / headless）沒有瀏覽器可開**，會退回手動貼碼流程。【binary 字串】提示原文是：

```
Please visit the following URL to authorize the application:
<一個很長的 https://... 授權網址>

After authenticating, copy the code displayed in the browser and paste it below:
```

（另有一句備援文案：`If you aren't automatically redirected, paste the authorization code below`）

**逐步做法**

1. 在遠端終端機執行 `agy`。
2. **把印出來的授權 URL 整段複製**，貼到**你自己筆電的瀏覽器**開啟。
3. 用 Google 帳號登入並授權。
4. 瀏覽器會顯示一段授權碼（authorization code）。
5. **把授權碼貼回遠端終端機**的提示後面，按 Enter。

**你應看到**：【binary 字串】`Authentication successful!`

**憑證存在哪**：【本機實測】`~/.gemini/antigravity-cli/antigravity-oauth-token`（權限 `600`）。
這個檔就是「已登入」的證據，也是第 7 節登出時要清的東西。

### 2.4 第一次在 repo 裡啟動會問你信不信任這個資料夾

【binary 字串】首次在一個 workspace 啟動 `agy` 會出現信任確認，選項文字是 `Yes, I trust this folder`。
選信任之後，【本機實測】該路徑會被寫進 `~/.gemini/antigravity-cli/settings.json` 的
`trustedWorkspaces` 陣列（本機該陣列目前正是這個 repo 的絕對路徑）。

⚠️ 官方文件未載明「不信任」時具體會停用哪些功能。**合理推論**是 `.agents/` 底下會執行程式碼的
customization（尤其 hooks）不會生效 —— 所以第 5 節驗收失敗時，先回來確認你有選信任。

---

## 3. 確認裝好了

三個命令，全部**唯讀、不消耗 AI credits**。

### 3.1 版本與位置

```bash
agy --version
command -v agy
```

**你應看到**：一組版本號 + 執行檔絕對路徑。【本機實測】輸出：

```
1.1.12
/home/os-sunnie.gd.weng/.local/bin/agy
```

### 3.2 模型清單 —— 這一步同時驗證「認證成功」

```bash
agy models
```

這個命令會**連線到 Google 拉取可用模型**，所以它列得出東西 = 你的憑證是有效的。

**你應看到**：【本機實測】輸出（2026-08-11）：

```
Fetching available models...
gemini-3.6-flash-high	Gemini 3.6 Flash (High)
gemini-3.6-flash-medium	Gemini 3.6 Flash (Medium)
gemini-3.6-flash-low	Gemini 3.6 Flash (Low)
gemini-3.5-flash-high	Gemini 3.5 Flash (High)
gemini-3.5-flash-medium	Gemini 3.5 Flash (Medium)
gemini-3.5-flash-low	Gemini 3.5 Flash (Low)
gemini-3.1-pro-high	Gemini 3.1 Pro (High)
gemini-3.1-pro-low	Gemini 3.1 Pro (Low)
claude-sonnet-4-6	Claude Sonnet 4.6 (Thinking)
claude-opus-4-6-thinking	Claude Opus 4.6 (Thinking)
gpt-oss-120b-medium	GPT-OSS 120B (Medium)
```

左欄是傳給 `--model` 的字串。清單會隨 Google 上架而變，**數量與名稱不同不代表壞掉**；
真正的通過條件是「印得出清單、exit code 0」。

### 3.3 Plugin 狀態

```bash
agy plugin list
```

**你應看到**：全新環境沒裝 plugin 時，【本機實測】輸出就是一行 `No imported plugins.`。
**這是通過，不是錯誤** —— 本 repo 不依賴任何 plugin。

### 3.4 一次跑完的驗收腳本

```bash
agy --version && agy models >/dev/null && agy plugin list >/dev/null && echo "AGY OK"
```

**你應看到**：版本號 + `AGY OK`。沒印出 `AGY OK` 就別往下走，先看第 6 節。

> ⚠️ 不要用 `agy -p "hello"` 之類的命令來「測試」——那會真的呼叫模型並消耗額度。
> 上面三個命令已經足以證明安裝與認證都成功。

---

## 4. Antigravity IDE（在**有桌面**的那台）

**這台機器跳過本節。**（第 0 節已說明：無 `DISPLAY`、無 Wayland、非 WSL。）

下載頁：**<https://antigravity.google/download>**。系統需求：

| 平台 | 需求 | 注意 |
|---|---|---|
| **macOS** | 12（Monterey）以上，且在 Apple 安全性更新支援範圍內（通常是當前版本與前兩版） | **僅 Apple Silicon。Intel Mac（x86）不支援** |
| **Windows** | Windows 10（64-bit）以上 | — |
| **Linux** | glibc ≥ 2.28、glibcxx ≥ 3.4.25（例：Ubuntu 20、Debian 10、Fedora 36、RHEL 8） | 需求與 CLI 相同，但**還必須有桌面環境** |

IDE 與 CLI 是**兩個獨立的安裝**：裝了 IDE 不會讓遠端主機多出 `agy`，反之亦然。
兩邊都讀同一份 repo 內的 `AGENTS.md` 與 `.agents/`，所以 harness 不用改。

⚠️ 官方文件未載明 IDE 的解除安裝程序，見第 7 節。

---

## 5. 把本 repo 的 harness 接上

`agy` 從**當前目錄往上走到 repo root**（含 `.git` 的目錄）尋找設定，
所以下面全部要在 **repo 根目錄**執行。

> 本節只驗證，**不建立任何檔案**。檔案缺了代表該分支還沒把這部分合併進來，不是安裝失敗。

### 5.1 檔案存在性（純 shell，可立刻跑）

```bash
cd <你的 repo 根目錄>
git rev-parse --show-toplevel          # 確認你真的在 repo root
ls -d AGENTS.md .agents .agents/skills .agents/rules .agents/agents
echo "skill 資料夾: $(ls -d .agents/skills/*/ 2>/dev/null | wc -l)"
echo "SKILL.md   : $(ls .agents/skills/*/SKILL.md 2>/dev/null | wc -l)"
```

**你應看到**：

- 五個路徑都列得出來，沒有 `No such file or directory`
- **「skill 資料夾」與「SKILL.md」兩個數字相等** —— 不相等代表有資料夾少了 `SKILL.md`，
  那個 skill 不會被載入

### 5.2 `agy` 有沒有真的讀到 skills

在 repo 根目錄啟動：

```bash
agy
```

在互動介面裡輸入 slash command：

```
/skills
```

**你應看到**：`.agents/skills/` 底下每個 skill 的 `name` 與 `description` 出現在清單裡，
標題會顯示 **workspace skill 數 + 內建 skill 數** 的總和，並分成
`Workspace skills · Workspace config` 等分組。

【本機實測 2026-08-12】本 repo 有 31 個 workspace skill，`/skills` 標題顯示 **`33 skills`**
（31 + 2 個內建 `agy-customizations`、`antigravity-guide`），清單裡逐一列出
`adhd-dev-mode`、`branch-name`、`build-check`、`code-review`… 等，`description` 完整顯示。
**harness 確認在 Antigravity 互動模式下真的生效。**

> ### ⚠️ 陷阱：`agy -p` headless 模式**不會**載入 workspace customization
>
> 【本機實測 2026-08-12】同一個 repo、同一個根目錄，改用 print mode：
>
> ```bash
> agy -p "列出你目前可用的 skill 名稱"
> ```
>
> 回答是「共 2 個：agy-customizations、antigravity-guide」——
> **31 個 workspace skill 一個都沒有**，`AGENTS.md` 與 `.agents/rules/` 同樣沒載入。
> 連續三種問法（含允許工具、指定 `view_file` 不走 shell）結果一致。
>
> 排除過的可能原因：workspace 已在 `trustedWorkspaces` 內、`SKILL.md` 格式正確、
> 確實在 repo root、log 也顯示 `workspaceDirs` 指向本 repo。log 另有一行
> `ApplyProjectPermissionGrants: no grants for project "CLI Project"`，
> 顯示 headless 跑在泛用 project 底下而非本 workspace。
>
> **⚠️ 官方文件未載明這個差異。** 對本課的意思是：
> **驗收 harness 一定要用互動模式 `agy`，不要用 `agy -p`。**
> 把 `agy -p` 寫進 CI 或腳本時也要知道它看不到 `.agents/`。
>
> 附帶一提，headless 模式**無法向使用者要權限，需要權限的工具會被自動拒絕**，
> 錯誤訊息會提示到 `settings.json` 的 `permissions.allow` 加規則，語法是
> `command(<target>)`（【本機實測】log 顯示目前有一條 `command(git status)`）。

沒出現時的三個常見原因，依序排查：

1. **不在 repo root 啟動** —— `pwd` 對一下。
2. **workspace 沒被信任** —— 回 2.4，重新啟動並選 `Yes, I trust this folder`。
3. **`SKILL.md` 的 frontmatter 缺 `description`** —— Antigravity 的 skill frontmatter 只有
   `name` 與 `description` 兩個欄位，而且**兩個都必填**；`description` 是 agent 判斷要不要載入的唯一依據。
   用 `head -5 .agents/skills/<名稱>/SKILL.md` 確認。

### 5.3 其他 harness 元件

| 元件 | 檔案 | 怎麼驗 |
|---|---|---|
| 專案長期 context | `AGENTS.md`（repo root） | 【事實】無 frontmatter，對所在目錄與所有子目錄永遠 active。存在即生效 |
| Rules | `.agents/rules/*.md` | 有 frontmatter，`trigger: always_on` 才無條件載入 |
| Subagents | `.agents/agents/` | `ls -d .agents/agents/*/agent.md`（只驗檔案存在性）。⚠️ `agy agents` 本機實測 exit 0、**零輸出**，不能當驗收，理由見 `ANTIGRAVITY.md` 第 4 章 |
| Hooks | `.agents/hooks.json` | `python3 -c "import json; json.load(open('.agents/hooks.json'))"` 先確認 JSON 合法 |
| MCP | `.agents/mcp_config.json` | 在 `agy` 內用 `/mcp` |

> ⚠️ Antigravity 的 workspace customization **只認 `.agents/`**。【本機實測】`agy` 1.1.12 執行檔內
> 大量出現 `.agents/` 路徑字串（`strings -n 4 ~/.local/bin/agy | grep -oF '.agents/' | wc -l`
> 回 263；`strings` 參數不同數字會變，重點是「大量出現」而不是精確次數），其他 AI CLI 的
> 設定目錄路徑則一次都沒有。放在其他工具專用目錄底下的設定一律不會被載入。

---

## 6. 卡住就看這裡

| # | 症狀 | 原因 | 處置 |
|---|---|---|---|
| 1 | 裝完之後 `agy` → `command not found` | 執行檔在 `~/.local/bin/agy`，但該路徑不在 PATH（或你用了 `--skip-path`） | 先 `ls -l ~/.local/bin/agy` 確認檔案在。在的話跑 **`~/.local/bin/agy install`**（用完整路徑呼叫，讓它自己補 PATH），然後開新的 shell 或 `source ~/.bashrc`。手動的做法是把 `export PATH="$HOME/.local/bin:$PATH"` 加進 `~/.bashrc` |
| 2 | 安裝腳本印 `Notice: 'agy' is already installed at ...` 就結束了 | 【安裝腳本原文】偵測到既有執行檔就不覆蓋 —— 這是設計，不是失敗 | 平常不用管，`agy` 會自己背景更新。真要重裝：先 `rm ~/.local/bin/agy` 再重跑安裝腳本 |
| 3 | 安裝中止，訊息是 `Security Halt: The downloaded payload checksum does not match the manifest.` | 下載的檔案與官方 manifest 的 checksum 不符（網路中斷、代理伺服器改寫、或真的被竄改） | **不要想辦法繞過。** 換網路環境重跑一次；仍失敗就停手，不要手動下載塞進去 |
| 4 | 安裝失敗，訊息是 `Write Error: Permission denied when attempting to write binary to ...` | 目標目錄不可寫 | 【安裝腳本原文】腳本自己給的建議：用 `--dir` 換一個可寫目錄。**不要用 `sudo` 解決** —— 那會讓執行檔與後續自動更新都變成 root 所有 |
| 5 | SSH 進來跑 `agy`，畫面停住、沒有授權 URL 也沒有貼碼提示 | CLI 在等 OS keyring 或瀏覽器回應，而這台永遠等不到 | `Ctrl+C` 中止。確認 `echo $SSH_CONNECTION` 有值。仍不出現貼碼提示的話 —— ⚠️ 官方文件未載明強制 device-code 的旗標 —— 改走路線 B：在有桌面的機器完成登入 |
| 6 | 貼完授權碼後失敗，訊息提到 region / country / not available | Google 帳號所在地區尚未開放，或組織政策封鎖 | ⚠️ 官方文件未列出可用地區清單。組織帳號請找 workspace 管理員；**不要用 VPN 繞過服務條款** |
| 7 | `agy models` 印不出清單或報認證錯誤 | 憑證過期或未完成登入 | `ls -l ~/.gemini/antigravity-cli/antigravity-oauth-token` 確認檔案在。在的話進 `agy` 執行 `/logout` 再重新登入一次（回 2.3） |
| 8 | `/skills` 列不到 `.agents/skills/` 的 skill | (a) 不在 repo root 啟動 (b) workspace 未信任 (c) `SKILL.md` frontmatter 缺 `description` | 依 5.2 的三步排查。frontmatter 只有 `name` / `description`，兩個都必填 |
| 9 | `.agents/hooks.json` 設定好了，hook 卻沒觸發或報找不到檔案 | hook 的相對路徑基準是 **`hooks.json` 所在目錄（`.agents/`）**，不是 repo root | 把 `command` 寫成 `./hooks/guard.py` 這種相對 `.agents/` 的路徑，或直接用絕對路徑。另外先確認 JSON 合法（見 5.3）與 workspace 已信任（見 2.4） |
| 10 | 在這台跑 Antigravity IDE，出現 `cannot open display` 或直接無回應 | IDE 是 GUI 程式，這台沒有 `DISPLAY` 也沒有 Wayland | 不要嘗試修。走第 0 節路線 B |

---

## 7. 解除安裝

### 只想登出（保留安裝）

在 `agy` 互動介面內執行：

```
/logout
```

它會清掉快取的憑證。要確認清乾淨，檢查 `~/.gemini/antigravity-cli/antigravity-oauth-token` 是否已消失。

### 移除 `agy` 執行檔

⚠️ 官方文件未載明完整的解除安裝程序。【安裝腳本原文】腳本自己提到的移除方式只有刪執行檔：

```bash
rm ~/.local/bin/agy                      # macOS / Linux
```

```powershell
Remove-Item "$env:LOCALAPPDATA\agy\bin\agy.exe"   # Windows
```

`agy install` 若曾改過 shell profile（沒加 `--skip-path` / `--skip-aliases` 時），
請自行檢查 `~/.bashrc` / `~/.zshrc` / `~/.profile` 有沒有殘留的 PATH 或 alias 片段，手動清掉。

### 清設定與資料

`agy` 的家目錄資料全部在 **`~/.gemini/antigravity-cli/`** ——【本機實測】裡面有
`antigravity-oauth-token`（登入憑證）、`settings.json`（`colorScheme` / `trustedWorkspaces` / `permissions`）、
`plugins/`、`conversations/`、`history.jsonl`、`log/`。全域 customization 則在 `~/.gemini/config/`。

```bash
rm -rf ~/.gemini/antigravity-cli        # 移除 CLI 的所有本機狀態
rm -rf ~/.gemini/config                 # 移除全域 customization（確定不要才刪）
```

> 🚨 `~/.gemini/` 是 Google 系列工具共用的命名空間。
> **不要無腦 `rm -rf ~/.gemini`** —— 請照上表逐項刪你確定要刪的。

### Antigravity IDE

⚠️ 官方文件未載明解除安裝程序。依各平台慣例移除應用程式即可
（macOS 丟 Applications、Windows 走「應用程式與功能」、Linux 依你當初的安裝方式）。
設定殘留一樣落在 `~/.gemini/`，處置同上。

---

## 下一步

跑一次第 3.4 節的驗收腳本；看到版本號與 `AGY OK` 之後，回 repo 根目錄執行 `agy`，
用 `/skills` 確認本 repo 的 skills 都被載入 —— 通過了就可以開始第一章。

- 第一冊（官方元件速成）：[`../ANTIGRAVITY.md`](../ANTIGRAVITY.md)
- `agy` 日常操作與 `.agents/` 速查：[`./CLI_GUIDE.md`](./CLI_GUIDE.md)
