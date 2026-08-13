# 這個 repo 怎麼工作

> 給在這個 repo 上工作的 coding agent。
>
> **Claude Code 讀 `CLAUDE.md` 而不是這一份**（官方明文）。要用 Claude Code 的話，
> 建一個 `CLAUDE.md`，第一行寫 `@AGENTS.md`，其餘留空即可 —— 兩份都要改的重複維護不值得。

---

## 這是什麼

一門課的教材，**不是應用程式**。這個分支裡沒有產品原始碼，也不會有。

| 檔案 | 角色 |
|---|---|
| `PRINCIPLES.md` | 第一冊：心法。七條不變量與四個 Mode |
| `BUILD.md` | 第二冊：實戰。CookCard 九個站點 |
| `docs/SKILL-MAP.md` | 技能速查：哪一站用哪個、什麼時候跳過 |
| `docs/FIXTURES.md` | 素材挑選準則（講師用） |
| `curriculum/README.md` | 講師手冊 |
| `.claude/skills/` | luca-skills 的**凍結副本，不要改**。見該目錄的 `README.md` |
| `THIRD-PARTY-NOTICES.md` | 上述副本的授權聲明。動 `.claude/skills/` 就要同步檢查 |

學生路線固定：`README.md` → `PRINCIPLES.md` → `BUILD.md`。**不要新增替代路線。**

---

## 這門課的設計原則，改教材時必須遵守

這四條是這條線和另外兩條線的根本差別。違反其中任一條，等於把這門課退化成照貼照跑。

### 1. 不給可以直接貼的 prompt

另外兩條線給。這裡不給。判斷不能照著腳本學。

### 2. 不給「你應看到」的螢幕輸出

只給**學生自己能跑的通過訊號**。學生要自己定義什麼叫對。

### 3. 不給選型答案

VLM vs STT、SQLite vs Postgres、cron vs queue —— 全部留給學生決定。
教材只列取捨，不列建議。

### 4. 不做參考實作

有參考實作，學生就會照抄。這條寫在 `BUILD.md` 附錄，是對學生的承諾。

---

## 站點不是章節

`BUILD.md` 的九個站點**順序可以亂，而且大部分可以跳過**。每一站都有「什麼時候跳過這一站」那一段 —— **那是全書最重要的內容**。

`.claude/skills/README.md` 有一張主流程表，看起來像一條線。**那是預設路徑，不是規定。** 教材教的是什麼時候偏離它。

改教材時如果你把某一站寫成「必須先完成前一站才能開始」，或刪掉「什麼時候跳過」那一段，就是把它改回流水線了 —— 那正是這條線存在的理由所要避開的東西。

---

## 事實與證據

- 教材裡的每條事實都要能回查來源。查不到就標「⚠️ 未驗證」，**不要推測後寫成肯定句**。
- 「跑起來會怎樣」的宣稱，只有實際跑過才能寫成已驗證。
- fixture 尚未挑選，因此 `BUILD.md` 的部分通過訊號目前跑不起來。這是已知狀態，README 有標。

---

## 工具鏈

這門課用 [luca-skills](https://github.com/Luca0x5755/luca-skills) 當工具鏈，凍結副本在 `.claude/skills/`。

### 不要改 vendored 的檔案

`.claude/skills/` 是**未修改的凍結副本**。改了它，你就從使用者變成維護一份分支：上游修 bug 合不回來，而教材會同時對不上兩邊。

要更新的話照 `.claude/skills/README.md` 的步驟整包重抓，**並且同步檢查 `docs/SKILL-MAP.md` 提到的每個技能還在不在、描述有沒有變**。

### 這條線實質是 Claude Code / Copilot 取向

luca-skills 依賴 `disable-model-invocation` 來區分「使用者觸發」與「模型觸發」的技能。
**Antigravity 與 Copilot 都不支援這個欄位**，編排型技能會被 agent 自行啟動。
教材已在 `docs/SKILL-MAP.md` 標明這個落差，不要淡化它。

### 技能放在 repo 裡，不用安裝

技能直接放在 `.claude/skills/`（攤平，無 `core`/`draft` 中間層）。**fork 下來打開 Claude Code 就可用**，不需要跑上游的 `install.sh`。

學生的 CookCard 蓋在 fork 的 `cookcard/` **子目錄**裡。Claude Code 的專案技能會從啟動目錄一路往上找到 repo 根，所以在子目錄啟動一樣吃得到。

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

這個分支沒有程式碼，所以檢查只有兩項：

```bash
bash -n .githooks/pre-commit .githooks/pre-push   # git hooks 語法
bash scripts/check-links.sh                       # 相對連結目標存在
```

兩條都必須無輸出（`bash -n` 只在有錯時輸出）。

`check-links.sh` 以**檔案所在目錄**解析相對路徑，並略過 `http*`、錨點與 GitHub 的
`../../tree/<branch>` 分支連結 —— 那三類不是本地檔案，用一般寫法檢查會誤報。
會誤報的檢查比沒有檢查更糟，因為人會學會忽略它。

未來加入 fixture 之後，再補 `expected.json` 的 schema 驗證。

---

## 回覆方式

- 繁體中文，技術術語保留英文
- 結論先行，只保留一條主要建議
- 區分**已確認**、**主要假設**與**未知**，不要把推測寫成根因
- 教材內容優先給「學生要自己決定什麼」與「通過條件」，不要給答案

---

## 安全底線

- 不硬編碼任何金鑰。fixture 的來源 URL 可以進版控，API 金鑰不行
- 教材裡示範 prompt injection 時，用的必須是自製的測試字幕，不要指向真實影片
- 不要在教材中重新發布完整影片檔，只保留課堂教學所需的最小重現素材
