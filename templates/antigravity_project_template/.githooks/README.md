# .githooks/ — 機械層安全閘門

> **為什麼有這個資料夾**：AGENTS.md §7 寫了「不准 commit secret、不准 force-push」，
> 但**寫進文件只有 ~70% 順從率**（研究數據，見 [`../.agents/AGENTS-GUIDE.md`](../.agents/AGENTS-GUIDE.md)）。
> 真正不可破的規則要放在**機械層**——這就是這些 git hook 的工作。

## 為什麼是 git hook，不是 Antigravity settings.json hook

| 層 | 攔什麼 | 攔得到誰 |
|---|---|---|
| **git hook（這裡）** | git 操作（commit / push） | **人 + 任何 AI agent，跨工具一律生效** |
| Antigravity `settings.json` hook | agent 的工具呼叫生命週期 | 只攔 agent，攔不到你手敲的 `git commit` |

「不准 commit secret」的威脅是 **git 操作**，所以正解是 **git hook**。這也貼合本模板「跨工具通用」的定位——換 Claude Code / Cursor / Codex 都不影響。

## 兩個 hook

| Hook | 擋什麼 |
|---|---|
| `pre-commit` | 寫死的 Google API key（`AIza…`）、誤加的 `.env`（真正的 secret 洩漏） |
| `pre-push` | 對 `main` / `master` 的 force-push（改寫歷史，不可逆） |

> 「忘了填金鑰 placeholder」不在這擋——那是功能 bug 不是洩漏，交給 `/check-key`（agent 有判斷力，不會誤擋 `.env.example` 或文件本身）。hook 只守「一旦發生就不可逆」的安全威脅。

## 啟用（每個新 clone / 複製出來的專案都要做一次）

git hook 預設不會自動啟用（`core.hooksPath` 是本地設定、不隨 commit 帶走）。複製模板後跑：

```bash
git init            # 如果還不是 git repo
git config core.hooksPath .githooks
chmod +x .githooks/*   # macOS / Linux / WSL
```

驗證：故意在某檔案貼一行 `AIza` + 35 個字元，`git add` 後 `git commit` 應被擋下。

> 真的要略過（你要為後果負責）：`git commit --no-verify` / `git push --no-verify`。
