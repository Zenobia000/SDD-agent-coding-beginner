# M3｜輸出格式你來定，不要它自由發揮

> 從「**希望**它回 JSON」→「**保證**它符合格式」。

## 老問題

叫它「請用 JSON 回我」，常會遇到：

- 前後多一層 markdown 的 ``` 圍籬
- `"age": "25"` —— 數字變成字串
- 少了一個欄位（例如 phone 沒了）

**關鍵動作：把約束從「prompt 層」搬到「API / 型別層」。**

## 三層保證，約束力由弱到強

| 層 | 手段 | 白話 | 保證什麼 |
|---|---|---|---|
| 1 | Prompt 要求 | 用嘴巴拜託 | 什麼都不保證 |
| 2 | JSON mode | 開個開關 | **弱**：保證能解析，但有哪些欄位它說了算 |
| 3 | **Structured Outputs** ★ | 給它一張表格 | **強**：保證完全符合你的格式 |

## 事後檢查 vs 事前約束

- **事後檢查**：讓它自由生成完，再回頭檢查有沒有錯 → 錯了只能重來
- **事前約束**：**它每生一個字，就被限制只能走向合法的結構** → 根本錯不了

> 一句話：**不要用 prompt 防漏欄位，要用 schema 讓漏欄位變成「不可能」。**

## Pydantic 三步（Python 生態的標準做法）

> **Pydantic** = Python 裡定義「這份資料長什麼樣」的工具；`BaseModel` 就是那張表格。

```
① 定義 BaseModel          ② SDK 自動轉成 JSON Schema     ③ output_parsed
   name: str                  拿去約束模型的解碼過程          直接就是物件
   age: int                                                 不用再 json.loads()
   is_subscriber: bool
```

## function calling 三步協定（讓 AI 呼叫你寫的程式）

```
① 帶著 tools 發請求（記得 strict=True）
      ↓
② 讀它回的 function_call：name / arguments / call_id
      ↑ call_id 千萬不能省 —— 它是「這是回答哪一次呼叫」的編號
      ↓
③ 你這邊真的執行那個 Python 函式，把結果用 function_call_output 回填
      ↓
④ 帶著結果再請求一次 → 拿到最終答案
```

> 重點：**你給模型看的工具說明（tool schema）和實際的 Python 函式，必須對得上。**

## 兩個鎖

| 鎖 | 作用 |
|---|---|
| `strict=True` + `additionalProperties=False` | 鎖死參數，**禁止它自創欄位** |
| `tool_choice` | `auto` = 它自己判斷要不要用工具；也可以**強制**它呼叫某個工具 |

> 提醒：**如果你只是想要結構化資料，就用 Structured Outputs，不要假裝定義一個工具去騙它。**

## 一個 model 同時是「格式」也是「驗證器」

| 用法 | 白話 |
|---|---|
| `Field(description=...)` | 在欄位旁邊寫說明，給模型看的提示 |
| `Literal[...]` | 鎖死可選值（只能填這幾個，不能自己發明） |
| 巢狀 BaseModel | 表格裡面還能包表格 |
| `model_validate_json` | **最後一道閘**：資料進來先驗一次 |
| `except ValidationError` | 接住壞資料，不要讓它往下游流 |
| 加一個 `reasoning` 欄位 | 讓它先寫推理、再寫結論 |

## 實際應用：先分類，再路由

```
使用者訊息「我想查一下退貨規則是什麼？」
    ↓
分類器 → 結構化 category { intent: inquire_policy, domain: after_sales, topic: return_policy }
    ↓
     ├─→ 工具（查退貨政策 API）
     └─→ 知識庫（檢索政策文件與 FAQ）
```

搭配 streaming（邊生成邊顯示）給使用者即時回饋。

## 這關的驗收

**100% 通過 `model_validate_json`** —— 沒有 ValidationError、沒有越界的類別。

## 心法

> **schema 本身就是保證。**
> 別人只要看你的 model，就知道輸出長什麼樣，下游不必再寫一堆 `if 'name' in data` 的防呆判斷。

---
