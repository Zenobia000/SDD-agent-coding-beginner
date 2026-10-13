# LeaveBot Starter

> 4 天實戰營的起點專案。**只有骨架，沒有請假的業務邏輯** —— 那是你要讓 agent 依規格寫出來的部分。

## 這裡已經有什麼

| 有 | 沒有（你要做的） |
|---|---|
| FastAPI app 與 `/health` | 請假相關的 API |
| SQLite 連線與 `schema.sql` 載入 | 資料表（依你們的 ERD） |
| LLM 介面、Claude 實作、測試用的 `FakeLLM` | 解析請假句子的 prompt 與格式驗證 |
| pytest 與共用 fixture | 規則引擎（剩餘天數、撞期）與它的測試 |
| 30 句 eval 起始集 | eval 腳本（Day 4） |

## 開始

**1. 進到專案資料夾**（每組的 fork 就是自己的一份，直接在這裡寫）：

```bash
cd leavebot
```

**2. 建虛擬環境並安裝**（Python 3.11 以上）：

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows：.venv\Scripts\activate
pip install -e ".[dev]"
```

**3. 確認一切正常：**

```bash
pytest                             # 全部要是綠的
cp .env.example .env
uvicorn app.main:create_app --factory --reload
```

瀏覽器打開 <http://127.0.0.1:8000/health>，看到 `"status":"ok"` 就完成了。<http://127.0.0.1:8000/docs> 是自動產生的 API 文件。

**還沒動任何東西之前，測試就要是綠的。** 不是綠的，先找講師。

## 接上真的 Claude

預設 `LLM_PROVIDER=fake`，不花錢也不用 key。要呼叫真的模型時，改 `.env`：

```bash
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=<你的 key>
LLM_MODEL=                         # 留空用預設模型；想省成本可以換成較便宜的模型
```

- 單元測試**永遠用假的**，不受這個設定影響。
- 模型拒答時，伺服器端會自動改由備援模型回答（`fallbacks="default"`），見 `app/llm.py`。

用 OpenAI 或其他供應商：在 `app/llm.py` 照 `LLMClient` 介面寫一個類別，加進 `build_llm`。可以直接請 agent 做 —— 先寫測試，這本身就是 Day 3 的練習。

## 專案大腦

`AGENTS.md`（Codex 讀）與 `CLAUDE.md`（Claude Code 讀，只是指向 `AGENTS.md`）是起點。
Day 2 會用 `curriculum/2-templates/agent-rules/` 的範本把它改成你們自己的版本。
