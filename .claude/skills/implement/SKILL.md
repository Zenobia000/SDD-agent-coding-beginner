---
name: implement
description: 依已確認的 spec 或 ticket 完成一個可驗證的垂直切片，持續跑回饋迴圈，最後做獨立雙軸 review。
disable-model-invocation: true
argument-hint: "spec、ticket、issue 或明確任務"
---

# Implement

只完成使用者指定的工作單位。若來源包含多張 tickets，先取一張 frontier ticket；不要在同一 context 偷做下一張。

## 1. 固定工作契約

- 讀完整來源、`docs/agents/project.md`、相關 glossary/ADR 與目前 git 狀態。
- 寫下 scope、out of scope、acceptance criteria、測試 seam 與 fixed point。
- 只有會改變行為或架構的缺失才詢問；可從 code 或 tracker 找到的事實自行查。

## 2. 垂直實作

- 新功能與可鎖定的 bug 使用 `tdd`，在已同意的 seam 一次完成一個 red → green slice。
- 每一片跑 focused test；定期跑 typecheck/lint。不要把整批測試拖到最後才第一次執行。
- 若遇到與本票無關的問題，記錄為 out-of-scope finding，不順手修。
- 實作過程若發現規格錯誤，停止該分支並帶證據回報，不自行重寫需求。

## 3. 收尾

1. 依 `docs/agents/project.md` 跑完整的 format check、typecheck、tests 與 build；不存在的命令標示不適用，未知命令不能猜。
2. 執行 `code-review`，fixed point 使用步驟 1 固定的基準，spec source 使用本票來源。
3. 對 authentication、authorization、payment、upload、外部 API、秘密或不可逆資料變更加跑 `security-review`。
4. 修正阻擋 findings 後重跑受影響的檢查；保留兩個 review 軸的原始結論。
5. 回報改了什麼、實際命令與結果、未驗證事項、review 結果與剩餘風險。

使用者明確要求 commit 時，先用 `commit-message` 根據 staged diff 產生符合 repo 慣例的訊息。不要自行 commit、push、開 PR、部署或關票；只有明確要求時，才以已通過驗證的當前狀態執行該外部動作。
