# 第 5 章　決策二 場景組合：先做量大、有標準答案、量得到的工作，少做幾個、做深

<p class="lede">第一個場景挑錯，第 2 章的四個根因會一起放大。先做的應該是量大、有標準答案、量得到、錯了代價可控的工作，多半落在後勤。台灣做出成效的企業都從資料已經在的單點開始，先數位化再談 AI；能買現成的就不要自建，但要把驗收標準寫進合約。</p>

## 預算多半花在看得見的前台，回報最高的卻是後勤

MIT NANDA 的研究指出，受訪主管估計約一半的生成式 AI 預算流向業務與行銷，後勤自動化則常被認為有較高回報。原文另一處以假設性預算分配寫出約 70%，因此這個比例不宜當成精確市場數字。研究包含 52 個組織訪談與 153 位主管問卷，數字多為自述，結論具方向性。[^nanda]

各部門的公開證據也是同一個樣子。證據最硬的場景，集中在量大、有標準答案的工作；預算最多的業務與行銷，公開的成效多半是廠商說法或還沒實現的目標：

| 部門 | 最硬的公開證據 | 證據等級 |
|---|---|---|
| **客服** | 5,179 名客服人員導入 AI 助理後，每小時解決件數平均多 14%，新手多 34% [^brynjolfsson] | 研究 |
| **人資問答** | IBM 內部的人資助理，常見問題 94% 不必轉給真人 [^askhr] | 廠商數據 |
| **IT 服務台** | ServiceNow 自家 IT 服務台，每件案子省約 45 分鐘 [^servicenow] | 廠商數據 |
| **業務** | AI 業務開發新創 11x 被報導在官網列出不是客戶的企業標誌 [^11x] | 個案 |
| **行銷** | Mondelez 投資逾 4,000 萬美元做生成式內容工具，內容成本降 30–50% 是目標，還不是實績 [^mondelez] | 個案 |

這不代表前台沒有價值。BCG 估計，AI 的潛在價值約七成集中在銷售行銷、製造、供應鏈、定價這些核心職能。[^bcg-gap] 長期的大錢在核心業務，第一個場景卻該從後勤挑：後勤的工作量大、規則清楚、出錯時不會直接傷到客戶，最容易量出前後差別，也最容易讓組織學會怎麼做。

**這代表什麼**：第一個場景的任務是讓公司學會「重新設計一個流程、量出成效」這整套動作，這件事做順了，再往核心業務擴。

## 用四個問題挑第一個場景：量大不大、有沒有標準答案、能不能量、錯了代價多大

挑場景時，問這四個問題就夠了：

| 問題 | 怎麼判斷 | 為什麼重要 |
|---|---|---|
| **量大不大** | 每週發生幾十次以上，而且有很多人在做 | 量小的工作，省下的時間撐不起導入成本 |
| **有沒有標準答案** | 兩位資深同事處理同一件事，答案會一樣 | AI 在能力邊界外反而更容易出錯，答對率可以從 84.5% 掉到 60% [^jagged] |
| **能不能量** | 現在就能拿到處理時間、錯誤率或件數 | 沒有基準線，就分不出是真的變快還是覺得變快（見第 1 章、第 8 章） |
| **錯了代價多大** | 出錯時是內部重做，還是對外承諾、影響個人權益 | AI 對外說的話由公司負責（見第 6 章） |

前三題決定效益，第四題決定風險。把前兩題合成「量與標準化程度」，第四題當另一個軸，就能把候選場景放進四個格子。第三題是門檻：量不到的場景，不管落在哪一格，都不適合當第一個。

