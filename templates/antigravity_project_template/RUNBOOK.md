# SmartTrip FX Runbook — 從一句痛點到可運行 App

> **這份 runbook 教的不是「做這個 App」，是「用 AI 蓋 App 的方法」。**
> SmartTrip FX 只是示範案例。學完後你會懂兩件事：
> 1. **Meta-prompt 迭代法**：不寫完美 prompt，而是讓 AI 幫你寫
> 2. **工具分工**：AI Studio 是 **prompt 工廠**，agy 是 **建造現場**

---

## 怎麼用這份 runbook

**適用對象**：
- 跑過一次 `mvp_fill_in_prompt.md` 的學員（如果完全沒跑過，先去那邊）
- 想做完整 SDD Sprint（Mode B）的人
- 已經會跟 AI 對話，但每次「做完原型不知道下一步」的人

**閱讀方式**：
- **第一次讀** → 從頭讀到尾，看「方法」
- **真的要動手** → 邊讀邊操作，每個 code block 都複製貼出去跑
- **教學現場** → 講師示範 Phase 0-4（30 分鐘），學員自己跑 Phase 5-8（2 小時）

**核心訊息（記這個就好）**：

```
                  AI Studio                     agy
                ┌──────────┐                ┌──────────┐
我的痛點 ──────▶│ prompt   │──prompt 草稿──▶│ 建造現場 │──▶ 可跑的 app
                │ 工廠     │                │          │
                └──────────┘                └──────────┘
                 探索 / 對話                 落地 / 版控
                 迭代 / 失敗                 結構 / 紀律
```

**不要混用**。AI Studio 不裝專案、agy 不適合探索 prompt。錯用會痛苦。

---

# Phase 0：從口語痛點到結構化簡報

## 你會做什麼

把你**含糊的「我覺得有個問題」** → 變成**5 段可追蹤的 markdown**（目標受眾 / 待解痛點 / 期望成果 / 主要約束 / 成功指標）。

## 為什麼這步不能跳

> **Linus 註解**：
> 99% 的 AI coding 失敗不是 AI 不夠強，是**你連自己想做什麼都說不清楚**。
> 結構化簡報 = 讓你**先跟自己對話**，再跟 AI 對話。
> 跳過這步等於直接叫廚師煮飯但不講你想吃什麼 — 端上來你怪廚師沒用。

## 操作

### 1. 用口語寫下你的痛點（不超過 3 句）

打開記事本，回答這個問題：「我為什麼想做這個？」

**SmartTrip FX 範例**：

> 我的痛點是：出國旅遊時，時常不清楚出國要帶多少現金，回國後現金太多又使用不了，
> 換回台幣又會有匯損。那麼要了解整個行程要帶多少錢需要一個 App 幫我自動排定行程。

注意這段話的特徵：
- **時機**（出國時 / 回國後）
- **症狀**（不清楚 / 太多 / 匯損）
- **想要**（自動排定行程的 App）

### 2. 用 5 個欄位把口語結構化

填這 5 個格子（檔名建議 `docs/seed-brief.md`）：

```markdown
## 目標受眾
[誰會用？年齡、身份、頻率、習慣 — 一段話講白]

## 待解痛點
[他現在怎麼解？解得多痛？量化金額或時間]

## 期望成果
[做完後使用者拿到什麼？量化成功的樣子]

## 主要約束
[不做什麼？技術 / 法規 / 時程的硬邊界]

## 成功指標
[3-5 個可量測的數字 — 啟用率 / 留存 / 準確度]
```

### 3. 對照範例（SmartTrip FX 種子簡報）

> 完整版見 [`../../種子簡報.md`](../../種子簡報.md)，這裡擷取重點：

```markdown
## 目標受眾
25–40 歲台灣衝動型出境旅客，一年 1–4 趟、以日韓泰為主、預算敏感、
習慣帶現金、決策快怕麻煩。

## 待解痛點
不知道該帶多少外幣現金、哪些地方只收現金、現在換匯划不划算。
換太多 → 回國再換虧匯差；換太少 → 現場狼狽。在一趟 NT$40,000
的旅程中，匯損與多換的成本可達數百到上千元。

## 期望成果
3 分鐘內得到一份含「精準建議換匯現金額」的行程，且事後實際現金
花費與建議值誤差 < 15%。

## 主要約束
- 不做帳號雲端同步（MVP 用 localStorage）
- 不做訂房比價（用外部連結導出）
- 4 週 MVP 驗證窗
- 法規：FX 換匯燈號需「非投資理財建議」免責聲明

## 成功指標
- 啟用率：進站者完成一次生成 ≥ 40%
- 存檔率：生成後按「儲存此行程」 ≥ 25%
- 30 天回訪：≥ 20%
- 換匯準確度：誤差 < 15% 的比例 ≥ 60%
```

## ✅ 完成檢核

- [ ] 5 個欄位都填了，沒有「___」或「TBD」
- [ ] 目標受眾**不是「所有人」**（如果寫所有人，重寫）
- [ ] 成功指標有**數字**（沒數字 = 沒辦法驗收）
- [ ] 主要約束至少寫 2 條（沒約束的專案會無止盡膨脹）

---

# Phase 1：Meta-Prompt 第一輪 — 求 prompt

## 你會做什麼

**不要直接叫 AI 做事，而是讓 AI 教你怎麼叫它做事。**

