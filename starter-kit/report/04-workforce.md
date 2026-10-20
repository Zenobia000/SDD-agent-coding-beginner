<div class="part" markdown>
<span class="kicker">第二部　五個決策</span>

**AI 能不能走出試點，取決於五個決策：人怎麼安排、先做哪裡、護欄怎麼設、agent 怎麼管、成效怎麼量**

第 4–8 章
</div>

# 第 4 章　決策一 人力政策：控制增量、保住品質底線，比削減人力更快拿到回報

<p class="lede">員工敢不敢把 AI 用進工作，看的是公司怎麼處理人力。目前的證據顯示，AI 的衝擊先落在少招新人，資深員工還沒有缺口；先裁人再驗證的企業，多半要走回頭路。比較穩的做法是控制增量：把目標訂成人數持平、處理量上升，同時重新設計新人的學習方式。</p>

## 衝擊先落在新鮮人的招募，資深員工目前還沒有缺口

史丹佛數位經濟實驗室用 ADP 的薪資資料追蹤每月 350 萬到 500 萬名美國勞工，發現 22 到 25 歲、在 AI 曝險最高職業工作的年輕人，就業低於「如果跟上低曝險同儕」應有的水準；資深勞工沒有同樣的缺口。缺口主要來自企業少招年輕人，裁員和離職沒有明顯增加。AI 被拿來「取代」任務的職業，年輕人就業往下走；被拿來「輔助」的職業，就業持平或上升。[^canaries]

這份研究已經改版數次，各版本的估計值不同，作者也明說這是早期的描述性指標，不是因果估計。本報告只引用方向，不引用單一百分比。

另外兩份研究看到同一個方向。Anthropic 用自家使用資料衡量職業曝險，發現高曝險職業的失業率沒有系統性上升，但 22 到 25 歲的人進入這些職業的求職成功率下降了；25 歲以上沒有類似變化。[^anthropic-labor] 另一組學者用 LinkedIn 履歷資料比較約 28.5 萬家美國企業，採用生成式 AI 的企業，初階員工人數相對下降，資深員工持續增加，主因同樣是招募變慢。[^hosseini]

```exhibit
{"id": "4.1", "type": "bar", "unit": "%",
 "title": "22 到 25 歲的人進入 AI 高曝險職業的求職成功率下降，25 歲以上沒有變化",
 "data": [
   {"label": "22–25 歲，進入最高曝險職業", "value": -14, "highlight": true},
   {"label": "25 歲以上", "value": 0, "display": "無明顯下降"}
 ],
 "source": "Anthropic，Labor market impacts of AI: A new measure，2026-03-05；美國勞工資料",
 "note": "相對 2022 年的每月求職成功率；廠商研究，作者自稱早期、暫定，僅勉強達統計顯著"}
```

**這代表什麼**：如果你的公司這一兩年「少招了一些新人」，這本身就是一項 AI 人力政策，只是沒有人寫下來。它的代價要五年後才看得到：今天沒有招的初階員工，就是五年後找不到的中階骨幹。

## 先裁人再驗證是最貴的順序，澳洲聯邦銀行和 Klarna 都走了回頭路

把 AI 當成裁員的理由，是目前最常被收回的決策。

<div class="case" markdown>
**澳洲聯邦銀行：裁了 45 個客服職位，一個月後道歉撤回**

2025 年 7 月，澳洲聯邦銀行以語音機器人讓職位多餘為由，裁撤 45 個客服職位。工會向勞資委員會提出爭議，指出機器人上線後來電量反而上升，主管還得加班接電話。8 月 21 日，銀行承認這些職位並不多餘，公開道歉並撤回裁員。[^cba]
</div>

Klarna 是另一個常被引用的例子。2024 年，它宣布 AI 客服助理第一個月就處理了約三分之二的客服對話，相當於 700 名全職客服的工作量。[^klarna] 一年後，執行長承認當初「成本的權重太高」，結果是服務品質下降，於是改成保證客戶隨時找得到真人。[^klarna-back] Klarna 沒有放棄 AI，2025 年第三季仍表示 AI 助理做了超過 853 名全職人力的工作。[^klarna-853] 它修正的是品質底線，AI 本身沒有撤掉。

