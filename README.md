# Progressive SDD：跟著 AI 做出一套真的能上線的系統

這條線和另外兩條不一樣。

`claude` 與 `antigravity` 兩條線教的是**工具怎麼用** —— 照著貼、看到綠燈、往下一章。那是必要的第一步，但走完之後你會發現一件事：**你學會了操作 agent，但沒學會怎麼開發軟體。**

這條線補的就是那一段。

---

## 這門課要解決什麼

AI 能一次生出幾百行程式碼。速度不再是瓶頸，**判斷**才是。

而判斷沒辦法照著腳本學。所以這門課不給你 prompt 貼，改成兩件事：

1. **心法**：七條不變量 + 一套判斷「什麼時候該把東西固化下來」的規則
2. **一個真的系統**：從一句話的想法，做到能部署、有排程、有前後端與資料庫的東西

中間你會親手違反每一條不變量，然後修回來。**那個修回來的過程就是這門課。**

---

## 兩冊

| | 檔案 | 時間 | 內容 |
|---|---|---|---|
| 第一冊 | [`PRINCIPLES.md`](./PRINCIPLES.md) | 約 40 分鐘 | 心法。七條不變量、四個 Mode、什麼時候該固化 |
| 第二冊 | [`BUILD.md`](./BUILD.md) | 多次 session | 實戰。CookCard，五個關卡 |

第一冊先讀完再進第二冊。它很短，而且第二冊每一關都會回頭引用它。

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
| **失敗會現形** | 抽出來的食譜照著做會不會成功 —— 你自己就能驗 |

技術面會涵蓋前端、後端、資料庫、多模態模型、容器化與排程自動化。但**這些是題目自己長出來的需求，不是為了教而塞進去的**。

素材全部來自網路，中文料理影片無限量。詳見 [`docs/FIXTURES.md`](./docs/FIXTURES.md)。

---

## 開始之前

```bash
git clone https://github.com/Zenobia000/SDD-agent-coding-beginner.git
cd SDD-agent-coding-beginner
git switch progressive-sdd
git config core.hooksPath .githooks
```

`core.hooksPath` 是每個 clone 各自的設定，沒設就等於 `.githooks/` 完全沒作用。確認一下：

```bash
git config core.hooksPath
```

必須印出 `.githooks`。

**這門課不指定 coding agent。** Claude Code、Antigravity、Cursor 都可以，甚至不用 agent 純手寫也能跑完 —— 因為教的是判斷，不是操作。想先熟悉工具本身，去 [`claude`](../../tree/claude) 或 [`antigravity`](../../tree/antigravity) 分支。

技術選型也不預先指定。**選型本身就是第二冊的一關**，先告訴你答案就沒得練了。

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

先走完任一條工具線再來這裡，會順很多 —— 你至少要能讓 agent 跑起來。但不是硬性前置。

---

## 目前進度

| 項目 | 狀態 |
|---|---|
| `PRINCIPLES.md` 心法篇 | ✅ 完成 |
| `BUILD.md` 實戰篇（五關） | ✅ 完成 |
| `docs/FIXTURES.md` 素材挑選準則 | ✅ 完成 |
| `curriculum/README.md` 講師手冊 | ✅ 完成 |
| **Fixture 影片實際挑選與下載** | ⬜ **開課前必做** —— 六支影片的 URL、`expected.json` 內容 |
| 參考實作 | ⬜ 刻意不做（見 `BUILD.md` 附錄） |

`BUILD.md` 的驗收訊號有幾條假設了 fixture 已就位（例如 `fixtures/baseline/`）。fixture 挑好之前，那些命令跑不起來 —— 這是已知狀態，不是 bug。

---

MIT License。
