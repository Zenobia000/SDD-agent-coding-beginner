# Git 安全閘門

`.claude/hooks/` 保護 Claude 的工具呼叫；這裡的 Git hooks 同時保護人與任何 agent 的 Git 操作。

| Hook | 阻擋 |
|---|---|
| `pre-commit` | 真實 `.env` 與疑似硬編碼 API key |
| `pre-push` | 對 `main`、`master` 的非快轉 push |

每個 clone 啟用一次：

```bash
git config core.hooksPath .githooks
chmod +x .githooks/*
```

Hook 是不可逆風險的最低保護，不取代 tests、review 或使用者授權。不要把 `--no-verify` 寫進自動化流程。
