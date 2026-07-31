# 講師手冊：Claude Code 元件速成＋SmartTrip FX 實戰

學生固定照兩冊前進：

1. [`../CLAUDE-CODE.md`](../CLAUDE-CODE.md)：先看懂官方元件。
2. [`../BUILD.md`](../BUILD.md)：再完成本課專屬 SmartTrip FX。

不要把第一冊當成第二冊的替代品，也不要另發答案、投影片、流程卡或預建專案。兩冊的目標不同，但路線只有一條。

## 完整教學目標

第一冊結束時，學生必須能：

1. 說出 Claude Code 的 agent loop。
2. 分辨 `CLAUDE.md` / Rules、Skills 與 Auto memory 的載入責任。
3. 分辨 Permissions、Hooks 與文字 instructions 的控制力。
4. 為探索、外部連接與跨 repo 分發，選對 Subagent、MCP、Plugin。
5. 知道 Agent teams 是實驗性功能，且平行寫入前要隔離 worktree。
6. 面對新需求時，只加入最少且必要的元件。

第二冊結束時，學生必須能：

1. 說出 SmartTrip FX 哪些判斷交給 AI、哪些規則留在 code。
2. 把需求寫成可 pass / fail 的 acceptance criteria。
3. 把 spec 切成有 dependency、能獨立驗證的 tickets。
4. 依 ticket 完成真實 red → green → refactor。
5. 用測試、compile、review 與 security review 證據宣稱完成。
6. 用 commit-message Skill 產出 atomic Conventional Commit。

驗收不是背元件或 Skill 名稱，而是能選對元件、完成行為並提出證據。

## 建議授課方式

### 兩次課程（推薦）

第一堂 3 小時走完官方元件速成；第二堂 4–5 小時完成 SmartTrip FX。中間讓學生休息、重新開乾淨 session，不要在同一個超長 context 裡連做兩冊。

### 一日工作坊

上午第一冊、下午第二冊，總長約 7–8 小時。若只有半天，不要刪掉專案實戰；改採下面的示範版。

### 3 小時示範版

- 第一冊：第 0、1、3、5、8 章。
- 第二冊：實戰第 0、2、3 章，由講師示範第 5.1 與第 6 章。
- MCP、Plugins、Agent teams、其餘兩張 ticket 留作課後自學。

## 第一冊課表：官方元件速成

| 段落 | 時間 | 學生動作 | 講師只檢查 |
|---|---:|---|---|
| 第 0 章 | 15 分 | 啟動、看 agent loop | 沒有立刻要求 AI 改檔 |
| 第 1 章 | 20 分 | 看 `/context`、分記憶層 | 沒把 instructions 當 enforcement |
| 第 2 章 | 20 分 | 看 settings / permissions / Plan mode | 能說出三層差異 |
| 第 3 章 | 25 分 | 讀 frontmatter、呼叫 `/workflow` | Skill 只按需載入 |
| 第 4 章 | 25 分 | 委派唯讀 Subagent | 主 context 只收摘要 |
| 休息 | 10 分 | | |
| 第 5 章 | 25 分 | 手動測試 `PreToolUse` hook | 看見 deterministic deny |
| 第 6 章 | 20 分 | 查看 MCP、做 runtime 分流 | 不新增連線或 secret |
| 第 7–8 章 | 30–45 分 | 比較 Plugin / team、做總選型 | 使用最少元件 |

## 第二冊課表：SmartTrip FX 實戰

| 段落 | 時間 | 學生動作 | 講師只檢查 |
|---|---:|---|---|
| 實戰第 0–1 章 | 25 分 | 開機、建立 project contract | 環境與真相源讀對 |
| 實戰第 2 章 | 30 分 | 固定需求與 AI / code 邊界 | 沒有模糊規則 |
| 實戰第 3–4 章 | 30 分 | 產 spec、切三張票 | criteria 可 pass / fail |
| 休息 | 10 分 | | |
| 實戰第 5 章 | 90–150 分 | 三個 TDD vertical slices | 有 RED 證據、一次一票 |
| 實戰第 6 章 | 30 分 | review、full test、commit | 沒把未跑寫成通過 |
| 實戰第 7 章 | 15 分 | 回顧與遷移 | 能說出下一個專案第一句 |

## 課前準備

學生需要 Git、Python 3.11+ 與可正常登入的最新版 Claude Code，環境支援 macOS、Linux 或 Windows WSL。核心課不需要 Node、Docker、MCP server、外部 API key 或雲端帳號。

講師應使用乾淨 clone 親自走完兩冊，先確認：

```bash
git --version
python3 --version
claude --version
python3 -m json.tool .claude/settings.json >/dev/null
```

