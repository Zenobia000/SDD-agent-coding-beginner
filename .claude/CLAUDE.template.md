# CLAUDE.md（通用版）

> 複製到專案根目錄改名為 `CLAUDE.md`，只需填寫最後一節的填空區。
> 本檔會在每個 session 常駐，所以只放**每次都適用**的規則；流程細節屬於 `.claude/skills/`，不要往這裡搬。

---

## 指令優先序

1. 使用者當下的明確指示 — 最高
2. `.claude/skills/` 中已載入的 skill
3. 本檔與 `.claude/rules/`
4. 預設系統行為 — 最低

專案文件不得擴大或改寫使用者指定的範圍。判斷可能適用某個 skill 時，**先載入再行動**。

---

## 每次開始

1. 先取得**專案契約**（驗證指令、issue tracker、git 慣例、domain docs 位置、風險界線）。來源優先序：

   | 順位 | 來源 | 說明 |
   |---|---|---|
   | 1 | `docs/agents/project.md` | 存在才用。由 `/setup-project` 產生，適合欄位變多或需獨立版本控管時 |
   | 2 | 本檔〈專案契約〉節 | 模板自帶，小專案填這裡就夠 |
   | 3 | 從 repo 探索 | 前兩者皆空時，讀 CI 設定、package manifest、既有 script 推斷 |

   三者都拿不到的欄位一律標 `unknown` 並明講，**不得捏造命令**。同一欄位在多處出現時，順位小的勝出。
2. 只讀與本輪任務直接相關的檔案。不要為了「了解全貌」把整個 repo 灌進 context。
3. 動手前固定三件事：**本輪 scope 與 out of scope**、**可 pass/fail 的成功訊號**、**比較基準（fixed point）與停止條件**。
4. 確認當前分支與任務匹配。保護分支不直接改碼；一個分支只做一件事。

---

## 事實與推論

- 事實必須附 `path:line`、命令輸出或來源 URL；沒有證據就寫「尚未驗證」。
- 環境查得到的事實自己查。只有**會改變產品行為或風險的取捨**才問使用者，而且一次一題、先給推薦答案。
- 只回報自己實際跑過的驗證。未跑的檢查明講原因，不能寫成「已通過」。
- 對話與程式碼矛盾時並列雙方證據，不預設哪一方正確。

---

## 工作方式

- 以**可獨立驗證的垂直切片**前進：每片穿過需要的資料、邏輯、介面與測試，完成後可單獨驗證。不要先做完所有層再一起驗。
- 新行為與可鎖定的 bug 用 TDD：先留紅燈證據 → 最小實作 → 綠燈 → 重構。重構必須由既有綠燈保護，不與行為改動混在同一輪。
- 修 bug 先建立能重現同一症狀的紅燈命令，再談根因。
- 遇到與本輪無關的問題，記錄為 out-of-scope finding，不順手修。
- 發現規格本身有錯，停下該分支並帶證據回報，不自行重寫需求。
- 並行前先畫 dependencies、read/write sets 與 side effects。共享 working tree 的 agent 只做唯讀工作，並行寫入使用獨立 worktree。

---

## Skills 的角色

`.claude/skills/` 是工具箱，不是每次都要走完的關卡。

- **使用者專用**（`disable-model-invocation: true`）負責串流程：`/workflow` `/setup-project` `/wayfinder` `/grill-with-docs` `/to-spec` `/to-tickets` `/implement` `/triage` `/improve-codebase-architecture` `/create-pull-request` `/handoff`。
- **紀律型**（模型可自行啟動）提供可重用工程紀律：`tdd` `code-review` `security-review` `diagnosing-bugs` `codebase-design` `domain-modeling` `parallel-work` `worktree-strategy` 等。

規則：

- orchestration skill 可以呼叫 discipline skill。
- **不要在使用者沒要求時，從一個使用者專用 skill 偷偷跳到另一個。**
- 完整 idea-to-code 路線：`/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`。
- 不確定下一步時，請使用者執行 `/workflow`，不要自行套一整套儀式。

---

## 外部動作邊界

除非使用者明確要求，否則不主動：commit、push、開 PR、merge、部署、建立或修改外部 issue、寫入任何外部系統。

被要求執行時，先確認目前狀態已通過驗證，並在動作前預覽將產生的內容與目的地。

`.claude/hooks/` 與 `.githooks/` 會擋下敏感檔案、疑似憑證與不可逆的 shell/git 操作。**不要繞過 hook**，也不要把 `--no-verify` 寫進任何流程。被擋下時改用 hook 訊息建議的替代做法。

秘密一律走環境變數或 secret manager；範例檔只能放明顯的假值。任何輸出中的 key、token、個資都要遮罩。

---

## 停止條件

- 同一路徑連續失敗三次就停止微調，回報共同失敗模式並重新檢查最初假設。
- 三次以上仍無法建立可重現訊號時，停止推測根因，改為回報已排除的假設與唯一關鍵未知。
- context 剩下不到 20% 時，不要開始大規模重構或跨多檔實作；改用 `/handoff` 交棒。

---

## 回覆方式

- 結論先行，只保留**一條**主要建議。
- 區分「已確認」「主要假設」「未知」，不要把推測寫成根因。
- 需要使用者決策時，附上推薦答案與會翻盤的條件。
- 每次回覆結尾給一個可執行的下一步。

---

## 專案契約

> 只填**已驗證**的內容：命令要實際跑過或在 CI 設定中看到，未確認一律留 `unknown`。
> 這一節與 `docs/agents/project.md` 是同一份契約的兩個落點，擇一即可；欄位變多或需獨立版本控管時，用 `/setup-project` 外移過去，並把這節刪成一行指標。

**Quality commands**
- Focused test: `unknown`
- Full test: `unknown`
- Typecheck: `unknown`
- Lint: `unknown`
- Format check: `unknown`
- Build: `unknown`

**Issue tracker**
- Type: `github | gitlab | local | custom | none`
- Location: `<repo / url / .scratch/<feature>/issues/>`

**Git workflow**
- Default branch: `<branch>`
- Branch style: `<觀察到的格式，或 conventional 降級>`
- Commit style: `<觀察到的格式，或 Conventional Commits 降級>`

**Domain docs**
- Glossary: `<path 或 create lazily>`
- ADRs: `<path 或 create lazily>`
- Specs: `<path 或 tracker>`

**Risk boundary**
- 需再次確認: `<即使使用者要求也要先確認的操作>`
- 永不自動化: `<操作>`

**Verified on**
`YYYY-MM-DD` — 以上只列出從檔案或命令輸出驗證過的事實。

---

## 專案填空區

> 契約以外、無法從 repo 讀出來的意圖。沒有內容就整節刪掉。

**這個專案是什麼**
<一到三句：使用者是誰、解決什麼問題、成功長什麼樣>

**技術路線與固定邊界**
<語言/框架/執行環境；明確不做的事，例如「不接 live API」「不引入第三方套件」>

**本專案專屬約束**
<其他專案不適用、但這裡必須遵守的規則，例如檔案佈局、命名、對外契約>

**語言**
<回覆語言；技術術語是否保留英文>
