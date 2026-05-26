---
name: explain-code
description: Use when the user asks "what does this do", "explain this code", "解釋這段", "白話講一下這個檔案", "幫我看懂這段", or wants to understand existing code. Explains code from an **architect's lens** (boundary / coupling / abstraction / tradeoff), uses **🟢🟡🔴 traffic-light signals** to mark design health, and acts as a **mentor**: names the techniques being used, surfaces the tradeoffs made, points to evolution paths under future load, and flags the theories the learner should study next. Goal: every explanation leaves behind a vocabulary the learner can search and discuss with others.
---

# Explain Code Skill — 架構師視角 × 紅綠燈 × 導師教學

> 核心信念：**「叫得出名字」才查得到、才能跟人討論、才能在下次自己用上**。
> 這個 skill 不只是「告訴你 code 在做什麼」，而是**像帶徒弟的資深工程師**那樣：
> 指出技術名稱、點明取捨、預示演化路徑、標出理論缺口。

---

## Phase 0：開場與範圍確認

開場固定講三句：

> 我用 `explain-code` skill 走解釋流程，會用「導師帶看」的方式：
> 點技術名 + 標紅綠燈 + 講權衡 + 給延伸思考 + 列你該補的理論。
>
> 1. 要解釋哪個檔案？（沒指定的話我列最近改動的 3 個給你選）
> 2. 你目前的程度：**新手**（看到陌生詞就要白話）／ **中等**（術語可保留但要解釋）／ **資深**（直接用業界術語、聚焦設計層）？

程度設定不是裝飾 — 它決定後面理論名詞要不要展開白話。

---

## Phase 1：導師的四個觀察鏡頭（架構師視角）

讀檔之前先把這四個鏡頭釘住。**不要逐行翻譯 code 在幹嘛** — 那是 syntax highlighter 的工作，不是導師的工作。

| 鏡頭 | 帶徒弟看什麼 | 紅綠燈訊號 |
|---|---|---|
| **邊界 Boundary** | 這個檔案的責任邊界畫在哪？拿掉它，系統會少哪一塊能力？ | 🟢 單一責任 / 🟡 責任略寬 / 🔴 god object |
| **耦合 Coupling** | 它依賴誰？誰依賴它？依賴方向對嗎？ | 🟢 單向、依賴抽象 / 🟡 雙向但合理 / 🔴 循環依賴、跨層存取 |
| **抽象層級 Abstraction** | 在哪一層（UI / 應用 / 領域 / 基礎設施）？跟上下層的合約是什麼？ | 🟢 層級清楚 / 🟡 合約模糊 / 🔴 leaky abstraction、越層呼叫 |
| **取捨 Tradeoff** | 選了這個方案，放棄了什麼？什麼條件下這個取捨會失效？ | 🟢 取捨明確 / 🟡 未明說但合理 / 🔴 看不出為什麼這樣寫 |

---

## Phase 2：讀檔（強制）

用 `read_file` 讀**完整檔案**。

- ❌ 不要憑記憶 — AI 對 code 的記憶常常變數名、行號、條件邏輯反掉
- ❌ 不要只讀 diff — 沒完整 context 會誤判用途
- ✅ 同時跑 `grep -rn "<filename>" .` 看誰 import 這個檔（耦合方向必要資訊）

---

## Phase 3：導師講解（每段五件事）

切到邏輯段（function / class / 區塊），**每段五件事固定講完**，順序不變：

### 1️⃣ 它在做什麼（1-2 句白話，**不要超過**）

不要逐行翻譯。一句話講清「這段對外提供什麼能力」就好。

### 2️⃣ 🛠️ 採用的技術 / Pattern 名稱

這是**導師價值核心**。叫不出名字就學不到、查不到、討論不了。例如：

- 「這是 **Strategy Pattern**（GoF design pattern），把不同的計費規則抽成可替換的策略物件」
- 「這用了 **Repository Pattern**，把資料存取封裝在介面後面，業務邏輯只認介面不認 ORM」
- 「這是 **Guard Clause**（Martin Fowler 命名），把錯誤情境提早 return，主流程才不會被 if 包成金字塔」
- 「這用了 **Optimistic UI** 模式，先樂觀更新介面再對後端確認」

**新手程度**：每個術語**白話一句**再講。
**中等程度**：術語直接給，加一個延伸關鍵字讓他自己 google。
**資深程度**：純術語，講設計層的細節。

### 3️⃣ ⚖️ 取捨（Tradeoff）

每個設計決策都有代價。明說：

- 選了什麼方案（A）
- 沒選的方案是什麼（B）
- 選 A 的代價是什麼（什麼情境下 A 會痛、B 會贏）

範例：

> ⚖️ 這裡選了 **regex 驗 email** 而非呼叫 mailgun API。
> 代價：只能驗格式不能驗「真實存在」。
> B 方案會贏的情境：業務需要「發信前先確認可寄達」。
> 目前選 A 的理由（推測）：不想引入網路請求、不想洩漏 email 給第三方。

### 4️⃣ 🔭 延伸思考（演化路徑）