再確認第一冊的 hook deny 命令，以及第二冊所有學生 prompt 所引用的 Skill 都存在。安裝方式、命令與實驗性標示在開課前以 [Claude Code 官方文件](https://code.claude.com/docs/en/overview) 重新核對，不沿用舊部落格截圖。

不要在課前發預建 SmartTrip FX。需要展示時，現場照同一份 prompt 產生；學生看到生成與驗證過程，才學得到工程迴圈。

## 巡場順序

學生卡住時只做四件事：

1. 指出他目前在哪一冊、哪一章、缺哪個通過條件。
2. 請他貼該章的「卡住就貼」。
3. 看最窄的本地檔案、`/context` 或命令真實輸出，不用記憶猜。
4. 同一路徑修正兩次仍偏離，就 `/clear`，用更窄 scope 與成功條件重開。

同一處有三位學生卡住，視為教材缺陷。記錄手冊、章節、原 prompt、實際輸出、Claude Code 版本與失敗命令，課後修教材，不把問題歸因給學生。

## 第一冊檢查題

| 章 | 問學生一句話 |
|---|---|
| 0 | Claude Code 一輪會做哪四件事？ |
| 1 | 為什麼完整 workflow 不該塞在 `CLAUDE.md`？ |
| 2 | Permission 已 allow，Hook 還能做什麼？ |
| 3 | 哪種 Skill 必須只有使用者能啟動？ |
| 4 | Subagent 幫主 session 省下什麼？ |
| 5 | 為什麼安全底線要用 command hook？ |
| 6 | App 的 runtime API 為什麼不自動等於 MCP？ |
| 7 | 什麼訊號表示該從 project config 升級成 Plugin？ |
| 8 | 這個需求最少需要哪些元件？ |

## 第二冊檢查題

| 章 | 問學生一句話 |
|---|---|
| 0 | 哪些是模型 instructions，哪些由 hook 強制？ |
| 1 | 後續 Skill 從哪裡讀測試命令？ |
| 2 | 為什麼 `unknown` 要計入現金？ |
| 3 | 哪一條 criterion 最容易直接寫成 test？ |
| 4 | 為什麼 CLI ticket 被前兩張阻擋？ |
| 5 | 你能指出哪一次 RED 嗎？ |
| 6 | 哪個完成宣稱有命令輸出支持？ |
| 7 | 下一個專案的第一句是什麼？ |

## 常見錯誤

- 第一冊講完就結課：學生只會名詞，沒有真實產物；必須保留第二冊。
- 第二冊直接開做：學生會把每個 `.claude` 檔都叫 prompt；先補第一冊責任分層。
- 把 `CLAUDE.md` 當 policy engine：回第一冊第 1、5 章比較。
- 看見 MCP 就替產品串 API：先分開 Claude 開發環境與產品 runtime。
- 為了展示平行而平行：先畫 dependencies、write sets、side effects。
- 直接啟用 Agent teams：先問單一 Subagent 是否已能隔離工作。
- 一口氣生成 SmartTrip 全部 code：退回 ticket，一次只做一個 vertical slice。
- 用「看起來沒問題」結案：要求實際命令、exit code 與未驗證清單。

## 沒網路或額度不足

Claude Code 本身需要可用服務。若課中無法呼叫模型：

- 兩人一組，一人扮使用者、一人依本地元件與固定案例回答。
- 第一冊第 1–5 章仍可用終端機讀檔與手動測 hook。
- 第二冊先在紙上判斷需求邊界、acceptance criteria 與下一個測試。
- 講師可用預先錄製的短輸出示範 `/context`、Subagent 與 `/mcp`。
- 恢復連線後從該章重新生成；不提供預建 `labs/`。

環境問題超過 10 分鐘就改成配對，不讓全班停在安裝階段。

## 教材 UX 規則

修改教材時，必須同時滿足：

- 固定順序仍是 `README.md` → `CLAUDE-CODE.md` → `BUILD.md`。
- 第一冊教官方元件選型，第二冊保留完整 SmartTrip 專案迴圈；不可互相取代。
- 每個操作區塊只要求一個動作。
- 每章都有預期輸出、通過條件與修正句。
- 本地元件名稱能在 `.claude/` 找到；未配置的官方元件要明說為何缺席。
- 第一冊核心練習唯讀，不要求 credential、付費服務或不可逆操作。
- 第二冊固定答案直接放在使用章節，不建立 `labs/`。
- 官方功能的 scope、路徑與穩定性標示附官方 URL，並保留核對日期。

最後執行相對連結檢查、官方 URL 檢查、JSON 語法檢查、hook 測試與 `git diff --check`，再用乾淨 clone 完整走一次。
