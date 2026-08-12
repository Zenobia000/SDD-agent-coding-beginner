# 講師手冊：Antigravity 元件速成＋SmartTrip FX 實戰

學生固定照兩冊前進：

1. [`../ANTIGRAVITY.md`](../ANTIGRAVITY.md)：先看懂 Google Antigravity 的官方元件。
2. [`../BUILD.md`](../BUILD.md)：再完成本課專屬 SmartTrip FX。

**安裝不在兩冊之內。** [`../docs/INSTALL.md`](../docs/INSTALL.md) 是課前作業，課堂不排安裝時間；[`../docs/CLI_GUIDE.md`](../docs/CLI_GUIDE.md) 是隨堂速查，不是要照走的章節。

不要把第一冊當成第二冊的替代品，也不要另發答案、投影片、流程卡或預建專案。兩冊的目標不同，但路線只有一條。

## 完整教學目標

第一冊結束時，學生必須能：

1. 說出 Antigravity 的 agent loop，以及 IDE / Agent Manager / Browser / `agy` CLI 四個入口共用同一份 `.agents/` 設定。
2. 分辨 `AGENTS.md`（永遠 active、不支援 frontmatter）與 `.agents/rules/*.md`（`trigger` 控制載入）的責任。
3. 說出 customization 的五層載入優先序，以及「沒接受信任提示會讓整個 `.agents/` 靜默失效」。
4. 說出 Skill 的 frontmatter 為什麼只有 `name` + `description`，`description` 要怎麼寫才會被啟用。
5. 判斷什麼工作留在主 agent、什麼工作交給 Subagent。
6. 說出為什麼 Hooks 是 workspace 裡**唯一**能做硬性攔截的元件。
7. 分辨 MCP 是 agent 的外部連接，不等於產品執行時的 API client；並說出什麼時候才值得做 Plugin。
8. 說出 Artifacts 與 Browser 各解決什麼，哪些只有圖形介面才有。
9. 面對新需求時，只加入最少且必要的元件。

第二冊結束時，學生必須能：

1. 說出 SmartTrip FX 哪些判斷交給 AI、哪些規則留在 code。
2. 把需求寫成可 pass / fail 的 acceptance criteria。
3. 把 spec 切成有 dependency、能獨立驗證的 tickets。
4. 依 ticket 完成真實 red → green → refactor。
5. 用測試、compile、review 與 security review 證據宣稱完成。
6. 用 `commit-message` Skill 產出 atomic Conventional Commit。

驗收不是背元件或 Skill 名稱，而是能選對元件、完成行為並提出證據。

## 建議授課方式

### 兩次課程（推薦）

第一堂 2.5–3 小時走完官方元件速成；第二堂 4–5 小時完成 SmartTrip FX。中間讓學生休息、開一個乾淨的新對話，不要在同一個超長 context 裡連做兩冊。

### 一日工作坊

上午第一冊、下午第二冊，總長約 7–8 小時。若只有半天，不要刪掉專案實戰；改採下面的示範版。

### 3 小時示範版

- 第一冊：第 0、1、3、5、9 章。
- 第二冊：實戰第 0、1、2、3 章，由講師示範第 5.1 與第 6 章。
- 第 2、4、6、7、8 章與其餘兩張 ticket 留作課後自學。

第一冊第 1 章不能跳——它是學生第一次看到 `AGENTS.md` 與 Rules 的責任差別，跳掉後面每一章都會混成「一大份 prompt」。

第二冊第 1 章也不能跳。它產生的 `docs/agents/project.md` 是第 2、3 章的第一個輸入（`grill-with-docs`、`to-spec` 都先讀它）；跳過會讓學生從第 2 章就得自己回答 AI 問的專案設定問題。時間真的不夠，就由講師預先備妥該檔發給學生，不要讓 skill 落到自行探索的 fallback。

## 第一冊課表：官方元件速成（10 章）

| 段落 | 時間 | 學生動作 | 講師只檢查 |
|---|---:|---|---|
| 第 0 章 | 10–15 分 | 啟動 `agy`、接受信任提示、看 agent loop | 沒有立刻要求 AI 改檔；信任提示真的選了信任 |
| 第 1 章 | 15–20 分 | 讀 `AGENTS.md` 與 `rules/` 的 frontmatter | 沒把 instructions 當 enforcement |
| 第 2 章 | 15 分 | 走一次 customization 探索與五層優先序 | 能說出「未信任 = 靜默失效」 |
| 第 3 章 | 20–25 分 | 讀 SKILL.md frontmatter、啟動 `workflow` | Skill 只按需載入；知道兩欄都必填 |
| 第 4 章 | 15–20 分 | 委派 Subagent | 主 context 只收摘要；知道唯讀只是文字約束 |
| 休息 | 10 分 | | |
| 第 5 章 | 25 分 | 手動測試 `PreToolUse` hook | 看見 deterministic deny；知道沒意見要回 `{}` |
| 第 6 章 | 15 分 | 查看 `mcp_config.json`、做 runtime 分流 | 不新增連線或 secret |
| 第 7 章 | 15 分 | 跑 `agy plugin list`、判斷封裝邊界 | 不安裝任何 plugin |
| 第 8 章 | 10 分 | 認識 Artifacts 與 Browser | 知道本章無法在無桌面環境驗證 |
| 第 9 章 | 15 分 | 做總選型、查 `agy` 指令總表 | 使用最少元件 |