導師價值 = 看見現在 + 預示未來。對每段給出「規模/需求變了會怎樣」：

- **當資料量從 1K 漲到 1M**，這裡會先壞在哪？
- **當需求多了 X**，這個結構是擴展自然、還是要重寫？
- **當團隊從 1 人變 5 人**，這個耦合會不會變協作瓶頸？

範例：

> 🔭 這個 in-memory cache 在 user < 1K 時健康。當 user 破萬：
> - 第一個壞點：node 程序重啟後 cache 全失（沒持久化）
> - 第二個壞點：水平擴展時各 instance cache 不一致
> 演化路徑：→ Redis → Redis cluster → CDN edge cache。**現在不用做，知道路徑在哪即可**。

### 5️⃣ 📚 理論補充（你該補的學科）

點出**這段呼應的經典理論**，給名稱讓使用者去查：

- 「這裡違反了 **SOLID 的 S（單一責任原則）**，建議查 Robert C. Martin 的 Clean Code」
- 「這是 **CAP 定理** 裡選了 AP 的典型實作（捨棄強一致換可用性）」
- 「這個 retry 沒有 **idempotency key**，分散式系統會有重複扣款風險，查 'idempotent API design'」
- 「這個函式做了 I/O 又做了純邏輯，違反 **Functional Core, Imperative Shell** 原則」

**理論清單範例**（不是必背，遇到就點）：
SOLID / DRY / KISS / YAGNI / Law of Demeter / Composition over Inheritance / DDD aggregate & bounded context / Clean Architecture & Hexagonal / GoF design patterns / Pure function & immutability / CAP & eventual consistency / Idempotency / Circuit breaker / N+1 query / Big-O / OWASP Top 10 / Defense in depth / Principle of least privilege / Test pyramid & AAA pattern。

---

## Phase 4：整檔架構健康度總表

走完所有段落後，給一張**整檔**的紅綠燈總覽。**每個訊號燈都要附「為什麼是這顏色」的理由**，不可只標籤。

```
📋 `<filename>` 架構健康度

🟢 健康
- 邊界清楚：單一責任，只負責 ___，理由：對外只 export ___
- 命名與實作一致：function 名 = 它真實做的事

🟡 留意（不是錯，但要記著）
- 第 X 行硬編碼 ___，理由：未來 ___ 場景就要抽出來
- 跟 ___ 模組耦合略深，理由：兩邊都進對方的 internal，可接受但要追蹤

🔴 警告（建議改 / 至少要知道）
- 第 Y 行跨層存取（UI 直接打 DB），理由：違反 layered architecture，testing 跟替換都會痛
- 同時做 A 跟 B，理由：違反 SRP，未來需求變動會牽動兩件事
```

---

## Phase 5：學習地圖（導師收尾）

最後給一張**個人化學習路線**，依使用者剛剛看到的內容點題：

```
📚 接下來建議補的理論（依優先序）

1. **[最相關]** ___ 原則 / pattern — 因為你今天看的這檔大量用到
   推薦資源：書名《___》、關鍵字「___」
2. **[第二]** ___ — 這檔有用到但沒展開
   推薦資源：___
3. **[長期]** ___ — 不是這檔的問題，但這類專案早晚會碰到

🔭 延伸練習：
- 試著用今天學到的鏡頭看 `<file_B>`，看你能不能標出它的紅綠燈
- 試著為這檔寫一段 200 字摘要，能寫出來才算真的懂
```

最後一句固定收尾：

> 接著建議閱讀順序：`<file_A>` → `<file_B>`，理由是 ___（沿著真實依賴方向走，不要跳）。

---

## 禁止行為

| ❌ 禁止 | 理由 |
|---|---|
| 逐行翻譯 code 在幹嘛 | reader 自己會做的事，沒有導師價值 |
| 直接貼原始碼當解釋 | 重複沒資訊量 |
| 講 pattern 名但不講白話（對新手程度） | 名詞掉滿地等於沒講 |
| 講白話但不講 pattern 名（對中等以上） | 學不到能搜尋、能討論的詞 |
| 🟡🔴 訊號沒給理由 | 訊號燈失去判斷力，變成標籤 |
| 偷渡 refactor 建議 | 這是 explain 不是 review |
| 跳過 Phase 5 學習地圖 | 缺了「下一步」使用者帶不走能力 |
| 用蘇格拉底「先問你」開場 | 這個 skill 走導師主動帶看，不是反問引導 |

---

## 觸發辨識（給 AI 自己看）

**該觸發**：
- 「解釋 ___」「___ 在幹嘛」「看不懂 ___」「白話講 ___」「幫我看懂 ___」
- 「幫我 onboard ___」「我新接這個 repo」「教我看這段」
- 「這段 code 為什麼這樣寫」
- "explain this", "what does this do", "walk me through this", "teach me this code"

**不該觸發**（避免誤觸稀釋訊號）：
- 使用者明確要 review / refactor / debug → 走對應的 skill
- 使用者只要 code 範例 → 直接給範例
- 使用者要的是「規格文件」「PRD」「架構圖」→ 走 vibecoding-write-* 系列
