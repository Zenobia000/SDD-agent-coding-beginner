---
name: check-key
description: **部署 / push 到 public repo 前的 secret 雙保險掃描**。Use when user asks 檢查金鑰 / 要部署 / 要 push 到 GitHub / before pushing. 涵蓋面比 `/verify §5 Security` 更廣：未填 placeholder、hardcoded keys、env vars、`.gitignore` 覆蓋。Commit 前用 `/verify`、部署前再用本 skill。
---

# Check API Key Skill — 部署前雙保險

## 在系統中的位置

| Skill | 何時用 | 掃描範圍 |
|---|---|---|
| `/verify §5 Security` | **Commit 前**（每次） | npm audit / gitleaks / 基本 hardcoded key 掃描 |
| `/sec-scan`（本 skill） | **部署 / push public 前**（最後一道） | + 未填 placeholder + .gitignore 覆蓋 + 環境變數設定 + 已 commit 過的 secret rotate 建議 |

**心法**：`/verify` 是「日常每次 commit 的快檢」、`/sec-scan` 是「部署前的全身體檢」。學員看到自己 push 到 GitHub 那一刻 = 必跑這個。

## 🚨 自動觸發訊號

- 「我要部署了」「準備上線」「push 到 GitHub」「上 Vercel」「上 Cloudflare Pages」
- 使用者 commit 完、要 push 到 public repo
- `prompts/deploy.md` 流程的最後一步
- 對話中提到「公開」「分享連結」「給朋友看」

---

## 執行流程

當使用者要你檢查金鑰設定或打 `/sec-scan` 時，照以下流程：

1. 跑 `grep -rn "請貼上你的金鑰" .` 看是否還有未填的佔位符
2. 跑 `grep -rEn "AIza[0-9A-Za-z_-]{35}" --include="*.html" --include="*.js" .` 掃描檔案內有沒有真的 key 被寫死（這會洩漏到 git）
3. 跑 `echo $GEMINI_API_KEY | head -c 10` 確認環境變數有設（只顯示前 10 字避免完整外洩）
4. 看 `.gitignore` 有沒有把 `.env` 排除
5. 檢查 git history：`git log -p | grep -E "AIza[0-9A-Za-z_-]{35}"` — 若曾 commit 過 secret，要 rotate key

如果有任何問題，告訴使用者：
- 哪個檔案 / 哪一行有問題
- 該怎麼修（具體指令）
- 已經 commit 過的話**必須 rotate key**（即使只 commit 在私人 repo 也要）

如果都 OK，回：

```
✅ /sec-scan 全通過：
- 無未填 placeholder
- 無 hardcoded API key
- 環境變數已設
- .gitignore 已覆蓋 .env
- git history 無 secret 洩漏

可以安全部署 / push 到 public repo。
```