合計約 165–185 分鐘。**課前提醒兩件事**：每章的「照貼照跑：終端機」都是唯讀、無副作用；「照貼照跑：agy」會呼叫模型、**消耗學生的 AI credits**，一章跑一次就夠，不要反覆重跑。

## 第二冊課表：SmartTrip FX 實戰（8 章）

| 段落 | 時間 | 學生動作 | 講師只檢查 |
|---|---:|---|---|
| 實戰第 0–1 章 | 25 分 | 讓 Antigravity 讀對規則、建立 project contract | 環境與真相源讀對 |
| 實戰第 2 章 | 30 分 | 固定需求與 AI / code 邊界 | 沒有模糊規則 |
| 實戰第 3–4 章 | 30 分 | 產 spec、切三張票 | criteria 可 pass / fail |
| 休息 | 10 分 | | |
| 實戰第 5 章 | 90–150 分 | 三個 TDD vertical slices | 有 RED 證據、一次一票 |
| 實戰第 6 章 | 30 分 | review、full test、commit | 沒把未跑寫成通過 |
| 實戰第 7 章 | 15 分 | 回顧與遷移 | 能說出下一個專案第一句 |

## 課前準備

學生需要 Git、Python 3.11+ 與**已安裝且已完成認證**的 Antigravity CLI（`agy`）。`agy` 支援原生 Windows，但兩冊的驗收命令都是 Unix shell，**Windows 學生請在 WSL 執行**；macOS 與 Linux 直接用系統終端機。核心課不需要 Node、Docker、MCP server、外部 API key 或雲端帳號，也不需要 Antigravity IDE——本課全程走 CLI。

安裝與認證請學生**在開課前**照 [`../docs/INSTALL.md`](../docs/INSTALL.md) 完成。透過 SSH 連遠端主機的學生走 device code 流程，該文件有專節說明。

講師應使用乾淨 clone 親自走完兩冊，先確認：

```bash
git --version
python3 --version
agy --version
python3 -c "import json; json.load(open('.agents/hooks.json'))"
python3 -m json.tool .agents/mcp_config.json >/dev/null
git config core.hooksPath
```

最後一行必須印出 `.githooks`，否則第二層 guardrail 完全沒作用。再確認第一冊第 5 章的 hook deny 命令會如預期輸出 `{"decision": "deny", ...}`，以及第二冊所有學生 prompt 引用的 Skill 都存在（`ls .agents/skills`，目前 31 個）。

**開課第一件事：確認每位學生都接受了 workspace 信任提示。** 未信任的 workspace，`.agents/` 底下 rules、skills、hooks 全部不載入而且**不報錯**——這是本課最容易被誤判成「教材壞掉」的單一原因。回讀方式：

```bash
python3 -c "import json,pathlib; p=pathlib.Path.home()/'.gemini/antigravity-cli/settings.json'; print(json.load(p.open()).get('trustedWorkspaces','(尚未信任任何 workspace)') if p.exists() else '(尚未跑過 agy)')"
```

