# Progressive SDD：拿到一個新題目，從零到上線

這條線和另外兩條不一樣。

`claude` 與 `antigravity` 兩條線教的是**工具怎麼用** —— 照著貼、看到綠燈、往下一章。那是必要的第一步，但走完之後你會發現一件事：**你學會了操作 agent，但沒學會怎麼開發軟體。**

這條線補的就是那一段：**拿到一個新題目，怎麼拆解問題、拆解功能、建構系統，一路到部署上線。**

---

## Fork 下來就能用

工具箱已經在 repo 裡，**不用安裝任何東西**。

```bash
# fork 這個 repo，然後
git clone https://github.com/<你的帳號>/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner
git switch progressive-sdd
git config core.hooksPath .githooks
claude
```

打 `/compass`。看得到技能清單就成功了。

---

## 兩冊

| | 檔案 | 時間 | 內容 |
|---|---|---|---|
| 第一冊 | [`PRINCIPLES.md`](./PRINCIPLES.md) | 約 40 分鐘 | 心法。七條不變量、四個 Mode、什麼時候該固化 |
| 第二冊 | [`BUILD.md`](./BUILD.md) | 多次 session | 實戰。CookCard，七個站點 |

第一冊先讀完再進第二冊。它很短，而且第二冊每一站都會回頭引用它。

隨時可查：[`docs/SKILL-MAP.md`](./docs/SKILL-MAP.md) —— 哪一站用哪個技能、什麼時候可以跳過。

---

## 工具箱

36 個給 coding agent 用的工程技能，就在 [`.claude/skills/`](./.claude/skills/)。**它們是這個專案的一部分，可以改** —— 衍生自 [luca-skills](https://github.com/Luca0x5755/luca-skills)（MIT，聲明見 [`THIRD-PARTY-NOTICES.md`](./THIRD-PARTY-NOTICES.md)）。

覆蓋的範圍：

```text
/setup-skills → /grilling → /domain-modeling → /to-spec → /feasibility
  → /to-architecture → /frontend-spec → /test-blueprint → /to-tickets
  → /implement（含 /tdd、/code-review）→ /uat-cases → /browser-evidence
  → /wizard → /git-commit → /git-pr → /git-release
```

⚠️ **這條線實質是 Claude Code / Copilot 取向。** 技能用 `disable-model-invocation` 區分「只有你能叫」與「agent 也能叫」的技能，**Antigravity 與 Copilot 都不支援這個欄位** —— 在那兩邊，編排型技能會被 agent 自己啟動。落差寫在 `docs/SKILL-MAP.md`，沒有淡化。

---

## 專案：CookCard

> **把料理影片變成可以照著做的結構化食譜卡。**

痛點很小白：看 YouTube 學做菜，你得一直暫停、倒帶、記份量，做到一半忘記蒜末是兩瓣還是三瓣。

為什麼選這題當教材：

| 這題會逼你面對 | 具體長什麼樣 |
|---|---|
| **需求真的有歧義** | 「一把蔥」怎麼結構化？「適量」怎麼存？影片根本沒說份量怎麼辦？沒有標準答案 |
| **多模態是必要的，不是裝飾** | 份量常常只打在畫面字卡上，語音沒念。純語音轉文字一定做不出可用的食譜卡 |
| **有不可逆決定** | 食譜 schema。存了 80 份之後要加欄位，你得自己面對遷移 |
| **有真實邊界** | 任意 YouTube URL、三小時長片、字幕裡的 prompt injection |
| **要選型** | VLM 一次到底，還是 STT + 抽幀 OCR 兩段式？要不要 vector DB？ |
| **值不值得做是真問題** | 市面上食譜 App 一堆，還有人直接把連結丟給 ChatGPT。你得誠實比較 |
| **失敗會現形** | 抽出來的食譜照著做會不會成功 —— 你自己就能驗 |

技術面會涵蓋前端、後端、資料庫、多模態模型、容器化與排程自動化。**但這些是題目自己長出來的需求，不是為了教而塞進去的。**

素材全部來自網路，中文料理影片無限量。詳見 [`docs/FIXTURES.md`](./docs/FIXTURES.md)。

---

## 你的專案蓋在 fork 裡面

```text
SDD-agent-coding-beginner/     ← 你 fork 的這個 repo
├── PRINCIPLES.md              ← 教材，讀的
├── BUILD.md                   ← 教材，讀的
├── .claude/skills/            ← 工具箱，不用管
└── cookcard/                  ← 你要蓋的東西，所有產出都在這裡
```

在 `cookcard/` 裡啟動 Claude Code 一樣吃得到根目錄的技能 —— 專案技能會從啟動目錄一路往上找到 repo 根。

---

## 這條線和另外兩條的關係

```text
claude / antigravity          progressive-sdd
  ─────────────────           ────────────────
  工具怎麼操作          →      軟體怎麼開發
  照著貼，看綠燈               自己判斷，自己驗
  SmartTrip FX（純函式）        CookCard（完整系統）
  4–5 小時                      多次 session
```

先走完任一條工具線再來這裡會順很多 —— 你至少要能讓 agent 跑起來。但不是硬性前置。

---

## 目前進度

| 項目 | 狀態 |
|---|---|
| `PRINCIPLES.md` 心法篇 | ✅ 完成 |
| `BUILD.md` 實戰篇（七站） | ✅ 完成 |
| `docs/SKILL-MAP.md` 技能速查 | ✅ 完成 |
| `docs/FIXTURES.md` 素材挑選準則 | ✅ 完成 |
| `curriculum/README.md` 講師手冊 | ✅ 完成 |
| `.claude/skills/` 工具箱（36 技能 + guard hooks） | ✅ 已內建，fork 即用 |
| `docs/assets/route.svg` 七站路線圖 | ✅ 完成 |
| **Fixture 影片實際挑選與下載** | ⬜ **開課前必做** —— 六支影片的 URL 與 `expected.json` |
| 參考實作 | ⬜ 刻意不做（見 `BUILD.md` 附錄） |

`BUILD.md` 有幾條通過訊號假設了 fixture 已就位（例如 `fixtures/baseline/`）。挑好之前那些命令跑不起來 —— 這是已知狀態，不是 bug。

---

MIT License。`.claude/skills/` 衍生自第三方，授權見 [`THIRD-PARTY-NOTICES.md`](./THIRD-PARTY-NOTICES.md)。
