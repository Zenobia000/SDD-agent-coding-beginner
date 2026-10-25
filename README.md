# Vibe Coding × SDD × AI 開發實戰營

**上課看 PPT 跟講解，實作跟著 HTML 講義做。學生只需要一個講義入口。**

## 學生怎麼開啟

1. 下載講師提供的「學生講義 ZIP」，或下載此專案的 ZIP。
2. **先完整解壓縮**，再雙擊根目錄的 **[開啟講義.html](開啟講義.html)**。
3. 初次上課先看「課前準備」，之後依講師進度進入「第一天」或「第二天」。

講義可以直接用瀏覽器閱讀，不必啟動伺服器、安裝套件或開 Markdown。請保留 `handbook/site/` 的完整結構，圖片與功能才會一起載入。GitHub 檔案頁顯示的是 HTML 原始碼，請下載、解壓後開啟。

| 上課材料 | 用法 |
|---|---|
| 雙日主講 PPTX | 講師投影，說明目標與示範 |
| HTML handbook | 學生看當前任務、展開提示詞、操作與勾選驗收 |
| [LeaveBot 學生專案](https://github.com/Zenobia000/leavebot-bootcamp) | 第二天 fork `main`，在自己的專案實作 |

第一天在獨立資料夾體驗作品，最後留下簡版 PRD。第二天換共同題目 LeaveBot，以規格與測試完成表單、驗證、SQLite 與我的假單。只需閱讀目前單元，提示詞與補充說明需要時再展開。

## 企業贈禮

兩份 HTML 簡報另放在 **[企業贈禮入口](starter-kit/index.html)**，不影響學生上課順序。下載後可直接以瀏覽器開啟。

<details>
<summary>維護者：哪些上傳、哪些留在本機</summary>

| 保留在 Git | 用途 |
|---|---|
| `開啟講義.html`、`handbook/site/` | 學生入口、實作講義與必要圖片、腳本 |
| `handbook/d1-prompts.md`、`course-*.json`、`scripts/` | 維護、同步、檢查及打包網站 |
| `starter-kit/deck/`、`starter-kit/skill-deck/` | 企業贈禮，保留各自的素材與 LICENSE |
| README、LICENSE、Git 設定 | 使用說明與版本管理 |

`class_plan/`、`output/`、`封存/`、`handbook/slides/`、Markdown 匯出副本，以及企業啟動包的研究／報告／工具草稿均留在本機，不進公開版本。PPTX 與 PDF 另外交付，不放進學生操作專案。

網站維護方式見 [handbook/README.md](handbook/README.md)。產出兩個互相獨立的發放包：

```bash
python scripts/package-materials.py
```

學生包只含講義網站。企業包只含兩份贈禮簡報與相關授權。ZIP 產出到已忽略的 `dist/`。

`.gitignore` 只影響未追蹤檔案。已上傳過的檔案還要取消 Git 追蹤，才會從下一個版本移除；歷史提交仍保留。

</details>