```exhibit
{"id": "5.1", "type": "matrix",
 "title": "第一個場景從右下角挑：量大、有標準答案、錯了只是內部重做",
 "x": {"label": "量與標準化程度", "low": "量小、靠個人判斷", "high": "量大、有標準答案"},
 "y": {"label": "出錯代價", "low": "內部重做", "high": "對外承諾或影響個人權益"},
 "cells": [
   {"title": "別做", "text": "量小又高風險，例如錄取或淘汰、對外法律意見。AI 可以整理資料，決定留給人"},
   {"title": "謹慎做", "text": "量大但出錯會傷到客戶，例如對外客服回覆、退款判斷。加人工審核點、保留真人通道"},
   {"title": "暫緩", "text": "量小、出錯代價低，例如偶爾一次的簡報草稿。讓員工用企業版工具自己用，不必立專案"},
   {"title": "先做", "text": "量大、規則清楚、錯了只是內部重做，例如員工問答、請假查詢、發票辨識、訂貨建議", "highlight": true}
 ],
 "source": "桑尼資料科學整理（場景四問）",
 "note": "「能不能量」是門檻，量不到的場景不列入第一個"}
```

人事決策放在「別做」，是因為已經有實際的法律後果。Amazon 開發的 AI 履歷評分工具因為歧視女性而解散團隊；[^amazon] 美國法院在 Mobley v. Workday 案中，接受「AI 供應商可以當成雇主的代理人負責」的理論，讓案件進入實體審理。[^mobley] AI 可以幫招募排面試、回答求職者問題，錄取與淘汰要由人決定。

**練習題**：把你們列出的候選流程放進圖表 5.1。若某流程量不到、出錯代價又高，先補資料或縮小任務範圍，不要急著做 PoC。

## 台灣做出成效的企業，都從資料已經在的單點開始，先數位化再談 AI

台灣有公開成效的案例，大型零售和中小傳產都有，共同點很一致：

| 企業 | 規模與產業 | 做了什麼 | 成效（企業自述） |
|---|---|---|---|
| **全家便利商店** | 大型零售 | 2022 年起依銷售與天氣資料，用 AI 建議鮮食訂購量 | 訂貨時間省 75% 以上，鮮食報廢降一成以上 [^cvs] |
| **統一超商** | 大型零售 | 全台門市導入 AI 訂貨 | 每家店每年約少 365 小時工時 [^cvs] |
| **宜展科技農業** | 中小、食品加工 | 參加 AI 實作專班，用 AI 模擬蔬果乾燥的參數 | 製程縮短 40%，營收成長 10% [^moea] |
| **隴鈦銅器** | 中小、傳產金屬 | 在拋光工序加上 AI 視覺檢測 | 包裝合格率 99.99%，減少重工 [^moea] |
| **滿記實業** | 中小 | 在工研院場域用電子秤建立庫存系統，這一步還不是 AI | 原料登錄率 90% 以上，減少重複採購 [^moea] |

以上成效都是企業或主管機關自述，沒有第三方驗證。但五個案例走的路很像：都有歷史資料，都有明確的對錯標準，成效都能用工時、報廢率或合格率衡量。

滿記實業的案例最能說明起點在哪裡。它做的第一步是把原料庫存數位化，根本還沒用到 AI。對資料還在紙本或個人 Excel 裡的企業，這就是起點。

```exhibit
{"id": "5.2", "type": "ladder",
 "title": "台灣的成功案例走同一條路：先把資料數位化，再在單點用 AI，最後擴到全通路",
 "steps": [
   {"name": "把一個流程數位化", "text": "庫存、訂單、檢驗紀錄先進系統，不再靠紙本和個人 Excel", "signal": "資料每天自動產生，不用另外整理", "meta": "滿記實業"},
   {"name": "在單點用 AI", "text": "選一道有對錯標準的工序，例如視覺檢測、製程參數", "signal": "合格率或製程時間對照基準線有差", "meta": "隴鈦銅器、宜展科技農業"},
   {"name": "擴到全通路", "text": "同一套做法複製到所有門市或產線", "signal": "工時與報廢率在每個據點都量得到", "meta": "全家便利商店、統一超商", "highlight": true}
 ],
 "source": "桑尼資料科學整理；案例依中央社 2026-05-02、經濟部 2026-01-19 報導，成效為企業自述"}
```

