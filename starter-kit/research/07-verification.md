# 07 事實查核：報告引用數字回查原文

> 查核日：2026-10-20。範圍：12 項報告會用到的數字。
> 方法：能開原文就逐字引用原文（英文原句保留）；開不了原文就寫「仍未核實」並附最好的二手來源。
> Gartner、McKinsey 用一般抓取會被擋（403／逾時），改用瀏覽器開原頁讀全文；Shopify 用 SEC EDGAR 原件；MIT NANDA、Canaries、KPMG 讀原始 PDF。

## 總表

| # | 項目 | 研究檔寫法 | 原文結果 | 狀態 | 建議報告怎麼寫 |
|---|---|---|---|---|---|
| 1 | McKinsey State of AI 2025 | 88%、高績效者約 6%（EBIT ≥5% 且自評顯著）、約 3 倍重新設計流程；樣本「約 2,000」；報告 01-gap 註腳說 88% 與 6% 是「多篇報導交叉核對」 | 原文全部吻合：88%（前一年 78%）、約 6%、「nearly three times as likely」；1,993 人、105 國、2025-06-25～07-29 施測、**2025-11-05 發布**。另：39% 有 EBIT 影響、62% 至少在試驗 agent | ✅ 已核實（另有連帶問題，見下一欄） | 註腳改引原文，拿掉「多篇報導交叉核對」。**URL 要改**：`/the-state-of-ai` 現在指向 **2026 年版**（2026-08-25），2025 年版在 `/the-state-of-ai-2025`。研究檔裡「近四分之三 vs 四分之一」與「37% EBIT」是 **2026 年版**數字，不是 2025 年版，可直接改成「McKinsey 2026（原文）」，不用再標 ⚠️ 二手 |
| 2 | Gartner 2025-06-25 agentic | >40% 到 2027 年底取消；約 130 家真 agentic 廠商；3,412 人投票 | 原文吻合，逐字見下 | ✅ 已核實 | 照寫，標「預測」。130 家是 Gartner「估計」 |
| 3 | Gartner 2025-06-10 客服 | 2027 年前 50% 放棄縮編客服；163 位主管、95% 保留真人 | 原文吻合。母體是「原本**預期大幅**縮減客服人力的組織」，不是全部組織 | ✅ 已核實 | 寫「原本打算大幅縮編客服的組織中，一半會在 2027 年前放棄」，不要寫成「50% 的組織」 |
| 4 | Stanford Canaries | 02-ai-native 寫「相對下降約 13%」（2025-08）；01-gap、03-workforce 寫 19%（2026-08 修訂） | 最新版 **2026-08（網頁標 2026-08-12）**：**19% below**（描述性缺口，資料至 2026-06）。原文自述舊版：13%（2025-07 資料，迴歸）、16%（2025-09 資料）；同一描述性口徑在 2025-07 是 15%。網站上三個 PDF 網址現在都回傳同一份 2026-08 版 | ⚠️ 有出入（02-ai-native 用的是舊版數字） | 報告只用 **19%**，寫「比照低曝險同齡者應有水準低 19%（2026-08 版，資料至 2026-06）」。不要寫「下降 19%」；原文另有絕對值：最曝險兩個五分位 22–25 歲就業 2022-11 到 2026-06 **下降約 11%** |
| 5 | Shopify 10-K 員工數 | 約 8,100 → 約 7,600（-6%），「轉述，未開 SEC 原件」 | SEC 原件：2024-12-31「approximately 8,100」、2025-12-31「approximately 7,600」 | ✅ 已核實 | 註腳改引 10-K 原件（URL 見下），拿掉「依年報轉述」。「Jefferies 歸因 AI」仍是二手，要寫成分析師說法 |
| 6 | MIT NANDA GenAI Divide | 預算「一半以上」或「約 50–70%」流向銷售與行銷；外購／合作上線率約 67%、自建約 33% | 原文**自己就有兩個數字**：Takeaway 與研究附註寫 **50%**，同頁內文寫「approximately **70 percent**」（假設性分配 100 美元的問卷）。67% vs 33% 原文吻合，但圖表標 **66%**；作者自註是自陳、52 個組織訪談、不證明因果 | ⚠️ 有出入（原文內部不一致；「一半以上」也不精確） | 預算寫「約一半（原文另一處寫約 70%，屬假設性分配）」；上線率寫「約 67% 對 33%（自陳，52 個組織，非因果）」 |
| 7 | Salesforce Agentforce 約 6% | 約 15 萬客戶中，FY26 Q3 付費約 6%（SalesforceBen，分析師估算） | 財報只揭露「over 9,500 paid deals」，**沒有客戶數也沒有滲透率**。6% 是 SalesforceBen 作者 Henry Martin（2026-01-07）用 9,500 ÷ 15 萬算出；15 萬客戶數文中沒附出處；而且分子是「交易數」不是「客戶數」 | ⚠️ 有出入（不是公司揭露；口徑把交易當客戶） | 報告不要寫「6% 客戶」。改寫財報原文：「上線以來成交 18,500+ 筆，付費 9,500+ 筆」。要提滲透率就寫「媒體估算約 6%（付費交易數 ÷ 約 15 萬客戶，非公司揭露）」 |
| 8 | 台灣中小企業 AI 導入 7.4% 等 | 中企署委託工研院，10–199 人，「實際導入」7.4%；63.9%、25.5%、84.5% | 經濟部產發署 iTALENT 電子報（工研院產科國際所陳伊柔，2026-03-16）有全部四個數字，口徑「實際導入 AI 應用的比例卻僅有 7.4%」。tesa 轉述白皮書寫「已導入或正在規劃導入」7.4%。**白皮書 PDF 本體被 Cloudflare 擋，未讀到原文**；經濟部 2025-12-26 新聞稿與簡報都沒有這些數字 | ❌ 仍未核實（白皮書原文）；⚠️ 兩個轉述口徑不一致 | 主來源改引 iTALENT（工研院研究員撰文，官方電子報），寫「工研院受中企署委託調查（2025，10–199 人企業）」。口徑寫「導入 AI 應用」，不加「實際」或「規劃」二擇一，並註明白皮書口徑待核對。84.5% 只有 iTALENT 有，tesa 沒有。樣本數各來源都沒寫 |
| 9 | Microsoft WTI 2026 | 組織因素 67% vs 個人 32%；13% 覺得重塑失敗也會被獎勵 | 原文吻合。67/32 是「自陳 AI 成效」的關聯，作者註明非因果；13% 原句是「rewarded for reinvention of work with AI even if results aren't met」。2 萬人、10 市場、2026-05-05 發布 | ✅ 已核實 | 67/32 寫「關聯」不寫「取決於」；13% 寫「被獎勵」（rewarded），報告現用「被肯定」可接受但較寬 |
| 10 | KPMG × 墨爾本大學 2025 | 57% 員工隱藏 AI 使用並把 AI 產出當成自己的 | 原報告第 74 頁吻合：「Over half (57%) of employees also admit that they have used AI in non-transparent ways」。48,340 人、47 國、2024-11～2025-01 中 | ✅ 已核實（附但書） | 原文是「**包括**當成自己的成果**或**不說自己用了 AI」，是「或」不是「並」。母體依上下文是**工作上使用 AI 的受雇者**，不是全部員工 |
| 11 | BCG 10-20-70 與 60% KPI | 2024-10：10-20-70、74%、4%；2025-01：1,803 位 C-level、60% 沒有財務 KPI | 兩則新聞稿原文吻合。2024-10-24：1,000 位 CxO 與高階主管、59 國、20+ 部門；2025-01-15：1,803 位 C-level、19 個市場、12 產業 | ✅ 已核實 | 照寫。10-20-70 是 BCG 描述「領先者的做法」，不是實證比例 |
| 12 | Anthropic Economic Index 2026-01 | 約 60%（1 小時內）→ 約 45%（5 小時以上）；API 49%、Claude.ai 67% | 原文吻合，2026-01-15 發布，樣本 2025-11-13～20 各 100 萬筆對話／API | ✅ 已核實 | 寫明是 **API 資料**、「人類預估所需時間」，且「成功」由模型分類判定（廠商資料） |

