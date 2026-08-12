# 刻意設計，不是缺陷

> 從 [`codebase-map.md`](./codebase-map.md) 拆出來的「探索時容易誤判為 bug」清單。
> 動手改之前先看這裡，避免重複踩同一個坑。

- **Skill 的「只有使用者能呼叫」只是文字約束。** Antigravity 的 skill frontmatter 只有 `name` 與 `description`，沒有任何能結構性禁止模型自行啟動的欄位。11 個 orchestration skill 的限制只能寫在 SKILL.md 正文第一句，另在 `AGENTS.md` 的〈Skills 的角色〉節重複一次。這是**已知能力落差，不是 bug**，也不要為了「補齊」而發明不存在的欄位。
- **Subagent 的唯讀也只是文字約束。** `tools` / `disallowedTools` / `permissionMode` / `color` 在 binary 的 87 個 yaml struct tag 中出現 0 次（已驗證的負面結論）。要硬性阻擋寫入，唯一可驗證的做法是 `hooks.json` 的 PreToolUse guard。
- **Subagent 的檔案格式本身就是未驗證慣例。** `.agents/agents/` 路徑由 binary 字串確認，`<name>/agent.md` 檔名來自 binary 常數 `writing agent.md`（高信心推論）。`agy agents` 子命令本機零輸出，無法用來驗收。相關 skill 都寫了 fallback。
- **workspace 沒有 `settings.json`**（binary 內出現 0 次）：權限由使用者在 `/permissions` 設定，不能寫成可版控的專案設定檔。這是 `hooks.json` 成為唯一硬性攔截點的原因，不是漏設定。
- **沒有 `.agents/workflows/`**：binary 內查無該字串，CLI 是否支援 workspace workflows 未載明；能實測之前本 repo 不使用。
- **`.agents/plugins/`、`skills.json`、`plugins.json` 皆不存在**：對齊「最小元件能解決就停止」。`mcp_config.json` 只放兩個 `disabled: true` 的範例。
- **`.agents/context/` 不是官方元件**：Antigravity 不會自動載入它，那是給維護者與後續 session 的筆記。
- **`.scratch/` 被 gitignore**：tickets 不是 commit 交付物，`BUILD.md` 第 6 章的 `git add` 只收產品碼是正確行為。
- **`docs/agents/project.md` 不在 repo**：由 `BUILD.md` 第 1 章的 `setup-project` 於課堂產生。**不要預先建立**，否則第 1 章的 `test -f` 驗收直接通過、練習失效（`AGENTS.md:26`）。
- **`docs/specs/` 是學生領地**：harness 自身的工程規格不得放進去（`AGENTS.md:55`）。
- **`docs/exports/` 未被 gitignore 且內容過時**：`README.md:83` 已明標以 Markdown 主線為準。
- **`.gitattributes:2` 全庫 LF**：讓 `.githooks/*` 在 WSL 下 shebang 不壞。
- **未信任的 workspace 會讓 `.agents/` 靜默失效**：`trustedWorkspaces` 不含本 repo 路徑時 rules / skills / hooks 全部不載入且不報錯。
- **教材命令不使用 `rg`（ripgrep）**：那不是標準工具，本機 `which rg` 找不到。所有「通過」條件一律用 `grep -nE`。