起步的資源也有。經濟部的中小企業 AI 實作專班免費，2026 年目標開 113 班、訓練 1,200 人以上；宜展、隴鈦、滿記都是專班的案例。[^moea] 補助計畫多在每年上半年受理，2026 年的梯次大多已經截止，要提早準備下一梯次。[^grants]

## 能買就不要自建，但要求廠商貼合你的流程、能從回饋學習

在這份樣本中，向外部廠商購買或共同開發的 AI 專案，約 67% 回報已部署；內部自建約 33%。這是 52 個組織的自述結果，可能受組織能力等因素影響，不能據此認定採購方式造成差異。[^nanda]

```exhibit
{"id": "5.3", "type": "column", "unit": "%",
 "title": "向外部廠商購買或合作的 AI 專案，上線率約是自建的兩倍",
 "data": [
   {"label": "購買或與外部合作", "value": 67, "display": "約 67%", "highlight": true},
   {"label": "自建", "value": 33, "display": "約 33%"}
 ],
 "source": "MIT NANDA，The GenAI Divide: State of AI in Business 2025；52 個組織訪談、153 位主管問卷",
 "note": "受訪者自述；作者提醒差異可能來自組織能力本身，不一定是採購方式造成"}
```

台灣中小企業的選擇也一樣，近七成傾向採用外部現成方案。[^italent] 大型軟體廠商（SAP、Salesforce、Microsoft、Workday、ServiceNow）都在既有的 ERP、CRM、人資系統上加 AI，[^vendors] 對多數企業來說，第一個選項應該是你已經在用的系統裡內建的 AI。

買現成的不代表照單全收。研究裡做得成的企業，會要求廠商做兩件事：貼合自己的流程，以及能從使用回饋裡學習。[^nanda] 採購時再加上第三件：把「怎樣算做到」寫進合約。例如有些 AI 客服按「解決一件」計價，但客戶 24 小時沒回應也算成已解決；[^intercom] 這個定義沒先談好，帳單上的成效就是廠商說了算。

**我們的建議**：自建只留給兩種情況，一是這個流程就是你的競爭優勢，二是市面上找不到能接上你資料的產品。其他情況，先買、先上線、先量。

## 每個部門都有一個可以先做的場景

第四部逐一拆解十一個部門與工作領域。下表是各部門用場景四問挑出來的第一個場景，細節與雷區見各篇：

| 部門 | 先做的場景 | 留給人的決定 |
|---|---|---|
| 客服 | 常見問題回覆，目標放在處理量上升 | 退款、補償、客訴升級 |
| 財務 | 請款與應付帳款 | 付款放行、關帳簽核 |
| 人資 | 員工問答、請假查詢 | 錄取、績效、懲處 |
| 業務 | 準備客戶資料與會議紀錄 | 價格與折扣例外 |
| 行銷 | 內容初稿 | 品牌與法遵審核 |
| 採購 | 比價與合約摘要 | 供應商選擇 |
| 營運與庫存 | 需求預測與訂貨建議 | 停線、交期承諾 |
| 法務 | 契約初審 | 對外法律意見 |
| IT 與資安 | 服務台 | 權限授予、正式環境變更 |
| 管理報表 | 先定義指標與資料欄位，再開放自然語言查詢 | 指標的定義本身 |
| 研發 | 有明確測試、可回復的軟體維護任務 | 需求取捨、架構核定、正式發布 |

<div class="advice" markdown>
用一個下午挑出第一個場景：

1. 請各部門主管各寫三個「每週重複發生、很花時間」的工作，湊成一張候選清單。
2. 每個候選場景用四個問題打分，量不到的先刪掉。
3. 把剩下的放進圖表 5.1 的矩陣，只從「先做」那一格挑一個。
4. 寫下這個場景現在的基準線：每件花多久、錯誤率多少、每週幾件。
5. 指定一位對結果負責的主管，約好 90 天後用同一把尺再量一次。

