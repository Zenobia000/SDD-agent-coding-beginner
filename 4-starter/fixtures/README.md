# Eval 起始集：`leave-sentences.jsonl`

30 句請假句子與人工標註的預期假單，Day 4 單元 13 用來量 AI 解析的準確率。
**這是起始集**，請加上你們公司真的會出現的說法。

## 格式

一行一筆 JSON：

```json
{
  "id": "L006",
  "today": "2026-10-12",
  "sentence": "下週三下午要看牙醫，週五順便連休",
  "expected": [
    {"start_date": "2026-10-21", "end_date": "2026-10-21", "period": "pm", "leave_type": null, "days": 0.5},
    {"start_date": "2026-10-23", "end_date": "2026-10-23", "period": "full", "leave_type": null, "days": 1}
  ],
  "clarify": false,
  "tags": ["multi", "type-unclear"]
}
```

| 欄位 | 意思 |
|---|---|
| `today` | 解析時假設的「今天」。全部是 2026-10-12（週一），「明天」「下週三」都以它為準 |
| `expected` | 一句話可能產生多筆假單 |
| `period` | `full` 整天、`am` 上午、`pm` 下午 |
| `leave_type` | `annual` 特休、`personal` 事假、`sick` 病假、`menstrual` 生理假、`marriage` 婚假、`bereavement` 喪假；`null` 代表句子裡看不出來，要員工確認 |
| `days` | 扣掉週末後的請假天數 |
| `clarify` | `true` 代表這句話資訊不足，系統應該追問，不該產生假單 |
| `tags` | 分類，方便看哪一類最常錯。`injection` 是 prompt injection 測試句 |

`tests/test_fixtures.py` 會檢查格式與天數算術，**不檢查 AI**。改了這個檔案之後跑一次 `pytest`。

## 標註時做的判斷

這些是課堂的約定，你們公司可以不同，**但要寫下來**：

- 「看醫生」「急診」算病假；「看牙醫」看不出是病假還是特休，標 `null`。
- 「照顧小孩」：好日子科技的規章沒有家庭照顧假，標 `null`。
- 「9 點到 12 點」算上午半天。
- `injection` 類的預期結果，只包含句子裡真正的請假需求，注入的指令一律不影響結果。

## 已知限制

- ⚠️ 天數只扣週末，**沒有扣國定假日**。挑選日期時已避開 2026 年 10 月可能的連假日，但沒有對照官方行事曆驗證過。
- 標準答案由課程作者標註。**開課前講師要逐筆複核一次**，有疑義的改掉或刪掉。
