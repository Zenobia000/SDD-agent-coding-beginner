# 第 2 章　卡住企業的是組織的四個根因，七成的困難在人與流程

<p class="lede">同樣的模型，在少數企業身上帶來回報，在多數企業身上只是多一個聊天視窗。差別出在模型以外的四件事：人、治理、資料、整合。四者會互相拖累，把企業困在試點裡。</p>

## 困難約七成出在人與流程，技術與演算法只占三成

BCG 訪談 1,000 位企業高階主管後，把導入 AI 遇到的困難分成三類，並建議資源照同樣比例分配：演算法占一成，技術與資料占兩成，人與流程占七成。[^bcg]

```exhibit
{"id": "2.1", "type": "stack", "unit": "%",
 "title": "導入 AI 的困難約七成在人與流程，資源也該照這個比例分配",
 "data": [
   {"label": "演算法", "value": 10},
   {"label": "技術與資料", "value": 20},
   {"label": "人與流程", "value": 70, "highlight": true}
 ],
 "source": "BCG，AI Adoption in 2024，2024-10-24；約 1,000 位高階主管"}
```

多數企業的預算剛好倒過來：大部分花在授權與系統，訓練、流程重設與變革管理只分到零頭。我們把這七成拆成四個根因，每一個都有可以觀察的症狀和可以下手的地方。

## 人：員工私下用得很熟，卻不敢讓公司知道

在多數企業裡，主管在會議上說要擁抱 AI，第一線卻照舊。實際上很多人私底下用得很熟，只是不讓公司知道。

```exhibit
{"id": "2.2", "type": "bar", "unit": "%",
 "title": "過半用 AI 的員工不讓公司知道，只有 13% 相信嘗試失敗會被肯定",
 "data": [
   {"label": "第一線員工固定使用 AI", "value": 51},
   {"label": "用 AI 的員工不說自己用了 AI，或把產出當成自己的", "value": 57},
   {"label": "相信用 AI 改變工作、失敗也會被肯定", "value": 13, "highlight": true}
 ],
 "source": "BCG AI at Work 2025（11 國 10,600 人）；KPMG × 墨爾本大學全球 AI 信任調查 2025（4.8 萬人）；Microsoft Work Trend Index 2026（2 萬人）",
 "note": "三項來自不同調查；57% 的分母是工作上使用 AI 的受雇者"}
```

員工的保留有它的道理。在公司還沒說清楚人力政策之前，私下用、不張揚、不分享，是最安全的選擇；績效制度又只看短期產出，花時間試新做法、結果沒成功，只會扣分。[^bcg-work] [^wti]

**要鬆開這一層，靠的是主管行為與人力政策，不是更多工具。** Microsoft 2026 年調查兩萬名 AI 使用者，和 AI 成效相關的因素裡，組織因素的關聯約是個人因素的兩倍（67% 對 32%）；成熟團隊和一般團隊差最多的，是主管會不會公開使用、有沒有訂品質標準、給不給實驗空間。[^wti] 人力政策怎麼訂，第 4 章會完整說明。

## 治理：審批流程為十年一次的系統採購設計，跟不上每季換代的 AI

一個 AI 試點要上線，要過資訊、資安、法務、採購，每一關都有理由再等一下。半年後，提案的人已經調到別的部門。

MIT NANDA 的研究顯示，大企業的試點數量最多，從試點走到正式上線卻最慢，平均要九個月以上，中型企業約 90 天。這是受訪者自述的數字，但和我們在企業看到的情況一致。[^nanda]

治理慢，常見的根源是「出錯誰負責」沒有先講清楚。

<div class="case" markdown>
**加拿大航空：AI 說的話就是公司說的話**

2024 年，加拿大航空的客服機器人告訴旅客可以事後申請喪親優惠退款，實際規定不允許。公司在仲裁時主張「機器人是獨立的法律實體，要為自己的行為負責」，仲裁人直接駁回，判公司賠償。[^aircanada]

責任歸屬沒有事先寫清楚，每個審核關卡都不敢放行，其實很合理。
</div>

**要鬆開這一層，就把執行權往下放、把問責集中。** 能跨過試點的企業，讓第一線團隊去試，每個專案有一位對結果負責的主管；同時用內規先回答「哪些資料不能放進去、出事時誰處理」。第 6 章談怎麼訂這份內規。

## 資料：AI 拿不到工作需要的脈絡，示範時很聰明，接上真實資料就失準

示範時用的是整理好的範例，正式上線要面對的是散在各部門的 Excel、紙本和互不相通的系統。

```exhibit
{"id": "2.3", "type": "bar", "unit": "%",
 "title": "用自然語言查報表，同樣的模型換到真實企業資料，準確率從七到九成掉到約兩成",
 "data": [
   {"label": "學術測驗資料庫", "value": 91, "display": "73–91%"},
   {"label": "真實企業資料庫", "value": 21, "display": "17–21%", "highlight": true}
 ],
 "source": "Spider 2.0 基準測試，2024／2025",
 "note": "長條長度以區間上限繪製"}
```

台灣的情況相同：資策會調查已經導入 AI 的電子資訊製造業者，約八成遇到資料方面的困難。[^mic] Anthropic 分析大量真實使用紀錄後也指出，複雜任務做不起來，常常是因為拿不到需要的資訊，模型能力反而不是瓶頸。[^anthropic]

