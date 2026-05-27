# .workstation/ — 跨平台一鍵 Terminal 工作站

一鍵啟動 3 格（或 4 格）開發工作站，**Mac / Linux / WSL / Windows 共用同一份設定**。

---

## 一、它解決什麼問題

每次開新專案都要：
1. 開 terminal
2. `cd` 到專案資料夾
3. 切多個分割視窗
4. 每格再 `cd` 一次
5. Windows 還要先 `wsl` 進去

**現在：雙擊一個檔案，全部搞定。**

---

## 二、一次性安裝

### Mac
```bash
brew install zellij
```

### Linux / WSL
```bash
cargo install --locked zellij
# 或下載 binary：https://github.com/zellij-org/zellij/releases
```

### Windows 原生
1. 裝 WSL（管理員 PowerShell）：
   ```powershell
   wsl --install
   ```
2. 從 Microsoft Store 裝 **Windows Terminal**
3. 進 WSL，依 Linux 步驟裝 zellij

---

## 三、啟動

### Mac / Linux / WSL
```bash
./start            # 3 格：RUN / WATCH / CHECK
./start 4          # 4 格：ENV / RUN / WATCH / CHECK
```

第一次需要 `chmod +x start`（git clone 後通常已保留執行權限）。

### Windows
**雙擊 `start.bat`**（最簡單），或 PowerShell：
```powershell
.\start.ps1
.\start.ps1 4
```

會自動：開 Windows Terminal → 跳進 WSL → cd 到專案 → 啟動 zellij。

---

## 四、Layout 對照

### 3 格（預設）

```
┌──────────────┬──────────────┐
│   RUN        │   WATCH      │
│  主任務       │  系統日誌      │
├──────────────┴──────────────┤
│          CHECK              │
│   驗證 / 測試 / 資源監控       │
└─────────────────────────────┘
```

### 4 格（多服務 / RAG / Agent）

```
┌──────────────┬──────────────┐
│   ENV        │   RUN        │
│  docker ps   │  pipeline     │
├──────────────┼──────────────┤
│   WATCH      │   CHECK       │
│  logs -f     │  curl / test │
└──────────────┴──────────────┘
```

---

## 五、zellij 操作

| 動作 | 快捷鍵 |
|------|--------|
| 切換 pane | `Ctrl+p` 然後方向鍵 |
| 全螢幕當前 pane | `Ctrl+p` 然後 `f` |
| 關閉 pane | `Ctrl+p` 然後 `x` |
| Detach（保留背景） | `Ctrl+o` 然後 `d` |
| 重新 attach | `zellij attach ws-<專案名>` |
| 看快捷鍵幫助 | 啟動後底部 status bar 會提示 |

---

## 六、自訂 — 讓每格自動跑指令

開 `.workstation/layout.kdl`，把每個 pane 的 args 改成你要的指令：

```kdl
pane name="RUN" {
    command "bash"
    args "-c" "make run; exec bash"          # 自動跑 make run
}
pane name="WATCH" {
    command "bash"
    args "-c" "docker compose logs -f; exec bash"
}
pane name="CHECK" {
    command "bash"
    args "-c" "watch -n 2 docker compose ps; exec bash"
}
```

`exec bash` 的用途：指令結束（或被 Ctrl-C）後留在 shell 裡，不會把 pane 關掉。

---

## 七、複製到新專案

```bash
# 從這個 repo 拷貝
cp -r path/to/this-repo/{.workstation,start,start.ps1,start.bat} /path/to/new-project/
chmod +x /path/to/new-project/start

cd /path/to/new-project
./start
```

只要四個檔案：`.workstation/`、`start`、`start.ps1`、`start.bat`。

---

## 八、Troubleshooting

| 症狀 | 原因 / 解法 |
|------|-------------|
| `./start: command not found` | `chmod +x start` |
| `zellij: command not found`（Mac/Linux） | 安裝 zellij（見上方） |
| Windows 雙擊 `.bat` 閃退 | 開 PowerShell 跑 `.\start.ps1` 看錯誤訊息 |
| `wsl.exe` 找不到 | 管理員執行 `wsl --install`，重開機 |
| `wt.exe` 找不到 | Microsoft Store 裝 Windows Terminal |
| 已在 zellij session 裡 | 先 `Ctrl+o d` detach，或開新 terminal |
| 想換 WSL distro | `start.ps1` 把 `wsl.exe --cd ...` 改成 `wsl.exe -d Ubuntu --cd ...` |

---

## 九、設計原理

```
┌─ 設定層 ──────┐   .workstation/*.kdl  （跨平台同一份）
│              │
├─ Layout 層 ──┤   zellij               （Mac / Linux / WSL 一致）
│              │
├─ Terminal 層 ┤   Windows Terminal / iTerm2 / 任何 (可換)
│              │
└─ 啟動層 ─────┘   start / start.ps1    （偵測 OS 自動分流）
```

**為什麼選 zellij 不選 tmux**：
- 原生支援宣告式 layout 檔（KDL）
- 不用記快捷鍵，畫面有提示
- WSL / Mac / Linux 設定完全一致

**為什麼不直接用 Windows Terminal 的 split**：
- Windows Terminal 的 layout JSON 跟 Mac / Linux 不通用
- 包一層 zellij 讓設定真正跨平台
