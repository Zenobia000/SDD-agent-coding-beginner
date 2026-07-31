# CONTEXT.md Format

```markdown
# <Domain or Project>

一句話說明這份 glossary 涵蓋的 bounded context。

## Language

**Canonical term**:
精確定義、生命週期或不變量。
_Avoid_: 容易混淆的替代詞，以及不用它的原因。

## Relationships

- A owns many B
- B belongs to exactly one A

## Flagged ambiguities

- `<term>` — 尚未決定的兩種意義與需要誰決定。
```

每個詞只放領域意義。不要寫 class 名、資料表、endpoint、套件或實作步驟。已解決的 ambiguity 移到正式定義或刪除。
