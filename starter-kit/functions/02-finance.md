# 財務：請款與應付帳款回報最高，但 AI 生成的假收據已經逼稽核改成全查

<p class="lede">後勤自動化是 AI 回報最好的地方之一，財務裡的應付帳款與費用報銷又是後勤裡量最大、規則最清楚的工作。同一項技術也讓造假變便宜：被抓到的假收據裡，AI 生成的比例在一年多內從零升到七成。財務導入 AI，要同時改兩件事：讓 AI 處理單據，也讓 AI 檢查每一張單據。</p>

## 現況證據

**分析機構調查**：Gartner 2025 年調查 183 位財務長與財務主管，59% 的財務部門在用 AI，2024 年是 58%，2023 年是 37%。[^gartner] 採用率已經持平，下一步的差距會出在「用在哪裡、量不量得到效果」，不再是「有沒有用」。

**顧問研究**：MIT NANDA 的研究指出，企業約一半的生成式 AI 預算流向業務與行銷工具，回報最大的卻是後勤自動化。這份研究的數字多為受訪者自述，作者自己說結論是方向性的。[^nanda]

**廠商數據**：SAP 表示，內部約 11 萬名員工在財務、人資、採購等工作上用 Joule 後，生產力提升約 20%。[^sap] 費用管理公司 Ramp 表示，它的 agent 在 90 天內標記了超過 100 萬美元的詐欺發票。[^ramp] 兩者都是廠商自述。

應付帳款常被引用的「每張發票處理成本」基準，各來源從不到 3 美元到 20 多美元都有，多為二手轉述，本書不引用。報價（CPQ）方面，Salesforce 已把報價系統重建成讓 agent 可以跨流程操作的 Revenue Cloud，但目前只有產品發表，找不到具名客戶的成效數字。[^cpq]

**這代表什麼**：財務是有效益方向、但缺少公開硬數字的部門。你要自己量基準線，不能拿廠商簡報上的數字當成你的預期。

## 先做這一件

**先做應付帳款的發票擷取與三方比對：AI 讀發票欄位，與採購單、驗收單核對，一致的排進付款建議清單，不一致的列為例外交給人。**

這件事量大，答案有標準（金額、數量、統編對不對得上，查原件就知道），前後差別也容易量。付款放行仍由人按，AI 出錯會停在例外清單裡，不會直接把錢付出去。

怎麼做：

1. 先挑一個供應商數量多、發票格式雜的事業單位，記下現在每張發票的處理時間與退件原因。
2. AI 只做擷取與比對，輸出「一致」「金額不符」「找不到採購單」等標記，每個標記附上比對到的原始欄位。
3. 每週抽查 AI 判為「一致」的發票，抽查結果記錄下來。
4. 抽查的錯誤率連續穩定，才考慮擴大到其他單位。

怎樣算成功：不需要人工處理的發票比例上升，每張發票的處理時間下降，錯付與重複付款沒有增加。

```exhibit
{"id": "財務 1", "type": "column", "unit": "%",
 "title": "被抓到的假收據裡，AI 生成的比例一年多內從 0 升到七成",
 "data": [
   {"label": "2024 年", "value": 0},
   {"label": "2025 年 9 月", "value": 14},
   {"label": "2026 年 5 月", "value": 70.8, "highlight": true}
 ],
 "source": "AppZen，經 TechRadar（2025）與 PYMNTS（2025／2026）報導；2026 年 5 月的樣本為 1,471 張",
 "note": "廠商數據；分母是被抓到的假收據，不是全部收據"}
```

## 不能交給 AI 的決策

| 決策 | 為什麼 | 依據 |
|---|---|---|
| 關帳與財報簽核 | 簽核人要對數字負法律責任，責任不能轉給工具 | 簽核責任在人；第 6 章的問責原則 |
| 會計判斷：收入認列、減損、估計 | 需要專業判斷，而且要能向會計師說明理由 | 判斷理由要由人簽名負責，簽證會計師查核時會問 |
| 付款放行與供應商銀行帳戶變更 | 商業電子郵件詐騙最常從這裡下手 | 供應商主檔與帳號變更是付款詐騙的熱點，要雙人覆核 |
| 稅務立場 | 影響對外申報，後果由公司承擔 | 申報責任在公司與簽核人 |
| 報價的價格與折扣例外 | 報出去的價格就是公司的承諾 | Moffatt v. Air Canada：AI 說的話公司要負責 [^aircanada] |

