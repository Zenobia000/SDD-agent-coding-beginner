# 第 8 章　決策五 衡量：先量基準線，品質和成本一起量

<p class="lede">量不出 AI 的效益，多半是量法出了問題。上線前先用同一把尺量一次沒有 AI 時的表現，上線後再量一次；前三個月看使用與品質，一年後看財務；成本指標和品質指標同一天上線。最後把「怎樣算做到」寫成可以自動檢查的測試，驗收就不用靠開會爭論。</p>

## 多數企業量不出效益，因為沒有基準線，也沒有財務指標

BCG 2025 年初調查 1,803 位高階主管，四分之三把 AI 列為前三大策略重點，但六成沒有定義或追蹤任何和 AI 有關的財務指標。[^bcg]

```exhibit
{"id": "8.1", "type": "bar", "unit": "%",
 "title": "四分之三的企業把 AI 列為前三大重點，六成沒有任何 AI 財務指標",
 "data": [
   {"label": "把 AI 列為前三大策略重點", "value": 75},
   {"label": "沒有定義或追蹤任何 AI 財務指標", "value": 60, "highlight": true},
   {"label": "看到有意義的價值", "value": 25, "display": "約 25%"}
 ],
 "source": "BCG，2025-01-15；1,803 位高階主管"}
```

沒有財務指標，至少還能看流程指標。問題是多數試點連流程指標的基準線都沒有。英國政府讓 2 萬名公務員試用 Microsoft 365 Copilot，回報每人每天省下 26 分鐘，這是使用者自己估的。[^gds] 英國工作與年金部（DWP）的官方評估涵蓋 3,549 人，報告自己就列出限制：授權不是隨機分配、資料是自陳、沒有試用前的基準線。[^dwp] 第 1 章的 METR 實驗已經看過，自己感覺的速度和實際量到的可以差到正負相反。

我們把研究裡反覆出現的原因歸成四個：**沒有基準線、只量使用率不量結果、只靠員工自陳、只把 AI 加進舊流程。** 前三個是量法的問題，第四個是第 3 章談過的設計問題。

別人的研究數字，也不能直接當成你的預期。有對照組的研究量到的效果差距很大：[^cui] [^brynjolfsson] [^metr]

```exhibit
{"id": "8.2", "type": "bar", "unit": "%",
 "title": "有對照組的研究，量到的效果從慢 19% 到多完成 26% 都有",
 "data": [
   {"label": "開發者完成的任務數（3 個隨機對照實驗）", "value": 26},
   {"label": "客服每小時解決件數", "value": 14},
   {"label": "資深開源工程師完成任務的速度", "value": -19, "highlight": true}
 ],
 "source": "Cui 等，Management Science，4,867 名開發者；Brynjolfsson, Li & Raymond，QJE 2025，5,179 名客服人員；METR，2025-07-10，16 位資深開發者",
 "note": "三項研究的指標與母體不同，只用來看效果的範圍；開發者研究的估計值誤差較大"}
```

效果會隨工作內容、人的資歷、工具與流程而變。DORA 2025 年調查近 5,000 名技術人員，結論是 AI 主要在放大團隊既有的優點和缺陷。[^dora] 所以你要量的是你自己的流程，用你自己的資料。

**基準線怎麼量**：

1. **選一個流程指標**。每件處理時間、每人每天處理件數、退件率，選一個業務主管本來就在看的。
2. **用系統紀錄量，不發問卷**。上線前取兩到四週的實際資料；工單系統、ERP、表單的時間戳記都可以用。
3. **同時記一個品質指標**。錯誤率、退件率、客訴件數，至少一個。
4. **上線後用同樣的定義、同樣的資料來源再量一次**。中途改了指標定義，前後就不能比。
5. **可以的話，分批上線**。先上線的組和還沒上線的組互相對照，就能排除淡旺季的影響。第 1 章的客服研究就是這樣量出來的。

## 三個月看使用與品質，十二個月看財務，兩種指標要搭配

財務效益要等流程改完、規模擴大才看得到，通常要一年以上。只看財務，前一年都在盲飛；只看使用率，會把「大家都在用」誤當成「有效果」。所以要兩種指標搭配：週、月就動的領先指標，告訴你方向對不對；季、年才動的落後指標，告訴你帳上有沒有變。

