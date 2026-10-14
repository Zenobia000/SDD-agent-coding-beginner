# AI Coding Agent 工程實戰課

這門課教的不是「怎麼跟 AI 聊天」，而是**怎麼用 AI 做出可驗證、可 review、可交付的軟體**。

**這個分支只負責導航，教材在下面的分支與 repo 上。**

---

## 三個層級

```text
第零層  想清楚要做什麼      sdd-lite                     不寫 code，用 no-code 平台
                                    ↓
第一層  學會操作工具        leavebot-bootcamp（repo）    Claude Code ／ Codex，4 天實戰營
                                    ↓
第二層  學會開發軟體        progressive-sdd              完整工具鏈，帶回自己的專案
```

### 第零層：定義線（不需要任何前置知識）

| 分支 | 教材 | 題目 | 特色 |
|---|---|---|---|
| [`sdd-lite`](../../tree/sdd-lite) | `DEFINE.md`（八站） | **SubTrim**（訂閱瘦身） | **一行 code 都不寫**，不用裝任何東西 |

給 Lovable、Bolt、Replit、Google AI Studio 這類 **no-code 造原型平台**的使用者。教的是**在你按下 Generate 之前，腦袋裡該先發生什麼事**。

八站從「一句抱怨」走到「可執行規格」：逼問痛點 → 種子簡報 → meta-prompt 逼出歧義 → **PRD → SRS → SAD** → 餵進平台並逐條驗收。三份文件俗稱 SDD 的簡易版。

⚠️ 這條線**只到 POC / MVP demo**。no-code 平台生出來的東西不能當正式產品上線 —— 為什麼、以及分界線在哪，寫在該分支的 `docs/TIERS.md`。

### 第一層：實戰營（入門）

| repo | 工具 | 題目 | 特色 |
|---|---|---|---|
| [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp) | **Claude Code ＋ Codex**，兩邊共用同一套技能 | **LeaveBot**（一句話請假） | 只帶上課用的 6 個技能與護欄，講義在 OneDrive |

4 天加自主期，混班上課：PM、SA、主管寫規格、審 AI 產出，工程師用 agent 實作。從需求、架構、拆票走到 TDD 與 AI 功能的驗收（eval、prompt injection）。

舊的 `claude` 與 `antigravity` 工具線已封存為 `archive/claude`、`archive/antigravity` tag，不再維護。

### 第二層：工程線（進階）

| 分支 | 內容 | 特色 |
|---|---|---|
| [`progressive-sdd`](../../tree/progressive-sdd) | `curriculum/` 講義原稿、38 個工程技能 | **完整工具鏈內建、fork 即用** |

實戰營的教材源頭，也是結訓後的武器庫：上課 repo 只帶 6 個技能，這裡有全部 38 個，Claude Code 用 `/技能名`、Codex 用 `$技能名`。

進階選修 **CookCard**（把料理影片變成能照著做的結構化食譜卡）也在這裡：七站、不給答案，會長出前端、後端、資料庫、多模態抽取、容器化與排程。

---

## 怎麼選

| 你的情況 | 去哪 |
|---|---|
| 不寫程式，但想把想法變成能用的東西 | `sdd-lite` |
| 在 Lovable / Bolt / Replit / AI Studio 上改到第二十次還是不對 | `sdd-lite` —— 問題八成不在平台，在輸入 |
| 想學怎麼寫 PRD / SRS / SAD | `sdd-lite` |
| 沒用過 coding agent，或要帶團隊導入 | `leavebot-bootcamp` |
| 會操作 agent 了，但不確定自己會不會「開發軟體」 | `progressive-sdd` |
| 覺得照著貼很順，但沒有一個決定是自己做的 | `progressive-sdd` |
| 只有無圖形介面的 Linux 主機（SSH） | `leavebot-bootcamp` 或 `progressive-sdd`，Claude Code 與 Codex 都是 CLI |
| 想要一套現成的工程技能可以帶去自己的專案 | `progressive-sdd` —— 38 個技能就在 `.claude/skills/`，MIT |

`progressive-sdd` 是 `leavebot-bootcamp` 之後難度上的下一階。

`sdd-lite` 不在這條難度軸上 —— 它教的是**上游**，走完之後接實戰營或工程線都可以，不接也行。

---

## 三分鐘開始

```bash
# 實戰營：獨立 repo，clone 下來就是上課要寫的專案
git clone https://github.com/Zenobia000/leavebot-bootcamp.git

# 定義線與工程線：這個 repo 的分支
git clone https://github.com/Zenobia000/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner
git switch sdd-lite           # 定義線：no-code 平台，不寫 code
# 或
git switch progressive-sdd    # 工程線：完整工具鏈
```

切過去之後**先讀該處的 `README.md`**，它會告訴你安裝什麼、從哪一章開始。

`sdd-lite` 連 clone 都不需要 —— 直接在 GitHub 網頁上讀 [`DEFINE.md`](../../blob/sdd-lite/DEFINE.md) 就能走完。

---

## 為什麼這樣分

- **實戰營是獨立 repo**：學員 clone 下來就是要寫的專案，只看得到上課用的 6 個技能。專案在 repo 根目錄，Claude Code 的護欄（guard hooks）才會生效 —— 放在子目錄時，Claude Code 不套用 repo 根的 hooks。
- **Claude Code 與 Codex 共用一套技能**：Codex 透過 `.agents/skills → .claude/skills` symlink 讀同一份，「只准使用者觸發」的設定兩邊各寫一份，由檢查腳本擋不同步。所以不再需要每個工具一條分支。
- **`sdd-lite` 另成一條線**：它的讀者不裝任何東西。沒有 CLI、沒有 harness、不需要會 git，教材裡出現一次終端機指令，那條線的讀者就走掉一半。

⚠️ 技能依賴「只准使用者觸發」的設定，**Antigravity、Copilot 都不認**（Cursor 未驗證），編排型技能會被 agent 自己啟動。因此目前只支援 Claude Code 與 Codex，落差寫在 `progressive-sdd` 的 `docs/SKILL-MAP.md`。

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
- 只影響實戰營的專案、技能或題目 → 提到 [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)
- 只影響講義或完整工具鏈 → 從 `progressive-sdd` 開分支
- 多條線都要改（例如 `.githooks/`）→ 分別提 PR，不要嘗試 cherry-pick 整個 harness

`main` 只接受導覽頁本身的修改。

---

MIT License。工具行為以各自的官方文件為事實來源；教材中每條事實都標了證據等級，未經實測的一律標明。
