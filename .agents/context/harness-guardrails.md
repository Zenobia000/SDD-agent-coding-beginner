# Harness 細節：`hooks.json` 與 guard 行為

> 從 [`../README.md`](../README.md) 第 1 節拆出來的細節。README 只留「哪一層負責什麼」，
> 這裡放「這個 repo 的 hook 實際擋什麼、為什麼這樣設計」。
> 改 `.agents/hooks/` 或 `.agents/hooks.json` 就必須同步改本檔。

## 1. `hooks.json` 的形狀

```jsonc
{
  "smarttrip-guard": {              // ← top-level key 是「具名 hook」，不是事件名稱
    "enabled": true,
    "PreToolUse": [                 // ← PreToolUse / PostToolUse 是 grouped：matcher + hooks 包一層
      {
        "matcher": "run_command|shell_exec|send_command_input",
        "hooks": [{ "type": "command", "command": "python3 ./hooks/guard.py", "timeout": 10 }]
      },
      {
        "matcher": "file_change|write_blob|edit_notebook|delete_directory",
        "hooks": [{ "type": "command", "command": "python3 ./hooks/guard.py", "timeout": 10 }]
      }
    ]
  }
}
```

三個容易踩到的點：

- **working directory 是 `hooks.json` 所在的目錄**，也就是 `.agents/`——不是 repo root，也不是腳本自己的目錄。所以命令寫 `python3 ./hooks/guard.py`，而 `guard.py` 開頭要手動把自己的目錄補進 `sys.path`，否則 `import guard_core` 會在 `PYTHONSAFEPATH` 環境下靜默失敗。
- **`matcher` 是 regex**，比對的是 tool 名稱。上面兩組名稱來自 `agy` 1.1.12 binary 實測的 121 個 tool。
- **所有 JSON key 是 camelCase**（protojson）。

## 2. guard 的行為對照表

> **這張表是教材承諾。改 `hooks/` 就必須同步改這張表。**
>
> **怎麼複驗**：本節第 4 小節有三行可直接貼進終端機的 stdin 樣本，涵蓋 deny 寫入、白名單放行、
> deny 破壞性 shell 三種路徑。移植當下另以 15 個 Antigravity 格式 fixture 實跑驗證過，
> 但那些 fixture **沒有進版控**（產生在移植 session 的暫存目錄），所以不要拿它們當可重現的證據。

分流在 `guard.py`，判定在 `guard_core.py`：

| tool 群組 | tool 名稱 | `deny`（直接擋） | `ask`（要求確認） | `{}`（不表態） |
|---|---|---|---|---|
| shell | `run_command`、`shell_exec`、`send_command_input` | 路徑操作數命中 `.env` / `.env.*` / `*.pem` / `id_rsa*` / 路徑含 `secrets` 目錄段；`rm -r` 且 `-f` 打到 `/`、`/*`、`~`、`$HOME`、`$PWD`、`.`、`..`、`./*`、`../*` 或任何 `workspacePaths` root | 其餘任何 `rm -rf`；`git reset --hard`、`git clean -f`、`git checkout --`、`git restore`、force push、`git branch -D`、`git stash drop` / `git stash clear`、`DROP DATABASE` / `DROP TABLE`、`TRUNCATE TABLE` | 其他全部 |
| 寫入 | `file_change`、`write_blob`、`edit_notebook` | 寫入真實 `.env` / `.env.*`；寫入 `*.pem` / `id_rsa*` / `secrets/`；內容含**長度足夠**的 `sk-` / `sk-ant-` / `ghp_` / `AIza` / `AKIA` 憑證樣式，或 `-----BEGIN … PRIVATE KEY-----` | — | 其他全部 |
| 刪除 | `delete_directory` | 目標是 workspace root 或上述 catastrophic 目標；目標是敏感路徑 | **所有其他目錄刪除**（`delete_directory` 本質是遞迴且不會停下來問） | 空路徑 |
| 其他 | 上述以外的 **114** 個 tool | — | — | 全部 |

「114」的算法：binary 實測共 121 個 tool，兩條 matcher 命中 7 個（`run_command`、`shell_exec`、`send_command_input`、`file_change`、`write_blob`、`edit_notebook`、`delete_directory`），121 − 7 = 114。

