# Deepening a Cluster

## 1. 畫出 cluster

列出入口 callers、目前 modules、共享 decisions、外部 systems 與 tests。把依賴分成：

- domain policy：真正應該被 module 隱藏的規則；
- volatile detail：database、HTTP、filesystem、clock；
- caller-specific presentation：不應塞進共用 module 的差異。

## 2. 選 seam

把 seam 放在穩定 domain capability 上，不放在 SDK 或 ORM method 形狀上。interface 只暴露 caller 必須知道的資料與錯誤；順序、重試、mapping、cache、transaction 等留在 implementation。

## 3. Replace, don't layer

新 module ready 後讓一個真實 caller 穿過它，測公開行為，再逐步搬其他 callers。不要保留舊 wrapper → 新 wrapper → 舊 helper 的永久層疊；完成 migration 後刪掉被取代的 pass-through。

## 4. 保持綠燈

寬改動使用 expand–contract：新增相容 form、分批 migrate callers、確認沒有使用後 contract。每一批有固定 command 與預期訊號。

完成後再做 deletion test：刪掉新 module 時，複雜度是否會重新分散？若不會，它可能仍然太淺。
