# 這個 repo 怎麼工作

> 給在這個 repo 上工作的 coding agent。
>
> **Claude Code 讀 `CLAUDE.md` 而不是這一份**（官方明文）。要用 Claude Code 的話，
> 建一個 `CLAUDE.md`，第一行寫 `@AGENTS.md`，其餘留空即可 —— 兩份都要改的重複維護不值得。

---

## 這是什麼

一門課的教材：**4 天規格驅動 × AI 開發實戰營**，題目是 LeaveBot（一句話請假）。
學員來自不同職位（PM、SA、主管、初學工程師），混班分兩軌上課。

> **如果你是學員專案裡的 agent**（工作目錄在 `4-starter/` 或學員自己的專案資料夾）：
> 以那個目錄的 `AGENTS.md` / `CLAUDE.md` 為準，這一份是給維護教材的人看的。

| 檔案 | 角色 |
|---|---|
| `README.md` | **唯一入口**。適合誰、從哪裡開始 |
| `0-setup/` | 課前環境檢核表 |
| `1-bootcamp/` | 4 天課表、題目 `LEAVEBOT.md`、自主期任務 |
| `2-templates/` | 規格模板、`AGENTS.md` 範本、範本 hook |
| `3-playbook/` | Prompt 魔法書、排解檢索表、防呆檢核表、導入評估表 |
| `4-starter/` | Starter 專案。只有骨架，**不准加入請假業務邏輯**。改動後 `pytest` 要全綠 |
| `5-casebook/` | 企業系統補充教材（建置中） |
| `advanced/cookcard/` | 進階選修 CookCard（原本的七站教材，教法不同，見下） |
| `instructor/` | 講師手冊。4 天版是 `BOOTCAMP.md` |
| `docs/SKILL-MAP.md` | 技能速查。`scripts/check-skill-map.sh` 綁這個路徑，**不要搬** |
| `.claude/skills/` | 本專案的工具鏈，36 個技能。**可以改**，見該目錄的 `README.md` |
| `.agents/skills` | 指向 `.claude/skills` 的 symlink，給 Codex 讀 |
| `THIRD-PARTY-NOTICES.md` | 上游授權聲明。**MIT 的要求，不要移除** |

學生入口只有一個：根目錄 `README.md`，然後照資料夾編號往下走。
**根目錄不要再新增教材檔**，新內容放進對應的編號資料夾。

---

## 主線教材的設計原則

主線以企業工作坊的形式為準：**給模板、給提示詞、給 Starter**。學員背景差異大，
沒有這些，一半的人會卡在空白頁。但給了之後，每一份都要守住下面四條，
否則課程會退化成照貼照跑。

### 1. 提示詞要附「你要自己改的地方」

每一段參考提示詞都要讓學員知道哪裡要換成自己的內容，並在提示詞裡示範
「限制 AI 的範圍」與「不要替我決定」這類句子。不要給一段貼上就能完成整個單元的提示詞。

### 2. 每個單元都要有學員自己能跑的通過訊號

通過訊號是**可以檢查的事**（檔案存在、指令跑得起來、測試是綠的、別人判斷得了），
不是「你應該會看到這個畫面」。

### 3. 給選項與取捨；只有在課程需要一致性時才直接決定

Starter 的技術棧（FastAPI + SQLite + pytest）直接決定，因為 4 天沒有時間選型。
但「哪些交給 AI、哪些寫成規則」「準確率多少才能上線」這類判斷，**教材只列取捨，答案留給學員**。

### 4. Starter 只給骨架，不給業務邏輯

`4-starter/` 可以有 app 骨架、資料庫連線、測試框架、假 LLM。
**請假的業務邏輯（解析、規則、核准）不能出現在 Starter 裡**，那是學員要讓 AI 寫、自己驗的部分。

### 混班兩軌

每個單元都要同時寫「規格軌做什麼」與「工程軌做什麼」。只寫一軌，另一軌的學員就會變成旁觀者。

### 進階選修 CookCard 的教法不同

`advanced/cookcard/` 保留原本的教法：**不給可貼的 prompt、不給選型答案、不做參考實作**，
站點可以跳過、順序可以亂。改那一區時沿用它自己的規矩，不要套用主線的原則。

---

## 事實與證據

- 教材裡的每條事實都要能回查來源。查不到就標「⚠️ 未驗證」，**不要推測後寫成肯定句**。
- 「跑起來會怎樣」的宣稱，只有實際跑過才能寫成已驗證。
- CookCard 的 `expected.json` 尚未完成，因此 `advanced/cookcard/BUILD.md` 的部分通過訊號目前跑不起來。這是已知狀態，`advanced/cookcard/README.md` 有標。
- LeaveBot 的「好日子科技」規章是**課堂假設**，不是勞動法規。教材引用真實法規時要附來源。

