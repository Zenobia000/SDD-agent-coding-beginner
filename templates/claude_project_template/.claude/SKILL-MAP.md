# SKILL-MAP — 這些積木怎麼接

> 本檔是 skill 之間**連動關係**的單一真相源。
> 各 skill 自己怎麼跑，看各自的 `SKILL.md`，本檔不重述。

---

## 一、全部積木一覽

**核心六塊**（幾乎每個專案都會用到）：

| Skill | 一句話 | 拍 |
|---|---|---|
| `/loop` | 跑一輪四拍，改到好為止 | 全程 |
| `/decide` | 給我一個建議，不要給我選項清單 | 全程 |
| `/spec-it` | 一句話需求 → 七欄位 spec | ① |
| `/eval-set` | 「做對了」變成可執行的考卷 | ① |
| `/tdd-cycle` | 紅 → 綠 → 重構 | ② |
| `/verify` | commit 前五維度驗證 | ③ |

**選用十塊**（該專案需要時再啟用）：

| Skill | 什麼時候啟用 | 拍 |
|---|---|---|
| `/adr` | 有 2 個以上合理選項在競爭 | ① |
| `/plan-sprint` | 有 PRD 但不知道先做哪個 | ② |
| `/data-pipe` | 要存資料 / 搬資料 | ② |
| `/ui-spec` | 要做介面 | ② |
| `/sync-it` | 有獨立文件，且 code 改了 | ③ |
| `/commit-msg` | 要 commit 了 | ④ |
| `/sec-scan` | 準備部署 / 開 public repo | ④ |
| `/ops-card` | 準備部署 / 要交接 | ④ |
| `/retro` | 這一輪跑完了 | ④ |
| `/explain-code` | 看不懂 AI 寫了什麼 | 任意 |

**四個 command**（薄編排層，不是 skill）：

| Command | 做什麼 |
|---|---|
| `/kickoff` | 問五題 → 產決策卡（S1 入口） |
| `/gate` | 對照二元判準，判斷能不能往前 |
| `/blocks` | 列積木 + 建議下一塊裝什麼 |
| `/ship` | 串起 verify → sec-scan → 考卷 → ops-card → 部署 |

> **skill 和 command 的差別**：兩者都產生 `/<name>`。
> skill 是目錄、可帶附件、可被 AI 自動載入；command 是單檔、通常由你主動打。
> 完整判斷見 [`docs/authoring/07-choose-which.md`](../../../docs/authoring/07-choose-which.md)。

---

## 二、Pre / Post 條件

跑某個 skill 之前該有什麼、跑完之後接什麼。

| Skill | 之前要有 | 之後接 |
|---|---|---|
| `/kickoff` | 一句話痛點 | `/spec-it` |
| `/spec-it` | 決策卡（或至少一句話需求） | `/eval-set` → `/adr`（如需要） |
| `/adr` | 2 個以上選項 + 比較依據 | `/plan-sprint` |
| `/eval-set` | PRD 的 Success criteria | `/plan-sprint` 或 `/tdd-cycle` |
| `/plan-sprint` | PRD + AC | `/tdd-cycle` |
| `/tdd-cycle` | 一個明確的 task + AC | `/verify` |
| `/data-pipe` | 知道資料從哪來、誰是真相源 | `/tdd-cycle`（實作驗證） |
| `/ui-spec` | 知道資料契約 | `/tdd-cycle` |
| `/verify` | 有測試、有 lint 設定 | `/sync-it` |
| `/sync-it` | `/verify` 綠燈 | `/commit-msg` |
| `/commit-msg` | staged changes + `/verify` 綠 | 下一個 `/tdd-cycle` 或 `/ship` |
| `/sec-scan` | 功能完成、準備部署 | `/ops-card` |
| `/ops-card` | `/sec-scan` 無阻擋項 | `/ship` |
| `/retro` | 這一輪的 task 都完成 | `/kickoff`（下一輪） |
| `/loop` | **三條限制都填得出來** | 依對象而定 |
| `/decide` | 一個具體問題 | 依決策結果而定 |

---

## 三、五條典型路徑

### A. 完整新專案（一天）
```
/kickoff → /spec-it → /adr → /eval-set → /plan-sprint
  → /tdd-cycle ×N → /verify → /sync-it → /commit-msg
  → /sec-scan → /ops-card → /ship → /retro
```

### B. 修一個 bug（30 分）
```
/tdd-cycle（先寫重現測試）→ /verify → /commit-msg
```
不要跑 `/spec-it`——bug 是「既有 spec 沒被滿足」，不是新需求。

### C. 品質不夠，要改到好
```
/eval-set（沒考卷先建）→ /loop → 分數夠了 → /verify
```
**這條是循環工程的主場。** 其他路徑是「做出來」，這條是「做好」。

### D. 卡住了
```
/explain-code（看不懂 code）
  或
/decide（不知道選哪個 / 找不到根因）
  或
派 explorer subagent（找不到東西在哪）
```

### E. 接手別人的專案
```
派 explorer（摸清結構）→ /spec-it（補 PRD）
  → 派 test-writer（補測試）→ /adr（補關鍵決策）
```

---

## 四、什麼時候派 subagent 而不是跑 skill

| 情境 | 用 skill | 派 subagent |
|---|---|---|
| 要理解一段 code | `/explain-code` | — |
| 要在大 repo 裡找東西 | — | `explorer` |
| 要為新功能寫測試 | `/tdd-cycle` | — |
| 要為既有 code 補一批測試 | — | `test-writer` |
| 例行的品質檢查 | `/verify` | — |
| 重要決策要第二意見 | — | `reviewer` |
| 例行的資安掃描 | `/sec-scan` | — |
| 碰到認證 / 金流 / 上傳 | `/sec-scan` 後 | 再派 `security-auditor` 覆核 |

**判斷原則**：
- 會產生大量中間資訊、但你只要結論 → **subagent**
- 需要獨立視角、不能被你的意圖污染 → **subagent**
- 是一套你要跟著走的流程 → **skill**

---

## 五、常見斷層（照這個表除錯）

| 症狀 | 斷在哪 | 修法 |
|---|---|---|
| AI 一直改，但不知道有沒有變好 | 缺 `/eval-set` | 先建考卷再繼續 |
| 寫完 code 才發現不是要的 | 跳過 `/spec-it` | 回去補 spec，不要繼續改 |
| 文件說的和 code 做的不一樣 | 缺 `/sync-it` | 每次 commit 前跑 |
| 部署後才發現 key 外洩 | `/sec-scan` 沒掃歷史 | 立刻輪換 key，再清歷史 |
| 半夜掛了不知道怎麼救 | 缺 `/ops-card` | 補維運卡，且要演練回滾 |
| 同樣的錯誤犯第三次 | 缺 `/retro` | 每輪結束跑，且要有 action item |
| AI 建議一堆 skill 很煩 | — | 說「不要建議任何 skill，我自己來」 |

---

## 六、不必全用

**Solo dev 的最小集是三個**：`/spec-it` + `/tdd-cycle` + `/commit-msg`。

刪掉用不到的 skill 是**正確做法**，不是偷懶：
```bash
rm -rf .claude/skills/retro       # 個人小工具不需要回顧
rm -rf .claude/skills/adr         # 沒有架構選擇要記錄
rm -rf .claude/skills/ui-spec     # 純 CLI 工具沒有介面
```

**留著沒在用的 skill，會讓 AI 在錯的時機建議它們。**
