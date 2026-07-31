# 實戰工程工作流

這套規則只定義工程紀律，不替使用者決定產品需求。使用者當下的明確指令永遠優先；不要讓其他專案文件擴大或改寫使用者指定的範圍。

## 每次開始

1. 先讀 `docs/agents/project.md`（若存在），取得本專案的驗證指令、issue tracker 與文件位置。
2. 只讀和任務直接相關的 `CONTEXT.md`、ADR、規格與程式碼。不要為了「了解全貌」把整個 repo 灌進 context。
3. 把事實與推論分開。事實附檔案行號、命令輸出或來源；缺證據就說尚未驗證。
4. 先固定本輪範圍、成功訊號與比較基準，再修改檔案。

## 執行原則

- 可以從環境查到的事實就自己查；只有真正的產品或取捨決策才問使用者，而且一次問一題並附建議答案。
- 功能以可獨立驗證的垂直切片前進。每一片都要縮短回饋時間，不要先做完所有層再一起驗證。
- 修 bug 先建立能抓到同一個症狀的紅燈命令，再推測根因。
- 新行為優先用 TDD；重構必須由既有綠燈保護，且不能把行為改動混進同一輪。
- 只報告自己實際跑過的驗證。未跑的檢查明講原因，不能寫成「已通過」。
- 並行前先畫 dependencies、read/write sets 與 side effects；共享 working tree 的 agents 只做 read-only 工作，並行寫入使用獨立 worktrees。
- commit message 必須來自 staged diff 並遵循 repo 歷史；不同意圖先拆 commit，不用一段訊息掩蓋混合變更。
- 不主動 commit、push、開 PR、部署、建立或修改外部 issue；只有使用者明確要求或核准後才做。

## 技能分層

- 使用者主動啟動的 skills 負責串流程，例如 `/grill-with-docs`、`/to-spec`、`/to-tickets`、`/implement`。
- 模型可自動啟動的 skills 只提供可重用紀律，例如 `tdd`、`diagnosing-bugs`、`codebase-design`、`code-review`。
- orchestration skill 可以呼叫 discipline skill；不要從一個使用者專用 skill 偷偷跳到另一個使用者專用 skill。
- 不知道該走哪條路時，請使用者執行 `/workflow`，不要自行套一整套儀式。
