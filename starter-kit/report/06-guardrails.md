# 第 6 章　決策三 護欄：先給員工好用的企業版工具，再談禁止

<p class="lede">員工已經在用 AI，禁止擋不住，只會讓使用轉進個人帳號，公司更看不到風險。比較有效的順序是：先提供好用的企業版工具，再依資料分級決定哪些資料能進哪個工具，對外的輸出一律留人工審核點。台灣的 AI 法規正處在空窗期，具體規範要等各部會在 2028 年前訂出來，這段時間正好先訂內規。</p>

## 禁止只會把使用推到個人帳號，風險反而看不見

2023 年，Samsung 工程師把內部原始碼貼進 ChatGPT，公司隨即在公司電腦上禁用生成式 AI；同一份禁令裡，也宣布要自建翻譯、摘要、開發用的內部工具。[^samsung] Apple、Amazon、JPMorgan 當年也都先限制，再改走企業版或內部工具。JPMorgan 在 2024 年推出內部的 LLM Suite，開放給大批員工使用。[^jpm] 這些公司很快就發現，禁令本身解決不了問題，員工要的是一個能用的工具。

瀏覽器資安廠商 LayerX 的遙測資料，把這件事量了出來：[^layerx]

```exhibit
{"id": "6.1", "type": "bar", "unit": "%",
 "title": "員工把資料貼進生成式 AI，八成以上走的是公司管不到的個人帳號",
 "data": [
   {"label": "員工會把資料貼進生成式 AI", "value": 77},
   {"label": "生成式 AI 連線走個人帳號", "value": 71},
   {"label": "貼上資料的行為發生在未受管的個人帳號", "value": 82, "highlight": true}
 ],
 "source": "LayerX，Enterprise GenAI Security Report 2025；PeopleMatters 轉述",
 "note": "廠商瀏覽器遙測；第三項的分母是有貼上資料的行為，不是全體員工"}
```

MIT NANDA 的研究看到同一件事：只有 40% 的公司買了官方的 LLM 訂閱，但超過九成公司的員工在用個人 AI 工具，使用者嫌公司買的工具不好用。[^nanda] 台灣的數字相近，61.8% 的 AI 使用發生在公司管控之外。[^aif]

風險已經有價格。IBM 2025 年的資料外洩成本報告指出，約兩成受訪組織的外洩事件涉及影子 AI，每起平均多出約 67 萬美元的成本；發生 AI 相關資安事件的組織，97% 沒有適當的 AI 存取控管。[^ibm]

**這代表什麼**：影子 AI 的根本原因，是公司沒有給員工好用的工具。只發禁令，員工照樣用，只是換成你看不到的帳號。先把企業版工具給出去，風險才會回到看得見的地方。

## AI 對外說的話就是公司說的話，法院已經這樣判

第 2 章提過加拿大航空的案子：客服機器人答應了公司規定不允許的退款，公司主張機器人要為自己的話負責，仲裁人不接受，判公司賠償。[^aircanada] 類似的後果，已經大量出現在法院和合約裡。

2023 年，美國一位律師在書狀裡引用了至少 6 件 ChatGPT 捏造的判例，被法官罰款 5,000 美元。法院在意的是律師被指出問題後沒有更正。[^mata] 2025 年，Deloitte 替澳洲政府做的一份報告出現捏造的判決引文和不存在的論文，最後同意退還最後一期款項。[^deloitte] 收錄這類判決的資料庫顯示，案件數還在快速增加：[^cases]

```exhibit
{"id": "6.2", "type": "column", "unit": "件",
 "title": "處理 AI 捏造引用的法院判決，半年內從 712 件增加到約 1,600 件",
 "data": [
   {"label": "2025 年底", "value": 712},
   {"label": "2026 年 6 月初", "value": 1600, "display": "約 1,545–1,600", "highlight": true}
 ],
 "source": "Damien Charlotin AI 幻覺判例資料庫；Bloomberg Law 2025-12-29、UNC Law Library 2026-06 整理",
 "note": "全球法院判決；柱高以區間上限繪製"}
```

台灣的專業人士已經意識到這個風險。Robert Walters 的調查裡，台灣專業人士擔心 AI 造成資料誤用或洩密的比例是 54%，擔心 AI 出錯時責任歸屬不清的是 51%，兩項都是調查的十個市場裡最高的。[^rw]

這幾個案例有一個共同點：AI 的輸出在送出去之前，沒有人查過。所以護欄的重點放在輸出端。只要是對外發布、法律意見、退款或價格承諾、刪除或修改正式資料這四類輸出，一律要有一位具名的人簽核。