## 加 AI 還是重建

**在既有系統加 AI**：SAP Joule、Dynamics 365 Copilot 在 ERP 上加對話與 agent；SAP Concur、Ramp、Brex 在報銷流程加收據辨識與政策檢核。顧問一再強調，SAP 這條路的前提是「clean core」：ERP 的核心沒有被大量客製改壞，資料結構乾淨。[^epiuse] 台灣多數企業的 ERP 客製很深，上 AI 之前要先盤點這一點。

**用 AI 重新設計流程**：Rillet、Campfire 這類 AI 原生的 ERP，由 agent 做自動入帳、對帳、營收認列與合併報表。Rillet 2026 年完成 1 億美元 C 輪募資，宣稱有 600 多家客戶，要取代 NetSuite 與 SAP。[^rillet] 目前客戶集中在中型 SaaS 公司，簽證會計師接不接受是關卡。除非你本來就要換 ERP，否則不必為了 AI 走這條路。

## 雷區

**繼續用抽查稽核報銷單。** AI 生成的假收據平均金額約 100 美元，刻意壓在審核門檻以下。[^appzen] 抽查與金額門檻正是它要繞過的東西。費用稽核要改成每張單據都由 AI 先檢查一次，人只看被標記的單據。

**把使用率當成果。** 財務部門 AI 使用率已經持平在六成左右，[^gartner] 再推高使用率說明不了任何事。要報告的是處理時間、錯誤率與稽核覆蓋率。

**讓報價 agent 自己給折扣。** 價格與折扣的上下限要寫在 agent 的權限裡，不能只寫在提示詞裡。超出範圍的報價一律轉人核准。

## 該量的三個指標

| 指標 | 怎麼量 | 多久看一次 |
|---|---|---|
| 不需人工處理的發票比例 | 從收到發票到排入付款都沒有人工介入的張數 ÷ 總張數 | 每月 |
| 每張發票的處理時間 | 收件到完成比對的時間，對照導入前基準線 | 每月 |
| 錯付、重複付款與被標記的可疑單據 | 金額與件數；可疑單據要追到結案 | 每月，關帳時一起看 |

<div class="advice" markdown>
本季就可以做的一件事：把費用報銷的稽核方式從「抽查」改成「AI 全查、人看例外」。即使你還沒導入任何 AI 處理單據，只要員工拿得到生成式 AI，你的報銷流程就已經暴露在假收據的風險裡。
</div>

【桑尼現場：待補】一個財務部門導入發票比對時，第一個月例外清單長什麼樣子。

[^gartner]: Gartner 新聞稿，2025-11-18；183 位財務長與財務主管，調查期間 2025-05 至 06。https://www.gartner.com/en/newsroom/press-releases/2025-11-18-gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025
[^nanda]: MIT NANDA,〈The GenAI Divide: State of AI in Business 2025〉，Fortune 報導，2025-08-18；52 個組織訪談、153 位主管問卷，多為受訪者自述。https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
[^sap]: SAP News，2026-07，廠商自述。https://news.sap.com/2026/07/sap-business-ai-release-highlights-q2-2026/
[^ramp]: Computerworld，2025，廠商自述。https://www.computerworld.com/article/4079701/new-ai-scam-fake-expense-receipts.html
[^cpq]: IT Brief，2025，產品發表。https://itbrief.com.au/story/salesforce-unveils-agentforce-to-speed-up-quoting-for-sellers
[^aircanada]: Moffatt v. Air Canada, 2024 BCCRT 149，2024-02-14。https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada
[^epiuse]: EPI-USE，SAP Sapphire 觀察，顧問觀點。https://www.epiuse.com/aws-services/blogs/sap-sapphire-highlights-gen-ai-success-relies-on-clean-core-and-customer-adoption
[^rillet]: The Next Web，2026-08，公司自述的客戶數。https://thenextweb.com/news/rillet-100m-series-c-1bn-accounting-ai
[^appzen]: AppZen 數據，TechRadar，2025。https://www.techradar.com/pro/security/workers-are-scamming-their-employers-using-ai-generated-fake-expense-receipts ；PYMNTS，2025／2026。https://www.pymnts.com/cybersecurity/2025/phony-ai-created-receipts-become-real-problem-for-businesses/