**有出入**：#4（02-ai-native 用舊版 13%）、#6（MIT 原文 50% / 70% 並存、66% / 67% 並存）、#7（6% 不是公司揭露，交易數當客戶數）、#8（7.4% 兩個轉述口徑不同）。
**仍未核實**：#8 的白皮書原文。
**順帶發現**：#1 McKinsey 的 `/the-state-of-ai` 網址已換成 2026 年版，報告 `report/03-ai-native.md` 註腳用的就是這個網址，點進去會看到別的數字。

---

## 逐項原文

### 1. McKinsey〈The state of AI in 2025: Agents, innovation, and transformation〉

- URL：https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025
- 發布：2025-11-05（頁首「November 5, 2025 | Survey」）
- 樣本原文：「The online survey was in the field from June 25 to July 29, 2025, and garnered responses from 1,993 participants in 105 nations」；38% 來自年營收 10 億美元以上組織；依各國 GDP 加權。
- 88%：「88 percent report regular AI use in at least one business function, compared with 78 percent a year ago.」
- 高績效者：「Respondents who attribute EBIT impact of 5 percent or more to AI use and say their organization has seen "significant" value from AI use—our definition of AI high performers, representing about 6 percent of respondents」
- 3 倍：「high performers are also nearly three times as likely as others are to say their organizations have fundamentally redesigned individual workflows (Exhibit 11). Indeed, this intentional redesigning of workflows has one of the strongest contributions to achieving meaningful business impact of all the factors tested.」
- 其他：「just 39 percent report EBIT impact at the enterprise level」；「Sixty-two percent of survey respondents say their organizations are at least experimenting with AI agents」；「Nearly two-thirds of respondents say their organizations have not yet begun scaling AI across the enterprise.」
- 2025 年版**沒有**「近四分之三 vs 四分之一」這組數字，那是 2026 年版的。

