# Rule 06 — Doc as Code

> **文件與 code 漂移 = 專案腐爛的最大來源。行為變，文件先變。**

## 鐵律

1. **任何行為改變必須同步更新對應文件**（不能只改 code）
2. **每次 commit 前跑 `/sync-it` 檢查 drift**
3. **發現 drift 不能「下次再說」** — Critical drift 必須在當下 commit 修掉
4. **ADR 一旦 accepted 永遠不改** — 要推翻就寫新 ADR superseded 它
5. **文件 PR 與 code PR 一起送** — 不允許「code 先 merge、文件下週補」

## 文件 vs code 哪個對齊哪個？

| 情境 | 對齊方向 | 理由 |
|---|---|---|
| 文件描述未來計畫、code 還沒做 | code 對齊文件 | 文件是合約 |
| 文件過期、code 是當前真相 | 文件對齊 code | 真實行為優先 |
| 兩邊都對、但 ADR 規定 X | 都對齊 ADR | ADR 是上層決策 |
| 兩邊矛盾、無 ADR 可參考 | **停下，問使用者** | 不腦補 |

## 文件 ↔ code 對應表

| 文件 | 對應 code 範圍 | 行為變時 |
|---|---|---|
| `docs/PRD.md` US-XXX | 對應 feature 的入口檔案 | 同 PR 更新 AC |
| `docs/api-contract.md` §endpoint | `app/routes/*.py` | 同 PR 更新 schema |
| `docs/db-schema.md` table | `db/migrations/*.sql` + ORM model | 寫新 migration + 更新文件 |
| `tests/features/*.feature` | 對應的 unit / integration test | 一起改 |
| `adr/ADR-NNNN-*.md` | 全專案架構 | **永不改** — 寫新 ADR |
| `tasks/backlog.md` | 全專案計畫 | 完成 / 改變優先序時更新 |

## 觸發 `/sync-it` 的情境

| 使用者說 | 你該做 |
|---|---|
| 「我要 commit 了」 | 跑 `/sync-it`，列 drift 給使用者裁決 |
| 「PRD 還對嗎」 | 跑 `/sync-it` |
| 「API 改了文件要動嗎」 | 跑 `/sync-it` |
| 「我這 sprint 改了哪些東西」 | 跑 `/sync-it` 摘要本 sprint drift |

## 為什麼

- **AI 讀過期文件 → 寫錯程式** — 文件是 AI 的長期記憶，記憶腐爛 = 行為腐爛
- **6 個月後你忘了** — 沒同步的文件比沒寫還糟（誤導）
- **新人 / 學員無所適從** — 不知道該信哪邊
- **Review 失準** — reviewer 看文件以為這樣，code 卻是那樣

## 違反這條規則的後果

```
Day 1：改 API 的 path，文件來不及改
Day 7：另一個 feature 依文件的舊 path 寫前端 → bug
Day 30：AI 讀文件 + 讀 code，自動推論「文件是新的，code 是舊的」 → 把對的 code 改回錯的
Day 90：沒人記得當初到底哪個對 → 全面重寫
```

## 心法

> **文件不是事後文書工作，是 spec 的一部分。**

> **改 code 同時改文件，不是負擔；改完 code 才補文件，才是負擔。**
