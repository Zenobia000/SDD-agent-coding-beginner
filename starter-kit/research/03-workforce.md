# 03 — AI 對不同角色的影響與應對（研究筆記）

> 研究日期：2026-10-20。用途：企業白皮書素材。
> 驗證等級標記：
> - **[原文]**：已直接讀到原始出處（論文 PDF、官方頁面、官方新聞稿）。
> - **[轉述]**：只讀到搜尋摘要或媒體轉述，原文未讀到；數字可用，但引用前建議回查原文。
> - **⚠️ 未驗證**：只有單一二手來源，或來源間數字互相衝突。
>
> 研究限制：本次 WebSearch 配額在研究後段用盡，WEF、KPMG/墨爾本大學原文頁面回 403，經濟部中小企業白皮書的數字沒有查到原文。這些都在對應條目標明。

---

## 一句話結論

**AI 目前沒有造成全面失業，但已經在「入門職缺的招募」這一端關門：受衝擊的是年輕人進不來，不是資深者被裁。** 生產力效果高度取決於任務是否落在 AI 的能力邊界內，以及組織（主管、文化、制度）有沒有跟上。個人努力只解釋一小部分。

---

## 1. 就業與工作的實證

### 1.1 入門職缺：證據最一致的一塊

| 研究 | 樣本 / 方法 | 主要發現 | 限制 |
|---|---|---|---|
| **Brynjolfsson, Chandar, Chen「Canaries in the Coal Mine?」**（Stanford Digital Economy Lab） | ADP 薪資行政資料，每月 350 萬–500 萬名美國勞工（ADP 服務的企業共雇用逾 2,600 萬人）；資料至 2026 年 6 月 | 22–25 歲、AI 曝險最高職業的就業，比「若跟上低曝險同儕」的水準**低 19%**；資深勞工沒有同樣缺口。以水準算：2022/11–2026/06 間，最高曝險兩個五分位的 22–25 歲就業**跌約 11%**，最低曝險三個五分位**升約 10%**。 | 作者明說是「早期描述性指標，不是因果估計」；控制教育程度後效果減弱；部分分歧在 ChatGPT 前就出現（疫情期間）；ADP 樣本的效果比全國調查明顯。 |

六個事實（最新版原文）[原文]：
1. **沒有**全經濟範圍的大規模失業證據。
2. 年輕人在 AI 曝險職業的就業落後 19%，資深者沒有缺口。
3. 這個分歧從 2025 年 8 月首次發表後**持續擴大**（2025/07 資料時為 15%，2026/06 為 19%）。
4. 主要透過**減少招募年輕人**發生，不是增加離職或裁員。
5. 下降集中在 AI 用來「取代」任務的職業；AI 用來「輔助」的職業，就業持平或上升，資深者尤其明顯。
6. 調整發生在**就業人數**，不是**底薪**。

機制線索：依賴「明文知識」（codified knowledge，教科書、書面程序能學到的）的職業，年輕人就業成長較慢；依賴「隱性知識」（tacit knowledge，靠實作累積）的職業，資深者就業成長較快。[原文]

版本差異（引用時要寫清楚是哪一版）：2025 年 8 月版用控制企業層級衝擊的迴歸，報 **13%**；2025 年 11 月版報 **16%**；最新版改用不需建模假設的描述性缺口，報 **19%**。
來源：[Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI（PDF，最新版內文標 August 2026）](https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf)（2026-08）[原文]；[SIEPR working paper 頁](https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial)
> 註：上述 PDF 網址檔名為 Nov25，但抓到的內文是 2026 年 8 月版（資料至 2026/06）。引用時建議以 SIEPR 頁面的最新版為準。

