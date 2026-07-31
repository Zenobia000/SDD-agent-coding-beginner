---
name: handoff
description: 把目前對話壓縮成可由新 session 接手的暫存 Markdown 文件，引用既有 artifacts 而不重複內容。
disable-model-invocation: true
argument-hint: "下一個 session 的目標"
---

# Handoff

把 handoff 寫到作業系統暫存目錄，不要放進 repo。檔名包含專案 slug 與時間戳。

內容只保留新 agent 無法從 artifacts 直接取得的脈絡：

- 下一個 session 的明確目標與停止條件。
- 已確認事實、已做決定、仍未決定與 out of scope。
- fixed point、目前 git 狀態與尚未驗證的風險。
- spec、tickets、ADRs、research、prototype、commits、diff 的路徑或 URL；不要複製全文。
- 建議在新 session 主動執行的 skills。
- 第一個具體動作與其預期輸出。

若使用者有傳參數，把它當成下一個 session 的焦點。遮罩 API keys、密碼、tokens、個資與內部敏感 URL。寫完後回報絕對路徑，提醒使用者開新 session 並引用該檔案；不要在原 session 繼續下一階段。
