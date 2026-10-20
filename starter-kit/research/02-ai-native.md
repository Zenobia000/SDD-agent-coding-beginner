# AI-native 公司與企業「數位員工」研究

> 研究日期：2026-10-20｜研究方式：WebSearch（未能逐篇開啟原文者已標註）
> 用途：企業白皮書素材

## 可信度分級（全文標註用）

| 標記 | 類型 | 怎麼用 |
|---|---|---|
| **[A 研究]** | 學術論文、官方統計（Census、OECD）、公司財報／SEC 文件 | 可直接當論據 |
| **[B 顧問／廠商調查]** | McKinsey、BCG、Gartner、Microsoft WTI、MIT NANDA | 樣本與定義由發布方決定，有立場；引用時寫明「某某調查」 |
| **[C 媒體報導]** | TechCrunch、Fortune、The Register 等轉述 | 數字多來自公司自述或匿名消息，需交叉比對 |
| **[D 個案／自述]** | CEO 貼文、新創自報 ARR、第三方估算站（Latka 等） | 只能當例子，不能當趨勢證據 |

**本次研究的整體限制**：多數條目透過搜尋結果摘要取得，未逐一打開原文全文。Microsoft WTI 2025 已直接讀取官方頁面；其餘標「轉述」者代表數字是由二手報導取得。

---

## 1. AI-native / AI-first 公司：定義與營運模式

### 1.1 定義：AI-enabled vs AI-native

目前**沒有權威機構的統一定義**，以下是業界常見用法的歸納 [C/D]：

| | AI-enabled | AI-native |
|---|---|---|
| AI 的位置 | 在既有流程上加一個 AI 模組，拿掉 AI 核心流程照樣運作 | 流程、人力、定價從一開始就以 AI 為前提設計；拿掉 AI 業務不成立 |
| 改變的東西 | 工具 | 誰做事、怎麼定價、決策怎麼做 |
| 典型問法 | 「這個步驟可以用 AI 加速嗎？」 | 「如果 agent 能做 80%，這個流程應該長什麼樣？」 |

