# 領域文件

## 配置

單一 context。根目錄一份 `CONTEXT.md`，ADR 放 `docs/adr/`。
無 monorepo 訊號，不需要 `CONTEXT-MAP.md`。

## 協作模式

`shared` —— 技能寫出的所有東西都進版控。

理由：實質單人 repo，且為公開教材。學生 fork 之後要看得到
`CONTEXT.md` 與 ADR 長什麼樣子，藏起來等於拿掉一半教學價值。
不排除任何路徑，`.git/info/exclude` 不動。

## 註解語言

繁體中文。

理由：repo 現有註解一致是繁中（`scripts/*.sh`、`.githooks/pre-commit`）。
`.claude/skills/*/hooks/*.sh` 的英文註解是 luca-skills 上游遺留，
不代表本 repo 慣例。

這一條是團隊事實，不是工具設定 —— 註解跟著程式碼出貨，所以它同時
寫在 `CLAUDE.md` 的 `## Agent skills` 區塊（shared 模式，該檔進版控）。
