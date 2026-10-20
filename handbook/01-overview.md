# 規格驅動 × AI 開發實戰營（2 天｜14 小時）

> **D1 寫規格，D2 從 0 做出 app。** 以 Claude Code / Codex 為核心，用 SDD agentic coding 走完一條 V-model：
> 左邊六份規格文件，右邊一個能跑的全端加 AI 應用，中間用編號一路串起來。

---

## 適合誰

**不限職位。** 在企業裡走過流程，或者看得懂一張流程圖的人，都跟得上。

| 你是 | 你會帶走什麼 |
|---|---|
| **主管** | 判斷團隊導入 AI 開發的成熟度，知道哪些環節不能交給 AI |
| **PM / SA** | 寫出 AI 讀得懂、人驗得了的六份規格；不寫程式也能審查 AI 的產出 |
| **QA** | 寫測試計畫，讓 AI 窮舉邊界、由你判斷哪些有意義，並訂出 AI 的上線門檻 |
| **初學工程師** | 用 agent 依規格一個疊代一個疊代做出 app，每一步都有測試接住 |

**課前要會的**：用過任何一種 AI 聊天工具；能照著說明在終端機打指令。
**不用會的**：寫程式。

---

## 核心觀念

**人收斂，AI 發散。** AI 生成草稿、窮舉情境、寫程式；人決定要做什麼、不做什麼、什麼叫做完。

**SDD agentic coding vs vibe coding**：兩者都讓 AI 寫程式。差別是我們的 AI 每一步都有規格可以對、有測試可以擋，做完了說得出「哪條需求被哪個測試驗過」。

**V-model**：D1 寫左邊，D2 寫右邊，每一層規格都有一層測試接住。對照表在上課 repo 的 [`TRACEABILITY.md`](https://github.com/Zenobia000/leavebot-bootcamp/blob/main/templates/TRACEABILITY.md)。

---

## 課表

每天 09:00–17:30，扣掉 1 小時午休與兩次 15 分鐘休息，淨 7 小時。

| | 主題 | 產出 |
|---|---|---|
| [**D1**](./02-day1.md) | 規格：V 的左邊，加上右邊的計畫 | `docs/01-brief.md` … `docs/06-test-plan.md`、`AGENTS.md`、I0–I4 疊代票 |
| [**D2**](./03-day2.md) | 從 0 到 1：V 的右邊 | 全端 app、標了需求的測試、eval 準確率、追溯報告 |

**D1**

| 時長 | 單元 | 技能 |
|---|---|---|
| 0.75h | 1. Harness 解剖與典範轉移 | `/compass` |
| 0.5h | 2. Project Brief | `/grilling` |
| 1.5h | 3. PRD：persona、user flow、epic、story、BDD | `/grilling` |
| 1h | 4. SRS：use case、FR、NFR | — |
| 1h | 5. SAD：C4、資訊流、技術選型 | `/to-architecture` |
| 1h | 6. SDS：ER、API、畫面、模組 | `/to-architecture` |
| 0.75h | 7. Test Plan：AI 窮舉、人篩選、訂門檻 | — |
| 0.5h | 8. 專案大腦與疊代拆票 | `/to-tickets` |

**D2**

| 時長 | 疊代 | 技能 |
|---|---|---|
| 0.75h | I0 骨架：依 `STACK.md` 生成前後端 | — |
| 1.5h | I1 第一條垂直切片 | `/tdd` |
| 1.25h | I2 規則與破壞測試 | `/tdd` |
| 1h | I3 主管核准與交換審查 | `/code-review` |
| 1h | I4 驗收 AI 本身：eval 與 prompt injection | — |
| 1h | 追溯報告、落地 SOP、成果發表 | — |

I1、I2 各含 15 分鐘緩衝（09:00–17:15，最後 15 分鐘問答）。**每個疊代結束都有講師檢查點**；落後的組，講師會給上一個疊代的保底版本讓你們接著做。

---

## 分組

每組 3–4 人，**角色混搭**：至少一位寫規格的（PM / SA / 主管 / QA）、一位寫程式的（工程師）。

| 軌 | D1 | D2 |
|---|---|---|
| 📋 **規格軌** | 主寫 Brief、PRD、SRS、Test Plan | 守住規格：親手跑驗收、判斷 AI 有沒有誤解、記錄誤解 |
| 🛠️ **工程軌** | 主寫 SAD、SDS，審 PRD 寫不寫得出來 | 驅動 agent 一個疊代一個疊代做 |

兩軌在同一個 repo 裡工作。規格軌寫的文件，就是工程軌餵給 agent 的輸入 —— 寫得不清楚，D2 當場就會卡住，這是故意的。

---

## 題目與上課 repo

**LeaveBot —— 一句話請假。** 題目、公司規章與這兩天的 MVP 範圍，見上課 repo 的 [`LEAVEBOT.md`](https://github.com/Zenobia000/leavebot-bootcamp/blob/main/LEAVEBOT.md)。**課前讀完。**

上課 repo [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp) 裡有：六份文件模板與另一個題目的完整範例、固定的技術棧（`STACK.md`）、LLM 工具包、追溯檢查與 eval 工具。**沒有 app 程式碼** —— 那是 D2 你們自己生出來的。

---

## 每個單元的固定格式

| 段落 | 是什麼 |
|---|---|
| **為什麼** | 這個單元要解決的問題 |
| **重點** | 講師會講的觀念 |
| **實作** | 規格軌、工程軌各做什麼 |
| **可以這樣問 AI** | 參考提示詞。先改成你的版本再用，原封不動貼上的效果通常最差 |
| **通過訊號** | 你自己能檢查的東西，做到了才算完成這個單元 |

---

## 課後帶走的東西

| 資產 | 位置 |
|---|---|
| 六份規格模板、追溯規則、`AGENTS.md` 範本、TDD hook | 上課 repo 的 [`templates/`](https://github.com/Zenobia000/leavebot-bootcamp/tree/main/templates) |
| 追溯檢查 `trace.py`、eval 工具 `run_eval.py` | 上課 repo 的 [`scripts/`](https://github.com/Zenobia000/leavebot-bootcamp/tree/main/scripts) |
| Prompt 魔法書、問題排解檢索表 | 本講義的[附錄](./appendix/) |
| 防呆檢核表、導入評估表 | [企業啟動包](../starter-kit/README.md) |
| 完整工具鏈（38 個技能） | 模板 repo [`agent-skills-starter`](https://github.com/Zenobia000/agent-skills-starter) |
| 企業常見系統的 AI 開發白皮書 | [企業啟動包](../starter-kit/README.md) |

**課後延伸**：回公司挑一個**小**專案，從模板 repo 開一個新 repo，照 D1 的六份文件走一次。第一次不用寫滿，但 `trace.py` 要跑得出矩陣。