| 面向 | 領先指標（每週、每月看） | 落後指標（每季、每年看） |
|---|---|---|
| 採用 | 啟用率、每週使用人數、企業版工具占全部 AI 流量的比例 | — |
| 生產力 | 每件工作的時間、流程週期時間 | 單位產出成本、人均營收 |
| 品質 | 人工退回率、被抓到的錯誤件數、上線後的事故數 | 客訴、法律事件、重工成本 |
| 財務 | — | 可歸因於 AI 的營業利益、授權與用量的總成本 |
| 人 | 員工對工具的信任度、使用體驗 | 留任率、技能提升的覆蓋率 |
| 風險 | 資料外洩防護的攔截數、未授權工具數 | 外洩事件數與損失 |

這張表綜合 DX、DORA 與 McKinsey 的衡量框架。[^dx] 採用列的最後一項要特別看：企業版工具的占比越高，影子 AI 越少，第 6 章的護欄是不是有效，從這個數字就看得出來。

```exhibit
{"id": "8.3", "type": "ladder",
 "title": "每個時間點只問一個問題，答案對了才看下一個",
 "steps": [
   {"name": "上線前", "text": "量基準線：一個流程指標、一個品質指標，用系統紀錄", "signal": "兩個數字都有，業務主管同意這就是起點"},
   {"name": "第 1–3 個月", "text": "看有沒有人用、用了品質有沒有掉", "signal": "目標使用者過半在用；品質指標沒有低於基準線"},
   {"name": "第 4–12 個月", "text": "看流程指標有沒有動", "signal": "處理時間或處理量對照基準線有差，而且品質守住", "highlight": true},
   {"name": "12 個月以後", "text": "看財務：單位成本、可歸因的營業利益、總成本", "signal": "效益扣掉授權、用量、訓練與審核的成本之後仍為正"}
 ],
 "source": "桑尼資料科學整理"}
```

保守一點的做法可以參考。JPMorgan 的使用者自估每週省下約 4 小時，銀行也估出一筆效率改善，但沒有把省下的時數直接換算成獲利或人力縮減，執行長也承認直接的獲利效益很難衡量。[^jpm] 自估省下的時間，最多只能當成領先指標。

## 只量成本會翻車，品質指標要和成本指標一起上線

<div class="case" markdown>
**Klarna：成本數字一路漂亮，品質卻撐不住**

2024 年 2 月，Klarna 宣布 AI 客服上線第一個月處理了 230 萬次對話，占客服聊天的三分之二，相當於 700 名全職人力；平均解決時間從 11 分鐘降到 2 分鐘以內，預估當年貢獻 4,000 萬美元的獲利改善。[^klarna]

2025 年 5 月，執行長承認公司把成本看得太重，服務品質因此下降，開始重新招募真人客服，讓客戶隨時找得到真人。[^klarna-back] 同年第三季法說會，Klarna 的說法變成 AI 做了 853 人份的工作、累計省下 6,000 萬美元。[^klarna-q3] 這些都是公司自述的數字。
</div>

Klarna 對外公布的數字，多半是處理量、速度和成本，這三個數字一路都很好看。服務品質下滑時，這一組指標發不出警訊。

**做法：每個成本指標配一個品質指標，同一天上線，並且事先訂好停損線。**

| 你要追的成本或效率指標 | 一起上線的品質指標 | 停損線的寫法 |
|---|---|---|
| 每件處理成本 | 同一問題再次來電或來信的比例 | 高於基準線一定幅度，就暫停擴大 |
| 平均處理時間 | 人工退回或更正的比例 | 退回率連續兩週上升，就回頭檢查 |
| 自動處理的比例 | 客訴件數、轉接真人的等待時間 | 客訴超過上限，就恢復真人優先 |

停損線的數字由業務負責人訂，不由導入團隊自己訂。這張表的每一格都要在上線前填好；上線後才訂，數字很容易被調成剛好過關。

## 上線前先講好「怎樣算做到」，把驗收標準寫成可以自動檢查的測試

衡量的最後一步，是把驗收標準寫到機器可以檢查的程度。「準確率要高」「使用者要滿意」不能驗收；「用一組標好答案的請假句子測，完全答對的比例要達到業務主管訂的門檻」可以。

這是規格驅動開發（Spec-Driven Development，SDD）的做法：先寫規格，規格裡包含驗收標準，再讓 AI 依規格產出程式或流程，每一條驗收標準都對應一個可以自動執行的測試或評測。以一個「一句話請假」的系統為例：