> ⚠️ **「長度足夠」不是修辭。** `guard_core.py` 的 `SECRET_PATTERNS` 都帶最小長度：`sk-` 後面要 20+ 字元、
> `ghp_` 要 30+、`AIza` 要 30+、`AKIA` 要正好 16 碼大寫英數。所以 `K=sk-test` 這種短字串**不會**被擋——
> 這是刻意的，避免把說明文件與測試 fixture 當成外洩憑證。

## 3. 四個必須理解的設計

1. **沒有意見時輸出 `{}`，不是 `{"decision":"allow"}`。**
   `allow` 會直接蓋過使用者的 permission 設定，等於把整個授權機制關掉。本 repo 的 guard 只輸出
   `deny`、`ask` 或 `{}`——`allow`、`force_ask`、`deny_unless_prior_grant` 刻意不使用
   （完整的 `decision` 值清單見 [`../../ANTIGRAVITY.md`](../../ANTIGRAVITY.md) 第 5 章）。
   ⚠️ **證據等級**：Google 內建規格把 `decision` 列為 **required**，**未載明**省略時的行為；
   「`{}` = 不表態」是本 repo 的設計選擇與合理推論，尚未端到端實測。選它而不選 `allow`
   的理由是失敗方向較安全：猜錯只會多問一次，猜 `allow` 錯了會直接繞過使用者授權。
2. **`deny` 的訊息一律指向替代做法**（例：改寫 `.env.example`），不是單純拒絕。`.env.example` / `.sample` / `.template` 白名單放行。
3. **shell 分支掃的是路徑操作數，不是整條指令的每個字。** `git commit` 等訊息型子指令的 `-m` 內容、以及 heredoc 內容都視為文字，commit message 提到 `.env` 或私鑰不會被誤擋。例外是餵給 `bash` / `sh` / `zsh` / `eval` / `source` 的 heredoc——那份內容會被當指令執行，照樣要掃。
4. **憑證掃描刻意排除「被取代掉的舊內容」**：`TargetContent`、`oldString`、`diff`、`contextLines`。把它們納入掃描，「把已經外洩的金鑰刪掉」這個修補動作反而會被 deny。

`guard.py` 讀不懂 stdin 時輸出 `{}` 並 exit 0——**fail-open**。guard 自己壞掉不該把 agent 卡死；真正的硬邊界由第 5 節的第二層兜底。

## 4. 可重跑的驗證樣本

在 repo 根目錄貼這三行（**不會真的建立 `.env`**）：

```bash
printf '%s\n' '{"toolCall":{"name":"file_change","args":{"AbsolutePathUri":"file:///tmp/x/.env","NewContent":"DEMO=value"}},"workspacePaths":["/tmp/x"]}' | python3 .agents/hooks/guard.py; echo
printf '%s\n' '{"toolCall":{"name":"file_change","args":{"AbsolutePathUri":"file:///tmp/x/.env.example","NewContent":"DEMO=fake-value"}},"workspacePaths":["/tmp/x"]}' | python3 .agents/hooks/guard.py; echo
printf '%s\n' '{"toolCall":{"name":"run_command","args":{"CommandLine":"rm -rf /"}},"workspacePaths":["/tmp/x"]}' | python3 .agents/hooks/guard.py; echo
```

依序應該是 `deny` / `{}` / `deny`。guard 的輸出**不含結尾換行**，上面每行結尾的 `; echo` 就是補這個換行用的。

## 5. 兩層 guardrail

倉庫根目錄的 `.githooks/` 是同一道防線的另一半：

| 層 | 管誰 | 擋什麼 | 啟用方式 |
|---|---|---|---|
| `.agents/hooks/` | Antigravity 的工具呼叫 | 敏感路徑、疑似憑證、不可逆的 shell 操作 | 信任 workspace 後自動生效 |
| `.githooks/` | **人與任何 agent** 的 git 操作 | `pre-commit` 擋 staged 的真 `.env` / 私鑰 / `secrets/` 與新增行的 secret；`pre-push` 對 `main` / `master` 用 `merge-base --is-ancestor` 要求快轉 | 每個 clone 手動 `git config core.hooksPath .githooks` |

換掉 AI 工具時第一層要重寫，第二層完全不用動——這是刻意的分層。
