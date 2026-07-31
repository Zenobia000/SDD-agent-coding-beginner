---
name: security-review
description: 對認證、授權、付款、檔案上傳、外部 API、秘密、資料遷移與高成本資源做攻擊路徑審查。當變更碰到敏感資料或對外 trust boundary 時使用。
---

# Security Review

先固定 diff 或明確 scope，再呼叫 `security-reviewer` 做獨立只讀審查。提供：

- fixed point 與 diff command；
- 相關 entrypoints、資料流與部署假設；
- `docs/agents/project.md` 的 risk boundary；
- 任何 security requirements 或 threat model。

要求 reviewer 從外部可控 input 追到具體 sink 與 impact，只列能以 code 證明的攻擊路徑。掃描秘密時只顯示檔案位置與遮罩後格式，不輸出原值。

聚合結果時分成：blocking paths、已檢查但不適用/未能推翻的假設、單一關鍵 unknown。不要自動修安全問題；先向使用者展示攻擊情境與修法，再依明確授權處理。
