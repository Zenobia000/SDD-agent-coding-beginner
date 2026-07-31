# 循環工程 · Loop Engineering

> **8 小時，用 Claude Code 跑完一輪完整的軟體開發循環。**
> 不是教你怎麼跟 AI 講話，是教你怎麼蓋一個**讓 AI 收斂的迴圈**。

[**▸ 我要學**](#一我要學學員) ｜ [**▸ 我要開課**](#二我要開課講師) ｜ [**▸ 我只想拿那套-claude**](#三我只想拿那套-claude工程師)

---

## 結論卡

| | |
|---|---|
| **這是什麼** | 一份可直接開課、也可自學的 Claude Code 實務教材 |
| **教什麼** | 循環工程四拍 → 問對問題 → 定契約 → TDD → 把方法變成 `.claude/` 資產 → 全端積木 → 交付 |
| **不教什麼** | for-loop、React hooks、prompt 咒語 |
| **帶走什麼** | 一個上線的全端小應用 + 一套自己動手改過的 `.claude/` |
| **下一步** | 讀 [`START-HERE.md`](./START-HERE.md) |

---

## 這堂課在解什麼問題

你已經會用 AI 寫程式了。問題是——

```
AI 產出一大堆        →   你自己找結論
它很有自信地講錯      →   你事後才發現
每次結果都不一樣      →   你以為是自己 prompt 沒寫好
```

**真正的病因**：你在對單次輸出許願，而不是在設計一個會收斂的流程。

這堂課的答案是**循環工程四拍**：

```
① 劃邊界 Constrain  —— 一個範圍 / 一個評分 / 一個預算
② 放它跑   Run       —— AI 產候選，人不插手
③ 打分數   Score     —— 二元判準；程式能判就別問人
④ 收判斷   Decide    —— 人只做三件事：看曲線、抽查最好的、決定收工
```

8 小時內你會對六個不同對象跑同一組四拍——題目、規格、程式、資產、積木、交付。
**六次重複 = 肌肉記憶。**

---

## 一日課表（S0–S7）

| 時間 | 站 | 對什麼跑四拍 | 你會產出 |
|---|---|---|---|
| 09:00 | **S0 開機** | — | 能跑的 `claude` + 專案骨架 |
| 09:30 | **S1 問對問題** | 題目 | `decision-card.md` |
| 10:35 | **S2 定契約** | 規格 | `docs/PRD.md` + `evals/eval-set.md` |
| 11:30 | **S3 先跑通** | — | 一站式平台產出的 v0 |
| 13:00 | **S4 迴圈開工** | 程式 | v1 + 綠燈測試 |
| 14:40 | **S5 方法變資產** | 資產 | 自己改過的 hook + command |
| 15:35 | **S6 積木裝配** | 積木 | 全端 v2 |
| 16:20 | **S7 守門與交付** | 交付 | 資安報告 + 公開 URL |

**實作 61%**。完整逐分鐘流程見 [`curriculum/README.md`](./curriculum/README.md)。

> **S3 排在 S1、S2 之後不是筆誤。**
> 先把題目和契約想清楚，再丟給一站式平台換一個會動的東西——體感是獎勵，不是起點。

---

## 三個入口

### 一、我要學（學員）

```bash
git clone https://github.com/<you>/ai-vibe-coding-beginner.git
cd ai-vibe-coding-beginner

# 把骨架複製出來當你的專案
cp -r templates/claude_project_template my-first-loop
cd my-first-loop && claude
```

沒有 Claude Code 訂閱？→ [`docs/setup/02-free-routes.md`](./docs/setup/02-free-routes.md) 有三條免費路線。

**接著讀** [`START-HERE.md`](./START-HERE.md)（8 小時導航，一次只給你一件事）。

### 二、我要開課（講師）

| 你需要的 | 在哪 |
|---|---|
| 8 小時逐分鐘流程 | [`curriculum/instructor/timing.md`](./curriculum/instructor/timing.md) |
| 課前準備清單 | [`curriculum/instructor/prep.md`](./curriculum/instructor/prep.md) |
| 卡關處理 SOP | [`curriculum/instructor/stuck-sop.md`](./curriculum/instructor/stuck-sop.md) |
| 印發教具 | [`curriculum/cards/`](./curriculum/cards/) |
| 老師的完整成品 | [`labs/reference-project/`](./labs/reference-project/) |

**授權 MIT**，可商用、可改編，保留作者標示即可。

### 三、我只想拿那套 `.claude/`（工程師）

不用上課。直接拿：

```bash
cp -r templates/claude_project_template/.claude your-project/
cp templates/claude_project_template/.mcp.json.example your-project/.mcp.json
```

裡面有 16 個 skill、4 個 subagent、5 個 hook、3 個 output style、9 條 rule。
先讀 [`templates/claude_project_template/README.md`](./templates/claude_project_template/README.md) 決定要留哪些——**不必全用**。

想知道這些東西怎麼自己寫？→ [`docs/authoring/`](./docs/authoring/)

---

## 「我做對了嗎」

這是本教材最重要的機制。

每一站結束打 `/gate`，AI 會拿 [`labs/reference-project/RUBRIC.md`](./labs/reference-project/RUBRIC.md) 的二元判準比對你的產出，回你三件事：

```
通過 / 未通過
缺什麼（具體到檔名）
下一步：一個動作
```

**不給分數，只給 yes/no。** 這是把「評估驅動開發」用在教學本身。

---

## 適合誰

| 適合 | 不適合 |
|---|---|
| 用過 Claude Code / Cursor，但覺得「有時很神有時很雷」 | 想學程式語法的完全初學者 |
| 寫過小專案，知道 function / API / 測試是什麼 | 只想看 AI 寫程式表演的人 |
| 想把 AI 協作變成可重複的流程，不是碰運氣 | 期待上完課就能接案的人 |
| 團隊要導入 AI coding，需要一套可交接的規範 | 想學 LLM 訓練 / 微調的人（那是另一門） |

---

## 倉庫結構

```
.claude/                  ← repo 自身的規則（也是教材展示品）
curriculum/               ← 課程主體：S0–S7 八站 + 講師手冊 + 教具
labs/
  reference-project/      ← ⭐ 老師的完整成品 + RUBRIC.md 二元判準
  blocks/                 ← 積木：db / api / frontend / etl / auth
templates/
  claude_project_template/← ⭐ 學員複製走的骨架（完整 .claude/）
docs/
  setup/                  ← Claude Code 安裝 / 免費路線 / MCP
  authoring/              ← ⭐ hook·rule·skill·subagent·command·output-style 怎麼寫
  concepts/               ← 心法與進階讀本
  ai-era-system-design/   ← AI 時代系統定義方法論
  legacy/                 ← 退役內容存檔（STRIKE / Antigravity）
```

---

## 從舊版來的人

**v2.0 是一次主軸重寫，不是改版。**

| 舊版 | 現在 | 為什麼 |
|---|---|---|
| Antigravity（`agy`）+ AI Studio | **Claude Code** | 工具收斂到一個，把省下的時間拿去教流程 |
| 入口是 STRIKE 提示詞戰法 | **循環工程四拍** | 問對問題與架構設計比寫 prompt 值錢 |
| 只教「用」現成 skill | **加教「寫」六種資產** | 會用是使用者，會寫才是工程師 |
| `.agents/` | **`.claude/`** | 對齊 Claude Code 原生慣例 |
| 沒有完成判準 | **`/gate` + RUBRIC** | 學員終於知道自己做對沒 |

STRIKE 與 Antigravity 教案完整保留在 [`docs/legacy/`](./docs/legacy/)，不會消失。

---

## 授權與貢獻

- **MIT License**（見 [LICENSE](./LICENSE)）—— 可商用、可改編，保留作者標示
- 教學現場踩雷 → 開 issue
- 補行業客製範例 → 提 PR
- 用這份教材開了課 → 開 issue 告訴我，會列入使用案例

---

## 下一步

打開 [`START-HERE.md`](./START-HERE.md)。