---

## 工具鏈

`.claude/skills/` 的 36 個技能是**本專案自己的工具鏈**，衍生自
[luca-skills](https://github.com/Luca0x5755/luca-skills)（MIT，commit `1434be8`）並已修改。

### 技能可以改，但有三條規矩

1. **`docs/SKILL-MAP.md` 要同步。** 教材靠那張表指路，改了技能沒改表，學生會照著找不到的東西操作。
2. **frontmatter 前不能有任何字元**，包括空行 —— 多一個空行整個技能會被靜默略過。
3. **`name` 必須等於資料夾名。**

已做過的修改列在 `.claude/skills/README.md`。要同步上游修正的話那裡也有 diff 指令 ——
已經分岔了，不會是無痛合併。

### 授權：可以改，不可以拿掉聲明

MIT 要求 copyright notice 與 permission notice 保留在所有副本與實質部分中。
所以可以改內容、改名、重組，但 **`THIRD-PARTY-NOTICES.md` 不能刪**。
這個 repo 是公開的，拿掉聲明就是授權違規。

### 支援 Claude Code 與 Codex，Copilot / Antigravity 有落差

技能用 `disable-model-invocation` 區分「使用者觸發」與「模型觸發」。

- **Codex**：透過 `.agents/skills → ../.claude/skills` symlink 讀同一份技能，用 `$技能名` 呼叫。
  Codex 不認 `disable-model-invocation`，對應設定是每個使用者觸發技能的
  `agents/openai.yaml`（`policy.allow_implicit_invocation: false`）。
  **新增或改動使用者觸發技能時兩邊都要改**，`scripts/check-codex-skills.sh` 會擋不同步。
- **Antigravity 與 Copilot**：不支援這個欄位，編排型技能會被 agent 自行啟動。
  教材已在 `docs/SKILL-MAP.md` 標明這個落差，不要淡化它。

### 技能放在 repo 裡，不用安裝

技能直接放在 `.claude/skills/`（攤平，無 `core`/`draft` 中間層）。**fork 下來打開 Claude Code 或 Codex 就可用**，不需要跑上游的 `install.sh`。

學員的專案蓋在 fork 的**子目錄**裡（LeaveBot 從 `4-starter/` 複製，CookCard 在 `cookcard/`）。Claude Code 與 Codex 都會從啟動目錄一路往上找到 repo 根的技能，所以在子目錄啟動一樣吃得到。

不要為了「乾淨」把技能搬走或改成 submodule —— 上課現場多一個下載步驟就會有人卡住，這是刻意的取捨。

`.githooks/` 是 Git 層的防護，與 agent 無關，兩者不衝突。

---

## 工程規範

### 分支

- `main` 是導覽頁，只接受導覽頁本身的修改
- 這條線的改動從 `progressive-sdd` 開分支
- **不要**把這條線的內容 cherry-pick 到 `claude` 或 `antigravity`，三條線的教法不同

### 不要動

`LICENSE`、`.githooks/`、`.gitattributes` 除非改動本身就是為了它們。

### Commit

Conventional Commits。Body 三段：WHY（動機）／WHAT（決策與取捨，不要重複 diff）／IMPACT（影響範圍、破壞性變更）。

### 品質檢查

```bash
bash -n .githooks/pre-commit .githooks/pre-push   # git hooks 語法，有錯才有輸出
bash scripts/check.sh                             # 全部檢查：連結、技能、Codex 設定、hook 測試
```

`check.sh` 會自動找出 `scripts/check-*.sh` 與所有 hook 測試，逐項印 ✓／✗。`4-starter/` 加入後，它的 `pytest` 也要全綠。

`check-links.sh` 以**檔案所在目錄**解析相對路徑，並略過 `http*`、錨點與 GitHub 的
`../../tree/<branch>` 分支連結 —— 那三類不是本地檔案，用一般寫法檢查會誤報。
會誤報的檢查比沒有檢查更糟，因為人會學會忽略它。

未來加入 fixture 之後，再補 `expected.json` 的 schema 驗證。

---

## 回覆方式

- 繁體中文，技術術語保留英文
- 結論先行，只保留一條主要建議
- 區分**已確認**、**主要假設**與**未知**，不要把推測寫成根因
- 主線教材可以給模板與提示詞，但每份都要標出「學員要自己判斷的地方」與通過訊號
- 用台灣慣用語（例如 tracer bullet 寫「垂直切片」，不寫「曳光彈」）

---

## 安全底線

- 不硬編碼任何金鑰。fixture 的來源 URL 可以進版控，API 金鑰不行
- 教材裡示範 prompt injection 時，用自製的測試句子或字幕，不要指向真實影片或真實員工資料
- 不要在教材中重新發布完整影片檔，只保留課堂教學所需的最小重現素材
