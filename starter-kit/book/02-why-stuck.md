# 第 2 章　推不動的四個根因

> **這一章回答**：模型一年比一年強，為什麼你的公司還在原地？
> **讀完你會知道**：卡住你們的是哪一類問題，以及每一類問題該從哪裡鬆開。

---

## 先看清楚落差有多大

如果你只看新聞，會以為每家公司都已經靠 AI 脫胎換骨。實際的數字冷靜得多。

全球近九成的組織說自己「經常使用 AI」，但真正讓 AI 貢獻 5% 以上營業利益的公司，大約只占 6%。[^mck] 換句話說，**用了，和賺到，是兩件事**。大多數公司停在中間：每個人都有在用，公司的帳上卻看不出差別。

台灣的落差更明顯。2024 年，台灣有 84% 的知識工作者已經在工作上用生成式 AI；[^ms-tw] 到了 2026 年，把 AI 真正整合進核心流程的企業只有 6.6%，而且有 61.8% 的 AI 使用發生在公司管不到的地方。[^aif] 員工早就在用，公司還沒接手。

同樣的模型，在少數公司身上帶來可觀的回報，在多數公司身上只是多一個聊天視窗，問題顯然出在模型以外。BCG 的研究估計，導入 AI 遇到的困難大約七成出在人與流程，只有三成跟技術和演算法有關。[^bcg-1020]

這一章談卡住企業的四個根因：**人、治理、資料、整合**。

【桑尼觀點：待補】一段你在輔導或授課現場看到的真實情況，可以匿名。例如「某公司買了全員授權，三個月後的使用率」。這一段是整章的開場，要讓讀者覺得「這就是我們公司」。

---

## 根因一　人：敢不敢用，有沒有人教

### 你在公司會看到的樣子

主管在會議上說要擁抱 AI，第一線的同事卻還是照舊。其實很多人私底下用得很熟，只是不讓公司知道。

### 數字怎麼說

- 主管和經理有四分之三以上每週用好幾次生成式 AI，第一線員工的固定使用率卡在 51%。只有約三分之一的員工覺得自己受過足夠的訓練。[^bcg-work]
- 全球有 57% 的員工會隱藏自己在用 AI。[^kpmg]
- 只有 13% 的員工覺得「用 AI 改變工作方式，就算失敗也會被肯定」；45% 覺得守住現有 KPI 比較安全。[^wti26]

### 為什麼會這樣

員工的擔心是有根據的。史丹佛的研究發現，在 AI 影響最大的職業裡，22 到 25 歲的就業人數明顯低於應有水準，資深員工則沒有這個缺口。[^canaries] 當公司一邊說「擁抱 AI」、一邊沒說清楚會不會因此裁員，最理性的選擇就是自己偷偷用、不張揚，也不分享。

再加上績效制度通常只看短期產出。花時間試一個新做法、結果沒成功，在考績上只會是扣分。誘因沒改，員工自然選擇不冒險。

### 怎麼鬆開

- **主管先公開用。** Microsoft 2026 年調查兩萬人後發現，AI 成效有 67% 取決於組織因素，個人因素只占 32%；成熟團隊和一般團隊差最多的，是主管會不會公開使用、有沒有訂品質標準、給不給實驗空間。[^wti26]
- **把人力政策講清楚。** Shopify 的做法是「要加人之前，先證明 AI 做不到」，員工數靠自然流失減少約 6%，反彈很小。[^shopify] Duolingo 把 AI 和停用約聘綁在一起對外宣布，引來強烈反彈，執行長兩度出面澄清。[^duolingo] 兩家都在用 AI，差別在於有沒有讓員工覺得自己是被犧牲的那一個。
- **訓練要給足。** 受過 5 小時以上訓練、而且有人面對面帶的員工，使用率明顯較高。[^bcg-work]

---

## 根因二　治理：每一關都能說不，沒有人能說好

### 你在公司會看到的樣子

一個 AI 試點要上線，要過資訊、資安、法務、採購，每一關都有理由再等一下。半年後，提案的人已經調到別的部門。