附錄的「場景挑選畫布」可以直接拿來打分。
</div>

[^nanda]: MIT NANDA,〈The GenAI Divide: State of AI in Business 2025〉。52 個組織訪談、153 位主管問卷、300 多件公開案例；數字多為受訪者自述，作者自稱結論為方向性。https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
[^brynjolfsson]: Brynjolfsson, Li & Raymond,〈Generative AI at Work〉，Quarterly Journal of Economics 140(2)，2025；5,179 名客服人員。https://arxiv.org/abs/2304.11771
[^askhr]: IBM,〈IBM AskHR〉案例頁，2025。廠商數據。https://www.ibm.com/case-studies/ibm-askhr
[^servicenow]: ServiceNow 客戶案例頁。廠商數據。https://www.servicenow.com/workflow/ai/leading-ai-revolution-customers.html
[^11x]: TechCrunch，2025-03-24。媒體報導。https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have
[^mondelez]: Digiday,〈Mondelez takes AI in-house to try and curb marketing costs〉，2025-10。https://digiday.com/marketing/mondelez-takes-ai-in-house-to-try-and-curb-marketing-costs/
[^bcg-gap]: BCG,〈The Widening AI Value Gap〉，2025-09-30；1,250 位高階主管。https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings
[^jagged]: Dell'Acqua 等,〈Navigating the Jagged Technological Frontier〉，Organization Science 37(2)，2026-03；758 名 BCG 顧問。https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/
[^amazon]: Reuters，CNBC 轉載，2018-10-10。https://www.cnbc.com/2018/10/10/amazon-scraps-a-secret-ai-recruiting-tool-that-showed-bias-against-women.html
[^mobley]: Proskauer,〈AI Bias Lawsuit Against Workday Reaches Next Stage〉，2025-06。https://www.proskauer.com/blog/ai-bias-lawsuit-against-workday-reaches-next-stage-as-court-grants-conditional-certification-of-adea-claim
[^cvs]: 中央社,〈超商雙雄拚降工時、減報廢〉，2026-05-02。企業自述。https://www.cna.com.tw/news/afe/202605020024.aspx
[^moea]: 經濟部新聞稿，中小企業 AI 實作專班，2026-01-19。企業自述。https://www.moea.gov.tw/MNS/populace/news/News.aspx?kind=1&menu_id=40&news_id=121637
[^italent]: 經濟部中小及新創企業署委託工研院，中小企業 AI 運用現況調查，母體為員工 10–199 人的企業；經濟部產業發展署 iTALENT 整理，2026-03-16。https://ipd.nat.gov.tw/italent/ePaperD/10/ePaper20260300008
[^grants]: 中企署「提升中小企業智慧化經營效能計畫」115 年受理至 2026-03-10，海基會兩岸經貿網，2026-02-04 https://www.seftb.org/cp-2-2657-e7d79-1.html ；產發署「中小製造業接班傳承 AI 應用數位轉型」受理至 2026-04-27，115 年申請須知，2026-02 https://keid.nat.gov.tw/cloud/Web/UpWebload/C2AE8EB2-2B7E-47AA-BDDA-1E68911EAE6A.pdf
[^vendors]: SAP Joule 產品頁 https://www.sap.com/sea/products/artificial-intelligence/ai-assistant.html ；Workday 新聞室，2025-10-01 https://newsroom.workday.com/2025-10-01-Workday-Completes-Acquisition-of-Paradox ；Salesforce Agentforce 營收，Nasdaq／Zacks https://www.nasdaq.com/articles/crms-agentforce-arr-jumps-330-y-y-it-next-growth-engine 。均為廠商資訊。
[^intercom]: Intercom 計價說明頁。廠商資訊。https://www.intercom.com/learning-center/intercom-pricing
