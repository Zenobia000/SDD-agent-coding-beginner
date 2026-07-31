---
name: codebase-design
description: 用 deep-module 詞彙設計或改善 module interface、測試 seam 與依賴方向。當模組難測、一改多處、interface 洩漏複雜度、需要比較替代設計，或其他 skill 需要架構紀律時使用。
---

# Codebase Design

設計 deep modules：用小 interface 隱藏大量行為，放在乾淨 seam，讓 caller 與 tests 從同一 surface 使用。

## 共用詞彙

- **Module**：任何具有 interface 與 implementation 的單位，可是 function、class、package 或跨層 slice。
- **Interface**：caller 正確使用 module 必須知道的一切，包含型別、invariants、errors、ordering、configuration 與效能特性。
- **Implementation**：module 內部做法。
- **Depth**：caller 每學一單位 interface 能取得多少行為；高 leverage 的 module 才深。
- **Seam**：不修改該處就能替換行為的位置，也是 interface 所在位置。
- **Adapter**：在 seam 上實作 interface 的具體角色。
- **Leverage**：一份隱藏複雜度被多個 callers/tests 重用。
- **Locality**：知識、變更、bug 與驗證集中在 module 內，而不散落 callers。

談架構時使用這些詞，避免把 module、interface、seam 混稱成泛化的「service」「component」「boundary」。

## 判斷

- **Deletion test**：刪掉 module 後，複雜度消失代表它只是 pass-through；複雜度重新散到 N 個 callers，代表它有深度。
- interface 同時是 test surface。測試必須伸進內部通常表示 seam 放錯或 module 形狀不對。
- 一個 adapter 只證明假想變化；第二個真實 adapter 出現才抽 seam。
- 按會一起變動的 domain 行為聚合，不按 controller/service/model 技術層機械拆分。
- core policy 不直接依賴 ORM、SDK、HTTP client；把它們放在 adapters。
- 優先 accept dependencies、return values 與小 surface，不在 module 內偷偷建立外部依賴。

## 設計流程

1. 定義 caller 需要的最小 capability 與必須知道的 invariants。
2. 畫出目前 interface、implementation、callers 與外部 dependencies。
3. 找出複雜度洩漏、shotgun surgery、重複 decision 與錯誤 seam。
4. 需要重要新 interface 時使用 [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md)，比較至少兩個根本不同方案。
5. 重構 cluster 時使用 [DEEPENING.md](DEEPENING.md)，replace 而非在舊層上再加一層。
6. 定義 migration path 與通過同一 interface 的 tests，再改 implementation。

不要以 implementation/interface 行數比衡量 depth，也不要為假想未來建立 adapters 或抽象。
