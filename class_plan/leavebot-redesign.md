# 上課 repo 改版規格｜leavebot-bootcamp

> 對象：[`Zenobia000/leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)，以 2026-10-24 的 `bcfaa9e` 為基準。
> 目的：讓上課 repo 對得上 [`README.md`](./README.md) 的課程設計，並讓講師上課時可以順順地帶。
> 講義（`handbook/`）已照這份的**目標狀態**撰寫。
>
> **進度（2026-10-24）**：P0-1、P0-2、P0-3、P1 全部、P2 已在 leavebot 的分支 `refactor/form-slice-course` 完成。
> Archify 收進來後是 5.6 MB（拿掉預先渲染的 HTML），在 Windows ＋ Node 24 上跑過 `doctor` 與 `demo`；`finalize` 的瀏覽器檢查是選用參數，沒驗。
> **剩下 P0-4 的 checkpoint 分支**，要在講師彩排 D2 時邊做邊推。

---

## 現況與問題

| 現況 | 問題 |
|---|---|
| 講義寫 `templates/`、`scripts/trace.py`、`scripts/run_eval.py`、`HARNESS.md` | `bcfaa9e` 已經把它們搬到 `course/`，`scripts/` 也刪了。舊講義照著打會失敗 |
| D2 主線是一句話 AI 解析，Next.js ＋ FastAPI，再加 eval 與注入測試 | 跟新設計的「表單切片為主、AI 解析為進階」對不上；Node 與 npm 在企業筆電上常常卡關 |
| 沒有保底版本 | 講義寫「講師會給上一個疊代的保底版本」，repo 裡卻沒有 |
| `/to-tickets` 寫死 I0–I4 五張票（I1 是 LLM 解析） | 跟新的 D2 切法不同 |
| 沒有 Archify | 新設計的 D1 單元 7、D2 投影片 36 要用 |
| 沒有 D1 的練習區 | D1 下午的 Demo 與 Archify 練習不知道該做在哪裡 |

---

## 不動的部分

- **空地原則**：`main` 上只有 `course/` 與設定檔，沒有 app 程式碼。
- `course/templates/` 的六份模板、`TRACEABILITY.md`、`LESSONS.md`、`agent-rules/`、`hooks/`。編號不變。
- `course/examples/it-asset/`。
- 10 個技能、兩個 guard hook、`.mcp.json`（context7、playwright）。
- Codex 相容層：`.agents/skills` symlink、`.codex/`。講義不教，但不刪。

---

## 改動清單

依優先順序排列。P0 沒做完，講義就對不上。

### P0-1 `course/STACK.md`：拿掉 Next.js，由 FastAPI 送出靜態頁

| 層 | 改成 |
|---|---|
| 前端 | 純 HTML ＋ 原生 JavaScript ＋ 一份 CSS，放在 `backend/app/static/`，由 FastAPI 掛在 `/` |
| 後端 | Python 3.12、FastAPI、標準庫 `sqlite3`、pytest（不變） |
| 套件白名單 | `fastapi>=0.115`、`uvicorn>=0.30`、`httpx>=0.27`；開發用 `pytest>=8.0`。`anthropic>=1.0` 改成**只有進階挑戰才加**的選用依賴 `[ai]` |
| 啟動 | 拿掉 `dev.sh`。一行指令：`.venv/bin/uvicorn app.main:app --app-dir backend --reload`（Windows：`.venv\Scripts\uvicorn …`），開 `http://127.0.0.1:8000/` |
| 測試目錄 | `backend/tests/acceptance/`（驗 PRD 的 AC，打 API）、`backend/tests/unit/`（驗規則模組）。表單切片用兩層就夠，`system/`、`integration/` 留給進階挑戰 |

骨架步驟（新的「骨架」段，取代原本的 I0）：

1. agent 生成 `pyproject.toml`，內容照白名單，pytest 設定照原本寫的（`testpaths`、`pythonpath`、`--import-mode=importlib`、登記 `req` marker）
2. `python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"`
3. agent 依 `docs/05-sds.md` 生成 `backend/app/main.py`：`GET /api/health`，以及把 `static/` 掛在 `/`
4. 驗收：瀏覽器打開首頁，頁面用 `fetch("/api/health")` 讀到回應，顯示在畫面上

同源，所以不需要 CORS，也不需要 rewrites。「不開 CORS」這條紅線照留。

保留「今天固定為 2026-10-12，從 `LEAVEBOT_TODAY` 讀」那一段，表單切片的「不可早於今天」驗證也會用到。

### P0-2 `course/LEAVEBOT.md`：MVP 改成表單主線

保留：一句話題目介紹、公司規章（好日子科技）、角色。這些是進階挑戰與 D1 例子的素材。

「這次的範圍」改成：

| 基本完成標準（全班） | 進階挑戰（做完基本的組自選） |
|---|---|
| 員工從下拉選單選自己（預設幾筆假資料，沒有登入） | C1 主管待核准畫面：核准／駁回，狀態只能 `pending → approved / rejected` |
| 填寫請假表單：假別、開始日期、結束日期、時段（整天／上午／下午）、理由 | C2 特休剩餘額度檢查 |
| 系統驗證：必填欄位、結束日期不早於開始日期、天數由程式計算（扣週末、半天算 0.5） | C3 同組同日人數提醒 |
| API 存進 SQLite | C4 一句話 AI 解析：`POST /api/parse`（合約不變）、`course/fixtures/` 的 eval 集 |
| 「我的假單」畫面列出申請與狀態（送出後是「待審核」） | C5 Prompt injection：理由欄塞指令，狀態不可改變 |
| 自動化測試通過，加上人工驗收 | |

規模上限改成：PRD 的 story ≤ 4、AC ≤ 10；SRS 的 FR ≤ 10；Test Plan 的 TC 6–12 個。

「唯一替你定好的 API」移到進階挑戰 C4 底下。基本範圍的所有 API 都由學員的 SDS 決定。

### P0-3 `/to-tickets` 技能：改成新的票型

| 票 | 範圍 |
|---|---|
| `issues/000-skeleton.md` | 照 `STACK.md` 的骨架段：`pyproject.toml`、`GET /api/health`、首頁讀得到它。不寫業務邏輯 |
| `issues/001-submit-leave.md` | 垂直切片：表單 → 驗證 → `POST` 存檔 → 「我的假單」顯示狀態。Test Plan 裡基本範圍的 TC 全部落在這一張 |
| `issues/1xx-*.md` | 進階挑戰 C1–C5，一張一個，只在學員要求時才切 |

票的格式（「這張票讓哪些 TC 變綠」、垂直切片原則）照舊。

### P0-4 checkpoint 分支

講師把 D2 彩排一次，依 [`README.md`](./README.md#checkpoint-分支) 的表格推出 `cp1-requirements` … `cp5-delivered` 與 `advanced-ai-parse`。

- 每個分支從**前一個分支**長出來，是同一條線上的快照，不是各自獨立的版本。
- `cp1`～`cp3` 的文件是講師版本的答案。**範例看深度用，不要照抄**這條原則一樣適用。給學員的說法是：「切過來是讓你們接著做，不是對答案。」
- 每個分支的 README 頂端加一行：這是哪個時間點的快照、下一步做哪張卡。
- 改了 `main` 的 `course/` 之後，要把改動一路 rebase 或 merge 到每個 cp 分支。在 `.maintain/` 加一支檢查：每個 cp 分支都包含 `main` 的最新 commit。

學員 fork 時要**取消勾選**「Copy the `main` branch only」，否則 fork 裡沒有 cp 分支。保險做法是加 upstream：

```bash
git remote add upstream https://github.com/Zenobia000/leavebot-bootcamp.git
git fetch upstream
git switch -c rescue-cp2 upstream/cp2-design   # 原本的進度留在原分支，不會不見
```

### P1-1 把 Archify 收進 `.claude/skills/archify/`

- 來源：[tt-a1i/archify](https://github.com/tt-a1i/archify)，MIT，固定在 3.2。在 `.claude/THIRD-PARTY-NOTICES.md` 補上授權聲明。
- 收進專案層，而不是讓學員自己裝到使用者層：**全班同一個版本，課前少一步可能失敗的安裝**。
- 整包大約 18 MB。可以先試著拿掉 `examples/` 等非執行期用的目錄，但拿掉之後要跑一次 `node bin/archify.mjs doctor` 確認還能用。⚠️ 未驗證。
- 執行時需要 Node 18 以上，不需要 `npm install`。⚠️ `finalize` 的瀏覽器檢查需要什麼（是否要另外裝瀏覽器）還沒在乾淨的 Windows 上驗證過。
- 產出位置約定：D2 的圖一律放 `diagrams/`，Archify 預設的 `.archify/` 暫存資料夾加進 `.gitignore`。

### P1-2 D1 練習區 `playground/`

- `.gitignore` 加上 `playground/`。D1 單元 6、7 的 Demo 網站、PRD 草稿和流程圖都放在這裡，不會跟 D2 的 `docs/` 混在一起。
- `AGENTS.md` 原廠規則加一段：`playground/` 是 D1 練習區，不受 `STACK.md` 限制，也不需要寫測試。
- 為什麼不另開一個 repo：agent 一律要在這個 repo 根目錄啟動，hooks 和 Archify 才會生效。

### P1-3 `AGENTS.md` 原廠規則

- 「模型只透過 Anthropic API 呼叫」「測試不准呼叫真的模型」移到「進階挑戰 C4 起適用」的小節。基本範圍沒有 LLM。
- 刪掉 Next.js、`dev.sh`、context7 查 Next.js 的字句；context7 改成「查 FastAPI 的寫法」。
- `.venv/bin/pytest` 的規則照留。

### P1-4 `course/HARNESS.md`

- 技能表加上 Archify（11 個技能）。
- 「常用操作」表以 Claude Code 為主；Codex 欄改成附註。
- 單元編號改成新的：HARNESS 是 D1 **單元 5** 的標本，不再是單元 1。

### P1-5 模板瘦身

- `04-sad.md` 的 C4 範例圖把 `前端 Next.js` 改成 `靜態頁（由 FastAPI 提供）`。
- `06-test-plan.md` 的「AI 驗收」與 eval 門檻段落標成**進階挑戰 C4 才填**；基本範圍只要求 TC 表與追溯矩陣。
- `TRACEABILITY.md` 的 V-model 圖改成兩層測試（`acceptance/`、`unit/`）。

### P2 README

- 「課前」第 2 步：Python 3.12、Claude Code、Node 18 以上（只給 Archify 用）。拿掉 Node 24 與 create-next-app 預熱。
- 「課前」第 3 步：Anthropic API key 改成**選用**，只有進階挑戰 C4、C5 需要。
- fork 時提醒取消勾選「只複製 main」。
- Windows symlink 那一步標成「只有用 Codex 才需要」。

---

## 落地順序建議

1. P0-1、P0-2、P0-3、P1-3、P1-5 開在同一個分支改完，一個 PR。
2. 收 Archify（P1-1）、開 `playground/`（P1-2），用另一個 PR，順便驗證 Archify 在 Windows 上能不能跑。
3. 合併之後，照講義把 D2 完整彩排一次，邊做邊推 cp 分支（P0-4）。**彩排時遇到的每一個講義錯誤，回頭改講義。**
4. 最後才做 P1-4、P2。

---

## 驗收這次改版

- [ ] 在乾淨的 Windows 筆電上，照講義 `00-setup.md` 從 fork 做到 `pytest` 全綠，不需要 Node 也能完成 D2 的基本範圍
- [ ] 講義裡出現的每一個 repo 路徑都存在（`grep` 講義裡的 `course/`、`.claude/` 路徑，逐一檢查）
- [ ] 彩排一次 D2，七個單元各自在表定時間 ±10 分鐘內完成
- [ ] 每個 cp 分支切過去之後，`pytest` 的結果和分支說明一致（每個分支都全綠；`cp3` 只有 health 測試）
