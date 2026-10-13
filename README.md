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

在 Claude Code 裡打 `/compass`（Codex 打 `$compass`），看得到技能清單就成功了。

詳細步驟與卡關排解見 [`curriculum/0-setup/`](./curriculum/0-setup/)。下一步打開 [`curriculum/1-bootcamp/`](./curriculum/1-bootcamp/)。

---

## 這個 repo 裡有什麼

**課程的東西全部在 [`curriculum/`](./curriculum/)。** 其他都是工具鏈，不用管。

```text
README.md        ← 你在這裡
curriculum/      ← 課程：從這裡開始
docs/            ← 技能速查表（開始用 /指令 之後才需要）
scripts/         ← 檢查腳本（維護者用）
AGENTS.md  CLAUDE.md  LICENSE  THIRD-PARTY-NOTICES.md
.claude/  .agents/  .githooks/   ← agent 與 Git 的設定，在背景運作
```

`curriculum/` 裡面照編號往下走：

| 位置 | 給誰 | 什麼時候打開 |
|---|---|---|
| [`0-setup/`](./curriculum/0-setup/) | 所有人 | **開課前一週**：環境檢核表 |
| [`1-bootcamp/`](./curriculum/1-bootcamp/) | 所有人 | 上課期間：4 天課表、題目、自主期任務 |
| [`2-templates/`](./curriculum/2-templates/) | 所有人 | 寫規格、寫專案規則時：填空模板 |
| [`3-playbook/`](./curriculum/3-playbook/) | 所有人 | 隨時查：Prompt 魔法書、問題排解、防呆檢核表 |
| [`4-starter/`](./curriculum/4-starter/) | 工程軌 | 自主期開始時：複製一份當你們的專案起點 |
| [`5-casebook/`](./curriculum/5-casebook/) | 所有人 | 結訓後：報價、請款、庫存等七個企業系統的 AI 開發思考 |
| [`advanced/cookcard/`](./curriculum/advanced/cookcard/) | 想挑戰完整系統的人 | 結訓後的進階選修：把料理影片轉成食譜卡，多模態加部署 |
| [`instructor/`](./curriculum/instructor/) | 講師 | 學員不用看 |

---|---|---|
| `README.md`（這一頁） | 所有人 | 現在 |
| [`curriculum/0-setup/`](./curriculum/0-setup/) | 所有人 | **開課前一週**：環境檢核表 |
| [`curriculum/1-bootcamp/`](./curriculum/1-bootcamp/) | 所有人 | 上課期間：4 天課表、題目、自主期任務 |
| [`curriculum/2-templates/`](./curriculum/2-templates/) | 所有人 | 寫規格、寫專案規則時：填空模板 |
| [`curriculum/3-playbook/`](./curriculum/3-playbook/) | 所有人 | 隨時查：Prompt 魔法書、問題排解、防呆檢核表 |
| [`curriculum/4-starter/`](./curriculum/4-starter/) | 工程軌 | 自主期開始時：複製一份當你們的專案起點 |
| [`curriculum/5-casebook/`](./curriculum/5-casebook/) | 所有人 | 結訓後：報價、請款、庫存等七個企業系統的 AI 開發思考 |
| [`curriculum/advanced/cookcard/`](./curriculum/advanced/cookcard/) | 想挑戰完整系統的人 | 結訓後的進階選修：把料理影片轉成食譜卡，多模態加部署 |
| [`docs/SKILL-MAP.md`](./docs/SKILL-MAP.md) | 開始用技能之後 | 查哪一步該用哪個 `/指令` |
| [`curriculum/instructor/`](./curriculum/instructor/) | 講師 | 學員不用看 |
| `.claude/`、`scripts/`、`.githooks/` | 工具鏈 | **不用管**，它們在背景運作 |

---

## 工具箱

[`.claude/skills/`](.claude/skills/) 裡有 36 個工程技能，打 `/` 加名稱就能叫出來，例如 `/grilling`、`/to-spec`、`/tdd`。

- 衍生自 [luca-skills](https://github.com/Luca0x5755/luca-skills)（MIT），聲明見 [`THIRD-PARTY-NOTICES.md`](./THIRD-PARTY-NOTICES.md)。
- Claude Code 用 `/技能名`，Codex 用 `$技能名`，兩邊讀的是同一份技能。
- ⚠️ Copilot、Antigravity 對技能的支援有落差，寫在 [`docs/SKILL-MAP.md`](./docs/SKILL-MAP.md)。
- ⚠️ Windows 使用者 clone 前先跑 `git config --global core.symlinks true`（需開啟開發人員模式），否則 Codex 找不到技能。

---

MIT License。