打開 [aistudio.google.com](https://aistudio.google.com)，貼下面這段。

## 為什麼這樣做

> **Linus 註解**：
> 新手寫 prompt 都犯一個錯：直接問結果（「幫我安排行程」），然後拿到不痛不癢的爛答案。
> **資深玩家的套路**：先問「**這類問題的專業 prompt 怎麼寫**」。
> 因為 AI 自己最知道**它要什麼格式的輸入才能給好輸出**。
> 這叫 meta-prompt — 用 prompt 求 prompt。比你自己摸索 10 次有效。

## Prompt 全文（複製到 AI Studio）

```text
6/12-6/18 幫我安排日本的京都、大阪的行程包含食、住、行、娛樂並且
安排好行程、飯店、飛機以及景點。
我是 24 歲學生還在打工而且有點窮預算 3 萬至 5 萬。
請你用旅行社、行程規劃師來幫我安排行程。

請告訴我專業的 prompt 怎麼寫。
```

## 拆解：這個 prompt 為什麼會成功

| 元素 | 內容 | 為什麼必要 |
|------|------|-----------|
| **時間錨點** | 6/12-6/18 | 沒時間 = AI 沒辦法判斷季節 / 機票 / 旺淡季 |
| **地點清單** | 京都、大阪 | 兩個城市 vs 一週 = AI 知道要分配天數 |
| **範圍** | 食住行娛 | 不限定 = AI 自己挑要不要含交通 / 餐廳 |
| **身份畫像** | 24 歲學生打工 | 暗示預算敏感、能走路、不需頂級住宿 |
| **預算數字** | 3 萬-5 萬 | 區間 vs 單點 = AI 可以給高低兩版 |
| **角色** | 旅行社、行程規劃師 | **觸發 AI 進入專業心智模式** |
| **真正目的** | 請告訴我專業的 prompt 怎麼寫 | **這是 meta-prompt 的精髓** |

## 卡關處理

- **AI 給你的不是 prompt，是直接的行程** → 重新打：「我要的是 **prompt 範本**，不是行程內容。請以 markdown 格式給我 Role / Constraints / Output Requirements 三段式 prompt。」
- **prompt 太空泛** → 補一句：「請把 User Profile 量化（年齡、預算數字、旅遊風格選項）」
- **prompt 沒有約束段** → 補一句：「請加入至少 5 條 Constraints（航班偏好、住宿偏好、預算上限、體力限制、必看景點）」

---

# Phase 2：取得結構化 prompt（並執行）

## 你會做什麼

AI 應該回給你一份**結構化的 prompt 範本**。你的任務：**直接複製、貼回 AI Studio 再跑一次**。

## AI 給你的（SmartTrip FX 範例）

> 把整段複製貼回 AI Studio，按 Run。

```markdown
# Role: 關西深度旅遊規劃師與在地導遊

# User Profile:
- 年齡 / 身份：24 歲大學生，目前有打工，預算有限（精打細算型）
- 旅遊人數：[請填入人數，例如：1 人獨旅 / 2 人同行]
- 旅遊風格：重視 CP 值。希望行程豐富、經典景點不漏接，但也想穿插
  一些拍美照、體驗在地文化的免費 / 低成本行程。可以接受多走路，
  住宿乾淨安全、交通方便即可。

# Constraints & Preferences:
1. 旅遊日期：2026 年 6 月 12 日至 6 月 18 日（7 天 6 夜）
2. 地點：日本京都、大阪（包含環球影城一日遊）
3. 總預算：新台幣 30,000 - 50,000 元（含機票、住宿、門票、食宿、交通）
4. 航班偏好：優先考慮廉價航空（LCC），可接受紅眼或早出晚回航班以最大化遊玩時間
5. 住宿偏好：京都住高質感青年旅館（單人床位或平價雙人房）；大阪住交通樞紐
   （如難波、新今宮、梅田）附近的平價商旅

# Output Requirements:
請幫我規劃一份詳細的旅遊企劃書，包含：
1. 【預算分配表】：估算機票、住宿、交通票券、環球影城門票及每日餐費，確保在預算內
2. 【交通與票券攻略】：推薦最省錢的交通組合（如 Haruka、大阪周遊卡、ICOCA 的搭配）
3. 【詳細每日行程】：以表格或條列式呈現 Day 1 - Day 7 的行程，包含
   （景點、高 CP 值在地美食推薦、交通移動方式、省錢小撇步）
4. 【環球影城免快通攻略】：指導如何在不買快速通關的情況下，玩到任天堂瑪利歐園區與熱門設施
```

## 拆解：為什麼這個 prompt 結構強

> **Linus 註解**：
> 學會看這份 prompt 的「骨架」比學會抄它重要。骨架是 4 段：
> **Role → User Profile → Constraints → Output Requirements**
> 這是業界 prompt engineering 的標準四段式。記住它，下次自己手寫也用這個結構。

| 段名 | 功能 | 不寫會怎樣 |
|------|------|-----------|
| **Role** | 把 AI 推進專業心智模式 | AI 回答得像維基百科，不像顧問 |
| **User Profile** | 量化使用者特徵 | AI 給「通用建議」，不會 tailor |
| **Constraints** | 列硬邊界（時間 / 錢 / 場域） | AI 自由發揮 → 出超出預算的方案 |
| **Output Requirements** | 規定回應格式 | 拿到一坨文字，無法拆解使用 |

## 預期結果

AI 會回給你一份**長長的旅遊企劃書**（預算表 + 交通攻略 + 7 天行程 + USJ 攻略）。

**不要評論這份企劃書好不好。** 這還不是終點。下一步要把它**轉成 App 需求**。

## 卡關處理

- **AI 沒有按 4 段格式回應** → 補一句：「請嚴格按照 # Role / # User Profile / # Constraints / # Output Requirements 四段式輸出，每段都不能省」
- **行程細節不夠** → 補：「Day 1 範例請列出時間、景點、移動方式、餐廳、預估花費，至少 5 個 entry」

---

# Phase 3：加入 painpoint 二輪精煉

## 你會做什麼

Phase 2 的企劃書「好看但沒解決你的問題」。現在把**真正的痛點**講出來，再讓 AI 把行程轉成 **App 需求**。

## 為什麼分兩步講

> **Linus 註解**：
> 為什麼不一開始就講「我要做 App 算換匯」？因為**講太多 AI 會丟資訊**。
> 第一輪先建立**領域共識**（旅遊規劃），第二輪再注入**真實痛點**（換匯）。
> 這叫**漸進加層**。一次給太多需求 = AI 思考被切斷 = 拿到爛東西。

## Prompt 全文

```text
1. 因為每一次依照這樣的行程，我必須要帶信用卡跟日幣。

2. 依照剛剛的行程我需要 AI 幫我查行程、飯店、交通工程娛樂。
   哪裡需要刷卡？哪裡需要付現金？

3. 我需要做一個 web base 的 app，將來當我告訴 AI 日期可以直接
   幫我找出行程。並自動算我需要帶多少日幣，何時換匯最划算，
   我不希望換太多日幣產生匯損，所以這個 app 日期一確定，
   第一步先出行程。一確定行程就自動告訴我該換多少日幣就能剛好。

請問要 AI 做一個完整的 app 要下什麼 prompt？
```

## 拆解：這段為什麼威力大

| 部分 | 內容 | 功能 |
|------|------|------|
| 第 1 句 | 「我必須要帶信用卡跟日幣」 | **點出現實情境**（兩種付款方式） |
| 第 2 句 | 「哪裡刷卡？哪裡現金？」 | **要 AI 把痛點分類** |
| 第 3 句 | 「web base app + 日期 → 行程 → 換匯」 | **完整的產品邏輯流** |
| 最後 | 「要下什麼 prompt？」 | **又一次 meta-prompt** |

> **Linus 註解**：
> 看到「最後再次問 prompt」嗎？這是**第二次 meta-prompt 迭代**。
> 你的目的不是要這次的答案 — 而是要**下一輪可以丟給工程 AI 的 prompt**。
> 高手都這樣玩。

## 卡關處理

- **AI 直接給你 code** → 補：「我要的是 prompt 範本，不是 code。請給我一份能丟給工程師 AI 的開發 prompt」
- **prompt 太籠統** → 補：「請列出至少 4 個 App 功能需求，每個附「功能名 / 輸入 / 輸出 / 技術需求」四段」

---

# Phase 4：取得完整 app 開發 prompt

## 你會做什麼

AI 應該給你一份**開發級 prompt**（Role 變成「全棧工程師」）。把它**再貼回 AI Studio 跑一次**，這次會拿到實際 code + 更完整的產品 prompt。

## 第一份開發 prompt（AI 給你的）

```text
**Role:** 你是一位精通全棧開發（Full-stack Developer）與旅遊數據分析的工程師。

**Task:** 我想打造一個基於 Web 的旅遊規劃 App。請提供完整的代碼架構與邏輯建議。

**App 功能需求：**

1. **自動行程生成：** 用戶輸入「日期」與「預算」，App 需透過 Google Maps API
   與 OpenAI API 自動生成包含食、住、行、娛樂的 7 天行程。

2. **財務預算拆解：** 根據行程地點，自動分析哪些是「大額消費（建議刷卡）」、
   哪些是「小額消費（需付日幣現金）」。

3. **精準換匯計算：** App 需統計行程中所有「僅限現金」的總額（如交通儲值、
   小吃、寺廟門票），並加上 10% 預備金，給出「精準換匯建議金額」。

4. **即時匯率與換匯點建議：** 串接現時匯率 API，並分析近 30 天匯率走勢，
   告知用戶現在換匯是否為低點，以避免匯損。
```

> **Linus 註解**：
> Role 從「旅遊規劃師」**升級為「全棧工程師 + 數據分析師」**。
> 這是換軌訊號：**從規劃模式進入建造模式**。
> 接下來這份 prompt 會引出更具體的技術 spec。

## 把這份貼回 AI Studio 後，會拿到什麼

兩個東西：

1. **三段 JavaScript code**（前端 / 後端 / 換匯計算）— 可跑但粗糙
2. **一份「完整產品開發 prompt」** — 這才是寶藏

完整產品開發 prompt 長這樣（SmartTrip FX 版本）：

```text
Role: 你是一位資深全端工程師（Next.js + Node.js）與金融數據分析師。

Task: 請幫我開發名為 "SmartTrip FX" 的 Web App 全套代碼。
這個 App 專門為精打細算的旅客設計，能一鍵生成行程並精算
「不浪費、不產生匯損」的精準日幣現金換匯量。

請依照以下進度與規格，分步驟提供代碼：

1. 前端 UI（Next.js 14 App Router + Tailwind CSS）：
   - 建立一個乾淨、Scannable 的儀表板（Dashboard）
   - 頂部有輸入框：[旅遊目的地：預設關西]、[出發日期]、[回程日期]、[台幣預算總額]
   - 左側區塊：顯示 7 天行程時間軸，每個行程卡片要標註景點名、預估花費（¥）、
     與支付標籤（刷卡 / 現金）
   - 右側區塊（財務面板）：大字顯示「建議換匯日幣：¥XXXXX」，並有一個 FX 換匯
     紅綠燈訊號（STRONG_BUY / BUY / HOLD）與文字建議

2. 後端 API 整合：
   - 請寫出 api/generate 的完整 Serverless Function
   - 當接收到前端的日期與預算後，呼叫 OpenAI API。請使用嚴格的 json_object
     提示詞，讓 AI 回傳帶有 payment_method: "cash_only" | "card_acceptable"
     標籤的行程

3. 財務與匯率演算法：
   - 撰寫一個獨立的計算模組。統計所有 cash_only 的總和，自動乘以 1.1
     （10% 預備金）作為最終換匯值
   - 模擬或串接一個匯率 API，讀取 30 天歷史數據，用當天匯率與 30 天均線
     （MA30）做對比，輸出換匯推薦燈號
```

## 拆解：這份 prompt 為什麼是 agy 級別的輸入

| 維度 | 內容 | agy 接收後會做什麼 |
|------|------|-------------------|
| **產品名** | SmartTrip FX | agy 直接拿來做專案資料夾名 |
| **價值主張** | 不浪費、不產生匯損 | agy 寫進 PRD §1 Problem Statement |
| **技術棧** | Next.js 14 + Tailwind | agy 寫進 ADR-0001 技術選型 |
| **分步驟** | 前端 → 後端 → 演算法 | agy 拆 sprint task 的順序 |
| **三大模組** | UI / API / 演算法 | agy 寫 PRD §2 功能清單的三個主項 |
| **量化規格** | ¥XXXXX 大字、MA30 燈號 | agy 寫進 acceptance criteria |

> **Linus 註解**：
> 這份 prompt 已經是「**規格級**」的 spec，不是「想法級」。
> 規格級 spec 的特徵：
> - 技術名詞精確（Next.js 14 App Router，不是「現代前端框架」）
> - 行為描述可驗證（「大字顯示」、「JSON 嚴格格式」、「10% 預備金」）
> - 分模組（前端 / 後端 / 演算法 各自獨立）
>
> **這是 AI Studio 的最終產出**。從這裡之後不要再回 AI Studio 改了 — 改去 agy。

---

# ═══════════════════════════════════
# 換手點：AI Studio → agy
# ═══════════════════════════════════

## 為什麼要換手

> **Linus 註解**：
> AI Studio 強在「**對話式探索**」 — 你來回問 10 次都不會收費、不會建檔。
> 但 AI Studio **不會**幫你：
> - 建立專案資料夾結構
> - 跟 git 整合
> - 維護跨對話的記憶（每次都從 0 開始）
> - 跑測試、驗證、commit
>
> agy 強在「**結構化建造**」 — `.agents/` 規則、`docs/PRD.md` 持久化、
> 跨對話的 `/memory`、skill 自動化、checkpoint 回滾。
>
> **混用會痛苦**。AI Studio 階段拼 prompt，agy 階段建專案。
> 切換的訊號：你拿到「規格級 prompt」之後（= Phase 4 結尾）。

## 換手清單

把這幾樣**保存好**（接下來會用到）：

- [ ] 你的種子簡報.md（Phase 0 寫的 5 段）
- [ ] Phase 4 拿到的「完整產品開發 prompt」（SmartTrip FX 那段）
- [ ] 第一輪企劃書（Phase 2 拿到的 7 天行程）— 之後 PRD 補商業背景會用到

---

# Phase 5：開 antigravity 工作站

## 你會做什麼

把 `antigravity_project_template/` **複製成你的專案**，第一次跑 `agy`。

## 操作

### 1. 複製模板

```bash
# 從這個 repo 把 template 拷貝到你想放專案的位置，並改名
cp -r /path/to/ai-vibe-coding-beginner/templates/antigravity_project_template \
      ~/projects/smarttrip-fx

cd ~/projects/smarttrip-fx
```

### 2. 把 Phase 0 的種子簡報塞進專案

```bash
# 把你 Phase 0 寫的種子簡報塞進去
# 建議檔名與位置
mv ~/路徑/seed-brief.md docs/seed-brief.md
```

### 3. 設定 API Key

```bash
# 申請 Gemini API Key：https://aistudio.google.com/apikey
export GEMINI_API_KEY="貼上你的金鑰"

# 永久生效（zsh）
echo 'export GEMINI_API_KEY="貼上你的金鑰"' >> ~/.zshrc
source ~/.zshrc
```

### 4. 第一次啟動 agy

```bash
agy
```

走過三次確認：

| 提示 | 你要選 | 為什麼 |
|------|--------|--------|
| 配色 | 看喜好 | 純美觀 |
| 條款 | Accept | 不接受就不能用 |
| 資料夾信任 | **Yes**（限這個資料夾） | agy 才能讀寫你的 code；**其他資料夾選 No** |

> **Linus 註解**：
> 第三題「資料夾信任」很重要：**只信任當前專案**，不要信任 `~` 之類的廣範圍。
> 信任 = agy 可以執行 shell、改檔案 — 你不會想讓它在 `~/Documents` 亂跑。

### 5. 確認 agy 讀到了規則

進入 agy 後打：

```text
/memory show
```

應該會看到 `AGENTS.md` 內容被載入。沒看到 → agy 沒讀到規則檔，檢查你在不在正確的資料夾。

## ✅ 完成檢核

- [ ] 專案資料夾改名了（不是 `antigravity_project_template`）
- [ ] `docs/seed-brief.md` 存在且內容正確
- [ ] `agy` 跑起來沒報錯
- [ ] `/memory show` 看得到 `AGENTS.md`

---

# Phase 6：把 Phase 4 的 prompt 餵給 agy

## 你會做什麼

**不要**直接複製 Phase 4 的 prompt 叫 agy 寫 code。
**要**讓 agy 跑 `/spec-it`，把 Phase 4 的 prompt 當作**「現有規格參考」**輸入。

## 為什麼這樣做（非常重要）

> **Linus 註解**：
> 新手最常見的錯：把 Phase 4 的 dev prompt 直接貼給 agy → agy 跳過 spec 直接寫 code。
> 結果是：**沒 PRD、沒 ADR、沒測試 — 跟 AI Studio 寫出來的爛 code 沒兩樣**，
> 還浪費了 template 的 SDD 紀律。
>
> **正確做法**：用 `/spec-it` 把 Phase 4 的內容**轉成結構化 spec**
> （PRD + API contract + BDD scenarios + 測試骨架）。**spec 在前，code 在後**。
> 這叫 **Spec-Driven Development**（SDD）。
>
> 沒有 spec，agy 寫的 code 跟一般 AI Studio 寫的沒差。

## 操作

### 1. 啟動 `/spec-it`

在 agy 對話框打：

```text
/spec-it
```

agy 會問你 5 個澄清問題（這是 `/spec-it` 的鐵律）。**老老實實答**，不要跳。

### 2. 範例對話（SmartTrip FX）

```text
你（在 agy）：
/spec-it 我要做一個叫 SmartTrip FX 的 web app，幫旅客算精準換匯。
規格如下：

[貼 docs/seed-brief.md 全文]

技術期望（從 AI Studio Phase 4 拿來的，可參考但不一定要照做）：

[貼 Phase 4 的「完整產品開發 prompt」全文]

請依 /spec-it 流程走 — 先問我 5 個澄清題，等我答完再開始寫 PRD。
```

```text
agy（回應，會問類似這樣的 5 題）：

我看完了你的種子簡報與技術期望。動工前先確認 5 題：

1. **目標使用者輪廓**：你 brief 寫「25-40 歲衝動型出境旅客」，
   是否限縮為「至少出過 1 次國」的旅客？還是包含完全新手？

2. **MVP 範圍**：第一版要做完 4 個功能（行程生成 / 付款拆解 /
   換匯計算 / 匯率燈號）嗎？還是優先 2-3 個？

3. **技術選擇 — Next.js vs 純靜態 + Flask**：
   - Phase 4 提到 Next.js 14 + Tailwind
   - template 預設較簡單的 Flask + 原生 HTML
   - 你優先哪個？（Next.js 學習曲線高，Flask 更新手友善）

4. **AI 模型**：Phase 4 寫 OpenAI API，但你的 GEMINI_API_KEY
   已經設好了。要用 Gemini 還是 OpenAI？

5. **匯率資料來源**：免費 API（如 exchangerate-api.com）就好，
   還是要付費精準源？
```

### 3. 你的回答（範例）

```text
1. 不限縮，包含新手。
2. 第一個 sprint 先做「行程生成」+「換匯計算」兩個。其他放 backlog。
3. Flask + 原生 HTML/CSS/JS。新手友善優先。
4. 用 Gemini（GEMINI_API_KEY 已經設好）。
5. 免費 API。
```

### 4. agy 接下來會做的事

```
1. 寫 docs/PRD.md（§1-§8 完整版）
2. 寫 docs/api-contract.md（/api/generate 規格）
3. 寫 tests/features/trip_generation.feature（BDD scenarios）
4. 寫 tests/unit/test_*.py 骨架
5. 更新 tasks/backlog.md（拆 user stories）
6. 偵測到「Next.js vs Flask」是技術未決，建議跑 /adr
```

## ✅ 完成檢核

- [ ] `docs/PRD.md` 8 個 section 都填好
- [ ] `docs/api-contract.md` 至少有一個 endpoint 寫好
- [ ] `tests/features/*.feature` 至少 3 個 scenario（主流程 + 2 邊界）
- [ ] `tasks/backlog.md` 至少 5 個 user story 帶 priority

---

# Phase 7：跑 SDD Sprint 10 站

## 你會做什麼

照 `.agents/WORKFLOW.md` 的 10 站順序，把 spec 變成可跑的 app。

## 完整 10 站對應 SmartTrip FX

| 站 | Skill | 做什麼 | 預期產出 |
|----|-------|--------|----------|
| 1 | `/spec-it` | (已做) | PRD / API / BDD |
| 2 | `/adr` | 寫關鍵決策 | ADR-0001 後端框架選 Flask、ADR-0002 匯率 API 選哪個 |
| 3 | `/plan-sprint` | 拆當前 sprint | sprint-1.md：行程生成 + 換匯計算 |
| 4 | `/tdd-cycle` | 紅綠燈循環 | code + 綠燈測試 |
| 5 | `/verify` | 5 維度驗證 | format / lint / type / test / security 全綠 |
| 6 | `/sync-it` | code ↔ 文件對齊 | 無 critical drift |
| 7 | `/commit-msg` | Conventional Commit | 可追蹤的 commit |
| 8 | 部署 | Vercel / Railway / 本機跑 | 公開網址或 demo URL |
| 9 | `/retro` | Sprint 回顧 | 4Ls 報告 |
| (cross) | `/explain-code` | 卡關時 | 架構師視角解釋 |
| (cross) | `/check-key` | 部署前 | 確認沒洩 API key |

## 站 2：`/adr` — 寫關鍵決策

`/spec-it` 結尾如果有提示「建議寫 ADR」，現在跑：

```text
/adr 後端框架選擇 — Flask vs Next.js

背景：MVP 目標是新手友善 + 快速驗證。
選項：
- A. Flask + 原生 HTML/CSS/JS — 學習曲線低、單檔後端、新手能改
- B. Next.js 14 App Router + Tailwind — 業界主流、SSR、未來擴充佳

決定：A
理由：MVP 4 週驗證窗，學習曲線優先於擴充性。V1 再評估遷移。
後果：未來若要做使用者帳號、SEO 優化，可能要重寫前端。
```

> **Linus 註解**：
> ADR 不是「我選了什麼」，而是「**為什麼選 + 之後會付什麼代價**」。
> 沒寫「後果」的 ADR 等於沒寫。

## 站 3：`/plan-sprint` — 拆任務

```text
/plan-sprint

當前 sprint 目標：4 週內做完「行程生成 + 換匯計算」MVP。
人力：1 人（你）
時間：每天 2 小時，4 週 = 56 小時。
```

agy 會把 `tasks/backlog.md` 內的 user stories 拆成可執行的 task：

```markdown
## Sprint 1 — 行程 + 換匯（4 週）

### Now (本週)
- [ ] US-001: 使用者輸入日期+預算，後端回 7 天行程 JSON
  - Size: M (4h) | Priority: P0
- [ ] US-002: 行程每個項目標 cash_only / card_acceptable
  - Size: S (2h) | Priority: P0

### Next (下週)
- [ ] US-003: 加總 cash_only × 1.1 = 建議換匯日幣
  - Size: S (2h) | Priority: P0
- [ ] US-004: 串匯率 API 顯示當前匯率
  - Size: M (4h) | Priority: P1

### Later
- [ ] US-005: 30 天均線比較 → 紅綠燈訊號
- [ ] US-006: localStorage 儲存歷史行程
- [ ] US-007: 「儲存此行程」按鈕

### Blocked
- 無
```

## 站 4：`/tdd-cycle` — 寫第一個功能

從 US-001 開始（行程生成 API）。

```text
/tdd-cycle US-001

請：
1. 先寫測試（RED）— /api/generate POST 回 200 + JSON shape
2. 寫最小實作（GREEN）— Flask route 接日期+預算，呼叫 Gemini，回固定樣板
3. Refactor — 抽出 prompt template、加錯誤處理
4. 全程跑 pytest，每階段都要綠
```

agy 會：

1. 寫 `tests/unit/test_generate.py`：
   ```python
   def test_generate_returns_7_day_itinerary():
       response = client.post('/api/generate', json={
           'start_date': '2026-06-12',
           'end_date': '2026-06-18',
           'budget_twd': 40000,
       })
       assert response.status_code == 200
       data = response.get_json()
       assert len(data['days']) == 7
       for day in data['days']:
           for activity in day['activities']:
               assert activity['payment_method'] in ['cash_only', 'card_acceptable']
   ```
2. 跑 pytest → 紅（route 不存在）
3. 寫 `server/app.py` 最小版本
4. 跑 pytest → 綠
5. Refactor → 抽出 `server/gemini_client.py`
6. 跑 pytest → 還是綠 → done

> **Linus 註解**：
> TDD 的順序是**測試先寫**。新手最常犯的錯：先寫實作，事後補測試。
> 結果測試會「順著實作寫」 — 等於沒測。
> 紅綠燈循環逼你**先想清楚行為**，再想怎麼實作。

## 站 5：`/verify` — 5 維度驗證

寫完 US-001 後跑：

```text
/verify
```

agy 會檢查 5 維度：

```
✅ Format: black / prettier — pass
✅ Lint:   flake8 / eslint — pass
✅ Type:   mypy / tsc — N/A (此專案無 type)
✅ Test:   pytest — 12/12 pass
⚠️ Security: 發現 1 個 medium — server/app.py:24 CORS 設成 *

請修 CORS 後重跑，或加 known-issue。
```

決策：開發階段 CORS=* 沒差，加 `known-issues.md`。production 再修。

## 站 6：`/sync-it` — 文件對齊

```text
/sync-it
```

agy 掃描 code 跟 docs 之間的 drift：

```
📊 Drift Report:
- docs/api-contract.md §POST /api/generate
  - 寫的回應 schema 沒包含 "warnings" 欄位
  - 但 server/app.py:45 實際會回 warnings
  → 建議：補進 contract

- README.md §快速開始
  - 寫「pip install -r requirements.txt」
  - 但專案沒有 requirements.txt（用 pyproject.toml）
  → 建議：更新 README
```

照建議改完，再跑一次 `/sync-it` 直到無 critical drift。

## 站 7：`/commit-msg` — Conventional Commit

```text
/commit-msg
```

agy 看 staged diff 生 commit message：

```
feat(api): /api/generate 回 7 天行程含付款分類

新增 POST /api/generate endpoint，接受日期區間 + 預算，
透過 Gemini 生成行程，每個活動標 cash_only / card_acceptable。

實作 US-001（見 tasks/backlog.md）。

技術細節：
- Gemini prompt 用 json_object 嚴格模式
- 加 10 秒 timeout + 重試 1 次
- CORS=* 留待 production 收緊（known-issues.md）

Refs: PRD §2.1, ADR-0001
```

直接 commit 或先 review 再 commit。

## 站 8：部署

新手友善路線：

```bash
# 本機跑（demo 用）
python server/app.py
# → 給朋友看 http://localhost:5000

# Vercel（前後端都上線，免費）
vercel deploy
# → 給朋友看 https://smarttrip-fx.vercel.app
```

> **Linus 註解**：
> 部署前**強制跑 `/check-key`**：
> ```text
> /check-key
> ```
> 它會掃 git history 是否有 hardcoded API key、`.env` 是否在 `.gitignore`、
> 環境變數設定。**這步不能省 — 洩 key 你會付錢給 OpenAI / Google**。

## 站 9：`/retro` — Sprint 回顧

```text
/retro
```

agy 用 **4Ls 法**問你：

```
Sprint 1 (2026-06-12 ~ 2026-07-10) Retrospective

📈 Liked（這次 Sprint 哪裡爽？）：
- /spec-it 把 Phase 4 prompt 轉成 PRD，省了我自己拆 spec 的時間
- TDD 寫測試先逼我釐清 API shape，比直接寫 code 順

📚 Learned（學到什麼？）：
- Meta-prompt 套路：求 prompt 比求答案有效
- AI Studio → agy 換手時機：拿到「規格級」spec 之後

🚧 Lacked（缺什麼？）：
- 還沒接真實匯率 API（用 mock）
- 沒寫 .env.example，新人 clone 不會跑

🎯 Longed for（下個 sprint 想要？）：
- 串實際匯率 API + MA30 燈號
- 加「儲存此行程」按鈕（localStorage）
```

retro 結果存進 `tasks/retros/<日期>-sprint-1.md`，Action Items 進 `backlog.md`。

## ✅ Phase 7 完成檢核

- [ ] ADR-0001（後端框架）寫好
- [ ] sprint-current.md 有具體 task + size + priority
- [ ] 至少 1 個 user story 走完 RED → GREEN → REFACTOR
- [ ] `/verify` 全綠（或有合理 known-issue）
- [ ] `/sync-it` 無 critical drift
- [ ] 至少 1 個 conventional commit
- [ ] Sprint retro 寫好

---

# Phase 8：收尾與部署

## 你會做什麼

把 MVP「**真的給人用**」。不是給講師看 — 是寄連結給朋友。

## 操作

### 1. 確認 deploy 真的活著

打開隱身視窗 / 換手機，直接打你的部署 URL。

確認：
- [ ] 首頁載得起來
- [ ] 輸入日期 + 預算後，按鈕能跑
- [ ] 行程結果出現
- [ ] 換匯數字顯示
- [ ] 至少手機版能看（不要求美）

### 2. 寫 30 秒 demo 文案

寄給朋友的話：

```
這是我做的小工具，可以幫你算出國該帶多少日幣現金，不會多換虧匯差。

→ https://smarttrip-fx.vercel.app

試一下，輸入「6/12-6/18 預算 4 萬」看看會出什麼。

（這是我用 AI 教學工作坊做的第一個 app，回饋我會珍惜）
```

### 3. 把這次經驗寫進 `tasks/retros/`

retro 已經寫了（Phase 7 站 9）。再補一份「30 天行動計畫」：

```markdown
## 接下來 30 天

### Week 1-2: 串真實匯率 API
- 替換 mock，接 exchangerate-api.com
- 寫 MA30 計算邏輯（pandas）
- 加紅綠燈訊號 UI

### Week 3: 加 localStorage
- 「儲存此行程」按鈕
- 首頁列出歷史行程
- 點開看詳情

### Week 4: 收使用者回饋
- 找 5 個朋友試用
- 收 3 個改進點
- 決定要不要做 V1
```

## ✅ 全部完成

- [ ] 公開 URL 至少 2 個人試用過
- [ ] 30 天行動計畫寫好
- [ ] retro 歸檔
- [ ] commit 全部推上 GitHub

---

# 附錄 A：完整 Prompt 速查卡（複製貼上區）

## A.1 — Phase 1 Meta-Prompt（求 prompt）

```text
[時間區間] 幫我安排 [地點] 的行程包含食、住、行、娛樂並且
安排好行程、飯店、飛機以及景點。
我是 [年齡 + 身份] 還在打工而且有點窮預算 [數字] 至 [數字]。
請你用 [角色 1]、[角色 2] 來幫我安排行程。

請告訴我專業的 prompt 怎麼寫。
```

## A.2 — Phase 2 結構化 Prompt 骨架（4 段式）

```markdown
# Role: [專業角色名稱]

# User Profile:
- 年齡 / 身份：
- [其他特徵]：
- 風格：

# Constraints & Preferences:
1. [硬限制 1]
2. [硬限制 2]
...

# Output Requirements:
請幫我規劃一份 [產出物]，包含：
1. 【段名 1】：[描述]
2. 【段名 2】：[描述]
```

## A.3 — Phase 3 加 Painpoint（漸進加層）

```text
1. 因為每一次依照 [既有方案] 我必須 [限制 / 麻煩]。

2. 依照剛剛的 [既有產出] 我需要 AI 幫我 [分類 / 拆解 / 分析]。
   哪裡是 [類別 A]？哪裡是 [類別 B]？

3. 我需要做一個 [產品形態] 將來當我告訴 AI [輸入] 就可以
   [自動產出]。並 [核心痛點解決邏輯]。

請問要 AI 做一個完整的 [產品形態] 要下什麼 prompt？
```

## A.4 — Phase 4 App 開發 Prompt（給工程師 AI）

```markdown
Role: 你是一位資深全端工程師（[技術棧]）與 [領域] 分析師。

Task: 請幫我開發名為 "[產品名]" 的 [產品形態] 全套代碼。
這個 [產品] 專門為 [目標族群] 設計，能 [核心價值主張]。

請依照以下進度與規格，分步驟提供代碼：

1. 前端 UI（[框架]）：
   - [元件 1]
   - [元件 2]

2. 後端 API 整合：
   - [endpoint 1]
   - [LLM 串接規格]

3. 核心演算法：
   - [計算邏輯 1]
   - [資料 API 串接]
```

## A.5 — agy `/spec-it` 開頭話術

```text
/spec-it 我要做一個叫 [產品名] 的 [產品形態]，[一句話價值]。

種子簡報：
[貼 docs/seed-brief.md 全文]

技術期望（從 AI Studio 拿來的，可參考但不一定要照做）：
[貼 Phase 4 完整產品開發 prompt]

請依 /spec-it 流程走 — 先問我 5 個澄清題。
```

---

# 附錄 B：工具對照 — 為什麼這份 runbook 用 agy

| 維度 | AI Studio | agy CLI | Claude Code | Gemini CLI (舊) |
|------|-----------|---------|-------------|----------------|
| 對話探索 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| 專案建立 | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Skill / Slash | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Subagent 平行 | ❌ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ❌ |
| Spec-Driven | ❌ | ⭐⭐⭐⭐⭐ (本 template) | 需自己配 | 需自己配 |
| 學員門檻 | ⭐⭐⭐⭐⭐（最低） | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 商業選擇 | 免費 | 免費（個人） | 付費 | 免費，但 2026-06-18 EOL |

**結論**：AI Studio 做 prompt 探索 → agy 做專案建造，是 2026 教學現場最務實的組合。

> 個人版 Gemini CLI 在 2026-06-18 退場，不要再學了。

---

# 附錄 C：學員常見錯誤對照表

| 錯誤行為 | 症狀 | 修正 |
|----------|------|------|
| Phase 1 直接問「幫我做 app」 | AI 給 generic boilerplate | 改用 meta-prompt：「請告訴我專業的 prompt 怎麼寫」 |
| 跳過 Phase 0 種子簡報 | 之後 PRD 寫不下去（不知道使用者是誰） | 回去寫 5 段 |
| 把 Phase 4 prompt 整段貼給 agy | agy 跳過 spec 直接寫 code，跟 AI Studio 沒兩樣 | 改用 `/spec-it` 開頭，把 Phase 4 prompt 當作「技術期望」輸入 |
| `/spec-it` 5 個澄清題只答 1 句敷衍 | PRD 寫得空洞，後續 `/tdd-cycle` 不知道測什麼 | 老老實實答，每題至少 1-2 句具體 |
| 沒設 `GEMINI_API_KEY` 就跑 | agy `/spec-it` 不影響，但 `/tdd-cycle` 寫的 code 跑不起來 | `export GEMINI_API_KEY=...` + 寫進 `.env.example` |
| 把 `.env` 提交到 git | API key 洩漏，被盜刷 | `/check-key` 部署前必跑 + `.env` 加進 `.gitignore` |
| 一次給 agy 4 個功能 | agy 拆解錯，sprint 1 跑半年 | 用 `/plan-sprint` 分批：MVP 只做 2 個，其他放 backlog |
| 跳過 `/verify` 直接 commit | 部署到 production 才發現 lint / type 錯 | commit 前必跑 `/verify` |
| `/sync-it` 的 drift 報告全部按「延後」 | 文件越來越偏離 code，新人 clone 跑不起來 | critical drift 一定當下修，trivial 才延後 |
| 沒寫 retro 就開下個 sprint | 一直重複同樣的錯 | 每個 sprint 結尾跑 `/retro` |

---

# 三句口訣

> **AI Studio 問 prompt**
> **agy 寫 spec 才寫 code**
> **每個 sprint 都 retro**

延伸版（5 句完整版）：

> **痛點先結構化**（Phase 0）
> **AI Studio 用 meta-prompt 迭代**（Phase 1-4）
> **拿到規格級 spec 換手到 agy**（換手點）
> **/spec-it 在前，/tdd-cycle 在後**（SDD 鐵律）
> **/verify 全綠才 commit，/retro 收尾**（每個 sprint）

---

# 延伸閱讀

- [`README.md`](./README.md) — Antigravity template 入口
- [`USAGE.md`](./USAGE.md) — Mode A vs Mode B 選擇器
- [`.agents/WORKFLOW.md`](./.agents/WORKFLOW.md) — 10 站工作流總圖
- [`.agents/SKILL-MAP.md`](./.agents/SKILL-MAP.md) — 10 個 skill 連動關係
- [`mvp_fill_in_prompt.md`](../mvp_fill_in_prompt.md) — 進度比較慢的學生用的填空版
- [`ai_ready_repo_blueprint.md`](./ai_ready_repo_blueprint.md) — 整套 template 為什麼這樣設計

---

**版本**：2026-05-27 v1
**對應 template**：antigravity_project_template/
**示範案例**：SmartTrip FX（旅遊精準換匯）
