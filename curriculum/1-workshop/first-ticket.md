# 第一張票（講師發）

> **2 天工作坊專用。** 4 天版的學員自己拆票，不用這一份。
>
> 開工時把下面框起來的內容，複製成上課 repo 的 `issues/001-first-slice.md`。
> 票裡的「依你們的架構」都要換成你們 `2_architecture.md` 的實際名稱 —— 這張票只定範圍，不替你們決定 API 長什麼樣子。

---

```markdown
# 一句寫死的請假句子，解析成假單並存進資料庫

## Done when
- 有一個測試：用 FakeLLM 回傳一份固定的假單 JSON，呼叫你們架構裡「送出請假」的 API，
  資料庫裡多一筆假單，欄位與 JSON 一致。這個測試是綠的。
- 有一個測試：FakeLLM 回傳不是 JSON 的東西（例如「我不能這樣做」），API 回錯誤，資料庫沒有新資料。
- `pytest` 全綠，包含骨架原本的測試。
- （選做）`.env` 設 `LLM_PROVIDER=claude-cli`，用一句真的請假句子打 API，資料庫多一筆合理的假單。

## Context
這是第一條垂直切片：從一句話 → LLM 解析 → 格式驗證 → 存進資料庫，薄到只走一條路。
規格見 2_architecture.md 的「資料模型」與「API」段落。

## Blocked by
nothing

## Notes
- 只做一種假別、一句句子。剩餘天數、撞期、核准**都不做** —— 那是後面的票。
- 不做畫面、不做登入。
- LLM 的輸出一定要先通過格式驗證才能存，這是 AGENTS.md 的紅線，不是可選的。
- 測試一律用 FakeLLM（tests/conftest.py 的 fake_llm），不准呼叫真的模型。
```
