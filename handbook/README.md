# HTML 講義

學生請在完整解壓後雙擊學生 ZIP 內的「開啟講義.html」，或直接打開 [site/index.html](site/index.html)。講師以 PPT 帶節奏，學生依 HTML 的當前單元操作，提示詞與補充內容按需展開。

以下是網站維護說明，學生不需執行。

## 來源與同步

- `site/day1.html`：第一天的單元、三題完整 Demo 與 Reference，目前直接維護此頁。
- `d1-prompts.md`：第一天的通用補充提示詞，是同步工具的必要輸入。
- 第二天與課前準備：讀取相鄰 `leavebot-bootcamp/course/01-上課/` 的 `01-SETUP.md`、`02-WORKFLOW.md`、`03-LEAVEBOT.md`、`04-STACK.md` 與編號 `prompts/`。
- 課程資料與 Checkpoint：讀取學生專案 `course/02-補充/04-PLAN.json` 與 `02-CHECKPOINTS.md`。
- `course-source.json` 記錄上游來源雜湊，`course-plan.json` 保存同版課程資料。

修改上游內容後執行：

```bash
python 封存/2026-10-26_課程整理/09-教材維護/scripts/sync-course.py --student-root ../leavebot-bootcamp
python 封存/2026-10-26_課程整理/09-教材維護/scripts/check-handbook.py --student-root ../leavebot-bootcamp
```

預設只同步網站與必要 JSON，不建立散落的 Markdown 副本。若本機確實需要副本，可加 `--export-markdown`；這些副本不納入 Git，也不影響學生下載的網站。

第二天的題目、技術棧、工作流程與救援說明都能在 HTML 內閱讀。Agent 執行時仍依學生專案裡的檔案工作，學生不必逐一打開那些 Markdown 才能跟課。

## 發放

在專案根目錄執行 `python 封存/2026-10-26_課程整理/09-教材維護/scripts/prepare-class.py`，把 `上課資料包/04-對外發放ZIP/學生講義.zip` 發給學生。學生完整解壓後，雙擊 `開啟講義.html`，不需開伺服器。講義本體可以離線閱讀；Agent、安裝下載與外部網站連結仍需網路。

企業贈禮另外打包，不混進學生講義。講師 PPTX、粗剪 PDF、備課稿、舊圖片投影片與產檔暫存均在 Git 之外保存。

講師需要把上課檔案帶到另一台電腦時，執行 `python 封存/2026-10-26_課程整理/09-教材維護/scripts/prepare-class.py`，使用根目錄的 `上課資料包/`。這個包有獨立的 HTML 導讀，不需要攜帶教材維護來源或封存。

學生公開的 Skill Deck 位於 `../starter-kit/skill-deck/`，可從講義首頁「課後補充」進入，學生 ZIP 也包含同一份簡報。企業 Deck 只在本機企業贈禮包內，不公開、不放入學生包。