## 台灣法規正處在空窗期，現在正是先訂內規的時候

台灣的 AI 法規基礎已經到位，但對企業的具體義務還沒有出來：

```exhibit
{"id": "6.3", "type": "ladder",
 "title": "台灣 AI 法規已經有基本法與風險框架，對企業的具體規範要等到 2028 年前",
 "steps": [
   {"name": "人工智慧基本法施行", "text": "2026-01-14 公布施行，主管機關為國科會。本法沒有罰則，要靠各部會修法落實", "meta": "2025-12-23 立法院三讀"},
   {"name": "數發部風險分類框架 v1.0", "text": "2026-07-07 生效，3 大類 20 項子類別，新增「AI 自主代理的授權外行為」。屬各部會共通指引，對民間沒有直接拘束力", "meta": "依基本法第 16 條訂定"},
   {"name": "各部會產業規範", "text": "各目的事業主管機關要訂出所主管領域的 AI 風險管理規範與產業指引", "meta": "2028 年 1 月前", "highlight": true}
 ],
 "source": "聯合報 2025-12-23；行政院 2026-05-21；理律法律事務所電子報 2026-07；中時新聞網 2026-07-09"}
```

在這之前，已經有幾份規範可以參考：

| 規範 | 性質 | 對企業的意思 |
|---|---|---|
| 行政院及所屬機關使用生成式 AI 參考指引（2023-08） | 公部門參考指引 | 機密文書禁用生成式 AI；地端封閉模型可依機密等級分級使用；AI 產出不能當作決策的唯一依據 [^ey-guide] |
| 金管會《金融業運用 AI 指引》（2024-06-20） | 行政指導，不遵循不罰 | 對金融業是事實上的稽核基準 [^fsc] |
| 資通安全管理法修正（2025-09-24 公布） | 法律，施行日期待定 | 委外廠商要有資安管理機制或第三方驗證；接政府或關鍵基礎設施案子的中小企業會被間接要求 [^cyber] |
| 個人資料保護法 | 法律 | 員工把客戶個資貼進公開 AI，可能構成未採取適當安全措施 [^pdpa] |
| EU AI Act 透明義務（2026-08-02 起適用） | 歐盟法規 | 產品或服務進入歐盟，要揭露使用者正在和 AI 互動；招募等高風險系統的義務延到 2027-12-02 [^euai] |

**這代表什麼**：到 2028 年之前，沒有法規會告訴你員工可以把什麼資料放進哪個工具，這件事要你自己決定。等規範出來再補內規，員工的使用習慣已經定型了。

## 用資料分級和人工審核點控制風險，比全面禁止有效

內規不必長。我們建議用一張表回答「什麼資料可以進哪個工具」，再用一張清單規定「哪些輸出一定要人看過」。下表是桑尼資料科學的資料分級框架，分級邏輯參考行政院指引：[^ey-guide]

| 資料等級 | 例子 | 可以用的工具 | 要求 |
|---|---|---|---|
| **公開** | 官網內容、已發布的新聞稿、公開法規 | 任何公司核准的工具 | 對外使用前查核事實 |
| **內部** | 內部流程文件、會議紀錄、一般專案資料 | 只限企業版工具：合約明定不拿資料訓練模型、走公司帳號登入、保留紀錄 | 禁止使用個人帳號 |
| **機密** | 客戶個資、財務未公開資訊、原始碼、合約 | 只限地端或封閉部署的模型，或不用 AI | 每個使用場景要有負責人核准 |
| **禁止** | 法規禁止外流的資料、主管機關要求保密的資料 | 不使用 AI | 違反視同資安事件通報 |

這張表要搭配三個機制，才不會變成貼在牆上的公告：

- **管帳號，不只管工具。** 允許清單要寫明核准的工具和帳號類型，再用瀏覽器或端點的防外洩設定，擋下個人帳號貼上內部以上等級的資料。圖表 6.1 顯示，貼上資料的行為八成以上發生在個人帳號，只列工具名稱，員工換個帳號就繞過去了。[^layerx]
- **人工審核點。** 前面列出的四類輸出，送出前一律要有具名的人簽核，並把簽核紀錄留下來。加拿大航空、Mata、Deloitte 三案缺的都是這一步。
- **定期稽核。** IBM 的報告顯示，有 AI 治理政策的組織裡，只有 34% 會定期稽核未授權的 AI 使用。[^ibm] 內規訂了沒查，等於沒訂。最簡單的稽核指標，是企業版工具的使用量占全部 AI 流量的比例，這個比例越低，影子 AI 越多。

