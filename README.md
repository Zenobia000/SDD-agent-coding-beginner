# Vibe Coding × SDD × AI 開發實戰營

**講師用 PPT 帶講解，學生跟 HTML 做操作。**

本機授課統一開 `上課資料包/00-開始這裡.html`，不用再找其他資料夾。此包包含行前檢核、五分鐘導讀、PPT 頁碼對照、學生 HTML 講義、兩份企業贈禮與發放 ZIP；完整複製到授課電腦即可。

## 哪些和上課有關

| 位置 | 用途 |
|---|---|
| `上課資料包/` | 講師實際帶進教室的一包檔案，本機保存、不納入 Git |
| [handbook/site/index.html](handbook/site/index.html) | 學生 HTML 講義來源，保留公開版與必要素材 |
| [starter-kit/index.html](starter-kit/index.html) | 課後企業贈禮，保留兩份完整簡報 |
| `封存/2026-10-26_課程整理/` | 舊備課、粗剪 PDF、舊簡報、研究草稿與維護工具；原位置與去向見整理清單 CSV |

`class_plan`、`output`、`scripts` 與根目錄重複的「開啟講義.html」已移至封存。上課只開資料包入口，不需要操作封存。

## 學生怎麼開啟

1. 收到「學生講義.zip」後，先完整解壓縮。
2. 雙擊 ZIP 解壓後的「開啟講義.html」。
3. 初次上課先看課前準備，之後跟著講師進入當前單元，按需展開提示詞與驗收。

若下載的是此 GitHub 專案 ZIP，解壓後直接開 `handbook/site/index.html`。講義不用啟動伺服器；Agent、安裝下載與外部連結仍需要網路。

第一天在獨立資料夾體驗作品，最後留下簡版 PRD；第二天 fork [LeaveBot 學生專案](https://github.com/Zenobia000/leavebot-bootcamp) 的 main，依 A–K 卡片完成表單、驗證、SQLite 與我的假單。

## 企業贈禮

[企業贈禮入口](starter-kit/index.html)包含「企業 AI 轉型啟動指南」與「從 Agent 到模組化 Skill」兩份簡報，課後另發企業贈禮 ZIP。原始素材與各自 LICENSE 均保留。

<details>
<summary>本機維護與重新打包</summary>

工具已放進本機封存的 `09-教材維護/scripts/`，可從專案根目錄執行：

```bash
python 封存/2026-10-26_課程整理/09-教材維護/scripts/prepare-class.py
```

此指令沿用上課資料包的最新版 44 頁 PPTX，更新 HTML 講義、導讀與兩個發放 ZIP。維護來源與同步說明見 [handbook/README.md](handbook/README.md)。

封存、授課包、PPTX 與 PDF 不納入 Git。已取消追蹤的內容仍存在歷史提交，這次整理沒有改寫歷史。

</details>
