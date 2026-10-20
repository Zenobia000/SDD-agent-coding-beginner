# 前沿 AI vs. 一般企業導入的落差：為什麼企業推不動

> 研究日期：2026-10-20。
> 研究限制（先講清楚）：本輪 WebSearch 額度在中途用完，後半段改用 WebFetch 直接開已知的原始頁面。McKinsey 2026 的 PDF、Gartner 新聞稿、CanLII／CBC／CNBC／The Verge／Guardian 都擋爬蟲（403 或逾時），這幾筆只能引用二手報導或 Wikipedia 轉述，並且已逐條標註。
>
> **可信度分級**（每條事實後面都會標一個）：
> - 【研究】有公開方法、樣本或行政資料的學術或研究機構產出（NBER、Stanford、RAND、METR）
> - 【廠商數據】模型廠商用自家流量或客戶資料做的分析（Anthropic、OpenAI、Microsoft）。資料是真的，但樣本只限自家用戶，而且廠商有利益關係
> - 【顧問調查】顧問公司對高階主管的問卷（McKinsey、BCG、Deloitte、IBM IBV、Gartner、S&P）。回答的是受訪者「自認」的成效，不是經過稽核的財務數字
> - 【媒體】新聞報導
> - 【個案】單一公司事件，可以拿來舉例，不能推論到整體
> - ⚠️ 未驗證：找不到原始出處，或原文打不開

---

## 一句話結論

模型能力與個人採用都在快速上升（88–89% 組織「有在用」），但能在企業層級看到 EBIT 的只有約 37%，真正靠 AI 賺到錢的高績效者約 6%，比例兩年沒變。中間卡住的不是模型，主要是組織：流程沒有重新設計、資料與脈絡接不進去、治理與責任歸屬不清、員工不信任或不敢用。BCG 估計 AI 導入的困難約 70% 屬於人與流程。

---

## 1. 2025–2026 實際影響：可信數據

### 1.1 採用很廣，價值很窄