**Anthropic「Labor market impacts of AI: A new measure」** [原文]
- 樣本：美國勞工；以「observed exposure」（理論能力 × Claude 實際使用，自動化用途加權較高）衡量曝險。
- 發現：高曝險職業的**失業率沒有系統性上升**（可偵測約 1 個百分點的差異）。但 22–25 歲進入最高曝險職業的**每月求職成功率下降約 0.5 個百分點，相對 2022 年約少 14%**，僅勉強達統計顯著。25 歲以上沒有類似下降。
- 曝險最高職業：電腦程式設計師（任務覆蓋 75%）、客服代表、資料輸入員（67%）。
- 限制：年輕人可能留在原工作、換工作或回學校，不一定是被擋在外面；只涵蓋美國；作者自稱「早期、暫定」。
- 來源：[Labor market impacts of AI: A new measure](https://www.anthropic.com/research/labor-market-impacts)（2026-03-05，03-08 修正圖 7）

**Hosseini & Lichtinger「Generative AI as Seniority-Biased Technological Change」** [轉述]
- 樣本：Revelio Labs 的 LinkedIn 履歷與職缺資料，約 6,200 萬名勞工、28.5 萬家美國企業，2015–2025（2026/05 版約 6,500 萬人）。
- 方法：以是否刊登「GenAI integrator」職缺辨識採用 AI 的企業，做差異中的差異分析。
- 發現：2023Q1 起，採用企業的**初階員工就業相對非採用企業急降，資深員工持續上升**；主因是**招募變慢**而非離職；批發零售業影響最大；依學歷呈 U 型——**中段學校畢業生**受衝擊最大。
- 限制：working paper，未經同儕審查；各版本數字不同。
- 來源：[Stanford Digital Economy Lab 研討會頁](https://digitaleconomy.stanford.edu/event/seyed-m-hosseini-and-guy-lichtinger-generative-ai-as-seniority-biased-technological-change-evidence-from-u-s-resume-and-job-posting-data)（2025-09-22）；[2026/05 版 PDF](https://raw.githack.com/s-mahdihosseini/Website/b99fa2962dcc4c165bbc3c41dd283afa99c5ccfb/GenAI_SenBTC_May_2026.pdf)

**紐約聯儲：應屆大學畢業生** [轉述]
- 22–27 歲學士學位者失業率 2026 年 3 月約 **5.6%**（另一來源報 Q1 5.7%，全體 4.3%）；低度就業率約 41.5%（Q1 2026）。應屆畢業生失業率高於全體勞工，歷史上少見。
- 限制：失業率上升不能全歸因於 AI（升息、遠距工作、景氣都是候選因素）。有聚合網站稱聯儲研究把 64% 歸因於遠距工作 ⚠️ 未驗證。
- 來源：[Bloomberg Law: Unemployment for Recent College Grads Remains High, NY Fed Says](https://news.bloomberglaw.com/new-york-brief/unemployment-for-recent-college-grads-remains-high-ny-fed-says)（2026）

**對白皮書的意涵**：「AI 搶走工作」的說法不精確。比較精確的說法是「**AI 讓企業少招新人**」。這對企業的長期風險是：今天不招的初階員工，就是五年後缺的中階骨幹。

### 1.2 生產力：大但不均勻，而且會反過來傷人

**BCG × 哈佛「Navigating the Jagged Technological Frontier」**（Dell'Acqua, Mollick, Lakhani 等）[原文：HBS 摘要頁]
- 樣本：**758 名 BCG 顧問**，隨機分三組（無 AI／GPT-4／GPT-4＋提示工程簡介）。
- **能力邊界內的任務**（產品創新、上市規劃）：多完成 **12.2%** 子任務、快約 **25%**、品質評分高約 **32%**（working paper 版本常被引為「40% 以上」，引用時注意版本）。
- **能力邊界外的任務**（品牌策略個案）：答對率從無 AI 的 **84.5%** 掉到 GPT-4 組 **70.6%**、GPT-4＋訓練組 **60%**。**有 AI 反而更容易錯**，而且受過提示訓練的人錯更多。
- 原本表現後段的人進步 **31%**，前段 **11%**。
- 發表：*Organization Science* vol. 37 no. 2（2026 年 3 月正式刊出），working paper 2023 年 9 月。
- 來源：[Back to the beginnings of AI at work — HBS Digital Data Design Institute](https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/)（2026）
- 限制：顧問業、GPT-4 時期；邊界會隨模型移動。

**Brynjolfsson, Li, Raymond「Generative AI at Work」**（客服中心）[轉述]
- 樣本：約 5,179 名客服人員（後續版本 5,172）。
- 每小時解決問題數平均提升 **14%**（working paper）／**15%**（QJE 2025 刊出版）；**新手與低技能者提升 34%**（working paper），資深高技能者幾乎沒提升、品質略降。
- AI 把頂尖員工的做法擴散給新手，也提高留任率。
- 來源：[NBER w31161](https://nber.org/papers/w31161)；QJE 2025, vol. 140, pp. 889–942
- 對新鮮人的意涵：**AI 是新手的槓桿**，但前提是企業還願意招新手。

**METR 開發者 RCT**（2025）[原文]
- 樣本：**16 名資深開源開發者、246 個真實 issue**（平均約 2 小時），每個 issue 隨機決定能否用 AI；工具主要是 Cursor Pro＋Claude 3.5/3.7 Sonnet。
- 結果：**允許用 AI 時多花 19% 時間**。
- 認知落差：事前預期快 24%，事後仍自認快了約 20%。**「覺得變快」和「實際變快」可以完全相反。**
- METR 自列限制：不代表多數開發者、不代表其他領域、不代表近期不會變快；對不熟悉的程式碼庫或經驗較少的開發者可能不同。
- 來源：[Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)（2025-07-10）

**METR 後續更新**（2026）[轉述]
- 擴大到 57 名開發者、143 個 repo、800+ 任務。新招募開發者估計值 **-4%（95% CI -15% 到 +9%）**，信賴區間跨零。
- METR 自己說這次資料「不可靠」：**越來越多開發者拒絕參加，因為不願意在沒有 AI 的情況下工作**，造成選擇偏誤；同時跑多個 agent 的工時也難量。METR 認為 2026 年初的開發者「應該比 2025 年初更快」，但資料只是很弱的證據。
- 來源：[We are Changing our Developer Productivity Experiment Design — METR](https://metr.org/blog/2026-02-24-uplift-update/)（2026-02-24）
- **白皮書用法**：19% 是 2025 年初的快照，不能當成「AI 讓工程師變慢」的定論。真正可引用的教訓是「**自我感受不可靠，要量測**」。

**Anthropic：AI 輔助對學習的影響**（RCT）[原文]
- 樣本：**52 名以初階為主的軟體工程師**，學一個新的 Python 函式庫（Trio）。
- 結果：用 AI 組測驗平均 **50%**，手寫組 **67%**（差距顯著，Cohen's d = 0.738）；**落差最大在除錯題**。速度只快約 2 分鐘，不顯著。
- **用法決定學不學得到**：全部丟給 AI 寫、逐步依賴、用 AI 除錯 → 測驗 < 40%；先讓 AI 產生再追問理解、要求程式碼＋解釋、只問概念自己除錯 → ≥ 65%。
- 作者建議：刻意而非預設地大規模部署 AI；設計讓工程師邊做邊學的機制，才有能力監督自己建的系統。
- 限制：樣本小、只量當下理解、不是長期技能保留。
- 來源：[How AI assistance impacts the formation of coding skills — Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)（2026-01-29）

**Workslop（看起來完成、實際沒推進的 AI 產出）** [轉述]
- BetterUp Labs × Stanford Social Media Lab，發表於 HBR；樣本 1,100+ 名美國全職員工。
- 約 **40%** 過去一個月收過 workslop；每次平均耗費約 **2 小時**重工；**18%** 的 AI 使用者承認寄出過低品質 AI 內容。
- 來源：[Axios: AI "workslop" sabotages productivity, study finds](https://www.axios.com/2025/09/24/ai-workslop-workplace-efficiency-study)（2025-09-24）

### 1.3 AI 實際被拿來做什麼：Anthropic Economic Index

**2026 年 1 月報告（Economic primitives）** [轉述]
- Claude.ai 上，2025 年 8 月自動化一度超過輔助；到 2025 年 11 月回到 **輔助 52%／自動化 45%**。報告把回流歸因於檔案建立、記憶、Skills 等鼓勵反覆協作的功能。**企業 API 使用 75% 是自動化。**
- 2025 年 2 月首份報告：輔助 57%／自動化 43%。
- 來源：[Anthropic Economic Index report: Economic primitives](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)（2026-01）；[Introducing the Anthropic Economic Index](https://www.anthropic.com/news/the-anthropic-economic-index)（2025-02）

**2026 年 6 月報告（Cadences）** [原文]
- 樣本：2026/04/10–06/10 的 Claude 對話抽樣；另有約 **9,700 名**連結使用紀錄的受訪者（非母體代表樣本，偏穩定的知識工作者）。
- 自評效益：速度 **86%**、範圍 **82%**、品質 **69%**、省成本 27%；**68%** 說用 AI 學到更多；**57%** 說 AI 讓自己的技能更值錢。
- 失業預期：**10%** 認為明年自己可能失業；其中 38% 歸因於 AI（上限值）。**擔心別人失業多於擔心自己**，尤其擔心**初階同事**——超過三分之一受訪者認為初階同事明年失業機率高於 60%。
- 初階工作者自評 AI 能做的工作比例最高，也最擔心失業；15 年以上資深者自評曝險比第一年新人低約 10 個百分點。
- 超過三分之一預期 12 個月內 AI 會處理大部分工作任務；超過三分之一預期職責會大幅改變。
- 女性自動化比例比男性低 7.3 個百分點（控制職業後）。
- 來源：[Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report)（2026-06-26）

### 1.4 全球雇主預測：WEF Future of Jobs 2025 [轉述：官方新聞稿經搜尋摘要；原文頁 403]
- 樣本：1,000+ 家大型企業，代表 1,400 萬名員工、22 個產業、55 個經濟體。**這是雇主預期，不是實測。**
- 到 2030 年：新創 **1.7 億**個職位、取代 **9,200 萬**個，淨增 **7,800 萬**；相當於現有工作的 22% 受影響。
- 工作所需技能約 **40%** 會改變（常被引為 39%）；**63%** 雇主認為技能缺口是轉型最大障礙；**41%** 雇主預期會因 AI 減少人力。
- 成長最快的技能：AI 與大數據、資安、科技素養，加上創意思考、韌性與彈性。
- 來源：[WEF: Future of Jobs Report 2025 press release](https://weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/)（2025-01-08）

### 1.5 Microsoft / LinkedIn Work Trend Index

**2024 年版** [原文]
- 樣本：31 國 **31,000 人**＋LinkedIn 求才資料＋Microsoft 365 訊號。
- **75%** 知識工作者在工作中使用 AI；**78% 的 AI 使用者自帶工具（BYOAI）**（分母是 AI 使用者，不是全體）。
- **66%** 領導者不會雇用沒有 AI 技能的人；但只有 **39%** 的 AI 使用者受過公司訓練；**60%** 領導者說公司缺乏 AI 願景與計畫。
- LinkedIn：會員在檔案加 AI 技能的人數成長 **142 倍**（至 2023 年底）。
- 台灣：**84%** 知識工作者使用生成式 AI [轉述：INSIDE 引台灣微軟]。
- 來源：[Microsoft and LinkedIn release the 2024 Work Trend Index](https://blogs.microsoft.com/blog/2024/05/08/microsoft-and-linkedin-release-the-2024-work-trend-index-on-the-state-of-ai-at-work/)（2024-05-08）；[INSIDE：台灣知識工作者已有 84% 使用生成式 AI](https://www.inside.com.tw/article/35378-microsoft-copilot)

**2025 年版（Frontier Firm）** [原文]
- **81%** 領導者預期 12–18 個月內 agent 會中度或大幅整合進 AI 策略；**82%** 有信心用「數位勞動力」擴充產能。
- **36%** 領導者預期五年內會管理 agent（員工 21%）；**51%** 經理人認為 AI 培訓會成為團隊的關鍵責任。
- **78%** 領導者考慮 AI 專職招募；**28%** 經理人考慮設「AI workforce manager」帶領人機混合團隊。
- 提出「**agent boss**」（每個人都會委派、指導、在必要時介入 agent）與「**human-agent ratio**」（每個團隊人與 agent 的配比：太少浪費、太多壓垮人的判斷，帶來風險與倦怠）。
- 來源：[2025: The year the Frontier Firm is born](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)（2025-04-23）

**2026 年版（Agents, human agency）** [原文]
- 樣本：10 個市場 **20,000 名使用 AI 的知識工作者**（Edelman，2026/02/18 起）＋約 10.5 萬則 Copilot 對話＋另一份 1,800 人的經理人研究（2025/07）。
- **組織因素（文化、主管支持、人才制度）解釋 67% 的 AI 成效關聯，個人因素只解釋 32%。**
- 只有 **26%** 認為領導層在 AI 上清楚一致；**65%** 怕不快用 AI 會落後，但 **45%** 覺得專注現有目標比較安全；只有 **13%** 覺得「用 AI 重塑工作即使沒成功也會被獎勵」。
- 「Frontier Professionals」只占 AI 使用者 **16%**。他們的主管：**公開使用 AI（85% vs 64%）、訂 AI 產出品質標準（83% vs 57%）、留出實驗空間（84% vs 61%）**。
- **主管以身作則**與 AI 價值感提升 17 個百分點、對 agentic AI 信任提升 30 個百分點相關。
- **86%** AI 使用者把 AI 產出當起點而非終稿；Frontier Professionals 更常**刻意不用 AI 做事（43% vs 30%）**、**動手前先決定哪些給 AI 哪些給人（53% vs 33%）**。
- Microsoft 365 中活躍 agent 年增 **15 倍**（大企業 18 倍）。
- 來源：[2026 Work Trend Index: Agents, human agency, and the opportunity for every organization](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)（2026-05-05）

### 1.6 企業層級的價值落差

- **BCG「The Widening AI Value Gap」**[轉述]：只有約 **5%** 企業是「future-built」，**60%** 沒有得到實質價值。領先者相對落後者：營收成長 1.7 倍、三年 TSR 3.6 倍、EBIT 利潤率 1.6 倍；AI 投資超過兩倍。Agent 占 AI 價值 17%（2025），預期 2028 年 29%。報告第一條策略是「強力領導與清楚的野心願景」；落後者常把 AI 策略丟給中低階主管 ⚠️（此點來自二手報導）。來源：[BCG press release](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings)（2025-09-30）；[報告 PDF](https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf)
- **MIT NANDA「The GenAI Divide」**[轉述]：常被引用的「95% 企業 AI 沒有可量測損益效果」，分母是**整合式試點**；樣本為 300+ 公開案例、52 場訪談、153 名高階主管問卷，作者自稱「方向性快照」。只有約 5% 企業級系統進入正式上線。來源：[MediaPost](https://mediapost.com/publications/article/408575/95-of-companies-get-zero-roi-from-gai-initiatives.html)（2025-08）。**引用時務必加註樣本小、自我選擇。**

---

## 2. 各角色怎麼應對

### 2.1 年輕人／新鮮人：入門職缺變少時怎麼累積能力

**處境**（證據見 1.1）：被擋在門外的方式是「沒被招」，不是「被裁」。受衝擊最大的是靠**明文知識**就能做的入門工作（程式、客服、資料輸入、行政文書）。

**應對（附支撐）**
1. **用 AI 的方式要能留下能力，不是只交差。** Anthropic RCT：全部委派給 AI 的人測驗 < 40%；先生成再追問、要求解釋、只問概念自己除錯的人 ≥ 65%。除錯能力流失最多。（[Anthropic, 2026-01-29](https://www.anthropic.com/research/AI-assistance-coding-skills)）
2. **往隱性知識靠：現場、客戶、判斷。** Canaries 發現依賴隱性知識的職業，資深者就業成長較快；AI 補的是明文知識。（[Canaries, 2026-08](https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf)）1111 調查中上班族認為最難被取代的能力是人際溝通 55.6%、情緒判斷 44.3%、現場應變 41.4%（見 3.2）。
3. **找「AI 輔助型」而非「AI 取代型」的崗位。** Canaries：AI 用來輔助的職業，就業持平或上升。
4. **AI 能力已是入場門票，不是加分。** 66% 領導者不雇沒有 AI 技能的人（[WTI 2024](https://blogs.microsoft.com/blog/2024/05/08/microsoft-and-linkedin-release-the-2024-work-trend-index-on-the-state-of-ai-at-work/)）；LinkedIn 2026 Skills on the Rise 中「AI literacy」不再上升，因為已成基本要求，上升的是 AI 實作、AI 商業策略等應用型技能 [轉述：[Philstar 專欄](https://www.philstar.com/business/2026/06/13/2534753/ai-literacy-new-floor)，2026-06-13 ⚠️ 意見專欄，需回查 LinkedIn 原文]。
5. **台灣不限科系的 AI 職缺很多。** 104：2026Q1 歡迎新鮮人的 AI 相關職缺 6.7 萬個，62% 不限科系，應用端（資訊軟體 1.3 萬、操作技術維修／客服門市業務各 8 千）已超越研發（7 千）（見 3.1）。
6. **要能證明「我驗得了 AI 的產出」。** BCG 研究中能力邊界外，用 AI 的人反而錯更多（[HBS](https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/)）；Robert Walters 調查中 76% 台灣雇主把「批判性思考與事實查核」列為 AI 時代最重要技能（見 3.1）。

**給企業的對應責任**：不招新人等於在拆自己的人才管線。Gartner 的組織扁平化預測也被指出會破壞傳統師徒路徑（見 2.3）。企業若要減少初階招募，至少要回答「五年後的中階從哪裡來」。

### 2.2 一般員工：哪些技能變值錢、哪些貶值

**貶值（AI 曝險高、以自動化為主）**
- 明文知識型、可標準化的任務：程式設計師任務覆蓋 75%、客服、資料輸入 67%（[Anthropic labor market, 2026-03](https://www.anthropic.com/research/labor-market-impacts)）。
- 台灣上班族自評最易被取代：翻譯 53.3%、行政文書 42.5%、美編設計 39.1%、行銷文案 32.4%、基礎程式開發 28.3%（1111，見 3.2）。

**變值錢**
- **判斷 AI 何時會錯**：jagged frontier 研究中，邊界外任務用 AI 答對率從 84.5% 掉到 60–70%。會判斷邊界的人才有價值。
- **工作設計**：Frontier Professionals 在動手前先決定哪些給 AI、哪些給人（53% vs 33%），也更常刻意不用 AI（43% vs 30%）（[WTI 2026](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)）。
- **批判思考與事實查核**：台灣雇主 76% 列為第一（Robert Walters，見 3.1）。
- **人際與現場能力**、隱性知識（Canaries 機制、1111 調查）。
- **WEF 2025**：AI 與大數據、資安、科技素養，加上創意思考、韌性與彈性。

**員工的具體動作**
1. **量測，不要憑感覺。** METR：開發者自認快 20%，實際慢 19%。
2. **把 AI 產出當起點。** 86% AI 使用者已這樣做（WTI 2026）；workslop 每次耗費接收者約 2 小時重工。
3. **受訓有用，但要夠量。** BCG AI at Work 2025：受過 5 小時以上訓練、有面對面教練的員工，規律使用率明顯較高；但只有約三分之一說受過適當訓練（[BCG, 2025-06-26](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)）[原文]。

### 2.3 中階主管：管人也管 agent、成為流程設計者

**結構性壓力**
- Gartner（2024-10）預測：到 2026 年，**20% 組織**會用 AI 扁平化，**砍掉一半以上的中階管理職**。這是預測，目前沒有 Gartner 的後續驗證。同篇報導也指出扁平化會破壞傳統師徒路徑，讓初階員工更少發展機會。來源：[CIO Dive](https://www.ciodive.com/news/Gartner-symposium-top-predictions-CIOs-AI-impact/730659/)（2024-10）[轉述]
- Amazon 2026 年 1 月約 1.6 萬人裁員被描述為「明確鎖定管理層」⚠️ 未驗證（只見二手意見文章）。
- BCG AI at Work 2025：**領導者與經理人（43%）比第一線（36%）更擔心十年內失業**（[BCG](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)）[原文]。

**新角色（附支撐）**
1. **Agent boss**：委派、指導、必要時介入 agent。36% 領導者預期五年內會管 agent（[WTI 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)）。
2. **決定人機配比（human-agent ratio）**：太少浪費、太多壓垮人的判斷（WTI 2025）。
3. **流程設計者**：WTI 2026 建議組織要定義「誰審查 agent 表現、誰能改 agent 工作流程、地方性成功怎麼擴散」，並把 agent 的經驗寫成共享、有文件的例行流程。
4. **以身作則＋訂品質標準＋給實驗空間**：這三件事是 Frontier 團隊與其他團隊差最多的地方（85/83/84% vs 64/57/61%）；主管示範使用與 AI 價值感 +17 點、對 agent 信任 +30 點相關（WTI 2026）。
5. **讓團隊敢分享 AI 的技巧與失誤**：Frontier 團隊分享 AI 技巧與錯誤 61% vs 36%、討論品質標準 54% vs 29%（WTI 2026）。這直接對應第 4 節的「隱性使用」問題。
6. **負責培訓**：51% 經理人認為 AI 培訓會成為團隊的關鍵責任（WTI 2025）。

### 2.4 高階管理層：願景、資源、治理、以身作則

1. **組織問題大於個人問題**：組織因素解釋 67% vs 個人 32%（WTI 2026）。高層不能把 AI 當成「員工自己去學」的事。
2. **願景要清楚一致**：只有 26% 員工認為領導層在 AI 上一致（WTI 2026）；60% 領導者自承缺乏計畫（WTI 2024）；BCG 領先企業把 AI 當成董事會與 CEO 主導的多年計畫。
3. **改激勵，不只喊口號**：只有 13% 員工覺得「嘗試用 AI 重塑工作、即使失敗」會被獎勵；45% 覺得守住現有 KPI 比較安全（WTI 2026）。WTI 2026 建議高層「對齊指標、誘因與期望，讓改變工作方式的人被獎勵」。
4. **領導支持的效果最大**：有強力領導支持時，對 AI 持正面態度的員工從 15% 升到 55%；但只有約四分之一第一線員工說有得到支持（BCG AI at Work 2025）。
5. **治理 agent 像治理員工**：WTI 2026 建議把 agent 當成有身分、有權限的受治理實體，內建監控與稽核。
6. **以身作則的案例**：Shopify CEO Tobi Lütke 2025 年 3 月內部備忘錄——「反射性使用 AI」是基本期待、AI 使用納入績效與同儕評核、**申請人力前要先證明 AI 做不到**。[轉述：[Workplace Journal](https://workplacejournal.co.uk/2025/04/shopify-ceo-calls-for-reflexive-ai-use-as-baseline-expectation-no-headcount-growth-until-options-explored/)，2025-04；Lütke 本人在 X 公開全文]。**白皮書使用提醒**：這個做法會直接壓縮初階招募，與 2.1 的人才管線風險是同一件事的兩面。
7. **高層自己的使用落差**：Gallup 2025——管理者的管理者（leaders）頻繁使用 AI 比例 33%，是個別貢獻者（16%）的兩倍；26% 的個別貢獻者不知道公司有沒有正式導入 AI（領導者僅 7%）。[轉述：[Gallup](https://www.gallup.com/workplace/691643/work-ai-adoption-takes-hold-employees-leaders.aspx)，2025]

### 2.5 公司整體

- **價值集中在少數**：5% future-built vs 60% 沒拿到價值（BCG 2025）；95% 試點無損益效果（MIT NANDA，樣本小）。
- **第一線停滯**：BCG 2025 第一線白領規律使用率卡在 51%，經理人 78%（[BCG](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)）。
- **重設計流程的副作用**：全面重設計流程的公司，員工擔心工作保障的比例 46%，未重設計者 34%（BCG 2025）。**轉型越深，溝通與安心工程越重要。**
- **Agent 剛起步**：只有 13% 員工認為 agent 已深度整合進日常工作，三分之一理解 agent 怎麼運作（BCG 2025）。

---

## 3. 台灣的人才市場與職場數據

> 台灣資料的主要問題：**官方（勞動部、主計總處、國發會）沒有找到員工層級的 AI 使用率調查**；現有數字多為人力銀行與顧問公司調查，常未揭露樣本數。下表的口徑差很多（是否用過、每天用、企業導入），不能互相比較。

### 3.1 職缺、薪資、技能需求

| 數據 | 數字 | 來源 | 等級 |
|---|---|---|---|
| 2026Q1 歡迎新鮮人的 AI 相關職缺 | **6.7 萬個**，**62% 不限科系**（4.1 萬） | [104 新聞稿 PDF](https://corp.104.com.tw/archive/storage/news/filename_1604.pdf)（2026-04-07） | 原文 |
| 新鮮人應徵 AI 職務 | 2025 年逾 7 萬人，**年增 46%** | 同上 | 原文 |
| AI 職缺產業分布 | 電子資訊/軟體/半導體 3 萬、一般製造 1 萬、批發零售 5 千 | 同上 | 原文 |
| AI 職缺職類 | 資訊軟體 1.3 萬；操作技術維修、客服門市業務各 8 千；**研發 7 千（應用端已超越研發）** | 同上 | 原文 |
| 2026 年歡迎新鮮人的正職 | 約 78 萬個；新鮮人月薪中位數 **3.6 萬元** | [104 職場力：2026 新鮮人求職趨勢](https://blog.104.com.tw/2026-fresh-graduate-job-search-trends/)（2026-05-14） | 原文（104 自家數據，未揭露方法） |
| 企業為 AI 技能加薪 | **75%** 企業願意，平均加薪逾 **9.5%**；光電業 AI 新人加薪可達 22.5% | 同上，引 104《2025 企業年終及 2026 薪酬趨勢大調查》 | 轉述 |
| 台灣專業人才使用 AI | **96%**（亞洲 93%）；**73%** 有信心持續更新 AI 技能（10 市場最高） | Robert Walters《未來職務洞察》，近 5,000 名亞洲專業人士與雇主；見 [104 職場力轉載經濟日報](https://blog.104.com.tw/?p=250253)（2026-08-31） | 轉述 |
| 台灣雇主預期員工需轉型 | **逾 90%** 預期五年內員工需為 AI 再培訓；18% 認為過半員工需技能轉型 | 同上 | 轉述 |
| 台灣雇主最重視的 AI 時代技能 | **批判性思考與事實查核 76%**（亞洲 64%） | 同上 | 轉述 |
| 台灣專業人士的 AI 憂慮 | 資料誤用或保密 54%、AI 錯誤的責任歸屬 51%（皆為 10 市場最高） | 同上 | 轉述 |

### 3.2 員工使用率與態度

| 數據 | 數字 | 來源 | 等級 |
|---|---|---|---|
| 104《2025 員工 C.E.O. 調查》生成式 AI 使用 | 半數以上用過；**八年級後 80%、七年級 54%、六年級 38%、四五年級 22%** | [遠見城市學：104 調查](https://city.gvm.com.tw/article/123666)（2025-08-21） | 轉述（樣本數未揭露） |
| 同上，用途 | 文件撰寫 47%、報告生成 44%、創意設計 25% | 同上 | 轉述 |
| 同上，考慮減少使用的原因 | 隱私與資安 31%、準確性低 25%、**主管或高層不接受 16%** | 同上 | 轉述 |
| PwC《2025 希望與恐懼調查》台灣 | 過去一年工作用過 AI：**台灣 64%**（全球 54%）；**每天用：台灣 13%**（全球 14%） | [中央社](https://cna.com.tw/business/chinese/418385)（2025-11-12）；全球 49,843 人，台灣 413 人 | 轉述 |
| 同上，每日使用者的獲益 | 生產力提升 台灣 94%／全球 92%；工作保障 55%／58%；薪資 **38%／52%** | 同上 | 轉述 |
| 資策會 MIC 網友調查 | **46%** 用過生成式 AI；18–25 歲 **69%**；每天用 1 次以上僅 **9%**；**個人自費 17%**、企業付費 22% | [經理人引 MIC](https://www.managertoday.com.tw/articles/view/70536)（2025-06） | 轉述（MIC 原文未見） |
| TWNIC《2025 台灣網路報告》 | **43.19%** 民眾用過生成式 AI；8.54% 願付費 | 同上搜尋結果轉述 | ⚠️ 未驗證 |
| 微軟 WTI 2024 台灣 | **84%** 知識工作者使用生成式 AI | [INSIDE](https://www.inside.com.tw/article/35378-microsoft-copilot)（2024） | 轉述 |

### 3.3 恐懼與準備

**1111 × 臺北市勞動局《2026 上班族 AI 焦慮與職涯準備調查》**[原文：1111 新聞頁；樣本數與調查期間未揭露]
- 擔心被 AI 取代的程度：平均 **6.29 分**（滿分 10）；預估 **2.56 年**內工作內容會明顯受影響。
- **75%** 感受到企業對 AI 能力要求增加；**85.7%** 認為 AI 能力有助求職。
- 但**只有 14.2% 已積極學習**；**58.9% 想學但還沒開始**；學習困境首位是「不知道從哪裡開始」56.9%。
- **71.8%** 最希望企業提供 AI 培訓課程。
- 跨入 AI 工作的門檻：不懂 AI 工具 46.6%、不知從何開始 38.6%。
- 來源：[1111：上班族擔心 AI 取代工作](https://www.1111.com.tw/news/167165/amp/)（2026-08-17）

**1111 2025 年 7 月調查**：**61.5%** 上班族擔心工作被 AI 取代，19.1% 非常擔心。[轉述：[中時旺得富](https://wantrich.chinatimes.com/news/20250704900401-420501)，2025-07-04；原文頁 403]

### 3.4 企業導入與培訓

| 數據 | 數字 | 來源 | 等級 |
|---|---|---|---|
| AIF《2026 台灣產業 AI 化大調查》AI 化指數 | **46.32 分**（去年 36.77） | [經理人](https://www.managertoday.com.tw/articles/view/72095)（2026-05-04） | 轉述（樣本數未揭露；作者提醒受訪企業偏重視 AI，結果可能偏樂觀） |
| 同上，影子 AI | **61.8%** 的 AI 使用發生在組織控管之外 | 同上 | 轉述 |
| 同上，培訓 | **44.7%** 企業沒有任何 AI 人才培訓計畫；人才策略子項 29.17 分，所有子項最低 | 同上 | 轉述 |
| 同上，整合深度 | 只有 **6.6%** 企業把 AI 完整整合進核心業務流程 | 同上 | 轉述 |
| 同上，產業差異 | ICT 52.7 分 vs 營建與農業 26.9 分 | 同上 | 轉述 |
| 1111「AI 如何驅動台灣產業升級調查」 | **79.8%** 企業導入 AI；但只有 **6.3%** 廣泛應用於各工作流程；18.6% 營運效率顯著提升 | [NOWnews](https://www.nownews.com/news/6689465)（2025-05-30） | 轉述 |
| 經濟部中小企業白皮書 | 中小企業實際導入 AI 約 **7.4%**（OECD 中小企業 39%） | 只見搜尋摘要轉述，未讀到白皮書原文 | ⚠️ 未驗證 |
| 經濟部產業競爭力輔導團 | 至 2026/03 底輔導 2,058 家企業導入 AI，中小企業占 91% | 同上搜尋摘要 | ⚠️ 未驗證 |
| 勞動部 | 研議「勞資 AI 指南」，五大原則含公開透明、保護勞工個資、人為監督決策 | [104 職場力](https://blog.104.com.tw/the-principles-of-the-five-ai-guidelines/)（2026） | 轉述（政策規劃，非調查） |

**台灣的關鍵張力**：「企業導入」口徑可以從 7.4%（中小企業實際導入，未驗證）跳到 79.8%（1111 企業自報），但不管哪個口徑，**「完整整合進流程」都只有約 6%**（AIF 6.6%、1111 6.3%）。員工端則是「想學、覺得要學、但沒開始」（58.9%）加上「企業沒培訓計畫」（44.7%）。

---

## 4. 員工心理：恐懼、隱性使用、不敢說

### 4.1 隱性使用（Shadow AI / BYOAI）

| 研究 | 數字 | 來源 | 等級 |
|---|---|---|---|
| Microsoft/LinkedIn WTI 2024 | **78% 的 AI 使用者自帶 AI 工具上班** | [Microsoft](https://blogs.microsoft.com/blog/2024/05/08/microsoft-and-linkedin-release-the-2024-work-trend-index-on-the-state-of-ai-at-work/)（2024-05-08） | 原文 |
| BCG AI at Work 2025 | **過半**員工說沒有需要的 AI 工具時會自己找替代品照用（二手報導為 54%） | [BCG](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)（2025-06-26） | 原文（54% 為轉述） |
| AIF 2026 台灣 | **61.8%** AI 使用在組織控管外 | [經理人](https://www.managertoday.com.tw/articles/view/72095)（2026-05-04） | 轉述 |
| KPMG × 墨爾本大學 2025 全球信任研究 | 47 國、48,000+ 人（2024/11–2025/01）：**57%** 員工隱藏 AI 使用並把 AI 產出當成自己的成果；**近半**違反公司政策使用；**66%** 不查核就採用 AI 產出；**56%** 因 AI 出錯；只有 **47%** 受過 AI 訓練、**40%** 說公司有 AI 政策 | [University of Melbourne 新聞稿](https://fbe.unimelb.edu.au/newsroom/media-release-global-study-reveals-trust-of-ai-remains-a-critical-challenge-reflecting-tension-between-benefits-and-risks)（2025-04/05） | 轉述（新聞稿頁 403，數字見搜尋引用原文） |
| Cybernews（2025-08，1,003 名美國員工） | **59%** 使用雇主未核准的 AI 工具；其中 57% 說直屬主管知道且支持 | 搜尋摘要 | ⚠️ 未驗證 |

### 4.2 不敢說自己用 AI

| 研究 | 數字 | 來源 | 等級 |
|---|---|---|---|
| Slack Workforce Index（2024 秋） | **48%** 辦公室工作者不敢跟主管承認用 AI 做常見工作；原因：覺得像作弊 47%、怕顯得不夠能幹 46%、怕顯得懶 46%。**能自在跟主管談 AI 的人，使用 AI 的可能性高 67%** | [Slack Fall 2024 Workforce Index](https://slack.com/intl/zh-sg/blog/news/the-fall-2024-workforce-index-shows-executives-and-employees-investing-in-ai-but-uncertainty-holding-back-adoption)；[ITPro](https://itpro.com/technology/artificial-intelligence/nearly-half-of-workers-think-using-ai-makes-them-look-lazy-and-incompetent) | 轉述（樣本數各家報導不一：1 萬或 1.7 萬人） |
| WalkMe/SAP「AI in the Workplace 2025」（1,000 名美國員工） | **48.8%** 曾為避免被評價而隱藏 AI 使用；**C-suite 53.4%** 更高；Z 世代 62% 隱藏使用 | 搜尋摘要（[PeopleMatters](https://www.peoplematters.in/news/ai-and-emerging-tech/ai-shame-what-it-is-and-how-its-creeping-into-your-workplace-43213)） | ⚠️ 未驗證 |
| 104 員工 C.E.O. 2025（台灣） | 考慮減少使用 AI 的原因中，**「主管或高層不接受」16%** | [遠見城市學](https://city.gvm.com.tw/article/123666)（2025-08-21） | 轉述 |

**解讀**：隱藏使用不是個人道德問題，是**組織訊號問題**。Slack 的 67% 與 WTI 2026「主管公開使用 AI 85% vs 64%」指向同一件事——主管不先講，員工就不會講；員工不講，企業就看不到風險（KPMG：66% 不查核就用、56% 因 AI 出錯），也收不到可複製的好做法。

### 4.3 恐懼被取代

| 研究 | 數字 | 來源 | 等級 |
|---|---|---|---|
| 1111 × 北市勞動局 2026（台灣） | 擔憂 6.29/10；預估 2.56 年內明顯受影響 | [1111](https://www.1111.com.tw/news/167165/amp/)（2026-08-17） | 原文 |
| 1111 2025-07（台灣） | 61.5% 擔心被取代，19.1% 非常擔心 | [中時](https://wantrich.chinatimes.com/news/20250704900401-420501)（2025-07-04） | 轉述 |
| Anthropic Economic Index（2026-06） | 10% 認為明年自己可能失業；**擔心別人多於自己，最擔心初階同事** | [Anthropic](https://www.anthropic.com/research/economic-index-june-2026-report)（2026-06-26） | 原文 |
| BCG AI at Work 2025 | 經理人／領導者 43% vs 第一線 36% 擔心十年內失業；全面重設計流程的公司 46% vs 34% | [BCG](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)（2025-06-26） | 原文 |
| WTI 2026 | 65% 怕不快用 AI 會落後 | [Microsoft](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)（2026-05-05） | 原文 |

**有意思的反差**：恐懼最強的不一定是最被衝擊的人。實證上被衝擊的是**還沒進來的年輕人**（招募減少），但在職者中最擔心的反而是**經理人與領導者**（BCG 43%）。另外 Anthropic 的資料顯示，自動化程度越高的使用者，對薪資與求職反而越樂觀——「用得深」和「怕得少」相關（相關，不是因果）。

---

## 5. 研究缺口（白皮書引用前要注意）

1. **因果尚未確立**：Canaries、Anthropic labor market、Hosseini & Lichtinger 都是觀察性研究，作者都自稱早期或暫定。升息、遠距工作、疫情後調整都是競爭解釋。
2. **台灣官方數據缺席**：沒有找到勞動部、主計總處、國發會的員工層級 AI 使用率調查；人力銀行調查多未揭露樣本數。
3. **生產力研究的時效**：METR 19% 是 2025 年初工具；BCG jagged frontier 是 GPT-4 時期。能力邊界一直在移動，**「邊界」這個概念可引用，具體數字要標時間**。
4. **Shadow AI 數據多為廠商調查**（WalkMe、Cybernews 等），有推銷治理產品的動機，引用時要說明。
5. 本次未查到：LinkedIn Skills on the Rise 2026 原文、WEF 原文完整技能清單、經濟部中小企業白皮書 AI 導入率原文、天下／商周的台灣專題數據（付費牆）。

---

## 對企業白皮書最有用的 10 個洞見

1. **AI 衝擊的是「招募」不是「裁員」**：22–25 歲在 AI 曝險職業的就業比應有水準低 19%，主要因為少招，資深者沒有缺口。——[Brynjolfsson et al., Canaries in the Coal Mine?（2026-08 版）](https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf)
2. **AI 用來「輔助」的職業就業沒掉，用來「取代」的才掉**：企業怎麼部署 AI，決定它是擴大還是縮小人力。——[同上](https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial)
3. **AI 能力有鋸齒狀邊界**：邊界內品質提升約三到四成，邊界外答對率從 84.5% 掉到 60–70%，受過提示訓練的人錯更多。——[Dell'Acqua et al., Organization Science 2026 / HBS](https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/)
4. **「覺得變快」不等於「真的變快」**：資深開發者自認快 20%，實測慢 19%，所以導入 AI 一定要量測。——[METR（2025-07-10）](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
5. **用 AI 的方式決定新人學不學得會**：全部委派給 AI 的人理解測驗 < 40%，追問理解的人 ≥ 65%，除錯能力流失最多。——[Anthropic（2026-01-29）](https://www.anthropic.com/research/AI-assistance-coding-skills)
6. **AI 成效 67% 來自組織因素、32% 來自個人**：主管支持、文化與人才制度，比員工個人努力重要兩倍。——[Microsoft WTI 2026（2026-05-05）](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)
7. **主管公開用 AI、訂品質標準、給實驗空間**，是成熟團隊與一般團隊差最多的三件事；只有 13% 員工覺得嘗試失敗會被獎勵。——[同上](https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization)
8. **隱性使用是常態，不是例外**：全球 57% 員工隱藏 AI 使用，台灣 61.8% 的 AI 使用在組織控管外；敢跟主管談 AI 的人使用率高 67%。——[KPMG × 墨爾本大學 2025](https://fbe.unimelb.edu.au/newsroom/media-release-global-study-reveals-trust-of-ai-remains-a-critical-challenge-reflecting-tension-between-benefits-and-risks)；[AIF 2026 台灣產業 AI 化大調查](https://www.managertoday.com.tw/articles/view/72095)；[Slack Workforce Index 2024 秋](https://slack.com/intl/zh-sg/blog/news/the-fall-2024-workforce-index-shows-executives-and-employees-investing-in-ai-but-uncertainty-holding-back-adoption)
9. **台灣員工想學但沒開始，企業也沒教**：85.7% 認為 AI 能力有助求職但只有 14.2% 積極學習，44.7% 企業沒有 AI 培訓計畫，71.8% 員工最希望企業提供培訓。——[1111 × 北市勞動局 2026](https://www.1111.com.tw/news/167165/amp/)；[AIF 2026](https://www.managertoday.com.tw/articles/view/72095)
10. **台灣「導入」很多，「整合」很少**：企業自報導入近八成，但完整整合進核心流程只有約 6%，價值卡在流程重設計，不在工具採購。——[1111 產業升級調查（2025-05-30）](https://www.nownews.com/news/6689465)；[AIF 2026](https://www.managertoday.com.tw/articles/view/72095)；呼應 [BCG Widening AI Value Gap：僅 5% 企業取得規模價值](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings)