### 數字怎麼說

- 大企業的 AI 試點數量最多，從試點走到正式上線卻最慢，平均要 9 個月以上；中型企業約 90 天。這是受訪者自己回報的數字，僅供參考。[^nanda]
- 64% 的執行長承認，因為怕落後，在還沒搞清楚價值之前就先投資了；最後只有 25% 的專案達到預期報酬，16% 擴展到全公司。[^ibm-ceo]
- 2025 年放棄大部分 AI 專案的企業比例，從前一年的 17% 升到 42%；概念驗證平均有 46% 在上線前就被砍掉。[^sp]

### 為什麼會這樣

治理流程原本是為了「買一套系統、用十年」設計的。AI 的節奏完全不同：模型每幾個月就換代，用法要一邊試一邊改。用舊的審批流程管新的東西，結果就是兩種極端：什麼都不准，或是怕落後而什麼都亂買。

還有一件常被忽略的事：**出錯誰負責**。加拿大航空的客服機器人對旅客講錯退費規定，公司在仲裁時主張「機器人是獨立的法律實體，要為自己的行為負責」，仲裁人直接駁回，判公司賠償。[^aircanada] 責任沒先講清楚，每個審核關卡都不敢放行，其實很合理。

### 怎麼鬆開

- **把執行權往下放，把問責留在上面。** 能跨過試點的企業，通常讓第一線的團隊去試，但每個專案都有一位對結果負責的主管。[^nanda]
- **先訂內規，不用等法規。** 台灣的《人工智慧基本法》已在 2026 年 1 月施行，但各產業的具體規範要到 2028 年 1 月前才會由各部會訂出來。[^tw-law] 這段空窗期正好用來先訂公司自己的 AI 使用規範：哪些工具可以用、哪些資料不能放進去、出事時怎麼通報。啟動包附了範本。
- **少做幾個，做深一點。** 與其同時開十個試點，不如挑兩三個，每個都有一年的負責人和明確的成功標準。

---

## 根因三　資料：AI 拿不到它需要的東西

### 你在公司會看到的樣子

示範的時候很聰明，一接上公司的真實資料就開始答非所問。原因很簡單：資料散在各部門的 Excel、紙本和不同系統裡，欄位名稱不一致，權限也沒整理過。

### 數字怎麼說

- 台灣已經導入 AI 的電子資訊製造業者，約有八成遇到資料方面的困難。[^mic]
- 用自然語言查報表，同樣的模型在學術測驗上的準確率有七到九成，換到真實的企業資料庫只剩兩成左右。[^spider]
- RAND 訪談 65 位資深資料科學家，整理出 AI 專案失敗最常見的原因：問題定義錯、資料不夠、追技術而不追問題。[^rand]

### 為什麼會這樣

AI 再聰明，也只能根據你給它的東西回答。Anthropic 分析大量真實使用紀錄後指出，複雜的任務做不起來，常常是因為拿不到需要的資訊，而不是模型能力不足。[^anthropic] 資料還沒數位化、還分散在各處的公司，會發現 AI 很難在自己身上發揮。

### 怎麼鬆開

- **先數位化，再談 AI。** 台灣一家中小企業在工研院協助下，用電子秤把庫存登錄進系統，原料登錄率做到九成以上，重複採購減少了。[^cna] 這一步跟 AI 無關，但哪天要讓 AI 給採購建議，就得先有這些資料。
- **從資料已經在的地方開始。** 全家和統一超商的 AI 訂貨，用的是本來就有的銷售與天氣資料：全家的訂貨時間省下七成五以上，鮮食報廢少了一成以上；統一超商每家店每年省下約 365 小時工時。這些是企業自己公布的數字。[^cna]

---

## 根因四　整合：工具很多，接不上工作

### 你在公司會看到的樣子

公司買了好幾套 AI 工具，每套都有漂亮的展示。真正用的時候，要在五個視窗之間複製貼上，而且每次都要重新解釋一遍背景。

### 數字怎麼說

