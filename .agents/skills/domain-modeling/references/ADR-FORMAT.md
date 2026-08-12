# ADR Format

檔名使用 `NNNN-short-decision.md`，編號沿用目錄現有序列。

```markdown
# ADR-NNNN: <Decision>

Date: YYYY-MM-DD
Status: Accepted

## Context
哪個長期約束或張力迫使我們做決定。

## Decision
選了什麼，以及適用範圍。

## Alternatives considered
- <option> — 放棄原因與它原本的優點。

## Consequences
- 正面影響。
- 成本與新限制。
- 什麼訊號出現時應重新檢視。
```

不要把已由產品需求寫死的條件包裝成架構決策，也不要記錄暫時性偏好。
