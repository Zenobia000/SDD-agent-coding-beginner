# 05｜從業務端到幕僚單位：企業各部門與常用系統的 AI 賦能 vs AI 原生重建

> 研究日期：2026-10-20｜研究方式：WebSearch + WebFetch（約 50 次搜尋，**本 session 搜尋額度在後段用盡**，因此 P&G 實驗、Gartner Hype Cycle、McKinsey State of AI 原文數字等幾項未能二次核對，已標 ⚠️）。
>
> **可信度標記**（每條事實都標）：
> - 【研究】同儕審查論文、RCT、學術工作論文
> - 【顧問】McKinsey / BCG / MIT CISR 等顧問或研究機構調查（自填問卷，有樣本偏差）
> - 【分析】Gartner 等分析機構預測或調查
> - 【廠商】**廠商自己公布的數字，未經獨立稽核**——白皮書引用時務必加註
> - 【個案】媒體報導、公司公開發言、法院判決
> - ⚠️ 未驗證：只有二手來源，或數字在不同來源間矛盾

---

## 0. 一頁結論

1. **有硬證據的效益集中在「高量、規則清楚、有標準答案」的工作**：客服（RCT：每小時解決案件 +14–15%）、IT 服務台、HR 問答、應付帳款、資安分析。業務與行銷是預算最多的地方，但有效益數據的最少。
2. **最被高估的是「拿掉人」**：Klarna、澳洲聯邦銀行（CBA）都在 AI 取代客服之後又把人找回來；Gartner 預測 50% 原本打算靠 AI 縮編客服的組織會在 2027 年前放棄。
3. **大廠的做法全是「賦能」路線**：在既有 system of record（ERP/CRM/HCM/ITSM）上掛 copilot 與 agent，靠資料與權限護城河。「AI 原生重建」目前主要出現在新創（AI-native ERP、AI 客服），以及少數公司自建（Klarna）。
4. **組織面的分水嶺是「流程重設計」而不是「工具採購」**：McKinsey 的 AI 高績效者（約 6%）重設計流程的機率是其他人的近 3 倍；MIT CISR 的資料顯示停在 Stage 1–2（實驗、試點）的企業財務表現低於產業平均。
5. **不能交給 AI 的決策**有共同特徵：對外具法律效力的承諾（價格、退款、合約）、影響個人權益的判定（錄取、信用、懲處）、以及無法回溯驗證的判斷。法院已經判企業要為 chatbot 說的話負責（Air Canada）。

---

## 1. 部門別

### 1.1 客服（Customer Service）—— 證據最強的部門

