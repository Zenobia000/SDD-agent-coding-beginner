# AI 時代的系統定義方法論

> 這套文件回答兩個問題：**系統定義從何開始？** 以及 **AI 時代如何治理這個過程？**
>
> 它把「2020 年前沒有 AI 時，產品如何在文件不完整下啟動」的工程經驗，
> 與「AI 時代的 Human Gate + AI Factory 治理模型」整理在一起，
> 作為本 repo Vibe Engineering 方法論的脈絡補充。

---

## 它在整個 repo 的位置

| 層級 | 文件 | 角色 |
|------|------|------|
| 為什麼 | 本文件集 | 系統定義的歷史脈絡與 AI 治理原則 |
| 怎麼做（完整版） | [`../../labs/reference-project/`](../../labs/reference-project/) | 8 階段從痛點到可運行 App |
| 怎麼做（快速版） | [`../../curriculum/S3-prototype.md`](../../curriculum/S3-prototype.md) | 填空式 MVP 模板 |
| 自動化執行 | [`../../.claude/`](../../.claude/) | Agent 規則與 skills |

本文件講「原則與脈絡」，Runbook 講「實際操作」。讀本文件理解**為什麼**，讀 Runbook 知道**怎麼做**。

---

## 兩條閱讀路線

- **想懂脈絡** → 讀 `articles/`，從 01 依序到 06。
- **想直接套流程** → 讀 `process/`，每篇都是可直接執行的 SOP 或模板。

---

## 全文件地圖

### articles/ — 經驗分享

| # | 文件 | 一句話 |
|---|------|--------|
| 01 | [沒有 AI 的年代，系統定義如何開始](articles/01-pre-ai-how-systems-began.md) | 不是完整 top-down，而是最小共識加邊做邊補 |
| 02 | [為什麼一張架構圖就開工](articles/02-why-a-single-diagram-ships.md) | 需求不完整、時程壓力、文件易過期這三個壓力 |
| 03 | [逐層收斂取代完整 top-down](articles/03-converge-not-topdown.md) | 四種起手式與各自的適用場景 |
| 04 | [不完整不可怕，沒治理才可怕](articles/04-incompleteness-vs-governance.md) | 開發節奏 Phase 0–6 與治理機制 |
| 05 | [四級系統與最小可行文件集](articles/05-four-tiers-and-mvd.md) | POC / MVP / Product / Enterprise 與 MVD |
| 06 | [AI 時代：Human Gate + AI Factory](articles/06-ai-era-human-gate-ai-factory.md) | AI 是工廠，人類是 Gate |

### process/ — 開發流程與模板

| # | 文件 | 一句話 |
|---|------|--------|
| 01 | [最小可行文件集 SOP](process/01-minimum-viable-documentation.md) | 7 份文件清單，扣三層 Spec |
| 02 | [AI 協作五輪工作流](process/02-ai-collaboration-sop.md) | 發散→收斂→結構化→Gate→開發資產 |
| 03 | [結構化產出模板與可追溯性](process/03-schemas-and-traceability.md) | 需求 Schema、ADR、Traceability Matrix |
| 04 | [Human Gate 與 AI Agent 角色](process/04-human-gate-and-agent-roles.md) | 六道 Gate、Agent 分工、Review Queue |

---

## 一句話總結

> 大型系統主流程仍走傳統工程治理：需求、邊界、架構、資料、介面、測試、維運。
> AI 放在每一階段的發散、補洞、產生候選、檢查一致性與生成重複資產。
> 人類不再手寫所有文件，而是設計 Gate、Schema、Review Queue，把 AI 產出收斂成正式決策。
