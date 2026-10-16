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

## 兩個 repo，各做一件事

| repo | 是什麼 | 誰用 |
|---|---|---|
| [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp) | **上課用的專案**：LeaveBot 骨架、題目、規格模板，只帶上課用的 6 個技能與護欄 | 學員，clone 下來直接寫 |
| 這個 repo | **課程首頁與講義原稿**：`curriculum/` 的 4 天實戰營、開場投影片，加上完整工具鏈（38 個技能）與檢查腳本 | 講師與維護者；結訓後想要完整工具鏈的人 |

講義用 `bash scripts/export-handout.sh` 打包成 zip，放 OneDrive 發給學員。原稿留在這裡，才有版本紀錄與連結檢查。

**學員**：照 [`curriculum/0-setup/`](./curriculum/0-setup/) 裝好環境、clone 上課 repo，下一步打開你報名的課表：[4 天實戰營](./curriculum/1-bootcamp/)或 [2 天工作坊](./curriculum/1-workshop/)。

---

## 這個 repo 裡有什麼

```text
README.md        ← 你在這裡
curriculum/      ← 講義原稿：從這裡開始
scripts/         ← 檢查腳本、講義打包
AGENTS.md  CLAUDE.md  LICENSE  THIRD-PARTY-NOTICES.md
.claude/  .codex/  .githooks/   ← 護欄（guard hooks）與 Git 設定，在背景運作
```

`curriculum/` 裡面照編號往下走：

| 位置 | 給誰 | 什麼時候打開 |
|---|---|---|
| [`0-setup/`](./curriculum/0-setup/) | 所有人 | **開課前一週**：環境檢核表 |
| [`1-bootcamp/`](./curriculum/1-bootcamp/) | 4 天班 | 上課期間：4 天課表、自主期任務 |
| [`1-workshop/`](./curriculum/1-workshop/) | 2 天班 | 上課期間：2 天課表，內容連回 4 天版的單元 |
| [`3-playbook/`](./curriculum/3-playbook/) | 所有人 | 隨時查：Prompt 魔法書、問題排解、防呆檢核表 |
| [`4-casebook/`](./curriculum/4-casebook/) | 所有人 | 結訓後：報價、請款、庫存等七個企業系統的 AI 開發思考 |
| [`advanced/cookcard/`](./curriculum/advanced/cookcard/) | 想挑戰完整系統的人 | 結訓後的進階選修：把料理影片轉成食譜卡，多模態加部署 |
| [`slides/`](./curriculum/slides/) | 講師 | 開場投影片與視覺規範（莫蘭迪色票、黏土貓） |
| [`instructor/`](./curriculum/instructor/) | 講師 | 學員不用看，也不會打包進講義 |

規格模板、題目 `LEAVEBOT.md` 與程式骨架在上課 repo [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)，因為 agent 要在專案裡用 `@` 讀得到它們。


---

## 工具箱在模板 repo

38 個工程技能、agent 護欄、Git 安全閘門都在模板 repo [`agent-skills-starter`](https://github.com/Zenobia000/agent-skills-starter)：按 **Use this template** 就能開一個 Claude Code 與 Codex 都能用的新專案。上課 repo 只帶其中 6 個。

- 技能衍生自 [luca-skills](https://github.com/Luca0x5755/luca-skills)（MIT）。這個 repo 留著的 guard hooks 也是，聲明見 [`THIRD-PARTY-NOTICES.md`](./THIRD-PARTY-NOTICES.md)。
- ⚠️ 只支援 Claude Code 與 Codex。Copilot、Antigravity 不認「使用者觸發」設定，編排型技能會被 agent 自己啟動。

---

MIT License。