Gartner 預測，到 2027 年，原本打算靠 AI 大幅縮編客服的組織，有一半會放棄這個計畫；它在 2025 年 3 月調查的 163 位主管裡，95% 打算保留真人客服。[^gartner-cs] 這是預測，不是實測，但方向和上面兩個個案一致。

**這代表什麼**：AI 能做多少，要上線後量過才知道。先裁人，等於在還沒有證據時就押上品質和員工信任；押錯了，撤回的成本比當初省下的多。

## 把目標訂成人數持平、處理量上升，再用自然流失調整人力

比較穩的做法是控制增量：不動現有的人，管住新增的人。

Shopify 是這條路最清楚的例子。執行長 2025 年的內部信規定，團隊申請加人或資源之前，要先說明為什麼 AI 做不到；AI 使用也納入績效評核。[^shopify] 第 3 章提過，它沒有用 AI 為由裁員，人數靠自然流失慢慢調整，反彈很小。

控制增量有三個好處：

- **員工比較敢用。** 用 AI 做出成績不會讓自己或同事丟工作，隱藏使用的理由就少了一個。
- **有時間驗證。** 人力沒先砍，AI 做不好時還有人接手，品質底線守得住。
- **新手的效益最大。** 客服研究裡，AI 讓新手每小時多解決 34% 的問題，也提高了留任率。[^brynjolfsson] 處理量上升的空間，多半在新人身上。

轉型做得越深，越要先把人力政策講清楚。BCG 的調查發現，全面重新設計流程的公司，員工擔心工作保障的比例是 46%，沒有重新設計的公司是 34%。[^bcg-work] 流程改得越多，員工越會問「那我呢」，這個問題要在動工之前回答。

**我們的建議**：在驗證期內，不以 AI 為由裁員；新增人力前，先評估 AI 能不能做；AI 省下的時間用在哪裡，由主管和團隊一起決定，寫進季度目標。

## 少招新人會斷掉人才梯隊，新人的學習方式要重新設計

控制增量會壓縮初階招募，這是同一件事的另一面。企業可以少招新人，但要回答五年後的中階從哪裡來。

答案的一半在招募，另一半在新人怎麼學。Anthropic 讓 52 名以初階為主的工程師學一個新的程式庫，隨機分成可以用 AI 和不能用 AI 兩組。用 AI 的那組，理解測驗平均 50%，手寫組 67%，差距最大的是除錯題。[^anthropic-learn] 差別出在用法：

```exhibit
{"id": "4.2", "type": "column", "unit": "%",
 "title": "新人學新技術時全交給 AI，理解測驗不到四成；邊用邊追問的人有六成五以上",
 "data": [
   {"label": "全部交給 AI 寫、用 AI 除錯", "value": 40, "display": "< 40%"},
   {"label": "先讓 AI 產生，再追問、要求解釋、自己除錯", "value": 65, "display": "≥ 65%", "highlight": true}
 ],
 "source": "Anthropic，How AI assistance impacts the formation of coding skills，2026-01-29；52 名初階為主的軟體工程師，隨機對照實驗",
 "note": "樣本小，只量當下理解，不代表長期技能保留"}
```

訓練也要給得夠。BCG 調查 11 國一萬多名員工，受過 5 小時以上訓練、而且有面對面教練的人，固定使用 AI 的比例明顯較高；但只有約三分之一的人說自己受過適當訓練。[^bcg-work]

台灣的落差更明顯。員工想學，公司沒教：

```exhibit
{"id": "4.3", "type": "bar", "unit": "%",
 "title": "台灣上班族多數想學 AI 卻還沒開始，近半企業沒有任何 AI 培訓計畫",
 "data": [
   {"label": "希望企業提供 AI 培訓課程", "value": 71.8},
   {"label": "想學 AI 但還沒開始", "value": 58.9},
   {"label": "企業沒有任何 AI 人才培訓計畫", "value": 44.7},
   {"label": "已經積極學習 AI", "value": 14.2, "highlight": true}
 ],
 "source": "1111 人力銀行 × 臺北市勞動局，2026 上班族 AI 焦慮與職涯準備調查，2026-08-17；人工智慧科技基金會，2026 台灣產業 AI 化大調查，228 家企業",
 "note": "第一、二、四項為上班族調查，第三項為企業調查，母體不同；1111 調查未揭露樣本數"}
```

