# HTML 講義

學生請在解壓後雙擊根目錄的 **[開啟講義.html](../開啟講義.html)**，或直接打開 [site/index.html](site/index.html)。講師以 PPT 帶節奏，學生依 HTML 的當前單元操作，提示詞與補充內容按需展開。

以下是網站維護說明，學生不需執行。

## 來源與同步

- `site/day1.html`：第一天的單元、三題完整 Demo 與 Reference，目前直接維護此頁。
- `d1-prompts.md`：第一天的通用補充提示詞，是同步工具的必要輸入。
- 第二天、課前準備與 Checkpoint：讀取相鄰 `leavebot-bootcamp/course/` 的 `PLAN.json`、`LEAVEBOT.md`、`WORKFLOW.md`、`STACK.md`、`SETUP.md`、`CHECKPOINTS.md` 與 `prompts/`。
- `course-source.json` 記錄上游來源雜湊，`course-plan.json` 保存同版課程資料。

修改上游內容後執行：

```bash
python scripts/sync-course.py --student-root ../leavebot-bootcamp
python scripts/check-handbook.py --student-root ../leavebot-bootcamp
```

預設只同步網站與必要 JSON，不建立散落的 Markdown 副本。若本機確實需要副本，可加 `--export-markdown`；這些副本不納入 Git，也不影響學生下載的網站。

第二天的題目、技術棧、工作流程與救援說明都能在 HTML 內閱讀。Agent 執行時仍依學生專案裡的檔案工作，學生不必逐一打開那些 Markdown 才能跟課。

## 發放

在專案根目錄執行 `python scripts/package-materials.py`，把 `dist/學生講義.zip` 發給學生。學生完整解壓後，雙擊 `開啟講義.html`，不需開伺服器。講義本體可以離線閱讀；Agent、安裝下載與外部網站連結仍需網路。

企業贈禮另外打包，不混進學生講義。講師 PPTX、粗剪 PDF、備課稿、舊圖片投影片與產檔暫存均在 Git 之外保存。