**2026 年版（對照用）**
- URL：https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai （〈The state of AI in 2026: On the road to ROI〉，2026-08-25）
- 樣本：2026-05-04～06-08，1,719 人、97 國。
- 「Nearly three-quarters of high performers report fundamentally redesigning workflows because of their AI use, up from 55 percent last year. By comparison, just one-quarter of other respondents report doing so.」
- 高績效者「account for just 6 percent of survey respondents, unchanged from 2025」；EBIT 影響「37 percent」，與前一年大致持平。
- 研究檔 01-gap 裡標「McKinsey 2026（⚠️ 二手）」的數字，現在可以改成原文。

### 2. Gartner 2025-06-25 agentic AI

- URL：https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- 「Over 40% of agentic AI projects will be canceled by the end of 2027, due to escalating costs, unclear business value or inadequate risk controls, according to Gartner, Inc.」
- 「Many vendors are contributing to the hype by engaging in "agent washing" – the rebranding of existing products, such as AI assistants, robotic process automation (RPA) and chatbots, without substantial agentic capabilities. Gartner estimates only about 130 of the thousands of agentic AI vendors are real.」
- 投票：「According to a January 2025 Gartner poll of 3,412 webinar attendees, 19% said their organization had made significant investments in agentic AI, 42% had made conservative investments, 8% no investments, with the remaining 31% taking a wait and see approach or are unsure.」
- 同稿另有：到 2028 年至少 15% 日常工作決策由 agentic AI 自主做出；33% 企業軟體會內建 agentic AI。

### 3. Gartner 2025-06-10 客服人力