| 指標 | 數字 | 來源與可信度 | 樣本與限制 |
|---|---|---|---|
| 組織 AI 採用率 | 2025 年 88%（2023 年 55%）；GenAI 在至少一個職能使用 70% | [Stanford HAI AI Index 2026 – Economy](https://hai.stanford.edu/ai-index/2026-ai-index-report/economy)（2026-04）【研究彙整】 | AI Index 是二手彙整，採用率底層來自問卷（推測為 McKinsey，網頁未指名）。「有在用」不等於「有效益」 |
| AI agent 部署 | 幾乎所有職能都還是個位數 % | 同上【研究彙整】 | — |
| 生產力 | 客服 +14–15%、軟體開發 +26%、行銷產出 +50%；需要深度推理的任務增益較小 | 同上【研究彙整】 | 多為特定任務的實驗，不能直接外推到全公司 |
| 年輕勞工 | 美國 22–25 歲軟體開發者就業比 2024 年少近 20% | 同上【研究彙整】 | — |
| 年輕勞工（原始研究） | AI 高曝險職業中 22–25 歲就業比同齡低曝險者「應有水準」低 19%；衰退集中在 AI 偏向「取代」的職業，「輔助」型職業持平或上升 | [Brynjolfsson, Chandar, Chen – Canaries in the Coal Mine?](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/)（2025-08 初版，2026-08-12 修訂）【研究】 | ADP 薪資行政資料，美國數百萬勞工，資料到 2026-06。屬相關性分析 |
| 勞動市場整體 | 丹麥資料估出工資與工時的效果是「精確的零」，排除兩年內 >2% 的效果 | [Humlum & Vestergaard, NBER w33777](https://www.nber.org/papers/w33777)（2025-05，2026-03 修訂）【研究】 | 丹麥行政資料 × 採用問卷。可以拿來對照「個人覺得有幫助」與「總體數字還沒動」 |
| 事故 | 有記錄的 AI 事故 2025 年 362 件（2024 年 233 件） | [Stanford HAI AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)（2026-04）【研究彙整】 | 只算被公開記錄的事件 |
| 民間投資 | 美國民間 AI 投資 2025 年 2,859 億美元，中國 124 億美元 | 同上【研究彙整】 | — |

### 1.2 顧問公司調查：EBIT 卡在三分之一

- **McKinsey State of AI 2025**：88% 在至少一個職能固定使用 AI（前一年 78%）；只有 39% 回報企業層級 EBIT 影響；近三分之二還沒開始在全企業規模化；62% 至少在試驗 AI agent。[McKinsey – The state of AI in 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)（2025-11）【顧問調查】
- **McKinsey State of AI 2026「On the road to ROI」**（約 2026-08）【顧問調查】，⚠️ McKinsey PDF 逾時打不開，以下數字取自二手報導：
  - 採用 89%（幾乎沒漲）；在全企業規模化的比例從 38% 升到 44%
  - 回報任何 EBIT 貢獻的 37%，跟去年差不多
  - 高績效者（AI 貢獻 ≥5% EBIT）約 6%，持平
  - 約 80% 說 AI 提升個人生產力
  - 近四分之三的高績效者從根本重新設計工作流程，其他受訪者約四分之一
  - 營收 >10 億美元的企業有 40% 在規模化 agent（去年 27%），小型組織持平在 22%
  - 約 20% 說 AI 營運成本（含 token）限制了使用
  - 去年預期裁員的有 32%，實際回報因 AI 減少人力的只有 14%
  - 方法：2026-05-04～06-08 線上問卷，1,719 份，97 國，依 GDP 加權
  - 來源：[TechTarget – Enterprise AI got better, but the ROI didn't](https://www.techtarget.com/it-strategy/opinion/Enterprise-AI-got-better-but-the-ROI-didnt)（2026-09-25）【媒體】、[McKinsey chart – AI job losses fall short of forecasts](https://www.mckinsey.com/featured-insights/charts/ai-job-losses-fall-short-of-forecasts)【顧問調查】、[McKinsey PDF](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/the-state-of-ai-in-2026-on-the-road-to-roi.pdf)（未能開啟）
  - 限制：衡量的是受訪者「歸因給 AI」的效果，不是經過稽核的財報
- **BCG《The Widening AI Value Gap》**：5% 是「future-built」，35% 是 scalers，60% 是 laggards（營收與成本幾乎沒有改善）。future-built 對 laggards：營收成長 1.7 倍、三年 TSR 3.6 倍、EBIT margin 1.6 倍；AI 潛在價值有 70% 集中在核心職能（銷售行銷、製造、供應鏈、定價），IT 只佔 13%；agent 佔 2025 年 AI 價值 17%，預估 2028 年 29%。[BCG press release](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings)（2025-09-30）【顧問調查】。樣本：1,250 位高階主管，9 個產業，以 41 項能力評估成熟度。限制：成熟度分組跟財務表現之間是相關，不是因果
- **BCG 2024 前一版**：74% 公司還沒從 AI 看到具體價值，4% 達到前沿。**10-20-70 原則**：領先者把 10% 資源放在演算法、20% 放在技術與資料、70% 放在人與流程；導入困難約 70% 屬於人與流程。[BCG press release](https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value)（2024-10-24）【顧問調查】。樣本：1,000 位 CxO，59 國
- **IBM CEO Study 2025**：過去幾年的 AI 專案只有 25% 達到預期 ROI，16% 擴展到全企業；50% 說技術片段、彼此不相連；64% 承認因為怕落後，在搞清楚價值前就先投資。[IBM Newsroom](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles)（2025-05-06）【顧問調查】。樣本：2,000 位 CEO，33 國，2025 年 2–4 月，IBV × Oxford Economics
- **Deloitte State of AI in the Enterprise 2026**：66% 回報生產力或效率提升，但只有 20% 已經靠 AI 增加營收（74% 希望能做到）；「員工技能不足」是把 AI 整合進流程最大的障礙；只有五分之一的公司有成熟的 autonomous agent 治理模式。[Deloitte](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-generative-ai-in-enterprise.html)（2026，問卷 2025 年 8–9 月）【顧問調查】。樣本：3,235 位主管，24 國
- **S&P Global Market Intelligence**：放棄大部分 AI 專案的公司 2025 年 42%（2024 年 17%）；POC 平均有 46% 在上線前被砍；主因是成本、資料隱私與資安風險。[CIO Dive](https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/)（2025-03-14）【媒體轉述顧問調查】。樣本：北美與歐洲 1,000+ 人
- **Gartner（預測，不是量測）**：到 2027 年底，超過 40% 的 agentic AI 專案會因為成本失控、商業價值不明或風險控管不足而被取消；所謂 agentic 廠商數千家裡只有約 130 家是真的，其餘是「agent washing」；2025 年 1 月網路研討會投票（3,412 人）19% 已大量投資 agentic AI。[Gartner Newsroom](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)（2025-06-25）【顧問預測】。⚠️ Gartner 原頁 403，內容以多家二手報導交叉比對，數字一致。投票樣本是研討會聽眾，不具代表性
- **Gartner 前作**：到 2025 年底，至少 30% 的 GenAI 專案會在 POC 後被放棄（2024-07-29）。⚠️ 未驗證：原頁 403，僅憑記憶與標題，沒有二手報導可以核對

### 1.3 MIT NANDA「GenAI Divide」：95% 的說法與爭議

**原文說法**（已下載 PDF 核對）：
- 執行摘要寫的是「**95% of organizations are getting zero return**」，同一段又寫「Just 5% of integrated AI pilots are extracting millions in value」。也就是說，原文自己就在「組織」與「試點」兩種分母之間混用；媒體多數報成「95% 試點失敗」
- 另一個口徑：task-specific GenAI 工具 60% 被調查過、20% 進到試點、**5% 成功上線**；成功的定義是「使用者或主管認為造成明顯且持續的生產力或 P&L 影響」
- 方法：檢視 300+ 件公開 AI 專案、訪談 52 個組織、在 4 場產業研討會收集 153 位主管問卷；ROI 在試點後 6 個月衡量
- 其他發現：
  - 只有 40% 公司買了官方 LLM 訂閱，但 90%+ 公司的員工有在用個人 AI 工具（shadow AI）
  - 向外部夥伴購買或共同開發的上線率約 67%，自建約 33%
  - GenAI 預算一半以上流向銷售與行銷，但 ROI 最高的是後勤（back-office）自動化
  - 中型企業從試點到全面導入平均 90 天，大企業要 9 個月以上
  - 主要障礙依序是變革管理困難、缺乏高層支持、使用體驗差、模型輸出品質疑慮、不願意用新工具
- 來源：[MIT NANDA – The GenAI Divide: State of AI in Business 2025（PDF）](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)（v0.1，PDF metadata 2025-07；媒體 2025-08 報導）【研究機構報告，但方法偏弱】；[Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)（2025-08-18）【媒體】

**爭議**（白皮書引用時要一起交代）：
1. **報告自己承認**「directionally accurate based on individual interviews rather than official company reporting」，而且「success definitions may differ across organizations」
2. **樣本**：52 個組織加研討會問卷，作者也承認有自我選擇偏誤
3. **時間窗**：只看 6 個月，作者自己寫可能「understating success rates」
4. **分母混用**：組織、試點、工具三種分母都有出現
5. **外界批評**：BigDATAwire 等報導批評者稱報告「overhyped or methodologically weak」；有評論者質疑 MIT 教職員參與的程度（主作者 Aditya Challapally 的背景）。[BigDATAwire](https://www.bigdatawire.com/?p=89626)【媒體】。⚠️ 主作者任職背景只見於評論文章，沒有查到一手資料
6. **另一件 PDF 上的事實**：PDF metadata 的敏感度標籤是「Privileged」，顯示這是 v0.1 初稿

**白皮書建議用法**：不要寫「95% AI 專案失敗」。可以寫「MIT NANDA 的初步研究訪談 52 個組織，認為只有約 5% 的客製化 GenAI 工具在 6 個月內做出可量測的 P&L 影響」，並附上限制。

### 1.4 廠商數據：個人用得很兇，企業接不上

- **OpenAI《The state of enterprise AI》**：ChatGPT Enterprise 使用者自述每個活躍日省下 40–60 分鐘，重度使用者每週超過 10 小時；75% 說速度或品質有提升；第 95 百分位的「frontier 員工」訊息量是中位數員工的 6 倍，frontier 企業每個座位的訊息量是 2 倍。[OpenAI](https://openai.com/index/the-state-of-enterprise-ai-2025-report/)（2025-12）【廠商數據＋自述問卷】。⚠️ 原頁 403，數字取自搜尋摘要；發布日期有 12 月 8 日與 17 日兩種說法，未核實。限制：只有付費企業客戶，省時是自述
- **Microsoft Work Trend Index 2025**：
  - 24% 的主管說已在全組織部署 AI，12% 還停在試點
  - 53% 主管說生產力必須提高，80% 勞動力說沒有足夠時間或精力把工作做完
  - 主管 67% 熟悉 AI agent，員工只有 40%
  - 每天約 275 次干擾
  - 來源：[Microsoft WorkLab](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)（2025-04-23）【廠商數據】。樣本：31 國 31,000 人（Edelman），加上 M365 遙測與 LinkedIn 資料。限制：Microsoft 銷售 Copilot，有利益關係
- **Anthropic Economic Index（2025-09）**：
  - 企業 API 約 77% 是自動化模式（Claude.ai 約一半）
  - 複雜任務的部署「可能更受限於資訊取得，而不是模型能力」；資料分散或沒數位化的公司會很難部署
  - 價格敏感度低：成本增加 1%，使用量只降約 0.29%
  - 來源：[Anthropic](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)（2025-09-15）【廠商數據】。樣本：2025-08 的 100 萬筆 API transcript
- **Anthropic Economic Index（2026-01）**：
  - API 任務成功率從「人類 1 小時以內的任務」約 60%，降到「5 小時以上的任務」約 45%；API 整體成功率 49%，Claude.ai 67%
  - 以成功率校正後，對美國年勞動生產力成長的估計從 1.8 個百分點減半到約 1.0
  - 來源：[Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)（2026-01-15）【廠商數據】
- **Anthropic Economic Index（2026-06「Cadences」）**：約 9,700 位使用者的問卷，86% 回報速度提升、69% 回報品質提升，只有 27% 回報成本節省。[Anthropic](https://www.anthropic.com/research/economic-index-june-2026-report)（2026-06-26）【廠商數據】。限制：作者自己說樣本不具代表性，偏向電腦、數學與管理職

### 1.5 反證：個人「覺得」變快，不代表真的變快

- **METR**：16 位資深開源開發者、246 個真實 issue，開放使用 AI 後**慢了 19%**；開發者事前預期快 24%，事後仍覺得快了 20%。[METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)（2025-07-10）【研究，RCT】。限制：樣本小，用的是 2025 年初的工具；METR 已在 2026-02 發布後續研究，並說這份結果已經過時
- **Workslop**：HBR 提出「AI 生成的表面工作」會把整理成本轉嫁給同事。[HBR – AI-Generated "Workslop" Is Destroying Productivity](https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity)（2025-09-22）【研究者投書】。⚠️ 文中常被引用的比例與每次耗時，因付費牆無法核實，不引用數字

---

## 2. 企業卡住的根因（四類）

### 2.1 人與文化：官僚、恐懼、誘因

**證據**
- **導入困難大多屬於人與流程**：約 70% 的 AI 導入困難是人與流程問題。[BCG](https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value)（2024-10-24）【顧問調查】
- **第一線停在一半（silicon ceiling）**：
  - 主管與經理四分之三以上每週用 GenAI 好幾次，第一線員工的固定使用率卡在 51%
  - 只有約三分之一員工說受過足夠訓練；受過 5 小時以上訓練並有面對面指導的人，使用率明顯較高
  - 在做全面 AI 流程再造的公司，46% 員工擔心工作不保（其他公司 34%）
  - 缺工具的員工有一半以上說會自己找替代工具來用
  - 來源：[BCG AI at Work 2025](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)（2025-06-26）【顧問調查，11 國 10,600+ 人】
- **主管與員工的認知落差**：主管熟悉 AI agent 的比例 67%，員工 40%；每天省 1 小時以上的主管 29%，員工 20%。[Microsoft WTI 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)（2025-04-23）【廠商數據】
- **因為怕落後而投資**：64% 的 CEO 說，怕落後讓他們在搞清楚價值前就先投資。[IBM CEO Study](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles)（2025-05-06）【顧問調查】。這是「試點很多、擴展很少」的源頭之一
- **影子 AI 反映的是信任與體驗，不是禁令有效**：90%+ 公司的員工在用個人 AI，只有 40% 公司有官方訂閱；使用者覺得公司買的工具「rigid」，寧可用 20 美元的 ChatGPT。[MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)（2025-07/08）【研究機構報告】
- **頭痛醫頭的動機**：年輕人在「取代型」職業的就業下降。[Canaries](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/)（2026-08 修訂）【研究】。員工的恐懼不是沒有根據的，教材不應淡化

**個案**
- **Klarna：以成本為主的客服自動化，部分回頭**
  - 2024-02：AI 助理第一個月處理 230 萬則對話，約三分之二的客服對話，相當於 700 名全職客服；解決時間從 11 分鐘降到 2 分鐘以內；預估 2024 年獲利改善 4,000 萬美元。[Klarna press](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)（2024-02-27）【個案，公司自述】
  - 2025-05：CEO Siemiatkowski 接受 Bloomberg 訪問，承認當初「成本的權重太高」，結果是「lower quality」；改成保證客戶「永遠可以找到真人」，並試辦 Uber 式的遠端彈性真人客服。[Fortune](https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/)、[CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/)（2025-05-09）【媒體】
  - 但不是全面撤回：公司說仍然「AI-first」，而且員工人數從 2022 年 5,527 人降到 2,907 人。[Guardian 經 Wikipedia 轉引](https://www.theguardian.com/business/2025/nov/18/buy-now-pay-later-klarna-ai-helped-halve-staff-boost-pay)（2025-11-18）【媒體】，⚠️ Guardian 原文沒有直接開啟
  - 正確敘事：品質底線與「保留真人選項」被重新放回設計裡，不是「AI 失敗」
- **Duolingo「AI-first」備忘錄的反彈**：
  - 2025-04 CEO von Ahn 的全員信說，AI 能做的工作會逐步停止外包，寧可「接受偶爾的品質小損失，也不要動作太慢」
  - 社群強烈反彈，用戶取消訂閱並中斷連續學習紀錄；Duolingo 一度清空 Instagram 與 TikTok 影片，CEO 隨後出面澄清
  - 2025-08 財報會議上，CEO 說對財務指標的影響「不太顯著（not very material）」
  - 來源：[Wikipedia – Duolingo](https://en.wikipedia.org/wiki/Duolingo)（彙整多家報導）【媒體二手】。⚠️ The Verge 與 LinkedIn 原文沒能開啟，備忘錄全文未核實
  - 教訓：對外宣示「AI 取代人」會變成品牌風險；內部動員的語言要跟對外溝通分開
- **Commonwealth Bank of Australia（CBA）撤回 AI 裁員**：
  - 2025-07 以「語音機器人讓職位多餘」為由裁撤 45 個客服職位
  - 工會（FSU）向 Fair Work Commission 提出爭議，指出機器人上線後來電量反而上升，主管還得加班接電話
  - 2025-08-21 CBA 承認這些職位並非多餘，並道歉
  - 來源：[ABC News](https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-apologises-for-error/105679492)（2025-08-21）【媒體】
  - 教訓：先砍人、後驗證效果，是最貴的順序
- **IBM**：Krishna 2023 年說後勤職位暫停招募、2025 年說 AI 取代約 200 名 HR 但整體人數增加。⚠️ 未驗證：原始報導（Bloomberg、WSJ）無法開啟，不要引用數字。可以引用的是 IBM 自己的 CEO 調查（見上）

### 2.2 治理與流程：審批、法遵、採購、責任歸屬

**證據**
- **治理成熟度落後於 agent 部署**：只有五分之一公司有成熟的 autonomous agent 治理模式；由高層主導 AI 治理的組織看到的商業價值顯著較高。[Deloitte 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-generative-ai-in-enterprise.html)【顧問調查】
- **成本、隱私、資安是砍案主因**：[S&P Global via CIO Dive](https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/)（2025-03-14）【媒體轉述調查】
- **成本失控與風險控管不足是 agent 專案被取消的主因（預測）**：[Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)（2025-06-25）【顧問預測】；約 20% 組織說 token 等營運成本限制了使用（McKinsey 2026，⚠️ 二手）
- **採購與組織設計**：
  - 購買或合作的上線率約 67%，自建約 33%
  - 成功的組織「下放執行權但保留問責」，不等中央審批完美用例
  - 大企業試點數最多，但試點轉擴展的比例最低（要 9 個月以上，中型企業 90 天）
  - 來源：[MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)【研究機構報告，自述數據】
  - 作者也提醒：差異可能來自組織能力本身，不一定是採購方式造成的
- **跨部門筒倉與風險趨避**是 CEO 自己點名的障礙。[IBM CEO Study](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles)（2025-05-06）【顧問調查】

**個案：責任歸屬**
- **Moffatt v. Air Canada（2024 BCCRT 149）**：
  - 官網聊天機器人告訴旅客，喪親票價可以事後 90 天內申請退差價，但實際政策不允許
  - Air Canada 主張聊天機器人是「a separate legal entity that is responsible for its own actions」，仲裁人稱這個論點「remarkable」並駁回
  - 判定公司對網站上所有資訊負責，構成過失不實陳述，賠償 CA$812 加上費用與利息
  - 2024-02-14，BC 省民事解決仲裁庭
  - 來源：[Wikipedia – Moffatt v. Air Canada](https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada)【二手彙整，附判決連結】；[判決原文](https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do)（⚠️ 403，未直接開啟）
  - 教訓：**AI 說的話就是公司說的話**，法遵審查要涵蓋輸出，不能只審合約
- **NYC MyCity 聊天機器人**（建在 Microsoft Azure AI 上）教小商家違法：可以拒收 Section 8 租客、可以抽員工小費、可以拒收現金等。[The Markup](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)（2024-03-29）【媒體調查】
- **Deloitte Australia**：
  - 2025-07 交給澳洲政府一份 A$440,000 的報告，2025-10 被發現有不存在的學術引用與捏造的判決引文
  - Deloitte 改版重交並部分退款
  - 2025-11 加拿大紐芬蘭省一份 CA$1.6M 的報告也被指出有假引用
  - 來源：[Wikipedia – Hallucination (AI)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))【二手彙整】。⚠️ 退款金額與原始報導沒有直接核對
  - 教訓：顧問業本身也栽在「沒有人工驗證流程」

### 2.3 資料：品質、孤島、權限、脈絡

**證據**
- **缺的是脈絡，不是模型**：Anthropic 的分析認為，複雜任務的部署可能更受限於「資訊取得」而非模型能力；資料分散或沒數位化的公司會很難部署。[Anthropic Economic Index](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)（2025-09-15）【廠商數據】
- **RAND：AI 專案失敗的五大根因**：
  1. 問題定義錯或溝通錯（最常見）
  2. 缺乏足夠的資料
  3. 追技術、不追問題
  4. 資料與部署基礎設施不足
  5. 用 AI 處理它解決不了的問題
  - 也引述「超過 80% AI 專案失敗，是一般 IT 專案的兩倍」，但這是 RAND 引用他人估計，不是 RAND 自己量的
  - 來源：[RAND RR-A2680-1](https://www.rand.org/pubs/research_reports/RRA2680-1.html)（2024-08-13）【研究，訪談 65 位資深資料科學家與工程師；偏傳統 ML，在 GenAI 浪潮之前】
- **舊資料架構撐不起即時 agent**：Deloitte 指出舊有資料與基礎設施無法支援即時、自主的 AI；42% 認為策略準備充分，但對資料、基礎設施、風險、人才的準備度都比較低。[Deloitte 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-generative-ai-in-enterprise.html)【顧問調查】
- **Gartner「63% 組織沒有 AI-ready 的資料管理實務」**（2025-02）。⚠️ 未驗證：原頁 403，數字憑記憶，沒有二手來源核對，不建議引用
- **權限與外洩**：Samsung 2023 年因工程師把原始碼貼進 ChatGPT 而限制使用生成式 AI。⚠️ 未驗證：本輪沒有開到原始報導（Bloomberg 2023-05）

### 2.4 技術與整合

**證據**
- **工具不學習、不記憶、不貼合流程（MIT 所說的「learning gap」）**：
  - 使用者在簡單任務上偏好 ChatGPT，關鍵任務卻因為它「沒有記憶」而放棄
  - 有 CIO 說：「今年看了幾十個 demo，可能一兩個真的有用，其他都是 wrapper 或科學專案」
  - 來源：[MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)【研究機構報告】
- **長任務可靠度下降**：API 任務成功率從約 60%（1 小時以內）降到約 45%（5 小時以上）。[Anthropic Economic Index 2026-01](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)（2026-01-15）【廠商數據】。這解釋了為什麼 agent 從 demo 走到正式環境，往往在長流程中斷
- **技術片段化**：50% 的 CEO 說公司技術是片段的、彼此不相連。[IBM CEO Study](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles)（2025-05-06）【顧問調查】
- **Agent washing**：數千家「agentic」廠商裡只有約 130 家是真的。[Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)（2025-06-25）【顧問預測，⚠️ 二手核對】。採購端缺乏評估能力，就會買到換皮的 RPA
- **體感與實測脫節**：METR 實驗中開發者覺得快了 20%，實測慢了 19%。[METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)（2025-07-10）【研究】。沒有 eval 與基準線，企業會誤判試點成效

**個案**
- **McDonald's × IBM 得來速 AI 點餐**：2024-06 宣布結束在 100 多家門市的測試，社群上流傳大量點錯單的影片。[CNBC](https://www.cnbc.com/2024/06/17/mcdonalds-to-end-ibm-ai-drive-thru-test.html)（2024-06-17）【媒體】。⚠️ 原頁 403，門市數與結束日期憑記憶，未核實

---

## 3. 試點地獄（pilot purgatory）

### 3.1 成因

1. **試點的設計就沒打算上線**：只量 demo 的驚豔度，不量流程 KPI；沒有基準線，也沒有 6–12 個月的負責人。RAND 建議每個產品團隊至少承諾一年解同一個問題。[RAND](https://www.rand.org/pubs/research_reports/RRA2680-1.html)（2024-08-13）【研究】
2. **怕落後驅動的「很多小試點」**：
   - 64% CEO 因為怕落後而先投資，結果 25% 達到 ROI、16% 擴展。[IBM](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles)（2025-05-06）【顧問調查】
   - S&P 統計 POC 平均有 46% 在上線前被砍。[CIO Dive](https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/)（2025-03-14）
3. **只把 AI 疊在舊流程上**：只有約四分之一的非高績效者重新設計流程。[McKinsey 2026（⚠️ 二手）](https://www.techtarget.com/it-strategy/opinion/Enterprise-AI-got-better-but-the-ROI-didnt)
4. **預算放錯地方**：預算偏向看得見的前台（銷售、行銷），ROI 較高的後勤沒人做。[MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)
5. **大企業的審批鏈**：大企業試點最多，但轉換率最低，耗時 9 個月以上；中型企業 90 天。[MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)【自述數據】
6. **人沒跟上**：第一線使用率卡在 51%，只有三分之一受過足夠訓練。[BCG AI at Work 2025](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)（2025-06-26）
7. **擴大後成本與風險才浮現**：token 成本、資安、責任歸屬，在試點規模看不出來。[Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)、[S&P via CIO Dive](https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/)

### 3.2 跨過去的企業做對了什麼

| 做法 | 證據 |
|---|---|
| **重新設計流程，不是加裝工具** | 高績效者近四分之三從根本重新設計流程，其他人約四分之一（McKinsey 2026，⚠️ 二手）；BCG AI at Work 也發現做流程再造的公司，員工省下的時間明顯較多【顧問調查】 |
| **把 70% 資源放在人與流程** | BCG 10-20-70 原則（2024-10-24）【顧問調查】 |
| **高層訂多年目標，依價值排序並嚴格追蹤** | BCG future-built 五大策略的前兩條（2025-09-30）【顧問調查】 |
| **集中在少數核心職能，深做** | BCG：70% 潛在價值在核心職能，IT 只佔 13%【顧問調查】 |
| **能買就不要自建，要求廠商做流程客製並能從回饋學習** | MIT NANDA：購買或合作上線率約 67%，自建約 33%（自述，可能有混淆變數）【研究機構報告】 |
| **下放執行權、保留問責；從影子 AI 的重度使用者找用例** | MIT NANDA【研究機構報告】 |
| **先做後勤** | MIT NANDA：最高 ROI 在減少外包與代理商成本【研究機構報告】 |
| **訓練要夠量（≥5 小時，面對面指導）** | BCG AI at Work 2025【顧問調查】 |
| **高層主導治理，先建 agent 治理再擴大** | Deloitte 2026【顧問調查】 |
| **保留真人選項與品質底線** | Klarna 2025-05 修正【個案】；CBA 撤回【個案】 |
| **衡量要實測，不靠體感** | METR【研究】；Anthropic 以任務成功率校正後，生產力估計砍半【廠商數據】 |

---

## 4. 對企業白皮書最有用的 10 個洞見

1. **「有在用」跟「有賺錢」差很多**：88–89% 組織在用 AI，只有約 37% 看到任何 EBIT 貢獻，貢獻達 5% 以上的約 6%，兩年沒變。來源：[Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report/economy)、McKinsey 2026（⚠️ 經 [TechTarget](https://www.techtarget.com/it-strategy/opinion/Enterprise-AI-got-better-but-the-ROI-didnt) 轉述）
2. **區分高績效者的頭號因素是重新設計流程**（約 75% 對 25%），不是預算或模型。來源：McKinsey 2026（⚠️ 二手）
3. **困難約 70% 在人與流程**，所以資源也要 10/20/70 分配。來源：[BCG 2024-10-24](https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value)
4. **「95% 失敗」是方法很弱的初步研究**（52 個組織、6 個月、自述），白皮書要引用就得連同限制一起寫。來源：[MIT NANDA PDF](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)
5. **影子 AI 是需求訊號，不是紀律問題**：90%+ 公司的員工用個人 AI，只有 40% 公司有官方訂閱。來源：[MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)；[BCG AI at Work 2025](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)
6. **怕落後是試點地獄的燃料**：64% CEO 在搞清楚價值前就先投資，只有 25% 達到預期 ROI、16% 擴展。來源：[IBM CEO Study 2025-05-06](https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles)
7. **AI 說的話就是公司說的話**：Air Canada 主張聊天機器人是獨立法律實體，被仲裁庭駁回。來源：[Moffatt v. Air Canada, 2024 BCCRT 149](https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada)
8. **先砍人、後驗證，會原路退回**：CBA 撤回 45 人裁員並道歉，Klarna 承認過度看重成本導致品質下降。來源：[ABC 2025-08-21](https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-apologises-for-error/105679492)、[Fortune 2025-05-09](https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/)
9. **卡住企業的常常是脈絡與資料取得，不是模型**；而且任務越長，可靠度越低（約 60% 降到 45%）。來源：[Anthropic Economic Index 2025-09](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)、[2026-01](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
10. **體感不能當 KPI**：開發者覺得快 20%，實測慢 19%，所以試點一定要有基準線與 eval。來源：[METR 2025-07-10](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

---

### 附錄：本輪沒能核實、建議下一輪補的項目

- McKinsey 2026 PDF 原文（逾時），用來確認 37%、6%、44%、workflow redesign 的確切措辭
- Gartner 三則新聞稿原文（403）：40% agentic 取消、30% GenAI POC 放棄、63% 缺 AI-ready 資料
- OpenAI 企業報告原頁（403），用來確認發布日期與方法
- IBM Krishna 的 HR 取代說法、Samsung 2023 禁用、McDonald's 得來速：原始報導都沒開到
- HBR workslop 的量化數字（付費牆）
- Duolingo 備忘錄全文（The Verge 與 LinkedIn 沒開到）
