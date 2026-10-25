# 學員講義與維護入口

直接開 [site/index.html](site/index.html)。閱讀依「目標 → 當前任務 → 提示詞／補充」逐步展開；勾選進度存在自己的瀏覽器。

| 原稿／用途 | 網站 |
|---|---|
| [課前準備](00-setup.md) | [setup](site/setup.html) |
| [總覽](01-overview.md) | [overview](site/overview.html) |
| [D1：Vibe Coding到PRD](02-day1.md) | [day1](site/day1.html) |
| [D2：SDD實作與驗收](03-day2.md) | [day2](site/day2.html) |
| [提示詞](appendix/prompt-book.md) | [prompts](site/prompts.html) |
| [排解](appendix/troubleshooting.md) | [troubleshooting](site/troubleshooting.html) |

第二天單元與提示詞、課前準備、checkpoint取自學生專案 `course/PLAN.json`、`WORKFLOW.md`、`SETUP.md`、`CHECKPOINTS.md`、`prompts/`。修改來源後從講義repo執行 `python scripts/sync-course.py`；`--check`可驗證所有生成內容一致。`course-source.json`記錄來源雜湊，不手改生成頁。

第一天的三題與Reference在day1頁，通用補充提示詞來源為 [d1-prompts.md](d1-prompts.md)。D1只用獨立資料夾，不載入LeaveBot公司規則。

`slides/`是歷史視覺素材；現行講師流程在 [class_plan](../class_plan/README.md)。