- URL：https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai
- 「By 2027, 50% of organizations that expected to significantly reduce their customer service workforce will abandon these plans, according to Gartner, Inc.」
- 「A Gartner poll of 163 customer service and support leaders conducted in March 2025 found 95% of customer service leaders plan to retain human agents to strategically define AI's role.」

### 4. Stanford Digital Economy Lab〈Canaries in the Coal Mine?〉

- 頁面：https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ （修訂日 2026-08-12）
- 最新版 PDF：https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf （封面「August 2026」）。研究檔引的 `…/2025/11/CanariesintheCoalMine_Nov25.pdf` 與 2025-08 的 `…/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf` 現在下載下來都是同一份 2026-08 版（md5 相同），**已經拿不到舊版原文**。
- 摘要：「employment of young workers (ages 22–25) in AI-exposed occupations now stands 19% below where it would be had it kept pace with that of their less-exposed peers; experienced workers show no comparable gap.」
- 樣本：ADP 薪資資料「covering millions of U.S. workers through June 2026」。
- 版本差異（原文自述）：「Earlier versions of this study headlined regression estimates adjusting for firm-level shocks (a 13% relative decline as of July 2025 data; 16% as of September 2025 data). We now emphasize the simpler descriptive divergence, which requires no modeling choices: by this same measure, the kept-pace shortfall was 15% at the July 2025 data vintage and has since widened to 19% as of June 2026.」
- 絕對值：「employment of 22–25-year-olds in the two most exposed quintiles fell about 11% between November 2022 and June 2026, while employment of the same age group in the three least-exposed quintiles grew about 10%.」
- 作者自己的但書（摘要）：控制教育後效果變弱、部分趨勢在 GenAI 前就出現、ADP 樣本比全國調查明顯。
- 與研究檔的差：02-ai-native 第 203、243 行寫「相對下降約 13%」並標 2025-08，是最舊版的迴歸數字；03-workforce 第 37 行說「2025 年 11 月版報 16%」，原文說的是「2025-09 資料」報 16%，版本名稱與資料期間不同，寫法要改成資料期間。

### 5. Shopify 10-K 員工數

- FY2025 10-K（2026-02-11 申報）：https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm —「As of December 31, 2025, Shopify had approximately 7,600 employees worldwide.」
- FY2024 10-K（2025-02-11 申報）：https://www.sec.gov/Archives/edgar/data/1594805/000159480525000012/shop-20241231.htm —「As of December 31, 2024, Shopify had approximately 8,100 employees worldwide.」
- 降幅約 6.2%。Shopify 在 FY2023 以前申報的是 40-F，FY2024 起才是 10-K。
- 「減少主要來自自然流失、歸因 AI」是 Jefferies 分析師說法（Proactive Investors 轉述），10-K 沒寫原因。

### 6. MIT NANDA〈The GenAI Divide: State of AI in Business 2025〉

- 原文 PDF（2025-07，研究期間 2025-01～06）。方法原文：「a systematic review of over 300 publicly disclosed AI initiatives, structured interviews with representatives from 52 organizations, and survey responses from 153 senior leaders」。
- 預算（第 8 頁，3.4 節）：
  - Takeaway：「Investment allocation reveals the GenAI Divide in action, 50% of GenAI budgets go to sales and marketing, but back-office automation often yields better ROI.」
  - 同節內文：「we asked executives to allocate a hypothetical $100 to different functions. Sales and marketing functions captured approximately 70 percent of AI budget allocation across organizations in our survey.」
  - 第 9 頁研究附註：「the general functional allocation of GenAI investment (e.g., ~50% to Sales & Marketing) was relatively consistent across executive interviews」
  - 後段：「Despite 50% of AI budgets flowing to sales and marketing (from the theoretical estimate with executives)」
