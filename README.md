# AI Coding Agent 工程實戰課

這門課教的不是「怎麼跟 AI 聊天」，而是**怎麼用 AI coding agent 做出可驗證、可 review、可交付的軟體**。

同一套工程紀律，兩個工具各一條線。**這個分支只負責導航，教材在下面兩條線上。**

---

## 選一條線

| 分支 | 工具 | 第一冊 | 專案契約 | Harness |
|---|---|---|---|---|
| [`antigravity`](../../tree/antigravity) | **Google Antigravity**（`agy` CLI + IDE） | `ANTIGRAVITY.md` | `AGENTS.md` | `.agents/` |
| [`claude`](../../tree/claude) | **Claude Code** | `CLAUDE-CODE.md` | `CLAUDE.md` | `.claude/` |

兩條線的第二冊都是 `BUILD.md`，題目相同：**SmartTrip FX** —— 讀取行程 JSON，驗證輸入、計算旅費現金與匯率燈號，只用 Python standard library。差別只在你用哪個 agent 完成它。

```bash
git clone https://github.com/Zenobia000/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner

git switch antigravity     # 走 Antigravity 線
# 或
git switch claude          # 走 Claude Code 線
```

切過去之後**先讀該分支的 `README.md`**，它會告訴你安裝什麼、從哪一章開始。

---

## 怎麼選

| 你的情況 | 建議 |
|---|---|
| 已經有 Google 帳號，想留在 Google 生態系 | `antigravity` |
| 已經在用 Claude Code，或有 Anthropic 訂閱 | `claude` |
| 兩個都沒有，想先試一個 | `antigravity` —— CLI 是單一執行檔，不需要 Node.js 或任何套件管理器 |
| 只有無圖形介面的 Linux 主機（SSH） | 兩條線都可以，但都只能走 CLI；Antigravity IDE 需要桌面環境 |

沒有哪一條比較「進階」。元件模型不同，工程紀律相同。

---

## 為什麼要分成兩個分支

不是為了整齊，是因為**技術上無法共存**：

- Antigravity 只探索 `.agents/`（`agy` 執行檔內完全沒有 `.claude` 路徑字串）
- Claude Code 只讀 `.claude/`，且官方明文**不讀** `AGENTS.md`
- 兩者的 hook 阻擋協定不同，skill frontmatter 的可用欄位也不同

硬要塞進同一個分支，結果是兩份會各自腐爛的設定，加上一本必須不斷加註「如果你用 A 就…如果你用 B 就…」的教材。分支切開之後，每一條線的教材都能直述，不必到處分岔。

---

## 這個分支有什麼

只有導航與共用的東西：

| 路徑 | 用途 |
|---|---|
| `README.md` | 就是這一頁 |
| `.githooks/` | Git 層的安全閘門（擋真實 `.env`、疑似硬編碼憑證、對保護分支的非快轉 push）。兩條線共用 |
| `LICENSE` | MIT |

教材、harness、範例全部在 `antigravity` 與 `claude` 分支上，這裡刻意不放，避免和分支內容不同步。

---

## 貢獻

改動請提到對應的線上，不要提到 `main`：

- 只影響 Antigravity → 從 `antigravity` 開分支
- 只影響 Claude Code → 從 `claude` 開分支
- 兩條線都要改（例如 `.githooks/`、SmartTrip FX 的需求規格）→ 分別提兩個 PR，不要嘗試 cherry-pick 整個 harness

`main` 只接受導航頁本身的修改。

---

MIT License。第一冊的工具行為以各自的官方文件為事實來源；教材中每條事實都標了證據等級，未經實測的一律標明。
