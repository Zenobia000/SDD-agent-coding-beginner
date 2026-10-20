<div class="part" markdown>
<span class="kicker">第四部　部門與系統</span>

**每個部門先做一個量大、有標準答案、量得到前後差別的場景，對外承諾與影響個人權益的決定留給人**

十個部門
</div>

# 客服：客服是證據最硬的場景，目標放在處理量上升、保留真人選項

<p class="lede">客服是目前少數有大型實地研究支持的部門：AI 助理讓客服人員每小時解決的件數平均多 14%，新手多 34%。翻車的公開案例也集中在客服，共同點是拿 AI 取代人。目標訂成「同樣的人處理更多案件」，並保證客戶隨時找得到真人，是證據支持的做法。</p>

## 現況證據

**研究**：史丹佛與 MIT 學者追蹤 5,179 名客服人員，導入生成式 AI 助理後，每小時解決的問題平均多 14%，資歷淺的人多 34%，資深人員幾乎沒有變化。[^brynjolfsson] 這項研究裡的 AI 是給客服人員用的助理，回覆仍由人送出。它證明的是「AI 幫人」有效，不能拿來證明「AI 取代人」有效。

**個案與廠商說法**：Klarna 宣布 AI 助理上線第一個月處理 230 萬次對話、占客服聊天的三分之二，相當於 700 名全職人力，平均解決時間從 11 分鐘降到 2 分鐘以內。[^klarna] 這是公司自述。一年多後，執行長公開承認服務品質下降，重新招募真人客服。[^klarna-back] Salesforce 執行長在訪談中說，自家客服人力從約 9,000 人降到約 5,000 人，這是 CEO 發言，沒有正式文件佐證。[^salesforce]

**反向個案**：澳洲聯邦銀行以語音機器人為由裁撤 45 名客服，工會指出來電量其實上升，還要主管加班接電話；銀行在 2025 年 8 月公開道歉並撤回裁員。[^cba]

**分析機構**：Gartner 2025 年 3 月調查 163 位客服主管，95% 打算保留真人客服；Gartner 並預測，到 2027 年，原本計畫靠 AI 大幅縮減客服人力的組織，有一半會放棄這個計畫。[^gartner]

台灣也有企業公布數字，例如遠傳表示 AI 客服每年省下約 5,400 萬元人力成本，屬企業自述。[^fetnet]

**這代表什麼**：效益有研究撐腰的是「AI 協助客服人員」。「AI 直接面對客戶、減少人力」這一段，公開證據多半來自公司自己，而且有好幾家已經回頭。

## 先做這一件

**先做客服人員的回覆建議：AI 依知識庫草擬回覆並附上出處，客服人員確認或修改後送出。**

選這一件有三個理由。它和研究裡驗證過的做法一致；回覆還是由人送出，AI 說錯話不會直接變成公司的承諾；新人受益最多，客服又是流動率高的單位。

怎麼做：

1. 從工單系統拉出過去三個月的案件分類，挑出量最大的 20 類問題。
2. 把這 20 類問題對應的規定、流程、標準回覆整理成知識庫，每一條標上版本與負責人。
3. 讓 AI 只根據知識庫草擬回覆，每則回覆附上引用的條目。客服人員按「採用」「修改後採用」「不採用」，系統留下紀錄。
4. 跑四到八週，和導入前同期比較。

怎樣算成功：每小時解決件數比基準線高，客訴率與再聯繫率沒有變差，新人達到平均處理量的時間縮短。採用率高的問題類別，下一步才考慮讓 AI 直接回答客戶，而且保留一鍵轉真人。

```exhibit
{"id": "客服 1", "type": "matrix",
 "title": "答案有標準、對客戶影響小的問題先交給 AI，補償與客訴留給真人",
 "x": {"label": "答案有沒有標準", "low": "需要判斷", "high": "有標準答案"},
 "y": {"label": "對客戶的影響", "low": "小", "high": "大"},
 "cells": [
   {"title": "真人處理", "text": "客訴升級、補償金額、例外處理、情緒激烈或弱勢客戶"},
   {"title": "AI 草擬、真人確認", "text": "退款與保固規定、帳務問題。答案有規則，但說錯就是公司的承諾"},
   {"title": "AI 回答、可轉真人", "text": "產品比較、一般諮詢。答錯影響小，但要留轉真人的入口"},
   {"title": "AI 直接處理", "text": "查訂單、查物流、改密碼、營業時間。量最大、對錯最好驗", "highlight": true}
 ],
 "source": "桑尼資料科學整理"}
```

## 不能交給 AI 的決策