AI agent 會自己動手做事，風險比聊天工具高一個層級，需要另外的身分與權限管理，第 7 章專章討論。

**工作坊提問**：若公司明天提供企業版工具並訂出資料分級，哪些員工工作會先轉到公司可管理的環境？由 IT、資安與第一線主管共同列出前五種用法。

<div class="advice" markdown>
用 30 天訂出第一版內規：

1. **第 1 週**：匿名問卷盤點員工現在用哪些 AI 工具、放了哪些資料進去。目的是找出需求，不追究責任。
2. **第 2 週**：選定一套企業版工具，確認合約寫明不拿公司資料訓練模型、可以用公司帳號登入、保留使用紀錄。
3. **第 3 週**：用上面的四級表定出資料分級，列出必須人工簽核的四類輸出，指定出事時的通報窗口。
4. **第 4 週**：公告內規，主管在部門會議上示範一次怎麼用，之後每季稽核一次企業版工具的使用比例。

附錄的「AI 使用政策範本」可以直接改成你們的版本。
</div>

[^samsung]: Forbes Australia,〈Samsung bans ChatGPT among employees after sensitive code leak〉，2023-05-02。https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/
[^jpm]: Fortune，2024-07-26。https://fortune.com/2024/07/26/jpmorgan-chatbot-research-analyst-llm-suite-openai-chatgpt-asset-wealth-managemnet-jamie-dimon ；Apple 限制使用，Fortune，2023-05-19。https://fortune.com/2023/05/19/apple-restricts-chatgpt-employee-data-leaks-iphone/
[^layerx]: LayerX,〈Enterprise GenAI Security Report 2025〉，PeopleMatters 轉述。廠商遙測。https://sea.peoplemattersglobal.com/amp/news/ai-and-emerging-tech/ai-data-leaks-soar-as-employees-bypass-company-rules-45605
[^nanda]: MIT NANDA,〈The GenAI Divide: State of AI in Business 2025〉。52 個組織訪談、153 位主管問卷，數字多為受訪者自述。https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
[^aif]: 人工智慧科技基金會，2026 台灣產業 AI 化大調查，228 家企業，樣本偏向較積極的企業。CIO Taiwan，2026-04-30。https://www.cio.com.tw/111644/
[^ibm]: IBM,〈Cost of a Data Breach Report 2025〉，TechRepublic 轉述，2025-07。https://www.techrepublic.com/article/news-ai-breach-risks-rise-as-governance-lags/
[^aircanada]: Moffatt v. Air Canada, 2024 BCCRT 149，2024-02-14。英屬哥倫比亞省民事仲裁庭。https://www.torkin.com/insights/publication/bc-tribunal-confirms-companies-remain-liable-for-ai-chatbot-created-information
[^mata]: Mata v. Avianca, Inc.，美國紐約南區聯邦地方法院，2023-06-22。https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.
[^deloitte]: AP，CTV News 轉載，2025-10。https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
[^cases]: Bloomberg Law,〈AI-Faked Cases Become Core Issue Irritating Overworked Judges〉，2025-12-29。https://news.bloomberglaw.com/legal-ops-and-tech/ai-faked-cases-become-core-issue-irritating-overworked-judges ；UNC Law Library,〈Handling Hallucinations: A Reflection on the Last Three Years〉，2026-06。https://library.law.unc.edu/2026/06/handling-hallucinations-a-reflection/
[^rw]: Robert Walters,〈未來職務洞察〉，近 5,000 名亞洲專業人士與雇主；104 職場力轉載經濟日報，2026-08-31。https://blog.104.com.tw/?p=250253
[^ey-guide]: 行政院及所屬機關（構）使用生成式 AI 參考指引，2023-08。自由時報，2023-09。https://ec.ltn.com.tw/article/paper/1602420
[^fsc]: 金管會《金融業運用人工智慧（AI）指引》，2024-06-20。理律法律事務所。https://www.leeandli.com/TW/Newsletters/7287.htm
[^cyber]: 資通安全管理法修正，2025-08-29 三讀、2025-09-24 公布。理律法律事務所。https://www.leeandli.com/TW/NewslettersDetail/7505.htm
[^pdpa]: 《個人資料保護法》2023-05 修正，非公務機關未採取適當安全措施者罰 2 萬至 200 萬元。自由時報，2023-05。https://news.ltn.com.tw/amp/news/politics/breakingnews/4302756
[^euai]: Hunton,〈EU Digital Omnibus on AI Enters into Force〉，2026-07-28。https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force
