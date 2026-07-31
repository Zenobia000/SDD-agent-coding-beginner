# CLAUDE.md

本 repo 有一個最高目標：讓第一次接觸 Claude Code 的學生，照 [`BUILD.md`](./BUILD.md) 從空白狀態做出可執行、可測試、可 review 的 SmartTrip FX。

## 教材契約

- 固定題目：SmartTrip FX，不要求學生自行選題。
- 固定路線：Python 3.11+ standard library CLI，不使用第三方套件。
- 固定邊界：AI 產行程 JSON；程式負責驗證、金額計算與匯率燈號。
- 核心課程不接 live LLM、匯率 API、資料庫、登入、Web UI 或部署。
- 不建立 `labs/`、reference answer 或預建成品；範例與檢查直接寫在 `BUILD.md`。

修改教材時，學生路徑只能是 `README.md` → `BUILD.md`。新增入口、選項或先備工具前，必須證明它能降低完成成本。

## 工程核心

開始任何改動前，先固定：

1. 這輪的 scope 與 out of scope。
2. 可以 pass/fail 的成功訊號。
3. fixed point 與停止條件。

從 repo、文件或命令能查到的事實自行查。只有會改變產品行為或風險的決策才問使用者，而且一次問一題、先給推薦答案。

以可獨立驗證的 vertical slice 前進。新行為使用 TDD；先保留紅燈證據，再寫最小實作，最後重構。只回報實際跑過的檢查，未跑或無法驗證的項目必須明說。

## Skills 的角色

`.claude/skills/` 是工具箱，不是所有專案都必走的關卡。需要完整 idea-to-code 路線時使用：

```text
/grill-with-docs → /to-spec → /to-tickets → /implement
```

不知道下一步時用 `/workflow` 取得一條建議。`tdd`、`diagnosing-bugs`、`codebase-design`、`code-review` 與 `security-review` 提供工程紀律；不要在使用者沒要求時自行啟動另一條 user-invoked workflow。

## 回覆方式

- 使用繁體中文，技術術語保留英文。
- 結論先行，只保留一條主要建議。
- 區分已確認、主要假設與未知；不要把推測寫成根因。
- 每次回覆結尾給一個可執行的下一步。

## 安全底線

`.claude/hooks/` 會攔截敏感檔案、疑似 credential 與高風險 shell 操作；`.githooks/` 保護 commit 與 push。不要繞過 hook，也不要自行 commit、push、開 PR、部署或寫入外部系統，除非使用者明確要求。

同一路徑連續失敗三次就停止微調，回報共同失敗模式並重新檢查最初假設。