- 有資訊長說：「今年看了幾十個展示，可能一兩個真的有用，其他都是包了一層殼，或只是科學實驗。」[^nanda]
- 一半的執行長說，公司的技術系統是破碎、彼此不相連的。[^ibm-ceo]
- 任務越長，AI 越容易失手：一小時內能完成的工作，成功率約六成；拉長到五小時以上，掉到約四成五。[^anthropic-26]

### 為什麼會這樣

大部分 AI 工具不記得你上次說過什麼，也不知道公司的流程長什麼樣子。員工簡單的事會用它，重要的事反而不敢交給它。市場上又充滿「號稱是 AI agent」的產品，Gartner 估計數千家廠商裡真正在做 agent 的大約只有 130 家。[^gartner]

### 怎麼鬆開

- **能買就不要自建，但要求廠商貼合你的流程。** 調查中，外購或合作的 AI 專案上線率約 67%，自建約 33%。這是受訪者自述的數字，可能有其他因素影響，但方向值得參考。[^nanda]
- **用實測取代感覺。** 一項嚴謹的實驗裡，資深工程師用 AI 寫程式，自己覺得快了 20%，實測反而慢了 19%。[^metr] 每個試點都要先量「沒有 AI 時」的基準，才知道 AI 到底帶來什麼。第 8 章會講怎麼量。

---

## 四個根因交織在一起，就是「試點地獄」

四個根因很少單獨出現。常見的劇本是這樣：怕落後，所以同時開很多小試點（治理）；試點只比誰的展示比較驚豔，沒有基準線（整合）；接不上真實資料，效果出不來（資料）；第一線本來就不放心，看到效果不好，更確定不要碰（人）。半年後專案被砍，大家得到的結論是「AI 還不成熟」。

能跨過去的企業，做對了幾件事：

| 他們做的事 | 為什麼有用 |
|---|---|
| **重新設計流程，不是把 AI 加在舊流程上** | AI 帶來可觀回報的公司，從根本重新設計工作流程的比例，大約是其他公司的 3 倍 [^mck] |
| **七成的心力放在人與流程** | 困難本來就七成在這裡 [^bcg-1020] |
| **少數幾個核心場景，做深** | 一個場景有一年的負責人和成功標準，比十個沒人顧的試點有用 |
| **先做後勤** | 一半以上的預算花在業務和行銷，回報最高的卻是後勤自動化 [^nanda] |
| **保留真人和品質底線** | Klarna 曾宣稱 AI 客服抵得上 700 人，後來執行長承認品質下降，改回保證客戶隨時找得到真人 [^klarna] |

---

## 台灣企業要特別注意的一件事

台灣中小企業不導入 AI，最大的原因不是沒錢。調查中，有 63.9% 的企業回答「沒有明確的需求」，提到成本的只有 25.5%。另外，84.5% 的企業內部沒有 AI 人才。[^italent]

也就是說，多數台灣企業卡在第一步：**不知道 AI 該用在哪裡**。多買工具幫不上這個忙。啟動包的「場景挑選畫布」就是為這一步設計的：用「量大不大、有沒有標準答案、能不能量、錯了代價多大」四個問題，先挑出第一個值得做的地方。

【桑尼觀點：待補】這裡適合放你自己的主張，作為本章結尾。我依品牌核心價值「不只學會，更要交付」先寫一句草稿，請你改或換掉：

> **AI 專案和人一樣，要有驗收標準。** 沒有先講好「怎樣算做到」，試點只會停在「看起來很厲害」。

---

## 本章重點

1. **用了不等於賺到。** 近九成組織在用 AI，真正有感的約 6%。差別在組織，不在模型。
2. **四個根因是人、治理、資料、整合**，而且會互相拖累，形成試點地獄。
3. **跨過去的方法很樸實**：重新設計流程、把心力放在人、少做幾個但做深、用實測取代感覺。

## 帶回公司問的三個問題

1. 我們公司的同事，敢不敢讓主管知道自己在用 AI？
2. 現在進行中的 AI 專案，每一個都有一位對結果負責的人和一個「怎樣算成功」的數字嗎？
3. 我們要用 AI 處理的工作，需要的資料已經數位化了嗎？