- 外購 vs 自建（第 18 頁）：
  - 「In our sample, external partnerships with learning-capable, customized tools reached deployment ~67% of the time, compared to ~33% for internally built tools. While these figures reflect self-reported outcomes and may not account for all confounding variables, the magnitude of difference was consistent across interviewees.」
  - 同頁圖表標「Strategic Partnerships (Buy) 66%」「Internal Development (Build) 33%」。
  - 限制原文：「These percentages reflect our interview sample of 52 organizations and may not represent broader market patterns.」「The correlation between external partnerships and success does not necessarily prove causation.」
- 與研究檔的差：02-ai-native 寫「約 50–70%（報導不一）」，其實不一致來自原文本身；01-gap 寫「一半以上」，原文是「50%」與「約 70%」。

### 7. Salesforce Agentforce 滲透率約 6%

- 公司原文（FY26 Q3，2025-12-03）：https://www.salesforce.com/news/press-releases/2025/12/03/fy26-q3-earnings/ —「Salesforce has closed over 18,500 Agentforce deals since launch; over 9,500 paid deals, up 50% quarter-over-quarter.」Agentforce ARR「surpassed half a billion in Q3, up 330% Y/Y」。新聞稿**沒有**揭露客戶總數或 Agentforce 客戶滲透率。
- 6% 出處：Henry Martin，〈2026 Predictions: 'Mediocre' Agentforce Adoption Would Do Wonders for Salesforce〉，SalesforceBen，2026-01-07（2026-01-27 更新）：https://www.salesforceben.com/2026-predictions-mediocre-agentforce-adoption-would-do-wonders-for-salesforce/ —「That means that, of Salesforce's 150,000 customers, 12% are on an Agentforce deal, 6% of which are paid.」
- 問題：(a) 作者自行計算；(b) 15 萬客戶沒附出處；(c) 用「交易數」除以「客戶數」，一家客戶可能有多筆交易，所以這是上限估計，不是滲透率；(d) 原句「6% of which」文法上像是「12% 裡的 6%」，實際算式是 9,500 ÷ 150,000 ≈ 6.3%。

### 8. 台灣中小企業 AI 導入率 7.4% 等

- **最接近原始的來源**：陳伊柔（工研院產科國際所副研究員），〈AI浪潮下的中小企業突圍：利用政策資源建構數位與人才賦能策略〉，經濟部產業發展署 iTALENT 電子報，2026-03-16：https://ipd.nat.gov.tw/italent/ePaperD/10/ePaper20260300008
  - 調查：「經濟部中小及新創企業署於2025年委託財團法人工業技術研究院進行的「中小企業AI運用現況研究調查」」，「聚焦員工數10至199人之企業」。樣本數、調查月份未寫。
  - 7.4%：「實際導入AI應用的比例卻僅有7.4%，顯示多數企業仍處於觀望狀態。」
  - 4%：「以「行銷與銷售」部門的投入最為高(導入率4.0%)」；小標寫「僅約有4%」，和內文矛盾。
  - 挑戰：「高達63.9%的中小企業將「尚無明確應用需求」視為最大挑戰」；「其他挑戰依序為：「對AI技術不理解」(26.8%)、「導入成本高」(25.5%)以及「人才短缺」(21.3%)。」
  - 人才：「依據調查結果約84.5%的企業內部缺乏AI相關人才」
- **白皮書轉述**：tesa.center，2025-12-27：https://www.tesa.center/blog/posts/20251227 —「目前僅約 7.4% 的中小企業已導入或正在規劃導入 AI 應用」；63.9%、26.8%、25.5% 同上；**沒有 84.5%**。
- **白皮書原件**：中企署頁面 https://www.sme.gov.tw/article-tw-2853-13847 （PDF 連結 `https://www.sme.gov.tw/files/13847/EB0374F3-F6B7-48DB-8B4A-614F60A095F4`，頁面更新 2026-04-30）。抓取被 Cloudflare 擋，**本次沒有讀到白皮書內文**。
- 經濟部新聞稿（2025-12-26）https://www.moea.gov.tw/MNS/populace/news/News.aspx?kind=1&menu_id=40&news_id=121491 與附件簡報：只提到白皮書探討 AI 應用，**沒有 7.4% 等數字**。
- 結論：數字本身有工研院研究員在官方電子報的文字可查，但「實際導入」與「已導入或規劃導入」哪個是白皮書原口徑，仍待人工開 PDF 核對（建議搜尋「臺灣中小企業AI運用狀況」專章）。