想學但沒開始的人，最常說的原因是「不知道從哪裡開始」（56.9%）。[^1111] 中小企業的人才需求也指向同一個方向：有人才需求的企業裡，74.8% 要的是初階應用人才。[^italent] 對多數台灣企業來說，在職培訓比招募專家更實際。

**這代表什麼**：新人的養成計畫要改寫。舊做法是讓新人從重複的基礎工作做起，慢慢累積判斷力；這些工作現在很多交給 AI 了。新的做法要把「驗收 AI 的產出」變成新人的基本功：讓他們用 AI，但要求解釋、自己除錯、跟資深同事對答案。

## 高層、中階主管、員工、新鮮人各有一件最該先做的事

Microsoft 2026 年調查兩萬名 AI 使用者，和 AI 成效相關的因素裡，組織因素的關聯約是個人因素的兩倍（67% 對 32%）。[^wti] 所以人力政策不能只交給人資，每一層都有自己的那一件事。

中階主管是最常被跳過的一層，影響卻最直接。成熟團隊和一般團隊差最多的三件事，都是主管的行為：

```exhibit
{"id": "4.4", "type": "bar", "unit": "%",
 "title": "AI 成熟團隊的主管更常公開使用 AI、訂品質標準、留實驗空間",
 "data": [
   {"label": "公開使用 AI｜成熟團隊", "value": 85, "highlight": true},
   {"label": "公開使用 AI｜一般團隊", "value": 64},
   {"label": "訂 AI 產出品質標準｜成熟團隊", "value": 83, "highlight": true},
   {"label": "訂 AI 產出品質標準｜一般團隊", "value": 57},
   {"label": "留出實驗空間｜成熟團隊", "value": 84, "highlight": true},
   {"label": "留出實驗空間｜一般團隊", "value": 61}
 ],
 "source": "Microsoft Work Trend Index 2026，2026-05-05；10 個市場 2 萬名使用 AI 的知識工作者",
 "note": "廠商調查；成熟團隊指 Microsoft 定義的 Frontier Professionals，占 AI 使用者 16%"}
```

| 角色 | 最該先做的一件事 | 依據 |
|---|---|---|
| **高層** | 寫下人力政策並公開說明：AI 省下的人力怎麼用、驗證期內會不會因 AI 裁員；自己先公開用 AI | 只有 26% 員工認為領導層在 AI 上清楚一致，只有 13% 相信嘗試失敗會被肯定 [^wti]；有強力領導支持時，對 AI 持正面態度的員工從 15% 升到 55% [^bcg-work] |
| **中階主管** | 在團隊裡公開用 AI，訂出 AI 產出的品質標準，並留出試錯的時間 | 成熟團隊與一般團隊在這三件事上差 20 個百分點以上（圖表 4.4）[^wti] |
| **員工** | 動手前先決定哪些交給 AI、哪些自己做，並量一次前後差別，不靠感覺 | 成熟的使用者動手前先分工的比例是 53%，一般使用者 33% [^wti]；資深工程師自覺快 20%，實測慢 19% [^metr] |
| **新鮮人** | 用 AI 時要求解釋、自己除錯，練出驗收 AI 產出的能力 | 追問理解的人測驗 ≥ 65%，全交給 AI 的人 < 40%（圖表 4.2）[^anthropic-learn]；台灣雇主 76% 把批判性思考與事實查核列為 AI 時代最重要的技能 [^rw] |

【桑尼現場：待補】企業內訓時，員工最常私下問的人力問題，以及主管怎麼回答之後團隊的使用率有沒有改變。

<div class="advice" markdown>
用五個問題檢查你的人力政策是否已經寫清楚：

