# 循環工程：照著做完第一個 AI 協作專案

這是一份可以直接操作的 Claude Code 教科書。你不需要選題、選框架或先讀理論；全班都做同一題 **SmartTrip FX**，照順序貼上教材中的 prompt，就能做出可測試的 Python CLI。

## 三分鐘開始

支援環境：macOS、Linux 或 Windows WSL，並已安裝 Git、Python 3.11+、Claude Code。

```bash
git clone https://github.com/Zenobia000/ai-vibe-coding-beginner.git
cd ai-vibe-coding-beginner
git switch -c workshop/smarttrip-fx
git config core.hooksPath .githooks
claude
```

進入 Claude Code 後，打開 [`BUILD.md`](./BUILD.md)，從「第 0 章」開始複製。

## 你會做出什麼

SmartTrip FX 讀取一份 AI 產生的行程 JSON，完成兩件必須由程式決定的事：

- 算出現金項目、未知項目與 10% 預備金，向上取整成建議換匯金額。
- 比較今日匯率與 30 日均線，輸出 `GOOD`、`NEUTRAL` 或 `WAIT`。

核心課程不連外、不需要 API key，也不會把答案藏在另一個目錄。每章都有可貼 prompt、範例問答、預期輸出、通過條件與修正句。

## 你真正會學到什麼

1. 先固定 scope、成功訊號與停止點，再讓 AI 動手。
2. 把 AI 判斷與 deterministic code 分開，用 schema 當交界。
3. 把需求變成 pass/fail acceptance criteria。
4. 用 spec → tickets → TDD vertical slices 完成實作。
5. 只用實際測試與 review 證據宣稱完成。

## 只有三個入口

| 路徑 | 用途 |
|---|---|
| [`.claude/`](./.claude/) | 可直接用於實戰專案的工程設定與 Skills |
| [`BUILD.md`](./BUILD.md) | 學生唯一主線，從空 repo 做到可執行程式 |
| [`curriculum/README.md`](./curriculum/README.md) | 講師節奏、巡場檢查與教材維護規則 |

其他主題等完成本書後，再從 `.claude/skills/workflow` 選一條適合的新路徑；第一次不要同時學框架、API 與多代理協作。
