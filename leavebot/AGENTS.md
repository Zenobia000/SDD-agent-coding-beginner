# LeaveBot —— agent 工作規則

> 這是 Starter 附的**起點**。Day 2 單元 7 會用 `curriculum/2-templates/agent-rules/` 的範本改寫它，
> 加上你們自己的規格與紅線。Claude Code 透過 `CLAUDE.md`（只有一行 `@AGENTS.md`）讀這一份。

## 規格在哪

- 需求：`1_requirements.md`（Day 1 產出）
- 架構：`2_architecture.md`（Day 2 產出）
- 兩份衝突、或規格沒寫的行為：**停下來問**，不要自己決定。

## 怎麼跑

```bash
pip install -e ".[dev]"
pytest
uvicorn app.main:create_app --factory --reload
```

說「完成」之前，必須跑過 `pytest` 並貼出結果。

## 專案結構

| 位置 | 放什麼 |
|---|---|
| `app/main.py` | FastAPI 進入點，路由加在 `create_app` 裡或拆模組 include |
| `app/schema.sql` | 資料表定義，每張表用 `CREATE TABLE IF NOT EXISTS` |
| `app/llm.py` | LLM 介面。業務程式只透過 `request.app.state.llm.complete(...)` 呼叫模型 |
| `app/config.py` | 設定與環境變數 |
| `tests/` | 測試。`conftest.py` 已提供 `client`、`fake_llm`、`settings` |
| `fixtures/leave-sentences.jsonl` | eval 起始集，Day 4 用 |

## 紅線

- 單元測試**不准呼叫真的 LLM**，一律用 `FakeLLM`。
- 剩餘天數、撞期檢查、核准，**一律由程式碼或人決定**，不採用 LLM 給的任何數字或狀態。
- LLM 的輸出必須通過格式驗證才能存進資料庫。
- 不准新增套件，除非先說明理由並得到同意。
- API key 只放 `.env`，不准寫進任何其他檔案。
- 不准修改或刪除測試來讓測試通過。
