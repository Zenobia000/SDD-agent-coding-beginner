# Vibe Coding × SDD × AI 開發實戰營

兩天、14小時。**第一天在獨立資料夾體驗作品，收斂到PRD；第二天使用LeaveBot空白專案，以規格、通用skills與測試完成表單請假功能。**

| | 主線 | 學員帶走 |
|---|---|---|
| D1 | 網站臨摹、塔羅抽牌、捲動動畫；選一題做，補上下文比較，操作與修復 | 第一版與比較紀錄、簡版PRD |
| D2 | Brief／PRD／SRS → Archify流程 → 最小設計與TC → 兩張主線票 → TDD → 變更與交付 | 可執行表單、SQLite、測試與人工證據 |

**打開 [講義網站](handbook/site/index.html)**。下載時保留整個 `handbook/site/` 資料夾。
學生第二天 fork [leavebot-bootcamp](https://github.com/Zenobia000/leavebot-bootcamp) 的 `main`；只複製main即可，checkpoint從講師upstream取得。主線不需要模型API key，LLM解析為延伸。

| 對象 | 入口 |
|---|---|
| 學員 | [課前準備](handbook/site/setup.html)、[D1](handbook/site/day1.html)、[D2](handbook/site/day2.html)、[提示詞](handbook/site/prompts.html) |
| 講師 | [備課導航](class_plan/README.md)、[彩排清單](class_plan/instructor-prep.md) |
| 維護者 | [教材同步方式](handbook/README.md)、[整合紀錄](class_plan/leavebot-redesign.md) |
| 課後企業啟動包 | [starter-kit](starter-kit/README.md)；[簡報](starter-kit/deck/index.html) |

課程版本 `2026.10-unified-1`。學生 `course/PLAN.json` 與 `course/prompts/` 是第二天單元、路徑與提示詞來源：
```bash
python scripts/sync-course.py --student-root ../leavebot-bootcamp
python scripts/sync-course.py --student-root ../leavebot-bootcamp --check
python scripts/check-handbook.py --student-root ../leavebot-bootcamp
```
`dist/handbook.html` 導向現行網站；舊圖片投影片與既有PPTX是歷史參考，現行授課以兩天備課稿為準。
