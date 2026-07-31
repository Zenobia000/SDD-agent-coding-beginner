---
name: domain-modeling
description: 建立或銳化專案 domain model。當需求出現含糊或多義術語、需要 ubiquitous language、討論領域關係與邊界，或需要記錄難以逆轉的架構決策時使用。
---

# Domain Modeling

這是主動維護領域模型的紀律。單純讀 glossary 不算啟動本 skill；只有挑戰、決定或寫回術語與決策時才使用。

## 找到文件

先讀 `docs/agents/project.md` 的 Domain docs。缺少設定時：

- 根目錄 `CONTEXT.md` 代表 single-context。
- 根目錄 `CONTEXT-MAP.md` 代表 multi-context，依 map 找對應 glossary 與 ADR。
- 文件只在第一個內容確定時才建立，不預先 scaffold 空目錄。

## 工作方式

1. 使用者用詞與 glossary 衝突時立即指出，請他在兩個精確定義間選擇。
2. 模糊或多義詞先提出 canonical term；不要讓「帳號」「狀態」「處理」等詞同時代表多個概念。
3. 用具體 edge-case scenarios 壓測關係、生命週期、擁有權與不變量。
4. 使用者描述現況時以 code 查證；對話和實作矛盾時並列證據，不默認其中一方正確。
5. 術語一旦收斂立即更新 glossary，使用 [CONTEXT-FORMAT.md](CONTEXT-FORMAT.md)。glossary 只放領域語言，不放 implementation、spec 或 session notes。
6. 只有同時符合「難逆轉、缺脈絡會令人意外、存在真實取捨」才提議 ADR；使用 [ADR-FORMAT.md](ADR-FORMAT.md)，取得同意後才寫。

所有程式命名、spec 與 ticket 優先沿用 glossary 的 canonical terms。
