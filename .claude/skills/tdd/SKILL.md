---
name: tdd
description: 以 red-green-refactor 完成新功能或 bug regression。當使用者要求 test-first、提到 TDD/red-green、要新增可觀察行為，或 implement skill 需要逐片建立回饋迴圈時使用。
---

# Test-Driven Development

先讀 `docs/agents/project.md` 的 focused/full test 命令、相關 glossary 與 ADR。測試描述沿用 domain language。

## 先固定 seam

Seam 是不用伸進 implementation 就能觀察行為的公開 interface。開始前列出本輪要測的 seams 與理由：優先使用最高層既有 seam，數量越少越好。規格已明訂或 ticket 已核准的 seam 直接使用；只有新增或改變 seam 才詢問使用者。

## 每一個垂直 slice

1. 寫一個行為測試，expected value 來自 spec、已知 literal 或獨立計算。
2. 跑最窄命令並保留紅燈輸出；若測試一開始就綠，先證明它會因缺少行為而失敗。
3. 只寫讓這個測試通過的最小 production code，不預做下一片。
4. 重跑同一測試得到綠燈，再跑鄰近測試防止局部回歸。
5. 在綠燈上做小型 refactor；不改 observable behavior，每一步都重跑。

一個 test → 一個 implementation → 一次 feedback。不要先寫完整批測試再批量實作。

## 測試品質

- 測公開行為，不測 private methods 或內部協作者排列。
- mock 只放在真正外部 seam：network、clock、random、filesystem、process、第三方服務。
- 不用 tautological assertions、純 `not None`、無語意 snapshot 或只驗證 mock 被呼叫。
- 包含主流程、關鍵邊界與錯誤路徑，但不為覆蓋率窮舉沒有風險的排列。

例子見 [tests.md](tests.md)，mock 決策見 [mocking.md](mocking.md)。

完成一張 ticket 前依 project contract 跑 full test。任何未跑或 flaky 結果都列為未驗證，不能宣稱完成。