### 9. Microsoft Work Trend Index 2026

- URL：https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization （2026-05-05）
- 67/32：原句分兩段，「organizational factors like culture, manager support, and talent practices account for more than 2x」…「the reported AI impact of individual factors like mindset and behavior (67% vs. 32%)」。頁面註明是統計關聯，不是因果。
- 13%：「only 13% of AI users say they're rewarded for reinvention of work with AI even if results aren't met」
- 樣本：「among 20,000 full-time employed or self-employed knowledge workers who use AI at work across 10 markets」，施測「between February 18, 2026, and April 7, 2026」（Edelman DXI）。圖表註腳寫到 4 月 20 日，與方法段不一致。

### 10. KPMG × 墨爾本大學〈Trust, attitudes and use of artificial intelligence: A global study 2025〉

- 報告 PDF：https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2025/05/trust-attitudes-and-use-of-ai-global-report.pdf ；KPMG 介紹頁 https://kpmg.com/xx/en/our-insights/ai-and-technology/trust-attitudes-and-use-of-ai.html 。DOI 10.26188/28822919。
- 第 74 頁：「Over half (57%) of employees also admit that they have used AI in non-transparent ways, including presenting AI-generated content as their own or avoiding revealing when they have used AI tools to complete their work.」
- 同段上下文的母體是「employees who use AI」（「Almost one in two employees who use AI admit to doing so in ways that contravene organizational policies」），所以 57% 的分母應是工作上用 AI 的受雇者。
- 樣本：48,340 人、47 國；「data collected between November 2024 and mid-January 2025」；67% 受訪者為全職或兼職工作者。
- 墨爾本大學新聞稿頁面本次被擋（403），以報告原文為準。

### 11. BCG

**2024-10-24**：https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- 「Leaders follow the rule of putting 10% of their resources into algorithms, 20% into technology and data, and 70% in people and processes.」
- 「Seventy-four percent of companies have yet to show tangible value from their use of AI.」；「just 4% of companies have developed cutting-edge AI capabilities across functions」
- 困難來源：「with around 70% stemming from people- and process-related issues」
- 樣本：「a comprehensive survey of 1,000 CxOs and senior executives from over 20 sectors, spanning 59 countries in Asia, Europe, and North America, and covering ten major industries.」

**2025-01-15**（報告〈From Potential to Profit: Closing the AI Impact Gap〉）：https://www.bcg.com/press/15january2025-ai-optimism-autonomous-agents
- 「However, 60% of companies surveyed are failing to define and monitor any financial KPIs related to AI value creation.」
- 「while 75% of executives rank AI as a top three strategic priority, only a quarter report meaningful value from their AI initiatives.」
- 樣本：「BCG surveyed 1,803 C-level executives across 19 markets and 12 industries.」（原文寫 markets，不是 countries）

### 12. Anthropic Economic Index 2026-01

- URL：https://www.anthropic.com/research/anthropic-economic-index-january-2026-report （2026-01-15）
- 「success rates drop from around 60% for sub-hour tasks to roughly 45% for tasks estimated to take humans 5+ hours」（API 資料）
- Claude.ai 任務成功率 67%、API 49%。
- 生產力：「falls from 1.8 to about 1.0 percentage points of annual labor productivity growth over the next decade」
- 樣本：2025-11-13～20，Claude.ai（Free/Pro/Max）與第一方 API 各隨機 100 萬筆。廠商自有資料，任務時間是「人類預估所需時間」。