- 判斷測試：「把 AI 拿掉，這門生意還說得通嗎？說不通，AI 就是引擎而非功能。」——[What is an AI-native company (Leanware)](https://leanware.co/insights/ai-native-companies-definition-strategic-framework)（未標日期）[D]
- 有些作者另立第三類「AI-first」：上線後才重新以 AI 為平台改造的公司（Shopify、Duolingo 屬此類）。——同上 [D]
- **權威機構的對應框架**：McKinsey 用「agentic organization」描述同一件事：以 AI 為先重建 workflow、組織走向以成果為導向的扁平 agentic teams，人與 agent（虛擬與實體）並肩工作。——[The agentic organization: Contours of the next paradigm for the AI era (McKinsey)](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era)（2025）[B，轉述]
- ⚠️ 未驗證：McKinsey「五大維度」框架（策略、營運模式、技術資料、人才組織、治理）只見於二手部落格，未在 McKinsey 原文確認。

**為什麼這個區分重要（有數據的部分）**：
- McKinsey《The state of AI in 2025》：近九成受訪組織經常使用 AI，但「高績效者」（AI 貢獻 ≥5% EBIT，約佔樣本 6%）**根本性重新設計 workflow 的機率約是其他人的 3 倍**，且在多數職能中「正在規模化 agent」的機率至少是同儕的 3 倍。——[The state of AI in 2025: Agents, innovation, and transformation (McKinsey)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)（2025）[B，轉述]
- 同調查：預期未來一年員工數減少 32%、不變 43%、增加 13%。——同上 [B，轉述]
- BCG：只有 5% 公司屬於「future-built」，相較落後者營收成長 1.7 倍、三年 TSR 3.6 倍、EBIT margin 1.6 倍；60% 屬落後者，幾乎沒有實質營收或成本效益。Agent 佔 2025 年 AI 總價值 17%，預估 2028 年 29%。——[BCG press release: AI leaders outpace laggards](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings)（2025-09-30）；[The Widening AI Value Gap (BCG PDF)](https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf)（2025-10）[B]
- MIT NANDA《The GenAI Divide: State of AI in Business 2025》：企業在 GenAI 投入 300–400 億美元，95% 組織沒有可量測的報酬；主因是「學習落差」：workflow 脆弱、無法保留回饋與 context、跟日常營運脫節，而不是模型品質。——[MIT report finds most AI business investments fail (Virtualization Review)](https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx)（2025-08-19）[B，轉述]
  - **注意樣本小**：約 300 個公開專案、52 家組織訪談、153 位主管問卷，作者自稱是「方向性快照」。引用時不要寫成「95% AI 專案失敗」。

**小結**：「AI-enabled」是多數企業的現況，報酬普遍不明顯；有報酬的少數，共同點是**重新設計流程**，不是買更多工具。

### 1.2 Tiny teams 與人均營收（逐案查證）

> 全部是私人公司自報或媒體報導，**ARR 是年化 run-rate，不是經審計營收**。人均營收為本研究自行估算。

| 公司 | 營收指標 | 人數 | 估算人均 | 來源與可信度 |
|---|---|---|---|---|
| **Cursor（Anysphere）** | 2025-06 ARR > 5 億美元；2025-11 Series D 時年化營收 > 10 億美元（$2.3B，估值 $29.3B） | ⚠️ 說法分歧：約 150、182、「略多於 300」 | 以 10 億／300 人估約 330 萬美元；以 150 人估約 670 萬 | [Anysphere (Wikipedia)](https://en.wikipedia.org/wiki/Anysphere)；[Cursor statistics (SQ Magazine)](https://sqmagazine.co.uk/cursor-ai-statistics/) [C/D] |
| Cursor（後續） | ⚠️ 未驗證：2026-05 ARR 30 億美元；SpaceX 以 600 億美元收購 | — | — | 僅見於 Wikipedia 與彙整站，未找到一手公告 |
| **Midjourney** | 2024 營收約 2–3 億美元（說法分歧；3 億來自路透引用的訴訟資料）；2025 估約 5 億 | 約 107–163（LinkedIn 推估）；官網自稱約 60 人研究室 | 約 300–470 萬美元 | [Midjourney statistics (gradually.ai)](https://www.gradually.ai/en/midjourney-statistics/)；[How many people work at Midjourney (SQ Magazine)](https://sqmagazine.co.uk/how-many-people-work-at-midjourney/) [D]；**零外部募資**一致 |
| **Lovable** | 上線 8 個月 ARR 破 1 億美元 | 45 名全職（另有 14 個開缺） | 約 220 萬美元 | [Eight months in, Swedish unicorn Lovable crosses the $100M ARR milestone (TechCrunch)](https://techcrunch.com/2025/07/23/eight-months-in-swedish-unicorn-lovable-crosses-the-100m-arr-milestone)（2025-07-23）[C] |
| **Gamma** | 有獲利的 ARR 1 億美元、7,000 萬使用者，a16z 領投 $68M、估值 $2.1B | 約 50 | 約 200 萬美元 | [How Gamma built a profitable empire with 50 people (TNW)](https://thenextweb.com/news/gamma-grant-lee-profitable-ai-startup)；[Lenny's Newsletter](https://lennysnewsletter.com/p/how-50-people-built-a-profitable-ai-unicorn)（2025-11）[C] |
| **Base44** | 創辦人單人 side project、零募資，半年後被 Wix 以 8,000 萬美元現金（另有 earn-out）收購；25 萬使用者 | 6–8 人（說法分歧） | — | [Wix acquires Israeli vibe coding co Base44 (Globes)](https://en.globes.co.il/en/article-wix-acquires-israeli-vibe-coding-co-base44-1001513267)（2025-06）[C] |
| 對照：**Klarna**（AI-first 的成熟公司） | 人均營收從約 40 萬升至約 70 萬美元（換算匯率不同，說法 69–82 萬） | 約 3,800（高峰 5,000+） | — | [Klarna 1,800 employees AI replace IPO (Fortune)](https://fortune.com/europe/2024/08/28/klarna-1800-employees-ai-replace-ipo)（2024-08-28）[C] |

**解讀（給白皮書用）**：
- 傳統 SaaS 人均營收常被引用的量級約 20–30 萬美元（⚠️ 未驗證，本次未查到權威基準）。上表 AI-native 新創是其 **7–20 倍**，但多數**營收成長期極短、毛利受模型推論成本侵蝕**，人均營收高不等於人均獲利高（Gamma 是少數公開說有獲利的）。
- 共通做法（來自個案自述，[D]）：工程師自己用 AI 寫大部分程式碼、極少中階管理、產品本身就在吃 AI 的槓桿。這些是**新創從零設計**的結果，大企業無法直接複製人數比例。

### 1.3 決策與流程怎麼重新設計（有出處的做法）

1. **把「用 AI」變成預設，把「加人」變成例外**：Shopify、Duolingo 都把「先證明 AI 不能做才加人」寫進預算流程（見第 2 節）。
2. **把 AI 能力放進招募與考核**：Shopify、Duolingo、Zapier 都這樣做；但 Duolingo 後來**拿掉**考核裡的 AI 使用項目（見 2.2）。
3. **以 workflow 為單位重設，而不是以工具為單位**：McKinsey 高績效者的主要區別因子（見 1.1）。
4. **組織層因素大於個人**：Microsoft WTI 2026 稱組織因素（文化、主管支持）對 AI 成效的影響是個人心態的兩倍以上（67% vs 32%）；只有約四分之一 AI 使用者說領導層對 AI 策略一致。——[Microsoft 2026 Work Trend Index highlights (Pulse 2.0)](https://pulse2.com/microsoft-2026-work-trend-index-highlights-expanding-role-of-ai-agents-in-enterprise-workflows/)（2026）[B，轉述；未讀到微軟原文]

---

## 2. 公開的 AI-first 宣言：原文、作法、效果與反彈

### 2.1 Shopify（2025-04）

- **原文**：CEO Tobi Lütke 內部備忘錄，因「正被惡意外洩」而自行貼到 X。核心句：「Reflexive AI usage is now a baseline expectation at Shopify」。——[Internal memo: Shopify CEO declares AI non-optional (Digital Commerce 360)](https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/)（2025-04-08）[C 轉載原文]；原 X 貼文 ⚠️ 本次未直接開啟
- **作法**：
  - 申請加人或資源前，團隊必須說明為什麼 AI 做不到。——[Shopify CEO tells teams to consider using AI before growing headcount (TechCrunch)](https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/)（2025-04-07）[C]
  - AI 使用納入績效與同儕評核問卷；適用全員含領導層（⚠️「原型階段應以 AI 為主」一條常被引用，但本次未在原文核對）。——同上、[eMarketer](https://www.emarketer.com/content/shopify-sets-ai-use-core-expectation-workers--requires-proof-ai-can-t-do-job-before-hiring-more) [C]
  - Lütke 自述先前的推動「太像建議」，所以改成強制。——[Barchart](https://www.barchart.com/story/news/31785636/shopify-relying-on-ai-to-keep-employee-headcount-flat) [C]
- **效果**：Form 10-K 揭露員工從 2024 年底約 8,100 人降到 2025 年底約 7,600 人（約 -6%）；Jefferies 分析師歸因於「AI 帶來的效率與費用紀律」，且主要是自然流失而非裁員。——[Shopify Q4 strength highlights AI (Proactive Investors)](https://www.proactiveinvestors.co.uk/companies/news/1087574/shopify-q4-strength-highlights-ai-and-marketplace-growth-analysts-1087574.html)（2026-02）[C；10-K 數字為轉述，⚠️ 建議回查 SEC 原件]
- **背景**：Shopify 在 2022 年裁 14%、2023 年裁 20%。——[NBC San Diego / CNBC](https://www.nbcsandiego.com/news/business/money-report/shopify-ceo-says-staffers-need-to-prove-jobs-cant-be-done-by-ai-before-asking-for-more-headcount/3797338)（2025-04）[C]
- **反彈**：相對溫和；主要批評是「把 AI 當凍結人力的理由」。這份備忘錄後來成為一波 CEO AI-first 備忘錄的範本。

### 2.2 Duolingo（2025-04-28）—— 反彈最大的案例

- **原文**：CEO Luis von Ahn 的內部信，後貼在 Duolingo LinkedIn。三條「constructive constraints」：逐步停止讓約聘人員做 AI 能做的事；招募看 AI 能力；績效考核看 AI 使用；**只有在團隊無法再自動化更多工作時才加人**。關鍵句：「Making minor tweaks to systems designed for humans won't get us there.」——[Duolingo announces AI-first strategy (Mind the Product)](https://www.mindtheproduct.com/duolingo-announces-ai-first-strategy/)（2025-04-28）；[Duolingo goes 'AI first' as it phases out human contractors (Computing)](https://www.computing.co.uk/news/2025/ai/duolingo-goes-ai-first-as-it-phases-out-human-contractors)（2025-04）[C 引原文]
- **反彈與修正**：
  - 2025-05 von Ahn 在 LinkedIn 承認「我發這份備忘錄時沒做好」，說目標不是取代人、招募速度不變。——[Duolingo CEO clarifies AI stance after backlash (Entrepreneur)](https://www.entrepreneur.com/business-news/duolingo-ceo-clarifies-ai-stance-after-backlash-read-memo/492141)（2025-05）[C]
  - 2025-08 接受 NYT 訪問：「I did not give enough context」；公司從未裁過正職、也不打算裁；約聘人數會隨需求浮動。——[Duolingo CEO admits controversial AI memo did not give enough context (Fortune)](https://fortune.com/2025/08/18/duolingo-ceo-admits-controversial-ai-memo-did-not-give-enough-context-insists-company-never-laid-off-full-time-employees)（2025-08-18）[C]
  - 後續報導稱 Duolingo 已不再把 AI 使用納入績效考核。——⚠️ 未驗證（僅見於社群轉貼的 podcast 摘要）
- **效果（混合）**：
  - 正面：管理層把一年上線 148 門新語言課歸功於 GenAI；2025 年 DAU 破 5,000 萬、bookings 破 10 億美元、adjusted EBITDA 破 3 億美元。2026 Q1 單季發布 20,500 個課程單元。——[Duolingo's AI-first strategy (Nasdaq/Zacks)](https://www.nasdaq.com/articles/duolingos-ai-first-strategy-data-secures-dominance-ed-tech)（2026）[C，公司財報轉述]
  - 負面：DAU 年增率從 2025-02 的 56% 一路降到 2025-06 的 37%，媒體推測部分與 AI-first 反彈有關；股價自 2025 高點大幅回落（不同來源 -57% 至近 -80%）。——[Slashdot / Motley Fool](https://tech.slashdot.org/story/25/06/28/2036249/)（2025-06-28）[C]
  - **因果未證實**：成長放緩也可能來自 ChatGPT 類工具的競爭。不能寫成「AI-first 導致股價下跌」。

### 2.3 Fiverr（2025-09-15）

- **原文**：CEO Micha Kaufman 致員工信，宣布轉為「AI-first」公司、減少管理層級；信中說 AI 專案顯示「我們不需要這麼多人來運作現有業務」。約 250 人被裁，佔比報導不一（約 25%–30%，2024 年底員工 762 人）。——[Fiverr laying off 250 as part of AI-focused restructuring (Staffing Industry Analysts)](https://www.staffingindustry.com/news/global-daily-news/fiverr-laying-off-250-as-part-of-ai-focused-restructuring)（2025-09）；[Calcalist](https://www.calcalist.co.il/ctechnews/article/my0gxhpzg)（2025-09）[C]
- **前情**：Kaufman 2025-04 已有一封廣為流傳的「AI is coming for your jobs」信。⚠️ 未驗證：本次搜尋未取得該信原文出處。
- **反彈**：LinkedIn 留言批評「tone deaf」。——[Ragan](https://www.ragan.com/the-week-in-comms-fiverr-ford-att/)（2025-09）[C]
- **效果**：⚠️ 本次未查到裁員後的營運數據。

### 2.4 Zapier（2025-05-30）

- **原文**：CEO Wade Foster 在 LinkedIn 宣布「100% of new hires must be fluent in AI」，並提供候選人 AI 訓練素材、改版 onboarding。——[Zapier mandates AI fluency for all new hires (PPC Land)](https://ppc.land/zapier-mandates-ai-fluency-for-all-new-hires/)（2025-06）[C]
- **作法特點**：公開 AI fluency 評分表（從 resistant 到 transformative 分級），並建議**按職能各自定義 AI fluency 的具體用例**，不要一套通用標準。——[The 90% rule: why Zapier's AI strategy mixes humans + agents (SaaStr)](https://saastr.com/the-90-rule-why-zapiers-5b-ai-strategy-mixes-humans-agents-and-4-mistakes-that-kill-ai-rollouts-with-ceo-wade-foster/)（2025）[C/D]
- **反彈**：未見顯著反彈（未裁員、只提高招募門檻）。
- ⚠️ 未驗證：PPC Land 列出的具體測驗題（建 MCP server 等）屬評論者 Robert Scoble 的提案，不是 Zapier 官方流程。

### 2.5 Box

- ⚠️ **未找到「Box AI-first 備忘錄」原文**。二手彙整稱 Box 是 Shopify 之後跟進發 AI-first 備忘錄的公司之一，但沒有引文。
- 可查到的是 CEO Aaron Levie 的公開說法：「我們告訴全公司每個人，要盡可能用 AI 提升生產力，在整個業務中積極使用」；每週 all-hands 有員工 AI 使用 demo。——[GeekWire Podcast: Box CEO Aaron Levie on AI agents (GeekWire)](https://www.geekwire.com/2025/geekwire-podcast-box-ceo-aaron-levie-on-ai-agents-enterprise-data-and-the-future-of-work/)（2025）[C/D]
- 白皮書引用時應寫「Box 執行長公開表示…」，**不要寫「Box 發布 AI-first 備忘錄」**。

### 2.6 補充：Klarna（最常被引用的「翻車再修正」案例）

- 2024 年宣稱 AI 助理處理 75% 客服對話、相當於 700 名客服人力；2023-12 起凍結非工程招募。2025-05 CEO 對 Bloomberg 說 AI 客服雖便宜但品質較低，重新招募人類客服，讓客戶「永遠找得到真人」；公司稱是「雙軌」而非倒退。——[Klarna reverses AI customer service overhaul (Tech.co)](https://tech.co/news/klarna-reverses-ai-overhaul)（2025-05）；[Entrepreneur](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)（2025-05）[C]

### 2.7 第 2 節歸納

| | 宣言重點 | 是否裁員 | 反彈程度 | 可觀察效果 |
|---|---|---|---|---|
| Shopify | 加人前先證明 AI 不能做 | 否（自然流失） | 低 | 員工 -6%（10-K 轉述） |
| Duolingo | 取代約聘、考核看 AI | 否（正職），約聘減少 | **高** | 產能大增；用戶成長放緩（因果未證） |
| Fiverr | AI-first + 裁 25–30% | 是 | 中高 | 未知 |
| Zapier | 新人 100% 須 AI fluent | 否 | 低 | 未知 |
| Klarna | AI 取代 700 名客服 | 以凍招＋自然流失為主 | 品質問題 → 改回雙軌 | 人均營收上升 |

**模式**：**「AI 做不到才加人」（控制增量）** 比 **「AI 取代既有人」（削減存量）** 的反彈小得多；Duolingo 的教訓是溝通——說「取代約聘」卻沒說清楚正職不受影響。

---

## 3. 數位員工 / AI agent 的實際部署

### 3.1 Microsoft Work Trend Index 2025：Frontier Firm 與 agent boss

來源：[2025: The year the Frontier Firm is born (Microsoft WorkLab)](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)（2025-04-23）[B，已讀原文]
方法：Edelman Data x Intelligence 調查 31 國約 31,000 名知識工作者（2025-02-06 至 03-24），加上 Microsoft 365 遙測與 LinkedIn 資料。**是 Microsoft 自己的調查，Microsoft 賣 Copilot 與 agent，有立場。**

- **Frontier Firm 定義**：全組織部署 AI、AI 成熟度高、正在且計畫使用 agent、認為 agent 是 AI ROI 關鍵。9,037 名受訪主管中 844 人（約 9%）屬此類。
- **三階段**：① AI 當助理 → ② agent 作為「數位同事」在人的指揮下執行任務 → ③ 人設定方向，agent 跑整段業務流程。
- **Human-agent ratio**：**微軟沒有給數字**，只是提出這個新指標，要主管自問「每個角色需要幾個 agent、需要幾個人來引導它們」，並說比例是**依任務而定**。白皮書不應引用任何「微軟建議的人機比例」。
- **Agent boss**：每個員工都要學會建立、委派、管理 agent。主管 vs 員工落差：熟悉 agent 67% vs 40%；預期自己要管理 agent 36% vs 21%。
- 46% 主管說公司已用 agent 全自動化某些 workflow；82% 有信心 12–18 個月內用「數位勞動力」擴充人力；81% 預期 agent 會中度或大量整合進 AI 策略。
- 人力策略前三名：既有員工 AI 技能訓練 47%、維持人數並以 AI 當數位勞動力 45%、用 AI 減少人數 33%。
- 結果面：Frontier Firm 員工有 71% 說公司正蓬勃發展，全球平均 37%。（相關不等於因果）

**WTI 2026 後續（轉述）**：調查 10 國 20,000 名 AI 使用者（2026-02 至 04）。提出四種人機協作模式（Author、Editor、Director、Orchestrator），主張依工作流挑選模式，而不是一律上多 agent 協作；「Transformation Paradox」：採用速度超過組織重設速度。——[Pulse 2.0](https://pulse2.com/microsoft-2026-work-trend-index-highlights-expanding-role-of-ai-agents-in-enterprise-workflows/)（2026）[B，轉述，⚠️ 數字未在微軟原文核對]

### 3.2 Salesforce Agentforce

**採用數據（公司財報，[A/B]：財報數字可信，但 ARR 口徑由公司定義）**：

| 時間 | Agentforce ARR | 交易／客戶 | 來源 |
|---|---|---|---|
| FY26 Q1（2025-05） | 約 1 億美元 | 4,000 家付費客戶 | [No Jitter](https://www.nojitter.com/ai-automation/salesforce-highlights-agentforce-momentum) [C 轉述] |
| FY26 Q3（2025-12-03） | 破 5 億美元，年增 330%；Agentforce＋Data 360 ARR 近 14 億 | 上線以來成交 18,500+ 筆，其中 9,500+ 筆付費（季增 50%） | [Salesforce FY26 Q3 earnings](https://www.salesforce.com/news/press-releases/2025/12/03/fy26-q3-earnings/)（2025-12-03）[A] |
| FY27 Q2（2026-07-31 季末） | 破 15 億美元，年增 240%+（**口徑已改：含 Headless 360 與 Slackbot，無法與前期直接比**）；Agentforce＋Data 360 近 39 億（含約 11 億 Informatica） | 未揭露付費交易數；公司改為 milestone-based ARR 揭露 | [CRM Q2 FY27 Quarterly Investor Deck](https://s205.q4cdn.com/626266368/files/doc_financials/2027/q2/CRM-Q2-FY27-Quarterly-Investor-Deck.pdf)（2026-09）[A] |

- 滲透率：約 15 萬客戶中，FY26 Q3 時有付費 Agentforce 交易的約佔 6%。——[SalesforceBen](https://www.salesforceben.com/2026-predictions-mediocre-agentforce-adoption-would-do-wonders-for-salesforce/)（2025-12）[C，分析師估算]
- 對照：FY27 Q2 Salesforce 總營收 113.5 億美元、年增 11%。Agentforce 成長快，但佔比仍小。

**自用成效（Customer Zero）**：
- Benioff 在 podcast 說客服人力從約 9,000 降到約 5,000，客戶互動約一半由 agent 處理；Salesforce 發言人說部署 help.salesforce.com 的 agent 後案件量下降、**不再補缺**支援工程師職位，部分人轉調銷售與客戶成功。——[Salesforce sacrifices 4,000 support jobs on the altar of AI (The Register)](https://www.theregister.com/2025/09/02/salesforce_4000_jobs_ai)（2025-09-02）；[TechRepublic](https://www.techrepublic.com/article/news-salesforce-cuts-4k-jobs/)（2025-09）[C]
- 爭議：沒有正式文件確認「裁員 4,000」，SalesforceBen 稱為「再平衡」；Benioff 宣稱客服成本降 17%，無獨立佐證。——[SalesforceBen](https://www.salesforceben.com/ai-agents-drive-4000-job-cuts-in-salesforce-support-division/)（2025-09）[C]

### 3.3 ServiceNow

- 內部自用：GenAI 工具對員工內部問題的 deflection rate（不需再找真人）達 54%；客戶案件 deflection 用搜尋摘要提升 10%，用 Now Assist 摘要建議再翻倍；客服人員每案省 12–17 分鐘。——[Boosting customer support agent productivity with generative AI (ServiceNow blog)](https://www.servicenow.com/blogs/2024/support-agent-productivity-genai)（2024）[D，廠商自述，2024 數據]
- 財務：2025 Q2 財報電話會議，CFO 說 2025 年光人力就省 1 億美元，「如期實現」。——[ServiceNow projects $100m savings in AI-driven job cuts (Computing)](https://www.computing.co.uk/news/2025/ai/servicenow-100m-savings-ai-job-cuts)（2025-07）[C 轉述財報會議]
- ⚠️ 未驗證：「2025 年內部 AI 產生 5 億美元年化價值、2026 年費用節省倍增至 2 億」僅見於二手分析。

### 3.4 其他大企業部署

- **JPMorgan**：內部 LLM Suite 約 20 萬名員工使用，推出約 8 個月達此規模，正往 agentic 多步驟任務發展。——[JPMorgan Chase AI strategy 2025 (AI News)](https://www.artificialintelligence-news.com/news/jpmorgan-chase-ai-strategy-2025/)（2025）[C]；⚠️「每年 20 億美元」說法分歧（有的指支出、有的指價值），不要引用。
- **Workday Agent System of Record**：把 agent 當員工管理的平台，2025-02 發布；可登記 agent 角色、技能、資料權限，追蹤成本與績效，可開關整個 agent 或個別技能。——[Workday launches a platform to manage all of their AI agents (TechCrunch)](https://techcrunch.com/2025/02/11/workday-launches-a-platform-for-enterprises-to-manage-all-of-their-ai-agents-in-one-place)（2025-02-11）[C]；2026R1 GA 為二手報導。

### 3.5 Agent 怎麼管：權限、身分、績效、出錯責任

| 面向 | 業界做法（有出處） | 白皮書可用的建議 |
|---|---|---|
| **身分** | Microsoft Entra Agent ID（2025-05 Build 發表 preview）：給 Copilot Studio、Azure AI Foundry 的 agent 一個目錄身分；後續加入 ID Governance：access package、**sponsor（負責人）生命週期流程**；agent 註冊移到 Microsoft Agent 365。——[What's new in Agent ID (Microsoft Learn)](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id)（持續更新）[A，官方文件] | 每個 agent 一個獨立身分＋一位人類負責人；不共用員工帳號 |
| **權限** | OWASP 將「Excessive Agency」列為 LLM Top 10（2026 版 LLM03）；Agentic Top 10 的 ASI03 處理 agent 累積超出任務的權限、被委派鏈或跨 agent 提權利用。建議：只給完成任務所需的工具、每個工具獨立權限設定、高影響動作需人類確認、**在模型外部**執行最小權限。——[Indusface 整理](https://www.indusface.com/learning/owasp-top-10-agentic-ai/)、[Aembit](https://aembit.io/blog/the-owasp-top-10-for-llm-applications-2026-what-changed-and-why-it-matters/)（2026）[C 轉述，⚠️ 編號請回查 OWASP 原文] | 最小權限 + 破壞性動作人工確認 + 假設模型會出錯 |
| **績效** | Workday：追蹤每個 agent 的成效與預估成本、預算與預測。Salesforce／ServiceNow 用 deflection rate、每案節省分鐘數、案件量。 | 像管員工一樣訂 KPI，但要同時量**品質**（Klarna 教訓） |
| **出錯責任** | *Moffatt v. Air Canada*（2024 BCCRT 149，2024-02-14）：航空公司辯稱 chatbot 是「為自身行為負責的獨立實體」，仲裁庭稱此主張「remarkable」並駁回：資訊來自靜態網頁或 chatbot 沒有差別，公司要負責。賠償約 650.88 加幣。——[Moffatt v. Air Canada: a misrepresentation by an AI chatbot (Barry Sookman)](https://barrysookman.com/2024/02/16/moffatt-v-air-canada-a-misrepresentation-by-an-ai-chatbot/)（2024-02-16）[A 判決，經律師評論轉述]；注意這是 BC 省小額仲裁庭，不是上級法院判例 | **Agent 的錯就是公司的錯**，不能推給 agent 或廠商；對外 agent 的輸出要有可回查依據 |
| **治理失敗風險** | Gartner（2025-06）預測 2027 年底前超過 40% agentic AI 專案會被取消，原因：成本攀升、商業價值不明、風險控管不足；並指出「agent washing」：數千家 agentic 廠商中只有約 130 家是真的。——[Gartner: 40% of agentic AI projects could be canceled by 2027 (Outlook Business)](https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner)（2025-06）[B，預測非實測] | 先界定價值與風險控制，再擴大規模 |

---

## 4. 大企業 vs 新創 vs 中小企業

### 4.1 誰在用：規模落差是事實

- **美國 Census BTOS**：2025-12 至 2026-05 全體企業 AI 使用率約 17–20%；250 人以上企業 37%，4 人以下企業不到 20%。注意 2025-11 起題目從「用於生產商品或服務」改為「用於任何業務功能」，序列有斷點。——[Large Firms With at Least 20 Employees Biggest AI Users (U.S. Census Bureau)](https://census.gov/library/stories/2026/05/ai-use-businesses.html)（2026-05）[A]
- WeWork 用同一資料分析：2026-07 美國企業 AI 使用率 21.7%（2026-01 為 17.7%）。——[The new AI divide (WeWork)](https://www.wework.com/ideas/research-insights/the-new-ai-divide)（2026）[C，二手分析]
- **OECD**：大企業 AI 使用率（40%）是小企業（11.9%）的三倍以上；營建、餐旅、運輸低於 10%。另一份 2026-01 更新：2025 年 OECD 整體 20.2%，大企業 52.0% vs 小企業 17.4%（不同資料集，不要混用）。——[AI adoption by small and medium-sized enterprises (OECD, for G7)](https://assets.geteasy.ai/internal/files/oecd-report-ai-adoption-by-small-and-medium-sized-enterprises.pdf)（2025-12）[A，經第三方託管 PDF]
- OECD 重要警告：控制既有數位能力、技能與互補投資後，AI 採用者的生產力溢價**大幅縮小**。也就是說，「用 AI 的公司比較強」有一部分是「本來就比較強的公司才用 AI」。——同上 [A]

### 4.2 勞動市場：入門職位先受衝擊

- Stanford Digital Economy Lab（Brynjolfsson、Chandar、Chen）最新版以 ADP 薪資資料分析：截至 2026-06，AI 曝險最高職業中 22–25 歲員工的就業，較其若跟上低曝險同齡者原應達到的水準低 **19%**；資深員工沒有相同缺口。這是描述性差距，不是因果估計。——[Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI (Stanford)](https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial)（2026-08，資料至 2026-06）[A]
- 對企業的意涵：「AI 做不到才加人」政策最先擋掉的是入門職位，這會影響企業 5–10 年後的中階人才池。（推論，非研究結論）

### 4.3 三類企業比較表

| | 大企業 | 新創 | 中小企業 |
|---|---|---|---|
| **優勢** | 資料、通路、客戶信任、資本；可當自家產品的 Customer Zero（Salesforce、ServiceNow）；採用率最高（Census 37%、OECD 40–52%） | 從零以 AI 為前提設計流程與人力，人均營收可達百萬美元級（Lovable、Gamma、Midjourney） | 決策鏈短、老闆一句話就能改流程；現成 SaaS 已內建 agent，進入門檻下降 |
| **陷阱** | ① 只做「AI-enabled」：95% 無可量測報酬（MIT NANDA）、60% 屬落後者（BCG）② 宣言溝通失當引發反彈（Duolingo）③ 以 agent 取代人卻犧牲品質（Klarna）④ agent 權限蔓延與 shadow AI（Entra Agent ID 推出背景） | ① ARR 不等於獲利，推論成本壓毛利 ② 營收高度集中在少數熱門品類（AI coding），模型商可能直接競爭 ③ 「agent washing」，Gartner 估只有約 130 家是真的 | ① 採用率只有大企業的 1/3–1/2（OECD、Census）② 缺資料品質、技能、主管時間，不只是缺錢（OECD）③ 卡在 pilot，無法嵌入核心營運（G7 SME Blueprint） |
| **可行路徑（有來源支撐）** | 以 workflow 為單位重設（McKinsey 高績效者 3 倍）；「控制增量」型政策（Shopify：加人前證明 AI 做不到）優於「削減存量」；建立 agent 身分＋負責人＋最小權限治理 | 維持小團隊、讓產品本身承載 AI 槓桿；早期證明獲利（Gamma） | 選一個後勤流程先做（MIT NANDA 指出後勤自動化報酬常優於投入最多的銷售行銷）；用平台內建 agent 而非自建；先補資料與技能（OECD 四大 enabler：連網、資料與算力、技能、資金） |

- G7 SME AI Adoption Blueprint：許多中小企業有在試 AI 工具，但難以嵌入核心營運，生產力效益沒有實現。——[SME AI Adoption Blueprint (G7 2025 Canada)](https://g7g20-documents.org/fileadmin/G7G20_documents/2025/G7/Canada/Ministerial%20Meetings/IDT%20Ministers/3%20Miscellaneous/SME%20AI%20Adoption%20Blueprint_20251209.pdf)（2025-12-09）[A]
- MIT NANDA：研究摘要寫約 50% 預算流向銷售與行銷，內文另以假設性預算分配寫約 70%；後勤自動化常被受訪者認為回報更好。數字為小樣本自述，僅供看方向。——[MIT NANDA, The GenAI Divide](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)（2025）[B]

---

## 5. 未驗證與待查清單

- ⚠️ Box「AI-first 備忘錄」原文：未找到。
- ⚠️ Fiverr 2025-04「AI is coming for your jobs」信原文出處：未取得。
- ⚠️ Cursor 員工數（150／182／300）、2026 年 ARR 30 億、SpaceX 收購：僅二手來源。
- ⚠️ Shopify 10-K 員工數：轉述，未開 SEC 原件。
- ⚠️ Duolingo 取消績效考核 AI 項目：僅社群轉貼。
- ⚠️ Microsoft WTI 2026 細部數字：未讀微軟原文。
- ⚠️ OWASP 2026 編號（LLM03、ASI03）：轉述。
- ⚠️ 傳統 SaaS 人均營收基準：本次未查到權威數字。
- ⚠️ 台灣企業的對應數據：本次未涵蓋（建議另查經濟部中小及新創企業署、資策會 MIC）。

---

## 對企業白皮書最有用的 10 個洞見

1. **有報酬的公司重新設計流程，不是買工具**：AI 高績效者根本性重設 workflow 的機率是其他人的約 3 倍。——[McKinsey, The state of AI in 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025)（2025）
2. **多數企業還沒拿到 AI 報酬**：BCG 只有 5% 公司「future-built」、60% 幾乎無實質效益；MIT NANDA 稱 95% 組織沒有可量測報酬（樣本小，屬方向性）。——[BCG](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings)（2025-09-30）；[Virtualization Review](https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx)（2025-08-19）
3. **「人機比例」沒有標準答案**：Microsoft 提出 human-agent ratio 作為新指標，但明說依任務而定、沒有給數字。——[Microsoft WorkLab, WTI 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)（2025-04-23）
4. **控制增量比削減存量更可行**：Shopify「加人前先證明 AI 做不到」讓員工數透過自然流失降約 6%、反彈低；Duolingo 把 AI 跟取代約聘綁在一起，引發強烈反彈並兩度澄清。——[TechCrunch](https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/)（2025-04-07）；[Fortune](https://fortune.com/2025/08/18/duolingo-ceo-admits-controversial-ai-memo-did-not-give-enough-context-insists-company-never-laid-off-full-time-employees)（2025-08-18）
5. **只量成本不量品質會翻車**：Klarna AI 客服做了 700 人的量，但 CEO 承認品質較低，改回人機雙軌。——[Tech.co](https://tech.co/news/klarna-reverses-ai-overhaul)（2025-05）
6. **Agent 出錯，責任在公司**：Air Canada 主張 chatbot 是獨立實體，被仲裁庭駁回。——[Moffatt v. Air Canada (Barry Sookman)](https://barrysookman.com/2024/02/16/moffatt-v-air-canada-a-misrepresentation-by-an-ai-chatbot/)（2024-02-16）
7. **數位員工要有身分、負責人、最小權限**：Microsoft Entra Agent ID 為每個 agent 建身分並指定 sponsor；Workday 以「像管員工一樣」登記角色、權限、成本與績效。——[Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id)；[TechCrunch](https://techcrunch.com/2025/02/11/workday-launches-a-platform-for-enterprises-to-manage-all-of-their-ai-agents-in-one-place)（2025-02-11）
8. **企業 agent 平台正在起量**：Salesforce 財報揭露 Agentforce 上線以來成交超過 18,500 筆，其中付費交易超過 9,500 筆；公司沒有公布客戶滲透率。——[Salesforce FY26 Q3](https://www.salesforce.com/news/press-releases/2025/12/03/fy26-q3-earnings/)（2025-12-03）
9. **入門職位最先受衝擊**：最新版 Stanford 研究估計，AI 高曝險職業中 22–25 歲員工就業較「跟上低曝險同齡者」的反事實水準低 19%；這是描述性差距，不是因果估計。——[Stanford Digital Economy Lab](https://siepr.stanford.edu/publications/working-paper/canaries-coal-mine-six-facts-about-recent-employment-effects-artificial)（2026-08，資料至 2026-06）
10. **中小企業的瓶頸是資料、技能和主管時間，不只是錢**：小企業 AI 採用率只有大企業約三分之一；控制既有數位能力後，AI 生產力溢價大幅縮小，所以要先補基礎。——[OECD, AI adoption by SMEs](https://assets.geteasy.ai/internal/files/oecd-report-ai-adoption-by-small-and-medium-sized-enterprises.pdf)（2025-12）；[U.S. Census Bureau](https://census.gov/library/stories/2026/05/ai-use-businesses.html)（2026-05）
