---
name: diagnosing-bugs
description: 對難解 bug、例外、測試失敗、flake 或效能退化執行可重現的診斷迴圈。當使用者說 diagnose/debug、回報壞掉或變慢，且根因尚未由證據確認時使用。
---

# Diagnosing Bugs

依序執行；只有寫出明確理由才能跳過 phase。先讀 `docs/agents/project.md`、相關 glossary、ADR 與現有 bug report。

## 1. 建立 tight feedback loop

在提出根因前，先得到一個已實際執行、能抓到使用者同一症狀的命令。依序嘗試：

1. failing unit/integration/e2e test；
2. curl/CLI + fixture + 精確 assertion；
3. headless browser；
4. replay 真實 payload/trace；
5. 最小 throwaway harness；
6. seeded property/fuzz loop；
7. `git bisect run` 或新舊版本 differential；
8. 最後才用結構化 human-in-the-loop 步驟。

完成標準：命令能在秒級完成、結果 deterministic（flake 則提高到可調查的重現率）、無人值守，且 assertion 對準同一個使用者症狀，不只是「沒有 crash」。

建立不了時停止，列出試過的方式，請使用者提供能重現的環境或 HAR/log/core dump/帶時間戳的錄影，或核准暫時 instrumentation。沒有 red-capable loop，不進根因推測。

## 2. 重現與最小化

執行 loop 看到紅燈，確認不是鄰近但不同的錯誤。一次移除一個 input、caller、config 或資料條件，每次重跑；直到剩餘每個元素都 load-bearing。

## 3. 排序 hypotheses

列 3–5 個互斥或可區分的假說。每個使用：

> 如果 X 是原因，改變 Y 會讓症狀消失／惡化；觀測 Z 會是某值。

沒有 falsifiable prediction 的猜測刪掉。把排序與證據展示給使用者；若使用者沒有回覆可繼續第一名，不把 checkpoint 當阻塞。

## 4. Instrument

每個 probe 只對應一個 prediction，一次只改一個變數。優先 debugger/REPL，其次針對邊界的 log；臨時 log 使用唯一 `[DEBUG-<id>]` 前綴。效能問題先建立 baseline、profiler/query plan，再改 code。

## 5. Fix + regression

在能重現真實 bug pattern 的最高正確 seam 先寫 regression test，看到紅燈後才修。修正後重跑 regression、原始未縮小 loop 與鄰近測試。若沒有正確 seam，不寫假的單元測試；把「架構無法鎖住 bug」列為 finding，修完 bug 後建議 `/improve-codebase-architecture`。

## 6. Cleanup

- 原始 loop 已綠、regression 已綠。
- 移除所有 `[DEBUG-...]` 與 throwaway artifacts。
- 回報已確認根因、哪個 hypothesis 被證偽、修法與命令輸出。
- 問「什麼會讓這個 bug 更早被發現或不可能發生？」；架構改善另開工作，不混在 bug fix。