1. 員工問「用 AI 會不會讓我被裁」時，每位主管的回答一樣嗎？
2. 驗證期內，公司會不會以 AI 為由裁員？這句話有沒有寫下來？
3. 申請新增人力時，有沒有一欄要說明「AI 為什麼做不到」？
4. 新人的前三個月，有沒有一項訓練是「驗收 AI 的產出」？
5. 每位員工每年有沒有至少 5 小時、有人帶的 AI 訓練？

答不出來的題目，就是下一次主管會議的議程。
</div>

[^canaries]: Brynjolfsson, Chandar & Chen, Stanford Digital Economy Lab,〈Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI〉，2025-08 首版，最新修訂版資料至 2026-06；ADP 薪資行政資料，每月 350 萬至 500 萬名美國勞工。作者自稱早期描述性指標，非因果估計。https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial
[^anthropic-labor]: Anthropic,〈Labor market impacts of AI: A new measure〉，2026-03-05；美國勞工。廠商研究，作者自稱早期、暫定。https://www.anthropic.com/research/labor-market-impacts
[^hosseini]: Hosseini & Lichtinger,〈Generative AI as Seniority-Biased Technological Change〉，working paper，未經同儕審查；Revelio Labs 履歷與職缺資料，約 6,200 萬名勞工、28.5 萬家美國企業，2015–2025。https://digitaleconomy.stanford.edu/event/seyed-m-hosseini-and-guy-lichtinger-generative-ai-as-seniority-biased-technological-change-evidence-from-u-s-resume-and-job-posting-data
[^cba]: ABC News,〈CBA backtracks on AI job cuts, apologises for error〉，2025-08-21。媒體報導。https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-apologises-for-error/105679492
[^klarna]: Klarna 新聞稿，2024-02-27。公司自述。https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
[^klarna-back]: Fortune，2025-05-09。https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/
[^klarna-853]: CX Dive,〈Klarna says AI agent does work of 853 employees〉，2025-11。法說會公司自述。https://www.customerexperiencedive.com/news/klarna-says-ai-agent-work-853-employees/
[^gartner-cs]: Gartner 新聞稿，2025-06-10；2025-03 調查 163 位客服主管。屬預測，非實測。https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai
[^shopify]: TechCrunch,〈Shopify CEO tells teams to consider using AI before growing headcount〉，2025-04-07。https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/
[^brynjolfsson]: Brynjolfsson, Li & Raymond,〈Generative AI at Work〉，Quarterly Journal of Economics 140(2)，2025；5,179 名客服人員。34% 為 working paper 版本數字。https://arxiv.org/abs/2304.11771
[^bcg-work]: BCG,〈AI at Work 2025: Momentum Builds, but Gaps Remain〉，2025-06-26；11 國 10,600 多人。https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
[^anthropic-learn]: Anthropic,〈How AI assistance impacts the formation of coding skills〉，2026-01-29；52 名以初階為主的軟體工程師，隨機對照實驗。https://www.anthropic.com/research/AI-assistance-coding-skills
[^1111]: 1111 人力銀行 × 臺北市勞動局，〈2026 上班族 AI 焦慮與職涯準備調查〉，2026-08-17；樣本數與調查期間未揭露。https://www.1111.com.tw/news/167165/amp/ ；人工智慧科技基金會，2026 台灣產業 AI 化大調查，228 家企業，樣本偏向較積極的企業。經理人，2026-05-04。https://www.managertoday.com.tw/articles/view/72095
[^italent]: 經濟部中小及新創企業署委託工研院，中小企業 AI 運用現況調查，母體為員工 10–199 人的企業；經濟部產業發展署 iTALENT 整理，2026-03-16。https://ipd.nat.gov.tw/italent/ePaperD/10/ePaper20260300008
[^wti]: Microsoft,〈2026 Work Trend Index: Agents, human agency, and the opportunity for every organization〉，2026-05-05；10 個市場 2 萬名使用 AI 的知識工作者。廠商調查。https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
[^metr]: METR,〈Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity〉，2025-07-10；16 位資深開發者、246 個任務。https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[^rw]: Robert Walters,〈未來職務洞察〉，近 5,000 名亞洲專業人士與雇主；104 職場力轉載經濟日報，2026-08-31。https://blog.104.com.tw/?p=250253
