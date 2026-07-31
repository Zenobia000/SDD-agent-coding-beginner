# 循環工程

一套可以直接開工的 Claude Code 設定，加上一份帶你用它做出東西的文件。

```bash
git clone <this-repo> my-project && cd my-project
cp .mcp.json.example .mcp.json     # 用不到的整段刪掉
claude
```

**接著打開 [`BUILD.md`](./BUILD.md)**，把上面的東西一格一格貼進去。

---

## 一份文件，一個真實的題目

[`BUILD.md`](./BUILD.md) 用 **SmartTrip FX**（出國前算該換多少現金）走完整條線：
框題目 → 寫 PRD → 畫架構 → 定契約 → 建考卷 → 實作 → 交付。

裡面不是劇本，是**提問的範例**。題目、PRD、架構全部在 CLI 裡討論出來——
你貼的是問題，長出來的是你自己的答案。

**核心是第 3 步**：把系統切成「AI 判斷的部分」和「程式算的部分」。

```
AI 判斷（不可驗證 → schema + 考卷）
    排行程、標每一項是現金還是刷卡
────────── 交界處：schema + 一個 if ──────────
程式計算（可驗證 → 單元測試）
    加總 × 預備金、匯率燈號、幣別換算
```

**算術的事交給算術。** 多數人會想把整件事丟給 AI 一次做完——
那會得到一個偶爾算錯、而且錯了也不知道的系統。

老師的產出物在 [`labs/reference-project/`](./labs/reference-project/)（四份，比對結構不要抄）。

---

## 這裡沒有必經的關卡

`.claude/skills/` 有八個技能，是**參考書不是流程圖**——任何順序取用，也可以完全不用。

| Skill | 什麼時候翻它 |
|---|---|
| `frame` | 題目還很模糊 |
| `spec` | 要定介面、資料結構、或別人要接的東西 |
| `evals` | 改了幾輪還在原地，或講不出「怎樣算變好」 |
| `tdd` | 要寫新功能或修 bug |
| `review` | 要 commit / 開 PR / 重構 |
| `ship` | 要部署或交給別人維護 |
| `decide` | 卡在選擇，或找不到根因 |
| `next` | 不知道現在該做什麼 |

領域知識在 `.claude/references/`（資料層、介面、安全、維運、架構），需要時再讀。

---

## 唯一「你沒得選」的部分

四個 hook 擋的是不可逆的事：遞迴刪除、force push、`reset --hard`、
在保護分支 commit、把 secret 寫進檔案。

寫進文件的規則大約有七成順從率。不可逆的操作不能賭剩下那三成。

**其餘全部是建議。**

---

## 結構

```
BUILD.md            ⭐ 從這裡開始
.claude/            skills / references / hooks / agents / rules / output-styles
labs/
  reference-project/  老師的四份產出（判斷的產物，不是實作的產物）
  blocks/             可複製的積木：db / etl / api / auth / frontend（47 個測試）
docs/
  setup/              安裝與免費路線
  authoring/          怎麼自己寫 skill / hook / rule / subagent / command
  concepts/           心法與 M0–M9 進階讀本
curriculum/         開課用的講師手冊
tasks/              backlog / 當前工作 / 已知問題
```

---

## 想自己寫這些東西

[`docs/authoring/`](./docs/authoring/) 有六種資產的撰寫指南，
外加一份[決策樹](./docs/authoring/07-choose-which.md)：同一個需求該做成 skill、command、hook 還是 rule。

**會用是使用者，會寫才是工程師。**

---

## 沒有 Claude Code 訂閱

[`docs/setup/02-free-routes.md`](./docs/setup/02-free-routes.md) 有三條路線與各自的代價。
先用官方免費額度試，多半夠。

---

## 授權

MIT。可商用、可改編，保留作者標示即可。

**這些設定是拿來改的。** 刪掉用不到的 skill 是正確做法，不是偷懶。
