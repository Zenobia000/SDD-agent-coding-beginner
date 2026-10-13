# 規格驅動 × AI 開發：用 Claude Code / Codex 把需求做成系統

> **第一次來？只讀這一頁。** 讀完你會知道自己該不該上、要先裝什麼、下一份該打開哪個檔案。
> 其他資料夾你現在都不用管。

---

## 這是什麼

一套用 AI coding agent（Claude Code 或 Codex）開發軟體的訓練營教材。流程從商業需求開始，經過規格、架構、測試，最後到上線。

目標不是學會「叫 AI 寫程式」，而是學會**讓 AI 寫出你能驗收的東西**。

- 人負責收斂與決策
- AI 負責發散與生成

---

## 適合誰

不限職位。只要你**在企業裡走過流程**，或者**看得懂一張流程圖在說什麼**，就跟得上。

| 你是 | 這門課給你什麼 | 需要寫程式嗎 |
|---|---|---|
| PM、SA、主管 | 把模糊需求寫成 AI 讀得懂、人驗得了的規格，並審查 AI 的產出 | 不用 |
| 初學工程師 | 用 agent 把規格做成能跑、有測試的系統 | 會一點就好 |
| QA | 從驗收條件展開測試案例，判斷 AI 窮舉的邊界值哪些有意義 | 不用 |

上課時混班分組，每組都有寫規格的人和寫程式的人。真實專案就是這樣分工。

**不適合**：只想學某個工具的快捷鍵，或想拿一份可以直接上線的程式碼。

---

## 第一次來，照這三步

**1. 裝好工具**

你需要 Git，以及 Claude Code 或 Codex 其中一個。

**2. 把專案拿下來**

```bash
git clone https://github.com/<你的帳號>/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner
git switch progressive-sdd
git config core.hooksPath .githooks
claude
```

**3. 確認工具箱載得到**

在 Claude Code 裡打 `/compass`，看得到技能清單就成功了。

---

## 這個 repo 裡有什麼

依你會用到的順序排列。**新手只需要看前兩列。**

| 位置 | 給誰 | 什麼時候打開 |
|---|---|---|
| `README.md`（這一頁） | 所有人 | 現在 |
| [`advanced/cookcard/`](./advanced/cookcard/) | 想挑戰完整系統的人 | 進階選修：把料理影片轉成食譜卡，多模態加部署 |
| [`docs/SKILL-MAP.md`](./docs/SKILL-MAP.md) | 開始用技能之後 | 查哪一步該用哪個 `/指令` |
| [`instructor/`](./instructor/) | 講師 | 學員不用看 |
| `.claude/`、`scripts/`、`.githooks/` | 工具鏈 | **不用管**，它們在背景運作 |

4 天訓練營主線（請假系統題目、規格模板、Starter 專案、Prompt 魔法書）正在建置中，完成後會依閱讀順序放在 `0-setup/` 到 `5-casebook/`。

---

## 工具箱

[`.claude/skills/`](./.claude/skills/) 裡有 36 個工程技能，打 `/` 加名稱就能叫出來，例如 `/grilling`、`/to-spec`、`/tdd`。

- 衍生自 [luca-skills](https://github.com/Luca0x5755/luca-skills)（MIT），聲明見 [`THIRD-PARTY-NOTICES.md`](./THIRD-PARTY-NOTICES.md)。
- ⚠️ 技能是為 Claude Code 寫的。Codex、Copilot、Antigravity 對技能的支援程度不同，落差寫在 [`docs/SKILL-MAP.md`](./docs/SKILL-MAP.md)。

---

MIT License。
