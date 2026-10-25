# 2026-10-25 兩repo整合紀錄

新課程以LeaveBot `fb70f38` 的通用skills為基礎，從舊 `refactor/form-slice-course` 選取Archify工具。課程題目、技術棧、WORKFLOW、模板、提示詞與講義重新對齊。

## 保存舊版
LeaveBot：`archive/pre-unified-course-20261025`、`archive/form-slice-course-20261025`、`archive/barren-land-20261025` 保存舊版本。原分支名整合後停止作課堂入口，遠端tag確認存在才移除舊分支名。
講義原始提交保存在 `archive/handbook-before-unified-20261025`。工作開始前既有的本機檔案與使用者PPTX未作刪除。

## 維護來源
第二天單元與輸入／產出以學生 `course/PLAN.json` 為機器清單；具體課程限制在 `AGENTS.md`、`course/WORKFLOW.md`、`LEAVEBOT.md`、`STACK.md`；提示詞在 `course/prompts/A.md` 至 `K.md`。
講義執行 `python scripts/sync-course.py` 同步；`--check`驗證生成內容與來源雜湊。通用技能不放本課檔數、票數與技術棧。

## 空地與保底
學生main維持教材與工具，不加入app答案。五個checkpoint分支另含講師參考成果，附執行證據。舊分支中的README、題目與模板不得整批覆蓋新版main。
