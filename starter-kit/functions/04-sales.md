# 業務：業務的公開成效多半是廠商說法，先從準備客戶資料這種內部工作做起

<p class="lede">業務與行銷拿走企業約一半的生成式 AI 預算，公開的可信成效數據卻是各部門裡最少的。目前能查到的數字幾乎都來自賣工具的廠商，最受矚目的 AI 業務新創還被揭露列出不存在的客戶。先做拜訪前的資料準備與會後紀錄，輸出只給自己的業務看，效果也最容易量。</p>

## 現況證據

**公開的可信成效數據很少。** 這一節列出的數字，沒有一項來自研究或獨立調查。

**廠商數據**：Microsoft 表示，Lumen Technologies 的業務用 Copilot for Sales 後平均每週省約 4 小時，Lumen 估計價值每年 5,000 萬美元。Microsoft 不同頁面把這筆錢分別寫成「節省」「預計節省」與「營收價值」，口徑不一致。[^lumen] Microsoft Dynamics 365 的 Sales Qualification Agent 會自動研究潛在客戶名單、寄信跟進，只把有購買意圖的名單交給業務，2025 年 10 月起正式上線，目前找不到具名客戶的成效數字。[^dynamics]

**公司自估**：Morgan Stanley 的 Debrief 工具會產生會議紀錄與跟進信草稿，並寫回 Salesforce；公司估計 98% 的理財顧問團隊在用。[^ms] 這是使用率，不是成效。

**平台採用**：Salesforce 財報顯示，Agentforce 上線以來到 2025 年 12 月的財報為止，累計成交 18,500 多筆，其中 9,500 多筆是付費交易。[^agentforce] 交易數成長很快，但財報沒有揭露有多少家客戶在付費使用。

**失敗個案**：AI 業務開發新創 11x 被 TechCrunch 揭露，官網列出並非客戶的公司標誌；員工說早期客戶流失率達七到八成，公司則說目前留存率 79%。創辦人在 2025 年 5 月卸任執行長。[^11x]

**預算錯置**：MIT NANDA 的研究指出，約一半的生成式 AI 預算流向業務與行銷工具，回報最大的卻是後勤自動化。[^nanda]

**這代表什麼**：業務是 AI 預算最多、證據最少的地方。你不需要因此不做，但要把第一個場景選在你自己量得到效果的地方，不要買廠商簡報上的承諾。

## 先做這一件

**先做拜訪前的客戶資料準備與會後紀錄：AI 從 CRM 歷史、往來信件與公開資訊整理出一頁客戶簡報；會後依錄音或筆記產生紀錄與跟進信草稿，由業務確認後寫回 CRM。**

這件事是內部工作，輸出先給業務自己看，AI 寫錯了不會直接寄到客戶手上。每位業務每週都要做好幾次，做法有標準格式，準備時間和 CRM 紀錄完整度都量得到。Morgan Stanley 的 Debrief 也是從這一段切入。[^ms]

怎麼做：

1. 和業務主管一起定出一頁客戶簡報的固定欄位，例如往來紀錄、未結案商機、上次承諾的事項、公開新聞。
2. AI 只能讀 CRM 與這位業務有權限看的信件，不能讀其他業務的客戶。
3. 會後紀錄與跟進信由 AI 草擬，業務修改後按送出；系統記錄修改幅度。
4. 先找一組業務試六到八週，另一組維持原狀當對照。

怎樣算成功：拜訪準備時間下降，會後 24 小時內完成 CRM 紀錄的比例上升，業務在試點結束後還在用。

## 不能交給 AI 的決策

| 決策 | 為什麼 | 依據 |
|---|---|---|
| 折扣與價格例外核准 | 報出去的價格就是公司的承諾 | Moffatt v. Air Canada：AI 說的話公司要負責 [^aircanada] |
| 合約條款的讓步 | 影響公司的法律義務與毛利 | 屬對外具法律效力的承諾 |
| 大客戶的關係取捨 | 需要判斷長期關係與內部資源，資料裡看不到全貌 | 屬無法回溯驗證的判斷 |
| 業績預測的承諾數字 | AI 可以給預測，承諾給主管的數字要有人簽名負責 | 問責要落在人身上 |
| 以公司名義自動寄信給客戶 | 內容就是對外承諾，寄錯收不回來 | 同 Air Canada 案的邏輯 |

