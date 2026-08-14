# AI Coding Agent 工程實戰課

這門課教的不是「怎麼跟 AI 聊天」，而是**怎麼用 AI 做出可驗證、可 review、可交付的軟體**。

**這個分支只負責導航，教材在下面的分支上。**

---

## 三個層級，先選層級再選工具

```text
第零層  想清楚要做什麼      sdd-lite                     不寫 code，用 no-code 平台
                                    ↓
第一層  學會操作工具        claude ／ antigravity        照著貼，看綠燈
                                    ↓
第二層  學會開發軟體        progressive-sdd              自己判斷，自己驗
```

### 第零層：定義線（不需要任何前置知識）

| 分支 | 教材 | 題目 | 特色 |
|---|---|---|---|
| [`sdd-lite`](../../tree/sdd-lite) | `DEFINE.md`（八站） | **SubTrim**（訂閱瘦身） | **一行 code 都不寫**，不用裝任何東西 |

給 Lovable、Bolt、Replit、Google AI Studio 這類 **no-code 造原型平台**的使用者。教的是**在你按下 Generate 之前，腦袋裡該先發生什麼事**。

八站從「一句抱怨」走到「可執行規格」：逼問痛點 → 種子簡報 → meta-prompt 逼出歧義 → **PRD → SRS → SAD** → 餵進平台並逐條驗收。三份文件俗稱 SDD 的簡易版。

⚠️ 這條線**只到 POC / MVP demo**。no-code 平台生出來的東西不能當正式產品上線 —— 為什麼、以及分界線在哪，寫在該分支的 `docs/TIERS.md`。

### 第一層：工具線（入門）

兩條線內容對等，差別只在你用哪個 agent。第二冊題目相同：**SmartTrip FX** —— 讀取行程 JSON，驗證輸入、計算旅費現金與匯率燈號，只用 Python standard library。

| 分支 | 工具 | 第一冊 | 專案契約 | Harness |
|---|---|---|---|---|
| [`antigravity`](../../tree/antigravity) | **Google Antigravity**（`agy` CLI + IDE） | `ANTIGRAVITY.md` | `AGENTS.md` | `.agents/` |
| [`claude`](../../tree/claude) | **Claude Code** | `CLAUDE-CODE.md` | `CLAUDE.md` | `.claude/` |

### 第二層：工程線（進階）

| 分支 | 第一冊 | 第二冊 | 特色 |
|---|---|---|---|
| [`progressive-sdd`](../../tree/progressive-sdd) | `PRINCIPLES.md`（心法） | `BUILD.md`（CookCard，七站） | **工具鏈內建、fork 即用、不給答案** |

**CookCard**：把料理影片變成能照著做的結構化食譜卡。會長出前端、後端、資料庫、多模態抽取、容器化與排程 —— 但這些是題目自己長出來的需求，不是為了教而塞進去的。

路線分成**七站**，每一站是一個能被獨立跳過的判斷。整條線的重點不是「照這個順序做」，是**知道這次哪幾站不用做**。36 個 coding agent 工程技能已內建在 `.claude/skills/`，fork 下來就能用，不需要安裝。

---

## 怎麼選

| 你的情況 | 去哪 |
|---|---|
| 不寫程式，但想把想法變成能用的東西 | `sdd-lite` |
| 在 Lovable / Bolt / Replit / AI Studio 上改到第二十次還是不對 | `sdd-lite` —— 問題八成不在平台，在輸入 |
| 想學怎麼寫 PRD / SRS / SAD | `sdd-lite` |
| 沒用過 coding agent | 先走一條工具線。`antigravity` 或 `claude` 都行 |
| 已經有 Google 帳號，想留在 Google 生態系 | `antigravity` |
| 已經在用 Claude Code，或有 Anthropic 訂閱 | `claude` |
| 會操作 agent 了，但不確定自己會不會「開發軟體」 | `progressive-sdd` |
| 覺得照著貼很順，但沒有一個決定是自己做的 | `progressive-sdd` |
| 只有無圖形介面的 Linux 主機（SSH） | 都可以，但工具線只能走 CLI；Antigravity IDE 需要桌面環境 |
| 想要一套現成的工程技能可以帶去自己的專案 | `progressive-sdd` —— 36 個技能就在 `.claude/skills/`，MIT |

兩條工具線沒有哪一條比較進階，元件模型不同而已。`progressive-sdd` 才是難度上的下一階。

`sdd-lite` 不在這條難度軸上 —— 它教的是**上游**，走完之後接哪一條工具線都可以，不接也行。

---

## 三分鐘開始

```bash
git clone https://github.com/Zenobia000/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner

git switch sdd-lite           # 定義線：no-code 平台，不寫 code
# 或
git switch antigravity        # 工具線：Google Antigravity
# 或
git switch claude             # 工具線：Claude Code
# 或
git switch progressive-sdd    # 工程線：工具鏈內建
```

切過去之後**先讀該分支的 `README.md`**，它會告訴你安裝什麼、從哪一章開始。

`sdd-lite` 連 clone 都不需要 —— 直接在 GitHub 網頁上讀 [`DEFINE.md`](../../blob/sdd-lite/DEFINE.md) 就能走完。

---

## 為什麼要分成這幾個分支

不是為了整齊，是因為**技術上無法共存**：

- Antigravity 只探索 `.agents/`（`agy` 執行檔內完全沒有 `.claude` 路徑字串）
- Claude Code 只讀 `.claude/`，且官方明文**不讀** `AGENTS.md`
- 兩者的 hook 阻擋協定不同，skill frontmatter 的可用欄位也不同

硬要塞進同一個分支，結果是兩份會各自腐爛的設定，加上一本必須不斷加註「如果你用 A 就…如果你用 B 就…」的教材。

`progressive-sdd` 分開的理由不同：**它的教法和工具線相反。** 工具線給 prompt、給預期輸出、給通過條件；工程線刻意全部不給，因為判斷沒辦法照著腳本學。混在一起會讓兩種教法互相稀釋。

`sdd-lite` 分開的理由又不同：**它的讀者不裝任何東西。** 沒有 CLI、沒有 harness、不需要會 git，教材裡出現一次 `.claude/` 或終端機指令，那條線的讀者就走掉一半。它跟其他三條唯一共用的東西是 `.githooks/`，而它的讀者連那個都用不到。

⚠️ 工程線的技能庫依賴 `disable-model-invocation`，**Antigravity 與 Copilot 都不支援**，所以那條線實質是 Claude Code 取向。落差寫在該分支的 `docs/SKILL-MAP.md`。

---

## 這個分支有什麼

只有導航與共用的東西：

| 路徑 | 用途 |
|---|---|
| `README.md` | 就是這一頁 |
| `.githooks/` | Git 層的安全閘門（擋真實 `.env`、疑似硬編碼憑證、對保護分支的非快轉 push）。各線共用 |
| `LICENSE` | MIT |

教材、harness、範例全部在各自的分支上，這裡刻意不放，避免和分支內容不同步。

---

## 貢獻

改動請提到對應的線上，不要提到 `main`：

- 只影響定義線 → 從 `sdd-lite` 開分支
- 只影響 Antigravity → 從 `antigravity` 開分支
- 只影響 Claude Code → 從 `claude` 開分支
- 只影響工程線 → 從 `progressive-sdd` 開分支
- 多條線都要改（例如 `.githooks/`）→ 分別提 PR，不要嘗試 cherry-pick 整個 harness

`main` 只接受導覽頁本身的修改。

---

MIT License。工具行為以各自的官方文件為事實來源；教材中每條事實都標了證據等級，未經實測的一律標明。
