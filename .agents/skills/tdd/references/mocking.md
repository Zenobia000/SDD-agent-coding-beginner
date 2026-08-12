# Mocking Guide

## 可以替換

- HTTP、queue、email、payment 等第三方服務。
- clock、random、UUID。
- process、filesystem 與真正跨程序的 database seam。
- 很慢且已由其他測試單獨證明的外部 adapter。

## 不要替換

- 正在測的 domain logic。
- 同一模組內的 private function。
- 只是為了讓 assertion 容易寫的內部 collaborator。
- 你真正需要整合信心的 database/repository path。

優先提供小型 in-memory adapter 或 deterministic fake，而不是堆疊 mock expectations。Assertion 優先看公開結果與狀態，只有 interface contract 本身是互動時才驗證 call（例如「付款只扣一次」）。