| 決策 | 為什麼 | 依據 |
|---|---|---|
| 退款、優惠、保固等政策的解釋與承諾 | AI 對客戶說的話，法律上就是公司說的話 | Moffatt v. Air Canada：仲裁庭駁回「機器人是獨立實體」的主張，判公司賠償 [^aircanada] |
| 補償金額與例外處理 | 涉及金錢與裁量，錯了要公司買單 | 同上；屬對外具法律效力的承諾 |
| 客訴升級、情緒激烈或弱勢客戶 | 品質下降時最先受傷的客戶群 | Klarna 修正後的原則是客戶永遠找得到真人 [^klarna-back] |
| 客服人力縮編 | 最常被收回的決定 | 澳洲聯邦銀行撤回裁員；Gartner 預測一半縮編計畫會放棄 [^cba] [^gartner] |

## 加 AI 還是重建

**在既有系統加 AI**：ServiceNow Now Assist、Zendesk、Salesforce Service Cloud 都已經內建回覆建議、摘要與 agent。ServiceNow 自述，內部客服人員導入摘要建議後每案省 12 到 17 分鐘。[^servicenow] 前提是工單系統已經是客服人員的主要工作台，知識庫也放在裡面。台灣多數企業應該走這條路。

**用 AI 重新設計流程**：Intercom Fin、Sierra 這類 AI 優先的客服產品，由 AI 先接所有對話，人只處理例外，並且依「解決件數」計價。Intercom 以每次結果 0.99 美元計價，但客戶 24 小時沒有回應也算「推定已解決」。[^intercom] 走這條路的前提有三個：你能把「解決」的定義寫進合約、你有能力自己抽查品質、轉真人的通道在上線前就設計好。

## 雷區

**拿 AI 解決率當唯一的 KPI。** 客戶沒有回應可能是放棄了，不一定是問題解決了。解決率要配再聯繫率和客訴率一起看。

**先裁人，再看效果。** 澳洲聯邦銀行的來電量在裁員後上升，最後由主管加班補洞。[^cba] 人力調整放在數字穩定之後，而且優先用自然流失與不補缺。

**知識庫過時，AI 照樣說得很有把握。** Air Canada 的機器人講的是一條公司實際上沒有的規定。[^aircanada] 每條知識庫內容要有負責人和更新日期，規定改了，知識庫同一天改。

**服務歐盟客戶時忘了揭露。** EU AI Act 第 50 條的透明義務在 2026 年 8 月 2 日起適用，客戶在跟 AI 對話時要讓對方知道。[^euai]

## 該量的三個指標

| 指標 | 怎麼量 | 多久看一次 |
|---|---|---|
| 每人每小時解決件數 | 工單系統，對照導入前四到八週的基準線 | 每週 |
| 再聯繫率與客訴率 | 同一位客戶七天內就同一問題再來的比例；客訴件數 | 每月 |
| 新人達標時間 | 新進客服達到團隊平均處理量所需的週數 | 每季 |

<div class="advice" markdown>
上線前先回答三件事：

1. 客戶在任何畫面，最多幾步可以轉到真人？
2. 知識庫每一條內容的負責人是誰？規定改了，誰在同一天更新？
3. 導入前四週的每小時解決件數、再聯繫率、客訴率，已經記下來了嗎？

第三題答不出來，先別上線，你會無法證明任何效果。
</div>

[^brynjolfsson]: Brynjolfsson, Li & Raymond,〈Generative AI at Work〉，Quarterly Journal of Economics 140(2)，2025；5,179 名客服人員（正式版摘要為 5,172 人、平均 +15%）。https://arxiv.org/abs/2304.11771
[^klarna]: Klarna 新聞稿，2024-02-27，公司自述。https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
[^klarna-back]: Entrepreneur，2025-05。https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
[^salesforce]: Salesforce Ben，2025-09；CEO 訪談發言，無正式文件確認。https://www.salesforceben.com/ai-agents-drive-4000-job-cuts-in-salesforce-support-division/
[^cba]: Bloomberg，2025-08-21。https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots ；Information Age (ACS)，2025-08。https://ia.acs.org.au/article/2025/cba-reverses-ai-driven-job-cuts--admits--error-.html
[^gartner]: Gartner 新聞稿，2025-06-10；2025-03 調查 163 位客服主管。預測屬推估，非實測。https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai
[^fetnet]: 中時新聞網，2025-11，企業自述。https://wantrich.chinatimes.com/news/20251127900197-420101
[^aircanada]: Moffatt v. Air Canada, 2024 BCCRT 149，2024-02-14。英屬哥倫比亞省民事仲裁庭，非上級法院判例。https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada
[^servicenow]: ServiceNow blog,〈Boosting customer support agent productivity with generative AI〉，2024，廠商自述。https://www.servicenow.com/blogs/2024/support-agent-productivity-genai
[^intercom]: Intercom 定價頁，廠商資料。https://www.intercom.com/learning-center/intercom-pricing
[^euai]: Hunton,〈EU Digital Omnibus on AI Enters into Force〉，2026-07-28。https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force