**落地且有數據**
- 【研究】Brynjolfsson、Li、Raymond 對 5,179 名客服人員的研究：導入生成式 AI 助理後，每小時解決問題數平均 +14%，新手與低技能者 +34%，資深者幾乎無影響；機制是「把高手的做法擴散給新人」。正式版刊於 QJE 2025（140(2):889–942），正式版摘要寫平均 +15%、5,172 人。→ [Generative AI at Work (arXiv 2304.11771)](https://arxiv.org/abs/2304.11771)（2023/2024）；[BLS Monthly Labor Review 摘要](https://www.bls.gov/opub/mlr/2024/beyond-bls/ai-improved-the-productivity-of-a-fortune-500-software-company.htm)（2024）
- 【廠商/個案】Klarna AI 助理上線首月處理 230 萬次對話、占客服聊天 2/3，相當於 700 名全職人力；平均解決時間從 11 分鐘降到 2 分鐘以內；重複詢問 -25%；預估 2024 年貢獻 4,000 萬美元獲利改善。→ [Klarna press release](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)（2024-02-27）
- 【個案】Klarna 2025 Q3 法說會：AI 助理做了超過 853 名全職人力的工作，累計節省 6,000 萬美元。→ [CX Dive](https://www.customerexperiencedive.com/news/klarna-says-ai-agent-work-853-employees/)（2025）
- 【廠商/個案】Salesforce 以自己的 help 網站當「customer zero」，Benioff 表示支援人力從約 9,000 降到約 5,000、處理約 150 萬次對話、CSAT 與真人相近。→ [Salesforce Ben](https://www.salesforceben.com/ai-agents-drive-4000-job-cuts-in-salesforce-support-division/)（2025-09）；⚠️ 解決率等細節沒有一手資料
- 【廠商】Intercom Fin：據稱解決率從上線時約 25% 升到 65–70%；以每次「outcome」0.99 美元計價，但客戶 24 小時沒回應也算「assumed resolution」。→ [Intercom pricing](https://www.intercom.com/learning-center/intercom-pricing)；⚠️ 解決率數字來自二手報導 [Enterprise DNA](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-08-02-intercom-s-fin-ai-agent-is-nearing-100m-arr-roughly-half-of)（2026-08）

**失敗或被高估**
- 【個案】Klarna CEO 2025-05 承認自動化「走太遠」、服務品質下滑，重新招募真人客服（Uber 式彈性人力）；Forrester 分析師評為「over-pivoted」。→ [Entrepreneur](https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396)；[Maginative](https://www.maginative.com/article/klarna-dials-back-its-ai-customer-service-strategy-now-its-hiring-humans-again/)（2025-05）
- 【個案】澳洲聯邦銀行（CBA）以 voice bot 為由裁撤 45 名客服，工會指出來電量其實上升、還要主管加班接電話；CBA 2025-08-21 公開道歉並撤回裁員。→ [Bloomberg](https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots)；[Information Age (ACS)](https://ia.acs.org.au/article/2025/cba-reverses-ai-driven-job-cuts--admits--error-.html)（2025-08）
- 【分析】Gartner 預測：到 2027 年，50% 原本計畫大幅縮減客服人力的組織會放棄這個計畫；2025-03 對 163 位主管的調查中 95% 打算保留真人客服。→ [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai)（2025-06-10）
- 【分析】⚠️ Gartner 後續調查（321 位主管，2025 Q4）：只有 20% 因 AI 減少人力，55% 人數持平但處理更大量。→ 二手轉述 [The Register](https://www.theregister.com/2025/06/11/gartner_ai_customer_service/) 等；原始新聞稿未直接核對

**不能交給 AI 的決策**
- 【個案／法院】**對外承諾的政策解釋**：Moffatt v. Air Canada（2024 BCCRT 149）——chatbot 杜撰喪親票價退款政策，法庭駁回「chatbot 是獨立法律實體」的抗辯，判航空公司負責。→ [American Bar Association Business Law Today](https://businesslawtoday.org/topic/ethics/page/19)；[McCarthy/Sookman 評析](https://barrysookman.com/2024/02/16/moffatt-v-air-canada-a-misrepresentation-by-an-ai-chatbot/)（2024-02-14）
- 例外處理、退款與補償金額、客訴升級、情緒激烈或弱勢客戶 → 保留真人通道（Klarna 的修正正是「永遠能找到真人」）。

### 1.2 業務（Sales）

**落地且有數據**
- 【廠商】Lumen Technologies：Copilot for Sales 讓業務平均每週省約 4 小時，Lumen 估值 5,000 萬美元／年（不同 Microsoft 頁面分別寫成「節省」「預計節省」「營收價值」，口徑不一）。→ [Microsoft Source](https://news.microsoft.com/source/features/digital-transformation/the-only-way-how-copilot-is-helping-propel-an-evolution-at-lumen-technologies/)（2024）
- 【個案】Morgan Stanley：Debrief（會議紀錄與跟進信草稿，寫回 Salesforce）與知識助理，公司估 98% 理財顧問團隊在用。→ [The Daily Upside](https://www.thedailyupside.com/advisor/practice-management/ai-assistants-are-taking-over-wall-street/)（2024）
- 【廠商】Microsoft Dynamics 365 Sales Qualification Agent：自動研究名單、寄信跟進、只把有購買意圖的 lead 交給業務；2025-10 起 GA。**找不到具名客戶成效數字**。→ [Microsoft 365 Message Center MC1159615](https://mc.merill.net/message/MC1159615)（2025-10）

**失敗或被高估**
- 【個案】AI SDR 新創 11x：TechCrunch 報導其官網列出非客戶的 logo（ZoomInfo 試用後稱表現顯著不如自家 SDR）、ARR 以年約計但客戶可在 90 天內解約；員工稱早期客群流失 70–80%（公司稱目前留存 79%）；創辦人 2025-05 卸任 CEO。→ [TechCrunch](https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have)（2025-03-24）
- 【顧問】MIT NANDA 指出超過一半的生成式 AI 預算流向業務與行銷工具，但 ROI 最大的其實是後勤自動化。→ [Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)（2025-08-18）

**不能交給 AI 的決策**：折扣與價格例外核准、合約條款讓步、大客戶關係取捨、業績預測的最終承諾（AI 可以給 forecast，但 commit 數字要有人簽）。

### 1.3 行銷（Marketing）

**落地且有數據**
- 【個案】Mondelez 投資逾 4,000 萬美元，與 Publicis、Accenture 打造生成式內容工具，**目標**把行銷內容製作成本降 30–50%；目前只用在社群素材（Chips Ahoy、Milka），2026 年假期才預計做電視廣告。**這是目標不是實績**。→ [Digiday](https://digiday.com/marketing/mondelez-takes-ai-in-house-to-try-and-curb-marketing-costs/)（2025-10）
- 【研究】⚠️ P&G 與 Harvard 等的「Cybernetic Teammate」實驗（776 名員工）：用 AI 的個人產出品質可比沒 AI 的雙人團隊。本次搜尋額度用盡未能核對原文，引用前需查 SSRN 原稿。

**失敗或被高估**
- 大量生成素材 ≠ 轉換提升；Mondelez 主管被問到過往成效時沒有提供具體節省數字（同上 Digiday）。
- 品牌風險：AI 生成廣告的負面輿論 ⚠️（本次未查證具體個案，不列）。

**不能交給 AI 的決策**：品牌定位與調性、對外發布的最終審稿（法規、肖像權、著作權）、危機溝通。

### 1.4 財務會計（Finance & Accounting）

**落地且有數據**
- 【分析】Gartner 2025 財務 AI 調查（183 位 CFO／財務主管，2025-05–06）：59% 財務部門使用 AI，與 2024 年的 58% 幾乎持平（2023 年為 37%）——**採用率進入高原期**。→ [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025)（2025-11-18）
- 【顧問/產業調查】⚠️ 應付帳款（AP）基準：Ardent Partners 2025 稱最佳實務每張發票處理成本約 2.78 美元、touchless 比例約 50%，一般企業約 25%；各來源數字差距大（2.78–22.75 美元），且多為二手轉述。→ [Parseur 彙整](https://parseur.com/blog/ai-invoice-processing-benchmarks)（2025）
- 【廠商】Ramp：其 agent 在 90 天內標記超過 100 萬美元的詐欺發票。→ [Computerworld](https://www.computerworld.com/article/4079701/new-ai-scam-fake-expense-receipts.html)（2025）

**失敗或被高估：AI 讓「費用報銷」的風險上升**
- 【廠商數據/媒體】AppZen：2025-09 被抓到的假收據中約 14% 是 AI 生成，前一年為 0；PYMNTS 引述 AppZen 至 2026-05 已達 70.8%（1,471 張）。AI 假收據平均約 100 美元，刻意低於審核門檻。→ [TechRadar](https://www.techradar.com/pro/security/workers-are-scamming-their-employers-using-ai-generated-fake-expense-receipts)（2025）；[PYMNTS](https://www.pymnts.com/cybersecurity/2025/phony-ai-created-receipts-become-real-problem-for-businesses/)（2025/2026）
- 【廠商調查】⚠️ Emburse 調查稱 4 成美國員工用過 AI 生成假收據（同上 TechRadar 轉述，樣本未見）

**不能交給 AI 的決策**：關帳與財報簽核、會計判斷（收入認列、減損、估計）、付款放行與銀行帳戶變更（BEC 詐騙熱點）、稅務立場。

### 1.5 人資（HR）

**落地且有數據**
- 【廠商】IBM AskHR（watsonx Orchestrate）：常見問題 94% containment、過去四年 HR 營運成本 -40%、自 2016 年起工單 -75%、每年 210 萬次對話、80+ 項 HR 任務；採「AI 處理例行、真人處理複雜」雙層模型。→ [IBM case study](https://www.ibm.com/case-studies/ibm-askhr)（2025）
- 【個案】Workday 2025-10-01 完成收購 Paradox（對話式招募 agent，主打第一線大量招募的排面試與 24/7 回應）。**沒有公開的錄取時間或成效數字**。→ [Workday newsroom](https://newsroom.workday.com/2025-10-01-Workday-Completes-Acquisition-of-Paradox)（2025-10-01）

**失敗或被高估**
- 【個案】Amazon 2014 年起開發 AI 履歷評分工具，因以 10 年男性為主的履歷訓練而歧視女性，最終解散團隊。→ [Reuters via CNBC](https://www.cnbc.com/2018/10/10/amazon-scraps-a-secret-ai-recruiting-tool-that-showed-bias-against-women.html)（2018-10-10）
- 【法院】Mobley v. Workday：法院 2025 年 5 月有條件認證 40 歲以上求職者的 ADEA 集體訴訟；Workday 自己的文件稱期間約 11 億份申請在其系統中被拒。法院接受「AI 供應商可作為雇主的 agent 負責」的理論進入實體審理。→ [Proskauer](https://www.proskauer.com/blog/ai-bias-lawsuit-against-workday-reaches-next-stage-as-court-grants-conditional-certification-of-adea-claim)（2025-06）；[Davis Wright Tremaine](https://www.dwt.com/blogs/employment-labor-and-benefits/2025/05/ai-hiring-age-discrimination-federal-court-workday)（2025-05）
- 【法規】EU AI Act 將招募、升遷、解僱、績效評估等列為 Annex III 高風險；Digital Omnibus 把適用日從 2026-08-02 延到 2027-12-02，但人為監督、偏誤監測等要求不變。→ [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)（2026-05）；⚠️ 官方公報刊登狀態未核對

**不能交給 AI 的決策**：錄取／淘汰、績效評等、懲處與資遣、薪酬調整、性騷與申訴調查。AI 可以做排程、FAQ、文件草稿與資料彙整。

### 1.6 採購（Procurement）

**落地且有數據**
- 【個案/廠商】Walmart × Pactum 自主議價 chatbot：加拿大試點 89 家供應商，64% 達成協議（目標 20%），平均節省 1.5%、平均 11 天完成；擴大到美國、智利、南非後，68% 成交、平均節省 3%；83% 成交供應商給正面評價。範圍限於非貨架商品（購物車、店內耗材）。→ [Harvard PON](https://www.pon.harvard.edu/daily/negotiation-skills-daily/chatbot-negotiations-what-can-ai-do-for-you/)；[ASCM](https://www.ascm.org/ascm-insights/scm-now-impact/ai-powers-procurement-at-walmart)（2023）
  - 註：網路常見「64% 節省」是誤傳，64% 是**成交率**。
- 【分析】Gartner 2024 調查 258 人：72% 採購主管把 GenAI 列為優先；Gartner 點名 agentic reasoning、多模態、AI agents 三項將重塑採購。→ [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2024-11-20-gartner-identifies-three-key-advancements-in-generative-ai-that-will-shape-the-future-of-procurement)（2024-11-20）

**失敗或被高估**：⚠️ 本次未找到採購 AI 失敗的具名公開個案。風險面：供應商主檔與銀行帳號變更詐騙、假發票（見 1.4 Ramp）。

**不能交給 AI 的決策**：策略供應商選擇與汰換、單一來源採購、超過授權額度的合約簽署、供應商違規處分。尾端支出（tail spend）的標準品議價是目前唯一有公開成效的「交給 AI 談」場景。

### 1.7 法務（Legal）

**落地且有數據**
- ⚠️ 本次搜尋額度用盡，未能核對 Harvey、A&O Shearman 等法律 AI 的使用數字。

**失敗或被高估**
- 【研究】Stanford RegLab/HAI：Lexis+ AI 與 Thomson Reuters 的 AI 研究工具在 200+ 個法律問題上幻覺率約 17%–33%（低於 GPT-4，但遠非零）；TR 抗議測試用錯產品，研究團隊後續補測。→ [Stanford HAI](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries)（2024-05）；[LawNext](https://www.lawnext.com/2024/05/stanford-will-augment-its-study-finding-that-ai-legal-research-tools-hallucinate-in-17-of-queries-as-some-raise-questions-about-the-results/)（2024-05）
- 【個案】Damien Charlotin 的資料庫到 2025 年底已收錄 712 件法院處理 AI 幻覺內容的判決，約 90% 出現在 2025 年，速度從每天 2–3 件升到 5–6 件。→ [Bloomberg Law](https://news.bloomberglaw.com/legal-ops-and-tech/ai-faked-cases-become-core-issue-irritating-overworked-judges)（2025-12-29）

**不能交給 AI 的決策**：對外法律意見、訴訟策略、和解決定、合約最終條款。所有引用必須人工逐條查證原始判例/條文。

### 1.8 IT／資安

**落地且有數據**
- 【廠商】ServiceNow「Now on Now」：「Report an Issue」表單 54% 轉向自助、AI 搜尋讓約 20% 案件免開單；ServiceNow 自家頁面稱 IT help desk 每案省 45 分鐘、員工每年省 21,000 小時。→ [ServiceNow customers page](https://www.servicenow.com/workflow/ai/leading-ai-revolution-customers.html)；⚠️ 54%/20% 來自二手 [Kellton](https://www.kellton.com/kellton-tech-blog/blogs/unlocking-it-efficiency-how-now-assist-uses-genai-to-cut-ticket-volume)
- 【廠商 RCT】Microsoft Security Copilot：有經驗的分析師快 22%、準確度 +7%（147 人，模擬環境，微軟首席經濟學家辦公室執行）。→ [Microsoft infographic](https://www.microsoft.com/content/dam/microsoft/final/en-us/microsoft-brand/documents/EconStudy-Speed-accuracy-and-sentiment-Infographic-Final.pdf)（2024）
- 【研究預印本】釣魚郵件分類 agent：每分析師分鐘真陽性最多 6.5 倍、判定準確度 +77%。→ [arXiv 2511.13860](https://www.arxiv.org/abs/2511.13860)（2025-11）
- 【個案】廣達：導入 AI 輔助軟體開發約兩年，工程師開發效率約 +33%，且使用率持續上升。→ [iThome](https://www.ithome.com.tw/news/171350)（2025-09）

**失敗或被高估**
- 【研究 RCT】METR：16 位資深開源開發者、246 個真實任務，用 AI（Cursor + Claude 3.5/3.7）反而**慢 19%**，但他們自認快了 20%。→ [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)（2025-07-10）
  - 白皮書寫法：**自評生產力不可信，必須量測**。

**不能交給 AI 的決策**：正式環境的變更核准、權限授予、資安事件的對外通報與隔離決策、資料外洩判定。

### 1.9 營運／供應鏈

**落地且有數據**
- 【顧問】⚠️ McKinsey 常被引用「AI 需求預測讓預測誤差降 20–50%」，但本次未找到 McKinsey 原文，「缺貨損失 -65%」更只有二手來源。→ 二手彙整 [HubSpot](https://blog.hubspot.com/sales/ai-demand-forecasting)
- 【分析】Gartner 調查 509 位供應鏈主管（2025-07–10）：55% 預期 agentic AI 會減少基層招募，51% 預期整體人力下降，86% 認為需要新的人才培養流程。→ [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2026-02-25-gartner-survey-shows-55-percent-of-supply-chain-leaders-expect-agentic-ai-to-reduce-entry-level-hiring-needs)（2026-02-25）
- 【分析】Gartner 預測：2030 年 50% 跨功能 SCM 方案將使用能自主執行決策的 agent。→ [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2025-05-21-gartner-predicts-half-of-supply-chain-management-solutions-will-include-agentic-ai-capabilities-by-2030)（2025-05-21）
- 【個案】台積電魏哲家：每提升 1% 生產力約可創造 10 億美元（**估算**，非實績）；2026-09 稱晶圓廠導入大量 AI 輔助、在既有產能下提高產出，但也指出 agent 帶來的智財保護風險，且 AI 在 A14 等下一代製程探索的作用「相當有限」。→ [TechNews](https://technews.tw/2026/01/15/cc-wei-see-ai-bubble-at-2025-q4-financial-report/)（2026-01-15）；[TechNews 財經](https://finance.technews.tw/2026/09/21/ai-still-has-limitations-in-the-development-of-next-generation-advanced-manufacturing-processes/)（2026-09-21）
- 【個案】廣達：台灣廠、美國廠以 NVIDIA Omniverse 模擬自動化產線；⚠️ 無量化數字、報導日期未標。→ [鉅亨網](https://m.cnyes.com/news/id/5587147)

**不能交給 AI 的決策**：停線、召回、安全事件處置、跨廠產能分配的取捨、對客戶的交期承諾。

---

## 2. 系統別：AI 賦能 vs AI 原生重建

### 2.1 定義（本研究採用）

| | AI 賦能（AI-augmented） | AI 原生重建（AI-native） |
|---|---|---|
| 資料模型 | 沿用既有 system of record 的表結構 | 以 AI 可讀為前提重建（事件流、知識圖譜、語意層） |
| 互動 | 表單 + 側邊 copilot | 對話／意圖為主，表單退居稽核介面 |
| 工作分配 | 人做、AI 建議 | AI 做、人審例外（management by exception） |
| 計價 | 加購座位或 credits | 依結果（per resolution / outcome） |
| 代表 | SAP Joule、Agentforce、Dynamics Copilot、Workday、ServiceNow Now Assist | Rillet / Campfire（ERP）、Intercom Fin / Sierra 類（客服）、Klarna 自建 |
| 主要風險 | 效益分散、難量測（McKinsey 的「gen AI paradox」） | 稽核、法遵、會計師接受度；遷移成本 |

### 2.2 各系統

| 系統 | AI 賦能（目前主流） | AI 原生重建的樣子 | 公開證據與限制 |
|---|---|---|---|
| **ERP** | SAP Joule、Joule Agents；Dynamics 365 Copilot | Rillet、Campfire：以 AI agent 做自動入帳、對帳、營收認列、合併報表 | 【廠商】SAP 稱內部 11 萬員工在財務/HR/採購約 +20% 生產力，Bosch Digital 開發 +20%（[SAP News](https://news.sap.com/2026/07/sap-business-ai-release-highlights-q2-2026/)，2026-07）；顧問強調 **clean core** 是前提（[EPI-USE](https://www.epiuse.com/aws-services/blogs/sap-sapphire-highlights-gen-ai-success-relies-on-clean-core-and-customer-adoption)）。【個案】Rillet Series C 1 億美元、估值 10 億、600+ 客戶，宣稱替換 NetSuite、SAP 等（[The Next Web](https://thenextweb.com/news/rillet-100m-series-c-1bn-accounting-ai)，2026-08）；Campfire A 輪 3,500 萬（[Crunchbase News](https://news.crunchbase.com/venture/ai-fintech-campfire-raise-seriesa-accel-ribbit/)）。限制：AI-native ERP 目前集中在中型 SaaS 公司，**稽核師接受度**是關卡 |
| **CRM** | Salesforce Agentforce、Dynamics 365 Sales agents | Klarna 2024 宣布停用 Salesforce，改用自建資料層（含 Neo4j 圖資料庫）+ AI | 【個案】Agentforce FY26 Q3 ARR 約 5.4 億美元（+330%），累計 18,500 筆交易中 9,500 筆付費（[Nasdaq/Zacks](https://www.nasdaq.com/articles/crms-agentforce-arr-jumps-330-y-y-it-next-growth-engine)）；評論指出許多是既有客戶加購或試點。Klarna 案被 Bersin 等質疑能否取代數十年的流程功能（[TipRanks](https://www.tipranks.com/news/private-companies/klarnas-strategic-shift-embracing-in-house-ai-over-salesforce)；[Salesforce Ben](https://www.salesforceben.com/klarna-salesforce-workday-partnership-called-off-amidst-major-gen-ai-overhaul/)，2024-09） |
| **HRM／差勤** | Workday agents（Payroll、Policy、Contracts）、「Agent System of Record」把 agent 當員工一樣管理；IBM AskHR | 員工直接對話請假、查餘額、改班，表單只做稽核 | 【廠商】IBM AskHR 94% containment（見 1.5）。限制：招募篩選屬高風險（Mobley 案、EU AI Act），**差勤請假是低風險高頻、最適合起手** |
| **費用報銷／請款** | SAP Concur、Ramp、Brex 的收據辨識與政策檢核 | 卡片交易即時對帳、AI 自動稽核 100% 單據而非抽樣 | 新風險：AI 假收據占被抓假單 14%→70.8%（見 1.4）。**AI 稽核成為必要，而非選配** |
| **報價（CPQ）** | Salesforce 把 CPQ 重建為 Revenue Cloud（API-first，讓 agent 跨報價流程運作），Agentforce 可在 opportunity / quote 上直接產生報價 | 自然語言需求 → 自動配置 + 定價 + 合約草稿 | 【廠商】只有產品發表（[IT Brief](https://itbrief.com.au/story/salesforce-unveils-agentforce-to-speed-up-quoting-for-sellers)，2025）；⚠️ **沒有找到具名客戶成效數字**。價格與折扣例外不能交給 agent |
| **客服工單** | ServiceNow Now Assist、Zendesk、Salesforce Service Cloud | Intercom Fin、Sierra 等以「解決」計價的 AI-first 客服 | 證據最多（見 1.1）。AI-native 的計價定義（何謂「解決」）需寫進合約 |
| **庫存** | 既有 ERP/WMS 加需求預測模型、補貨建議 | 自主補貨 agent | Gartner 預測 2030 年 50% SCM 方案含自主 agent；⚠️ 預測誤差 -20–50% 缺原始出處 |
| **採購比價** | SAP Ariba、Coupa 加 GenAI 寫 RFP、比價摘要；Dynamics Supplier Communications Agent 追蹤交期 | 自主議價 agent（Pactum） | Walmart 成交率 64–68%、節省 1.5–3%（見 1.6）；只用在標準品尾端支出 |
| **BI／儀表板** | Power BI Copilot、Tableau、Looker 的自然語言查詢 | 語意層 + agent 主動推送異常與解釋 | 【研究】Spider 2.0：學術基準（Spider 1.0 91.2%、BIRD 73%）到真實企業任務驟降到約 17–21%，主因是上千欄位的 schema、業務定義不在資料表裡（[arXiv 2411.07763](https://arxiv.org/abs/2411.07763v2)，2024/2025）。⚠️ dbt「建語意層後準確度 64.5%→98%+」為廠商數字。**結論：沒有語意層（指標定義），NL-to-SQL 不能給主管直接用** |

### 2.3 五大廠做法比較

| 廠商 | 主打 | 公開成效 | 限制 |
|---|---|---|---|
| **SAP Joule** | 跨 S/4HANA、SuccessFactors、Ariba 的 copilot + agents；Joule Studio 自建 agent | 【廠商】內部 +20%；宣稱例行任務最多快 80%（行銷語言）（[SAP Joule](https://www.sap.com/sea/products/artificial-intelligence/ai-assistant.html)） | 需 clean core；跨平台 Agent Gateway 尚未 GA（[Forkast](https://forkast.news/?p=131812)）；Joule Studio GA 約 2026 初 |
| **Salesforce Agentforce** | CRM + Data Cloud 上的自主 agent，消費型計價（Flex Credits） | 【廠商/個案】自家客服降 4,000 人（見 1.1）；ARR 5.4 億 | 付費交易比例約一半；評論質疑多為試點與加購 |
| **Microsoft Dynamics 365 Copilot** | Sales Qualification、Supplier Communications 等現成 agent，用 Copilot Studio 擴充 | ⚠️ 未找到具名客戶量化成效；Lumen 是 M365 Copilot for Sales 案例 | agent 名稱與範圍改版頻繁 |
| **Workday** | HCM/財務 agents；Agent System of Record；收購 HiredScore、Paradox | ⚠️ 未找到量化成效 | 招募 AI 的訴訟風險（Mobley 案） |
| **ServiceNow** | Now Assist + AI Agent Orchestrator / Studio，定位為跨 IT/HR/CS 的「AI 控制塔」 | 【廠商】內部 54% 自助、每案省 45 分鐘 | 數字多為自家行銷頁；⚠️ AI Control Tower 細節未核對 |

**共同點**：五家都押注「既有 system of record + 權限模型 + 工作流」是 agent 的護城河，所以都走賦能路線。**AI 原生重建的威脅來自新創與大客戶自建**，目前規模仍小。

---

## 3. 組織導入的階段模型

### 3.1 主要模型對照

| 模型 | 階段 | 來源 |
|---|---|---|
| **MIT CISR Enterprise AI Maturity**（721 家企業，2022 調查 + 2024 訪談） | ① 實驗與準備（28%）② 建立試點與能力（34%）③ 發展 AI 工作方式（31%）④ AI Future Ready（7%） | 【顧問/研究】[MIT CISR](https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian)（2024-12） |
| **Gartner AI Maturity Model** | Awareness → Active → Operational → Systemic → Transformational；另有 7 支柱評估（策略、資料、治理、工程、營運模式、文化、AI 產品與價值） | 【分析】⚠️ 只找到二手描述 [BMC](https://www.bmc.com/blogs/ai-maturity-models/) |
| **BCG Build for the Future 2025** | Laggards（60%，幾乎無可量測價值）→ Scalers（35%）→ Future-built（5%） | 【顧問】[BCG press](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings)（2025-09-30） |
| **McKinsey State of AI 2025** | 以「AI 高績效者」（≥5% EBIT 來自 AI，約 6%）對照其他 | 【顧問】[McKinsey](https://www.mckinsey.com/solutions/ai-practice/our-insights/the-state-of-ai)（2025） |
| **Microsoft Work Trend Index 2025** | Frontier Firm：intelligence on tap、human-agent teams、每個人都是 agent boss；提出「人機比（human-agent ratio）」指標 | 【廠商調查】[Microsoft blog](https://blogs.microsoft.com/blog/2025/04/23/the-2025-annual-work-trend-index-the-frontier-firm-is-born/)（2025-04-23）。註：常見的「三階段（assistant → 人機團隊 → 人領導、agent 營運）」說法，本次 WebFetch 該頁未見，⚠️ 需查完整報告 |

### 3.2 MIT CISR 各階段財務表現（同產業平均比較，百分點）

| 階段 | 成長 | 獲利 | 這階段要做的事 |
|---|---|---|---|
| 1 實驗與準備 | -12.6 | -9.6 | 培訓、訂使用政策、讓資料可取用、試用工具、決定哪裡需要人監督 |
| 2 試點與能力 | -3.5 | -2.2 | 試點、簡化並自動化流程、發展 use case、以 API 串資料、用 LLM 支援工作 |
| 3 AI 工作方式 | +11.3 | +8.7 | 可擴充平台與可重用模型、儀表板分享成效、test-and-learn、擴大自動化、探索自主 agent |
| 4 Future Ready | +17.1 | +10.4 | AI 嵌入決策與流程、販售 AI 加值服務、結合分析/生成/agentic/機器人 AI |

→ [MIT CISR](https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian)（2024-12）。**注意**：資料是 2022 年，主要反映傳統分析式 AI；相關不等於因果。

### 3.3 其他關鍵數據
- 【顧問】McKinsey：高績效者「根本性重設計工作流程」的機率是其他人近 3 倍；高階主管親自負責 AI 的機率高 3 倍。→ [McKinsey](https://www.mckinsey.com/no/our-insights/the-state-of-ai)（2025）
- 【顧問】McKinsey「gen AI paradox」：78% 企業至少一個功能在用 gen AI，但約 8 成沒有實質 EBIT 影響；原因是水平式 copilot 擴散快但效益分散，垂直式 use case 約 90% 卡在試點。→ [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage)（2025-06）
- 【顧問】MIT NANDA「GenAI Divide」：95% 試點未帶來可量測 P&L 影響；主因是「學習落差」（工具不會記憶、不融入流程），不是模型品質。⚠️ 這是初步報告，樣本口徑在各報導間不一致（52 個組織訪談 / 153 位主管 vs 150 訪談 / 350 員工），**不宜當成通用失敗率**。→ [Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)（2025-08-18）
- 【分析】Gartner：到 2027 年底超過 40% agentic AI 專案會被取消（成本、價值不明、風險控管不足）；數千家 agentic 廠商中只有約 130 家是真的（其餘是 agent washing）。→ [Outlook Business 轉述](https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner)（2025-06）
- 【研究】丹麥 25,000 名勞工、7,000 個工作場所：AI chatbot 對薪資與工時「精確為零」的影響，時間節省約 3%，部分被新產生的整合與監督工作抵銷。→ [NBER WP 33777](https://ideas.repec.org/p/nbr/nberwo/33777.html)（2025-05）
- 【研究】BCG × Harvard「jagged frontier」實驗（758 名顧問）：在 AI 能力邊界內的任務，品質與速度顯著提升；邊界外的任務，用 AI 反而更差。低績效者提升 31%、高績效者 11%（⚠️ 後兩個數字為二手摘要）。2026-03 正式刊於 Organization Science。→ [SSRN 4573321](https://papers.ssrn.com/abstract=4573321)（2023）；[HBS AI Institute](https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/)（2026）

### 3.4 建議路徑：個人 → 團隊 → 跨部門 → AI-native

| 階段 | 對應模型 | 組織要做的事 | 工具用法 | 過關訊號 |
|---|---|---|---|---|
| **A. 個人生產力** | CISR 1／Gartner Awareness-Active | 使用政策、資料分級、全員培訓、找出 power users | 企業版 chat（M365 Copilot、Gemini、ChatGPT Enterprise）、內部 RAG 知識助理 | 使用率 > 50%、有量測（非自評）的時間節省；**METR 提醒：自評不可信** |
| **B. 團隊流程** | CISR 2 | 選 2–3 個高量、有標準答案的流程（客服 FAQ、HR 問答、AP 發票），定義基準線 | 既有系統內建 copilot（Now Assist、Joule、Agentforce）、低程式碼 agent（國泰 GAIA STUDIO 模式） | 流程指標（處理時間、解決率、錯誤率）對照基準線有差；人工覆核比例下降 |
| **C. 跨部門重設計** | CISR 3／McKinsey 高績效者 | 端到端流程重畫（如 Order-to-Cash、Procure-to-Pay）、資料平台與語意層、agent 治理（權限、稽核、人機比） | 多 agent 編排（ServiceNow Orchestrator、Workday Agent System of Record）、MCP/API 串接 | 財務指標（EBIT 貢獻）可歸因；有 agent 清冊與事故處理流程 |
| **D. AI-native** | CISR 4／BCG Future-built | 用「如果 agent 已在團隊裡，這個部門長什麼樣」重新設計組織（Shopify 規則：要人之前先證明 AI 做不到）；部分系統以 AI-native 產品替換 | AI-native ERP/客服、以結果計價、例外管理介面 | 新增人力需求必須附 AI 不可行說明；人機比成為管理指標 |

- 【個案】Shopify CEO 2025-04 備忘錄：「反射性使用 AI」是基本要求，申請人力前要說明為何 AI 做不到，AI 使用納入績效考核。→ [TechCrunch](https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount)（2025-04-07）

---

## 4. 有公開數字的企業案例

### 4.1 國際

| 企業 | 部門/系統 | 數字 | 可信度 |
|---|---|---|---|
| Klarna | 客服 | 2.3M 對話／首月、700 FTE 等值、解決時間 11→2 分；後來回聘真人 | 廠商自述 + 媒體（[press](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)） |
| Salesforce | 客服 | 支援人力 9,000→5,000 | CEO 發言（[Salesforce Ben](https://www.salesforceben.com/ai-agents-drive-4000-job-cuts-in-salesforce-support-division/)） |
| CBA | 客服 | 裁 45 人後撤回道歉 | 媒體（[Bloomberg](https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots)） |
| IBM | HR | 94% containment、HR 營運成本 -40% | 廠商（[IBM](https://www.ibm.com/case-studies/ibm-askhr)） |
| Walmart | 採購 | 成交率 64–68%、節省 1.5–3% | 廠商+媒體（[PON](https://www.pon.harvard.edu/daily/negotiation-skills-daily/chatbot-negotiations-what-can-ai-do-for-you/)） |
| Lumen | 業務 | 每週省 4 小時、估 5,000 萬美元/年 | 廠商（[Microsoft](https://news.microsoft.com/source/features/digital-transformation/the-only-way-how-copilot-is-helping-propel-an-evolution-at-lumen-technologies/)） |
| Morgan Stanley | 理財顧問 | 98% 團隊採用 | 公司自估（[Daily Upside](https://www.thedailyupside.com/advisor/practice-management/ai-assistants-are-taking-over-wall-street/)） |
| JPMorgan | 全員 | LLM Suite 2024 開放給 6 萬+ 員工 | 媒體（[NBC News](https://www.nbcnews.com/business/business-news/jpmorgan-chase-giving-employees-ai-assistant-powered-chatgpt-maker-ope-rcna166045)）；⚠️ 「20 萬人」說法未找到出處 |
| Mondelez | 行銷 | 投資 4,000 萬美元，目標成本 -30–50% | 媒體（目標非實績） |

### 4.2 台灣

| 企業 | 公開資訊 | 數字 | 可信度 |
|---|---|---|---|
| **台積電** | 製造與管理全面用 AI；內部 chatbot、SOP 優化、知識數位化 | 每 1% 生產力 ≈ 10 億美元（估算）；董事長承認 AI 對下一代製程探索作用有限、限制內部資訊與 AI 共享以防洩密 | 法說會/公開演講（[TechNews](https://technews.tw/2026/01/15/cc-wei-see-ai-bubble-at-2025-q4-financial-report/)、[TechNews 2025-01](https://technews.tw/2025/01/25/ai-business-tsmc-umc/)） |
| **國泰金控** | GAIA 生成式 AI 框架（2.0 走雲端優先）；國泰世華 GAIA STUDIO 員工低程式碼 AI 平台 | 近 50 項員工自建 AI 應用；國壽 8 成以上內勤完成 GenAI 課程、130+ 主管完成 AI 管理培訓、近 500 位認證數據分析師 | 公司新聞稿（[數位時代](https://www.bnext.com.tw/article/81192/cathaybk202411_01)；[經濟日報](https://money.udn.com/money/story/5613/9082615)）；**無工時節省數字** |
| **玉山銀行** | 行員助手「金秘書」（Vertex AI Search，3 個月上線）；AI 房貸顧問 | 分行打總行詢問電話 -30%；增貸申請填寫時間省約 9 成 | 廠商案例（[Google Cloud](https://cloud.google.com/customers/intl/zh-tw/esunbank)）+ 媒體（[TechNews](https://finance.technews.tw/2025/07/29/ai-mortgage-advisor/)，2025-07） |
| **中國信託** | AI 信用卡秘書（2025 金融博覽會）、AI 防詐 ATM；早期策略「先內部、後對客」 | ⚠️ 未找到員工效益數字 | 媒體（[優分析](https://uanalyze.com.tw/articles/5001838088)，2025-11） |
| **廣達** | AI 輔助軟體開發；Omniverse 產線模擬 | 開發效率 +33% | 媒體（[iThome](https://www.ithome.com.tw/news/171350)，2025-09） |
| **鴻海** | FoxBrain 繁中 LLM（Llama 3.1 70B，120 張 H100，約 4 週訓練），用於內部數據分析、決策輔助、文書、程式 | ⚠️ 製造效益只有規劃描述，無數字 | 公司發表（[自由時報](https://ec.ltn.com.tw/article/breakingnews/4975071)，2025-03-10） |
| **台灣中小企業整體** | 經濟部 2025 中小企業白皮書 | 約 7.4% 實際導入 AI（OECD 比較值 39%）；⚠️ 白皮書原文未取得 | 二手報導（[工商時報](https://www.ctee.com.tw/news/20260413701714-430104)） |

---

## 5. 對企業白皮書最有用的 10 個洞見

1. **AI 最確定的效益是把新手拉到老手水準**：客服 RCT 新手 +34%、老手幾乎不變，所以先導入在新人多、流動高的單位。→ [Brynjolfsson et al.](https://arxiv.org/abs/2304.11771)（2023/2025）
2. **「用 AI 取代人」是目前最常被收回的決策**：Klarna 回聘、CBA 撤回裁員、Gartner 預測一半縮編計畫會放棄——白皮書應把目標寫成「人數持平、處理量上升」。→ [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai)（2025-06）
3. **預算錯置**：超過一半的 GenAI 預算流向業務與行銷，ROI 最大的卻是後勤自動化。→ [MIT NANDA via Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)（2025-08）
4. **差異來自流程重設計而非工具**：AI 高績效者根本性重設計流程的機率是其他人近 3 倍。→ [McKinsey State of AI](https://www.mckinsey.com/no/our-insights/the-state-of-ai)（2025）
5. **停在試點階段的企業財務表現低於產業平均**：CISR Stage 1–2 成長 -12.6 / -3.5 個百分點，Stage 3–4 為 +11.3 / +17.1。→ [MIT CISR](https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian)（2024-12）
6. **自評生產力不可信，要量測**：資深工程師用 AI 慢 19%，卻自認快 20%。→ [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)（2025-07）
7. **企業要為 AI 對外說的話負法律責任**：Air Canada 案確立 chatbot 不是獨立實體。→ [Moffatt v. Air Canada](https://barrysookman.com/2024/02/16/moffatt-v-air-canada-a-misrepresentation-by-an-ai-chatbot/)（2024-02）
8. **人事決策是 AI 的法律雷區**：Mobley v. Workday 讓 AI 供應商也可能以「雇主的 agent」身分被告，EU AI Act 將招募列為高風險。→ [Proskauer](https://www.proskauer.com/blog/ai-bias-lawsuit-against-workday-reaches-next-stage-as-court-grants-conditional-certification-of-adea-claim)（2025-06）
9. **AI 同時是幕僚單位的新攻擊面**：被抓到的假收據中 AI 生成比例一年內從 0 升到 14%，再升到 70.8%，費用稽核要從抽查改成全查。→ [PYMNTS](https://www.pymnts.com/cybersecurity/2025/phony-ai-created-receipts-become-real-problem-for-businesses/)（2025/2026）
10. **BI 的自然語言查詢沒有語意層就不能上線**：同一批模型在學術基準 73–91%，到真實企業資料只剩約 17–21%。→ [Spider 2.0](https://arxiv.org/abs/2411.07763v2)（2024/2025）

---

## 附：本次未能完成的查證（給下一輪）

- McKinsey State of AI 2025 原文的整體數字（使用率、agent 擴展比例、EBIT 影響比例）——兩次 WebFetch 逾時。
- P&G「Cybernetic Teammate」實驗原文數字。
- Gartner AI Maturity Model 官方原文、Gartner Hype Cycle 2025。
- Microsoft Work Trend Index 2025 的「三階段」原文。
- 法務 AI（Harvey、A&O Shearman）與 CPQ 的具名客戶成效。
- 台灣：中信、富邦等金控的員工面量化效益；經濟部中小企業白皮書原文。