**要鬆開這一層，就從資料已經在的地方開始。** 第 5 章的台灣案例都有同一個特徵：先選一個資料已經數位化的單點，再談 AI。

## 整合：工具接不上工作流程，任務拉得越長越容易失手

公司買了好幾套 AI 工具，每套都有漂亮的示範。實際使用時，員工要在幾個視窗之間複製貼上，每次都要重新解釋背景。大部分工具不記得上次說過什麼，也不知道公司的流程長什麼樣子，簡單的事有人用，重要的事沒人敢交給它。[^nanda]

```exhibit
{"id": "2.4", "type": "column", "unit": "%",
 "title": "任務越長，AI 越容易失手",
 "data": [
   {"label": "一小時內可完成的任務", "value": 60},
   {"label": "五小時以上的任務", "value": 45, "highlight": true}
 ],
 "source": "Anthropic Economic Index，2026-01-15；API 任務成功率",
 "note": "廠商數據；數值為約略值"}
```

市場上又有大量換了包裝的產品。Gartner 估計，自稱在做 AI agent 的數千家廠商裡，真的在做的大約只有 130 家。[^gartner]

**要鬆開這一層，就把驗收標準寫在採購之前。** 先定義「這個流程上線後，哪個數字要變成多少」，再挑工具；能買就不要自建，但要求廠商接上你的流程。

## 四個根因互相拖累，形成試點地獄

四個根因很少單獨出現。常見的劇本是：怕落後，所以同時開很多小試點；試點只比誰的示範比較驚豔，沒有基準線；接不上真實資料，效果出不來；第一線本來就不放心，看到效果不好，更確定不要碰。半年後專案被砍，得到的結論是「AI 還不成熟」。

```exhibit
{"id": "2.5", "type": "funnel", "unit": "%",
 "title": "64% 的執行長在搞清楚價值前就先投資，最後擴展到全公司的專案只有 16%",
 "data": [
   {"label": "因為怕落後，先投資再找價值", "value": 64},
   {"label": "專案達到預期投資報酬", "value": 25},
   {"label": "擴展到全公司", "value": 16, "highlight": true}
 ],
 "source": "IBM CEO Study，2025-05-06；2,000 位執行長"}
```

S&P Global 的調查顯示，放棄大部分 AI 專案的企業比例，從 2024 年的 17% 升到 2025 年的 42%；概念驗證平均有 46% 在上線前就被砍掉。[^sp]

## 台灣企業卡在第一步：多數不知道 AI 該用在哪，成本只排第三

經濟部中小企業署委託工研院調查員工 10 到 199 人的企業，問它們導入 AI 最大的挑戰：

```exhibit
{"id": "2.6", "type": "bar", "unit": "%",
 "title": "台灣中小企業不導入 AI，最大的原因是沒有明確需求，成本只占四分之一",
 "data": [
   {"label": "內部沒有 AI 人才", "value": 84.5},
   {"label": "沒有明確的需求", "value": 63.9, "highlight": true},
   {"label": "成本", "value": 25.5}
 ],
 "source": "經濟部中小及新創企業署委託工研院，中小企業 AI 運用現況調查；經濟部產業發展署 iTALENT 整理，2026-03-16",
 "note": "母體為員工 10–199 人的企業"}
```

**多數台灣企業卡在第一步：不知道 AI 該用在哪裡。** 多買工具幫不上這個忙。第 5 章用四個問題幫你挑出第一個場景。

<div class="advice" markdown>
用四個根因做一次快速診斷，每一項問一個問題：

- **人**：同事敢不敢讓主管知道自己在用 AI？
- **治理**：現在進行中的 AI 專案，每一個都有一位對結果負責的人嗎？
- **資料**：要交給 AI 的工作，需要的資料已經數位化了嗎？
- **整合**：每個專案在採購前，都寫下了「上線後哪個數字要變成多少」嗎？

答「否」最多的那一項，就是你們要先處理的根因。
</div>

[^bcg]: BCG,〈AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value〉，2024-10-24。https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
[^bcg-work]: BCG,〈AI at Work 2025〉，11 國 10,600 多人，2025-06-26。https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
[^wti]: Microsoft Work Trend Index 2026，10 國 2 萬名 AI 使用者，2026-05-05。https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization ；KPMG × 墨爾本大學，2025。https://fbe.unimelb.edu.au/newsroom/media-release-global-study-reveals-trust-of-ai-remains-a-critical-challenge-reflecting-tension-between-benefits-and-risks
[^nanda]: MIT NANDA,〈The GenAI Divide: State of AI in Business 2025〉。52 個組織訪談、153 位主管問卷，數字多為受訪者自述，作者自稱結論為方向性。https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
[^aircanada]: Moffatt v. Air Canada, 2024 BCCRT 149，2024-02-14。英屬哥倫比亞省民事仲裁庭，非上級法院判例。https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada
[^mic]: 資策會 MIC 電子資訊製造業 AI 調查，經理人報導，2025-03-19。https://www.managertoday.com.tw/articles/view/70116
[^anthropic]: Anthropic Economic Index，2025-09-15。https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
[^gartner]: Gartner 新聞稿，2025-06-25。屬預測，非實測。https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
[^sp]: S&P Global 調查，CIO Dive 報導，2025-03-14。https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/