| 規格裡的一句話 | 對應的自動測試 |
|---|---|
| 員工打一句話，系統要解析出假別、起訖日期與時段 | 準備一組標好正確答案的句子，每次改版自動跑，算出完全答對的比例 |
| 剩餘特休不夠時，不能送出申請 | 餘額 0.5 天時申請 1 天，系統必須拒絕 |
| 判斷不出假別時要問使用者，不能自己猜 | 輸入「明天不來」，系統必須回問假別 |
| 每次解析的模型費用不能超過上限 | 跑完測試集，計算平均每次的費用 |

這樣做有三個直接的好處。模型換版本時，測試重跑一次就知道有沒有退步；向廠商採購時，可以把測試集交給對方，用你的資料驗收（第 7 章的採購五問第 5 題）；門檻由業務主管訂、測試由工程團隊寫，責任分得清楚。

桑尼資料科學的 SDD 實戰營用的就是這套做法：學員第一天寫規格與驗收標準，第二天讓 AI 依規格從零產出應用程式，再用自動評測量每一組的解析準確率。準確率要多少才能上線，由學員自己判斷，這個判斷本來就屬於業務端。

<div class="advice" markdown>
上線前，用這張檢核表確認衡量已經就位：

- [ ] 有一個流程指標的基準線，資料來自系統紀錄，涵蓋至少兩週
- [ ] 有一個品質指標，和成本或效率指標同時上線
- [ ] 每個品質指標都有停損線，由業務負責人訂
- [ ] 每一條驗收標準都對應一個可以自動執行的測試或評測集
- [ ] 訂好第 3 個月與第 12 個月回頭看的日期，以及當天要看哪幾個數字

附錄的[〈效益衡量表〉](../tools/04-impact-measurement-sheet.md)可以直接拿來填。
</div>

[^bcg]: BCG 新聞稿，2025-01-15；1,803 位 C-level 主管。https://www.bcg.com/press/15january2025-ai-optimism-autonomous-agents
[^gds]: Government Transformation，英國 GDS 試用 M365 Copilot，2024-09 至 12 月，約 2 萬名公務員，使用者自陳。https://www.government-transformation.com/transformation/government-trial-shows-ai-use-saves-civil-servants-two-weeks-per-year
[^dwp]: UK Department for Work and Pensions,〈An Evaluation of DWP's Microsoft 365 Copilot Trial〉，試用期間 2024-10 至 2025-03，3,549 人。https://www.gov.uk/government/publications/an-evaluation-of-dwps-microsoft-copilot-365-trial/an-evaluation-of-dwps-microsoft-365-copilot-trial
[^dora]: Google DORA,〈2025 State of AI-assisted Software Development〉，2025-09；近 5,000 名技術人員。https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/
[^dx]: DX AI Measurement Framework。https://getdx.com/ai-measurement-framework/ ；DORA AI 能力模型。https://www.dora.dev/research/ai ；McKinsey,〈The state of AI in 2025〉。https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai 。指標組合為桑尼資料科學綜合整理。
[^jpm]: JPMorgan 2026-02 公司更新，經 Zacks 報導，公司自述。https://www.zacks.com/stock/news/3001953/ ；Fortune，2024-07-26。https://fortune.com/2024/07/26/jpmorgan-chatbot-research-analyst-llm-suite-openai-chatgpt-asset-wealth-managemnet-jamie-dimon
[^cui]: Cui 等,〈Effects of GenAI on High-Skilled Work〉，Management Science；Microsoft、Accenture 與一家財星百大製造商共 4,867 名開發者，3 個隨機對照實驗；完成任務數 +26.08%（標準誤 10.3%，估計值不精確）。https://papers.ssrn.com/abstract=4945566
[^brynjolfsson]: Brynjolfsson, Li & Raymond,〈Generative AI at Work〉，Quarterly Journal of Economics 140(2)，2025。https://arxiv.org/abs/2304.11771
[^metr]: METR,〈Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity〉，2025-07-10。https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[^klarna]: Klarna 新聞稿，2024-02-27，公司自述。https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
[^klarna-back]: Entrepreneur，2025-05。https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 ；Fortune，2025-05-09。https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/
[^klarna-q3]: Customer Experience Dive，2025-11，引述 Klarna 2025 年第三季法說會。https://www.customerexperiencedive.com/news/klarna-says-ai-agent-work-853-employees/