## 加 AI 還是重建

**在既有系統加 AI**：Salesforce Agentforce、Dynamics 365 Sales agent、Microsoft 365 Copilot for Sales 都在既有 CRM 上加摘要、草稿與 agent。前提是 CRM 裡的資料是業務真的在填的。很多公司的 CRM 只在季末補登，AI 讀到的就是過時的資料，摘要也會跟著錯。

**用 AI 重新設計流程**：AI 業務開發（AI SDR）由 agent 自己找名單、寫開發信、約會議，業務只接有意願的客戶。這條路目前證據最弱，11x 的案例就是警訊。[^11x] Klarna 在 2024 年宣布停用 Salesforce、改用自建資料層加 AI，評論者質疑自建能否取代數十年累積的流程功能。[^klarna] 業務流程重建，先等這些案例有更多可查的結果。

## 雷區

**相信 AI 業務工具的客戶名單與成效。** 採購前要求廠商提供可以直接聯絡的參考客戶，並問清楚對方用了多久、還在不在用。

**用量計價沒有上限。** Agentforce 採消費型計價（Flex Credits），agent 每做一件事都在扣額度。試點階段就要設每月上限，並追蹤每筆商機的 AI 成本。

**拿使用率當成效。** 98% 的團隊在用，說明的是工具好上手，[^ms] 不代表商機推進得比較快。報告要看準備時間與商機推進，不看登入次數。

## 該量的三個指標

| 指標 | 怎麼量 | 多久看一次 |
|---|---|---|
| 每次拜訪的準備時間 | 試點組與對照組各自記錄，或抽樣訪談 | 每兩週 |
| 會後 24 小時內完成 CRM 紀錄的比例 | CRM 的建立時間與會議時間比對 | 每週 |
| 商機推進率 | 每季從某一階段推進到下一階段的商機比例，對照前一季與對照組 | 每季 |

<div class="advice" markdown>
業務主管最常被廠商推銷的是「AI 幫你找客戶」。先把順序倒過來：讓 AI 幫業務準備已經在手上的客戶，三個月後拿準備時間與 CRM 完整度的前後數字，再決定要不要往對外的開發走。
</div>

**盤點題**：先抽樣檢查 CRM 的客戶欄位完整率、重複率與最近更新時間，再決定 AI 是否有足夠資料準備客戶摘要。沒有前後實測前，不預設導入會改善資料品質。

[^lumen]: Microsoft Source，2024，廠商自述。https://news.microsoft.com/source/features/digital-transformation/the-only-way-how-copilot-is-helping-propel-an-evolution-at-lumen-technologies/
[^dynamics]: Microsoft 365 Message Center MC1159615，2025-10。https://mc.merill.net/message/MC1159615
[^ms]: The Daily Upside，2024；公司自估。https://www.thedailyupside.com/advisor/practice-management/ai-assistants-are-taking-over-wall-street/
[^agentforce]: Salesforce FY26 Q3 財報新聞稿，2025-12-03。https://www.salesforce.com/news/press-releases/2025/12/03/fy26-q3-earnings/
[^11x]: TechCrunch，2025-03-24。https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have
[^nanda]: MIT NANDA,〈The GenAI Divide: State of AI in Business 2025〉，Fortune 報導，2025-08-18；多為受訪者自述。https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
[^aircanada]: Moffatt v. Air Canada, 2024 BCCRT 149，2024-02-14。https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada
[^klarna]: Salesforce Ben，2024-09；TipRanks。https://www.salesforceben.com/klarna-salesforce-workday-partnership-called-off-amidst-major-gen-ai-overhaul/
