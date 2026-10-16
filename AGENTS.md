# 這個 repo 怎麼工作

> 給在這個 repo 上工作的 coding agent。
>
> **Claude Code 讀 `CLAUDE.md` 而不是這一份**（官方明文）。要用 Claude Code 的話，
> 建一個 `CLAUDE.md`，第一行寫 `@AGENTS.md`，其餘留空即可 —— 兩份都要改的重複維護不值得。

---

## 這是什麼

一門課的教材：**4 天規格驅動 × AI 開發實戰營**，題目是 LeaveBot（一句話請假）。
學員來自不同職位（PM、SA、主管、初學工程師），混班分兩軌上課。

> 上課用的專案在另一個 repo [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp)，它有自己的 `AGENTS.md`。
> 這一份是給維護講義原稿的人看的。學員的專案（LeaveBot、CookCard）都在各自的 repo，以那邊的 `AGENTS.md` 為準。

| 檔案 | 角色 |
|---|---|
| `README.md` | **唯一入口**。適合誰、從哪裡開始 |
| `curriculum/` | **講義原稿**，底下依編號排。用 `scripts/export-handout.sh` 打包成 OneDrive 講義 |
| `curriculum/0-setup/` | 課前環境檢核表 |
| `curriculum/1-bootcamp/` | 4 天課表、自主期任務（題目 `LEAVEBOT.md` 在上課 repo） |
| `curriculum/1-workshop/` | 2 天工作坊：只寫怎麼排、砍什麼、通過訊號，內容連回 4 天版的單元。**同一份內容只寫在 4 天版** |
| `curriculum/3-playbook/` | Prompt 魔法書、排解檢索表、防呆檢核表、導入評估表 |
| [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp) | **另一個 repo**：上課用的 Starter、題目 `LEAVEBOT.md`、規格模板 `templates/`、6 個技能。只有骨架，**不准加入請假業務邏輯** |
| `curriculum/4-casebook/` | 企業系統補充教材：七個系統，固定六段結構 |
| `curriculum/advanced/cookcard/` | 進階選修 CookCard（原本的七站教材，教法不同，見下） |
| `curriculum/instructor/` | 講師手冊。4 天版是 `BOOTCAMP.md` |
| `.codex/hooks.json` | Codex 的 hook 登記。腳本仍是 `.claude/hooks/`，Codex 不讀 `settings.json` |
| `THIRD-PARTY-NOTICES.md` | 上游授權聲明。**MIT 的要求，不要移除** |

學生入口只有一個：根目錄 `README.md`，然後進 `curriculum/` 照編號往下走。
**講義相關的一切都放 `curriculum/`**，根目錄只留入口、agent 規則、授權與工具鏈。新內容放進對應的編號資料夾。
**agent 要用 `@` 讀的檔案**（題目、規格模板、程式骨架）放上課 repo，不放這裡 —— 講義包裡的檔案，學員專案裡的 agent 讀不到。

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

`leavebot-bootcamp` 可以有 app 骨架、資料庫連線、測試框架、假 LLM。
**請假的業務邏輯（解析、規則、核准）不能出現在 Starter 裡**，那是學員要讓 AI 寫、自己驗的部分。

### 混班兩軌

每個單元都要同時寫「規格軌做什麼」與「工程軌做什麼」。只寫一軌，另一軌的學員就會變成旁觀者。

### 進階選修 CookCard 的教法不同

`curriculum/advanced/cookcard/` 保留原本的教法：**不給可貼的 prompt、不給選型答案、不做參考實作**，
站點可以跳過、順序可以亂。改那一區時沿用它自己的規矩，不要套用主線的原則。

---

## 事實與證據

- 教材裡的每條事實都要能回查來源。查不到就標「⚠️ 未驗證」，**不要推測後寫成肯定句**。
- 「跑起來會怎樣」的宣稱，只有實際跑過才能寫成已驗證。
- CookCard 的 `expected.json` 尚未完成，因此 `curriculum/advanced/cookcard/BUILD.md` 的部分通過訊號目前跑不起來。這是已知狀態，`curriculum/advanced/cookcard/README.md` 有標。
- LeaveBot 的「好日子科技」規章是**課堂假設**，不是勞動法規。教材引用真實法規時要附來源。

---

## 工具鏈：技能不在這個 repo

技能的唯一源頭是模板 repo [`agent-skills-starter`](https://github.com/Zenobia000/agent-skills-starter)（38 個技能，衍生自
[luca-skills](https://github.com/Luca0x5755/luca-skills)，MIT）。
上課 repo [`leavebot-bootcamp`](https://github.com/Zenobia000/leavebot-bootcamp) 帶的是其中 6 個的精簡改寫版。**這個 repo 只放講義，不放技能。**

| 要改的是 | 去哪改 |
|---|---|
| 某個技能本身 | `agent-skills-starter`，改完那邊跑 `bash scripts/check.sh` |
| 上課用的 6 個技能 | `leavebot-bootcamp`。上游有修正時手動搬過去，兩邊已經分岔 |
| 講義裡提到技能的地方（例如 CookCard 的 `SKILL-MAP.md`） | 這裡。模板的技能改名或增刪時回來對一次，**沒有腳本自動擋** |

這裡還留著的工具：

- `.claude/hooks/` 的兩支 guard，Claude Code 登記在 `.claude/settings.json`，Codex 登記在 `.codex/hooks.json`。
  `scripts/check-hooks.sh` 擋兩邊登記不同步；guard 的回歸規格是同目錄的 `test-*.sh`。
  guard 衍生自 luca-skills，所以 **`THIRD-PARTY-NOTICES.md` 不能刪**。
- `.githooks/` 是 Git 層的防護，與 agent 無關，兩者不衝突。

Antigravity 與 Copilot 不支援「只准使用者觸發」，編排型技能會被 agent 自行啟動。教材提到工具支援時，不要淡化這個落差。

---

## 工程規範

### 分支

- `main` 是課程首頁與講義原稿，也是預設分支。改動從 `main` 開分支、走 PR
- 一個分支只做一件事，合併後刪掉。**不要再開長期分支當另一條課程線** —— 另一群讀者就另開 repo
- 舊的 `claude`、`antigravity`、`progressive-sdd`、`sdd-lite` 線封存成 `archive/*` tag，不要復活成分支

### 不要動

`LICENSE`、`.githooks/`、`.gitattributes` 除非改動本身就是為了它們。

### Commit

Conventional Commits。Body 三段：WHY（動機）／WHAT（決策與取捨，不要重複 diff）／IMPACT（影響範圍、破壞性變更）。

### 品質檢查

```bash
bash -n .githooks/pre-commit .githooks/pre-push   # git hooks 語法，有錯才有輸出
bash scripts/check.sh                             # 全部檢查：連結、guard 登記、hook 測試
```

`check.sh` 會自動找出 `scripts/check-*.sh` 與所有 hook 測試，逐項印 ✓／✗。

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