Antigravity 的行為在開課前以本機 `agy` 實測重新核對：先跑 `agy --version` 與 `agy --help`，binary 行為與 [官方文件](https://antigravity.google/docs) 不符時以 binary 為準。不沿用舊部落格截圖。

不要在課前發預建 SmartTrip FX。需要展示時，現場照同一份 prompt 產生；學生看到生成與驗證過程，才學得到工程迴圈。

## 巡場順序

學生卡住時只做四件事：

1. 指出他目前在哪一冊、哪一章、缺哪個通過條件。
2. 請他貼該章的「卡住就貼」。
3. 看最窄的本地檔案或命令真實輸出，不用記憶猜。
4. 同一路徑修正兩次仍偏離，就**開一個新對話**（或先 `/rewind` 收回上一步），用更窄 scope 與成功條件重開。

先排除的三個系統性原因，順序固定：

1. **workspace 沒信任** → `.agents/` 全部靜默失效，症狀是「Skill 叫不動、hook 不擋」。
2. **不在 repo 根目錄啟動 `agy`** → Antigravity 從 CWD 往上找 `AGENTS.md` 與 `.agents/`，在子目錄啟動會漏設定。
3. **`core.hooksPath` 沒設** → `.githooks/` 不生效，症狀是「該被擋的 commit 過了」。

同一處有三位學生卡住，視為教材缺陷。記錄手冊、章節、原 prompt、實際輸出、`agy --version` 與失敗命令，課後修教材，不把問題歸因給學生。

## 第一冊檢查題

| 章 | 問學生一句話 |
|---|---|
| 0 | Antigravity 一輪會做哪四件事？IDE 與 `agy` 共用的是哪一份設定？ |
| 1 | 為什麼完整 workflow 不該塞在 `AGENTS.md`？`AGENTS.md` 為什麼不能加 frontmatter？ |
| 2 | 沒接受信任提示會發生什麼？你怎麼**看得出來**它發生了？ |
| 3 | Skill 的 frontmatter 只有兩欄，`description` 要寫進哪兩件事才會被啟用？ |
| 4 | Subagent 幫主 session 省下什麼？它的「唯讀」是誰在保證？ |
| 5 | 為什麼安全底線要用 hook，不能只寫在 `AGENTS.md`？沒有意見時該輸出什麼？ |
| 6 | App 的 runtime API 為什麼不自動等於 MCP？ |
| 7 | 什麼訊號表示該從 workspace 設定升級成 Plugin？ |
| 8 | Artifacts 與 Browser 各解決什麼？哪一個沒有圖形介面就用不到？ |
| 9 | 這個需求最少需要哪些元件？ |

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
- 第二冊直接開做：學生會把每個 `.agents/` 檔都叫 prompt；先補第一冊責任分層。
- 把 `AGENTS.md` 當 policy engine：回第一冊第 1、5 章比較。Antigravity 的 workspace **沒有 `settings.json`**，宣告式權限在這裡不存在。
- 以為 skill 正文的「只有使用者能叫」是強制：那是**文字約束**，Antigravity 沒有 `disable-model-invocation` 這種欄位。要硬擋只有 hook。
- 以為 subagent 的唯讀是結構性的：也只是文字約束，`tools` / `disallowedTools` 在 Antigravity 不存在。
- 看見 MCP 就替產品串 API：先分開 agent 開發環境與產品 runtime。
- 課堂上安裝 plugin 或註冊真實 MCP server：第 6、7 章都是唯讀辨識，不建立任何連線。
- 反覆重跑「照貼照跑：agy」：那些命令會消耗學生 AI credits，一章一次就夠。
- 用 `--dangerously-skip-permissions` 繞過卡住的授權：教學環境一律禁止，先找出被擋的真正原因。
- 一口氣生成 SmartTrip 全部 code：退回 ticket，一次只做一個 vertical slice。
- 用「看起來沒問題」結案：要求實際命令、exit code 與未驗證清單。

## 沒網路或額度不足

`agy` 本身需要可用服務。若課中無法呼叫模型：

- 兩人一組，一人扮使用者、一人依本地元件與固定案例回答。
- 第一冊每章的「照貼照跑：終端機」**全部不需要網路也不需要 credits**，第 0–5 章仍可用終端機讀檔與手動測 hook。
- 第二冊先在紙上判斷需求邊界、acceptance criteria 與下一個測試。
- 講師可用預先錄製的短輸出示範 `agy` 對話、Subagent 委派與 `/mcp`。
- 恢復連線後從該章重新生成；不提供預建 `labs/`。

環境問題超過 10 分鐘就改成配對，不讓全班停在安裝階段。

## 教材 UX 規則

修改教材時，必須同時滿足：

- 固定順序仍是 `README.md` → `ANTIGRAVITY.md` → `BUILD.md`；安裝維持在 `docs/INSTALL.md`，不要搬回主線。
- 第一冊教官方元件選型，第二冊保留完整 SmartTrip 專案迴圈；不可互相取代。
- 每個操作區塊只要求一個動作，並標明是「終端機」還是「agy」。
- 每章都有預期輸出、通過條件與修正句。
- 本地元件名稱能在 `.agents/` 找到；未配置的官方元件要明說為何缺席。
- 第一冊核心練習唯讀，不要求 credential、付費服務或不可逆操作。
- 第二冊固定答案直接放在使用章節，不建立 `labs/`。
- 每個事實標明出處等級：**【已驗證】**（本機 `agy` 實測）、**【依文件】**（只有官方文件這樣說）、**【⚠️ 未載明】**（查不到，不編答案）。官方網站與 binary 衝突時以 binary 為準並寫出差異。
- 官方功能的 scope、路徑與穩定性標示附官方 URL，並保留核對日期與對應的 `agy` 版本。
- 改動 `.agents/hooks/` 後，**必須同步更新 `.agents/README.md` 的 hook 行為對照表**——那是教材承諾。

最後執行相對連結檢查、官方 URL 檢查、JSON 語法檢查、hook 測試與 `git diff --check`，再用乾淨 clone 完整走一次。