---

[^mck]: McKinsey,〈The state of AI in 2025〉。高績效者定義為 AI 貢獻 5% 以上 EBIT，約占樣本 6%。https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai 【⚠️ 待查證：2026 年版原文的最新數字】
[^ms-tw]: Microsoft 台灣，2024 工作趨勢指數，2024-06-20。https://news.microsoft.com/zh-tw/ms-wti-ai/
[^aif]: 人工智慧科技基金會（AIF）2026 台灣產業 AI 化大調查，228 家企業，樣本偏向較進步的企業。經理人報導，2026-05-04。https://www.managertoday.com.tw/articles/view/72095 ；CIO Taiwan，2026-04-30。https://www.cio.com.tw/111644/
[^bcg-1020]: BCG,〈AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value〉，2024-10-24。https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
[^bcg-work]: BCG,〈AI at Work 2025〉，11 國 10,600 多人，2025-06-26。https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
[^kpmg]: KPMG 與墨爾本大學，全球 AI 信任調查，4.8 萬人，2025。https://fbe.unimelb.edu.au/newsroom/media-release-global-study-reveals-trust-of-ai-remains-a-critical-challenge-reflecting-tension-between-benefits-and-risks
[^wti26]: Microsoft Work Trend Index 2026，2 萬人，2026-05-05。https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
[^canaries]: Brynjolfsson 等,〈Canaries in the Coal Mine?〉，Stanford Digital Economy Lab。https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ 【⚠️ 待查證：各版本數字為 13%、16%、19%，正式稿要寫明引用哪一版】
[^shopify]: TechCrunch，2025-04-07。https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/ ；員工數變化依 Shopify 年報轉述。
[^duolingo]: Fortune，2025-08-18。https://fortune.com/2025/08/18/duolingo-ceo-admits-controversial-ai-memo-did-not-give-enough-context-insists-company-never-laid-off-full-time-employees
[^nanda]: MIT NANDA,〈The GenAI Divide: State of AI in Business 2025〉。52 個組織訪談加問卷，數字多為受訪者自述，作者自稱結論為方向性。https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
[^ibm-ceo]: IBM CEO Study，2,000 位執行長，2025-05-06。https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles
[^sp]: S&P Global 調查，CIO Dive 報導，2025-03-14。https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/
[^aircanada]: Moffatt v. Air Canada, 2024 BCCRT 149，2024-02-14。https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada
[^tw-law]: 行政院新聞稿，2026-05-21。https://www.ey.gov.tw/Page/9277F759E41CCD91/999df6da-6539-4941-913f-5125d684c58d
[^mic]: 資策會 MIC 電子資訊製造業調查，經理人報導，2025-03-19。https://www.managertoday.com.tw/articles/view/70116
[^spider]: Spider 2.0 基準測試，2024／2025。https://arxiv.org/abs/2411.07763v2
[^rand]: RAND,〈The Root Causes of Failure for Artificial Intelligence Projects〉，2024-08-13。https://www.rand.org/pubs/research_reports/RRA2680-1.html
[^anthropic]: Anthropic Economic Index，2025-09-15。https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
[^anthropic-26]: Anthropic Economic Index，2026-01-15。https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
[^cna]: 中央社，2026-05-02。成效皆為企業自述。https://www.cna.com.tw/news/afe/202605020024.aspx
[^gartner]: Gartner 新聞稿，2025-06-25。預測，非量測。https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 【⚠️ 原頁無法開啟，經多家報導交叉核對】
[^metr]: METR，2025-07-10。16 位資深開發者、246 個任務。https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[^klarna]: Fortune，2025-05-09。https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/
[^italent]: 經濟部產業發展署 iTALENT 電子報，整理中企署委託工研院之中小企業 AI 運用現況調查（員工 10–199 人企業），2026-03-16。https://ipd.nat.gov.tw/italent/ePaperD/10/ePaper20260300008
