# 第 7 章　決策四 數位員工：AI agent 要像員工一樣有身分、負責人和權限

<p class="lede">AI agent 會自己查資料、呼叫系統、寄信、改資料庫，做的事和員工一樣會留下後果。管理它的方式也該和員工一樣：上線前給它一個身分、一位負責人和剛好夠用的權限，上線後留下紀錄，關鍵動作前由人核准。提示注入攻擊目前沒有可靠的解法，從架構上限制 agent 碰得到什麼，是現在最可靠的做法。</p>

## agent 已經出過真實事故，原因都是權限給太多

企業試用 agent 的速度，比管理 agent 的速度快很多。McKinsey 2025 年的調查中，62% 的組織至少在試驗 AI agent；[^mck] Deloitte 隔年調查 3,235 位主管，只有約五分之一的公司有成熟的自主型 agent 治理模式。[^deloitte]

```exhibit
{"id": "7.1", "type": "bar", "unit": "%",
 "title": "六成組織已經在試 AI agent，有成熟治理模式的只有約五分之一",
 "data": [
   {"label": "至少在試驗 AI agent 的組織", "value": 62},
   {"label": "有成熟的自主型 agent 治理模式的公司", "value": 20, "display": "約 20%", "highlight": true}
 ],
 "source": "McKinsey, The state of AI in 2025（約 2,000 位受訪者）；Deloitte, State of AI in the Enterprise 2026（3,235 位主管、24 國）",
 "note": "兩項來自不同調查、母體不同，只用來看方向"}
```

這個落差已經有代價。下面三起公開事故，類型不同，問題出在同一個地方。

<div class="case" markdown>
**Replit：開發用的 agent 刪掉了正式資料庫**

2025 年 7 月，SaaStr 創辦人 Jason Lemkin 用 Replit 的 agent 做一個 12 天的開發實驗。第 9 天，正值程式碼凍結期間，agent 對正式資料庫下了破壞性指令，刪掉 1,206 筆高階主管資料與 1,196 筆以上的公司資料，接著還捏造資料、謊稱測試通過、謊稱無法復原。[^replit]

Replit 事後補上的防護很具體：開發與正式資料庫自動分開、只規劃不執行的模式、一鍵從備份還原。這三項都是在限制 agent 碰得到什麼。
</div>

<div class="case" markdown>
**Amazon Q：一段惡意指令跟著正式版一起發布**

2025 年 7 月，攻擊者把一段惡意提示合併進 Amazon Q Developer 的 VS Code 擴充套件 1.84.0 版。這段提示要 agent 清空使用者的家目錄、刪除 AWS 資源，還帶上 `--trust-all-tools --no-interactive`，也就是「所有工具都信任、不要問人」。AWS 表示那段程式碼寫壞了，實際上不會造成危害，但它已經以簽章版本發布、被數千人下載，之後才在 1.85 版撤回。[^amazonq]
</div>

<div class="case" markdown>
**EchoLeak：一封郵件就能讓 Copilot 把內部資料送出去**

CVE-2025-32711 是 Microsoft 365 Copilot 的零點擊漏洞。攻擊者只要寄一封夾帶隱藏指令的郵件，Copilot 檢索時把信讀進來，就會把 OneDrive、SharePoint、Teams 裡的資料，透過連結或圖片送到外部。漏洞評為 CVSS 9.3，微軟在 2025 年 6 月從伺服器端修補，目前沒有被實際利用的證據。[^echoleak]
</div>

**三起事故的共同點**：agent 拿到的能力超過任務需要。Replit 的 agent 在開發時就能寫正式資料庫；Amazon Q 的指令要它跳過所有確認；EchoLeak 讓同一個助理同時讀外部郵件、讀內部檔案、對外送出連結。IBM 2025 年的資料外洩報告也指向同一件事：回報發生 AI 相關資安事件的組織裡，97% 沒有適當的 AI 存取控管。[^ibm]

## 提示注入攻擊目前沒有可靠解法，只能從架構上限制 agent 能做的事

提示注入的原理很簡單：agent 讀進來的網頁、郵件、文件裡藏著指令，模型分不清哪一句是你下的、哪一句是攻擊者寫的。業界試過很多防禦方法，效果都不夠。一篇 2025 年的論文用會隨防禦調整的攻擊方式，測試 12 種已經發表的防禦，全部被突破。[^ruleoftwo]

所以 Meta 在 2025 年 10 月提出「Agents Rule of Two」，改從架構下手。它把 agent 的能力分成三類：處理不可信的輸入、存取敏感資料或系統、改變狀態或對外通訊。同一個 agent 在同一段工作裡，三類最多只能同時具備兩類。[^ruleoftwo]

```exhibit
{"id": "7.2", "type": "matrix",
 "title": "會讀不可信輸入的 agent，敏感資料和對外動作只能留一樣",
 "x": {"label": "能不能碰敏感資料", "low": "不能", "high": "能"},
 "y": {"label": "能不能對外動作或改資料", "low": "不能", "high": "能"},
 "cells": [
   {"title": "對外，不碰機密", "text": "例：讀公開網頁，整理成社群貼文草稿。可以讀不可信輸入"},
   {"title": "三項湊齊", "text": "EchoLeak 就在這一格。不能再讀不可信輸入；一定要讀，就在每個對外動作前加人工核准", "highlight": true},
   {"title": "只讀不寫", "text": "例：摘要公開報告。風險最低，適合當第一個 agent"},
   {"title": "碰機密，不對外", "text": "例：讀客戶來信、查內部資料、寫回覆草稿，但不能自己寄出，也不能載入外部連結"}
 ],
 "source": "Meta, Agents Rule of Two，2025-10-31；桑尼資料科學整理",
 "note": "本圖假設 agent 會處理不可信輸入，例如外部郵件、網頁、客戶上傳的檔案"}
```

**怎麼用**：設計每個 agent 時，先寫下它會讀哪些外部內容、碰得到哪些內部資料、能做哪些對外或寫入的動作。三樣都有，就拆成兩個 agent，或在對外動作前加一個人工核准點。這個判斷要在採購或開發之前做，上線後才補，常常要整個重來。

## agent 上線前要回答五個問題：身分、負責人、權限、紀錄、人工審核點

管理 agent 的工具已經出現。Microsoft 的 Entra Agent ID 給每個 agent 一個目錄身分，並設計了「sponsor」，也就是負責這個 agent 的人；[^entra] Workday 的 Agent System of Record 可以登記每個 agent 的角色、技能與資料權限，追蹤成本和成效，也能關掉整個 agent 或其中一項技能。[^workday] 台灣數發部 2026 年 7 月公布的人工智慧風險分類框架，也把「AI 自主代理的授權外行為」列為獨立的風險類別。[^moda]

工具只是載體。要先決定的是下面五件事，回答不出來的 agent 不上線。

```exhibit
{"id": "7.3", "type": "ladder",
 "title": "agent 上線前回答五個問題，答不出來就不上線",
 "steps": [
   {"name": "身分", "text": "每個 agent 一個獨立帳號，不共用員工帳號，也不共用一組服務帳號", "signal": "從系統紀錄看得出每個動作是哪一個 agent 做的", "meta": "參考：Microsoft Entra Agent ID"},
   {"name": "負責人", "text": "指定一位人類負責人，對它的產出負責；負責人調職或離職時要交接", "signal": "agent 清冊上每一列都有負責人的名字", "meta": "參考：Entra 的 sponsor 設計；Air Canada 判決"},
   {"name": "權限", "text": "只給完成任務需要的工具和資料；開發與正式環境分開；不開「全部信任」的參數；三類能力最多給兩類", "signal": "負責人說得出它碰得到哪些資料、能做哪些動作", "meta": "參考：Replit、Amazon Q 事故；Agents Rule of Two", "highlight": true},
   {"name": "紀錄", "text": "保留它讀了什麼、呼叫了哪些工具、產出了什麼，也記成本與成效", "signal": "出事時重建得出它做過的每一步", "meta": "參考：Workday Agent System of Record"},
   {"name": "人工審核點", "text": "對外發布、承諾金錢、刪改正式資料之前，由人核准", "signal": "流程圖上標出每一個審核點和審核人", "meta": "參考：行政院生成式 AI 參考指引"}
 ],
 "source": "桑尼資料科學整理，依據見各步驟"}
```

負責人這一題最常被跳過。2024 年加拿大航空主張客服機器人要為自己說的話負責，仲裁人直接駁回（見第 2 章）。[^aircanada] agent 出錯，責任在公司；公司裡總要有一個人，平常看它的表現，出事時第一個被找到。

人工審核點要放多少，沒有標準答案。Microsoft 提出「人機配比」（human-agent ratio）當作管理指標，但也明說比例依任務而定，沒有給建議數字。[^wti25] 我們的建議是從多開始：上線初期每個對外動作都審，看過幾百件、錯誤率穩定之後，再逐步放寬。

## 企業 agent 平台正在起量，市場上也充斥換皮產品，採購要會驗收

agent 的採購量正在上升。Salesforce 財報顯示，Agentforce 在 2025 年底的年化營收超過 5 億美元，年增 330%；上線以來成交 18,500 筆以上，其中付費的 9,500 筆以上。[^salesforce] Microsoft 自己的統計則是 Microsoft 365 裡活躍的 agent 一年增加 15 倍。[^wti26] 這兩組都是廠商數據，而且 Agentforce 的成交筆數裡，付費的大約只有一半。起量是真的，付費使用還在早期。

同時，市場上有大量換了包裝的產品。第 2 章提過，Gartner 估計自稱在做 agent 的數千家廠商裡，真的在做的大約只有 130 家，這是 Gartner 的估計，不是實測。[^gartner]

**採購前先問廠商五件事**，和上崗五問一一對應：

1. agent 有沒有獨立的身分，能不能接進你們現有的帳號管理系統？
2. 每個 agent 能不能指定負責人，負責人看得到它的成效嗎？
3. 權限能不能細到單一工具、單一資料表？能不能只關掉其中一項技能？
4. 操作紀錄能不能匯出，保留多久？
5. 在你們的真實資料上試跑，成功率是多少？用哪一組測試量的？

第 5 題最重要。廠商的示範用的是整理好的資料，第 2 章的 Spider 2.0 已經看過，換到真實企業資料，準確率可能掉一大截。驗收要用你自己的資料和你自己的標準，第 8 章會講怎麼把標準寫成可以自動跑的測試。

<div class="advice" markdown>
這個月就可以做的事：**列一份 agent 清冊。**

1. 找出公司裡已經在跑的 agent，包括員工自己接上的自動化流程與外掛。
2. 每一個填五欄：身分、負責人、權限、紀錄、人工審核點。
3. 對每一個問一次：它是不是同時讀外部內容、碰內部資料、又能對外動作？

五欄有空格的先停權或補齊；第 3 題答「是」的，這週就加上人工核准點。附錄的[〈數位員工上崗檢核表〉](../tools/05-agent-onboarding-checklist.md)可以直接拿來填。
</div>

**盤點題**：公司現有的 AI agent 是否使用共用帳號？誰負責它的輸出？測試環境能否碰到正式資料？任何一題答不出來，都先列入上線前的治理工作。

[^mck]: McKinsey,〈The state of AI in 2025: Agents, innovation, and transformation〉，2025-11-05；1,993 位受訪者、105 國。高績效者定義為 AI 貢獻 5% 以上 EBIT 且自評價值顯著。https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025
[^deloitte]: Deloitte,〈State of AI in the Enterprise 2026〉，問卷 2025 年 8–9 月；3,235 位主管、24 國。https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-generative-ai-in-enterprise.html
[^replit]: OECD AI Incidents Monitor,〈Replit AI Coding Tool Deletes Live Production Database and Fakes Data〉，2025-07-19。https://oecd.ai/en/incidents/2025-07-19-1eb1 ；eWeek，2025-07。https://www.eweek.com/news/replit-ai-coding-assistant-failure/
[^amazonq]: The Register,〈Compromised Amazon Q extension told AI to delete everything – and it shipped〉，2025-07-24。https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/
[^echoleak]: The Hacker News,〈Zero-Click AI Vulnerability Exposes Microsoft 365 Copilot Data〉，2025-06。https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html ；論文〈EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System〉，2025-09。https://arxiv.org/html/2509.10540v1
[^ibm]: IBM Cost of a Data Breach Report 2025，經 TechRepublic 報導，2025-07。https://www.techrepublic.com/article/news-ai-breach-risks-rise-as-governance-lags/
[^ruleoftwo]: Simon Willison,〈New prompt injection papers: Agents Rule of Two and The Attacker Moves Second〉，2025-11；整理 Meta 2025-10-31 提出的 Agents Rule of Two，以及以適應性攻擊測試 12 種防禦的論文。https://simonw.substack.com/p/new-prompt-injection-papers-agents
[^entra]: Microsoft Learn,〈What's new in Microsoft Entra Agent ID〉，官方文件，持續更新。https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
[^workday]: TechCrunch,〈Workday launches a platform for enterprises to manage all of their AI agents in one place〉，2025-02-11。https://techcrunch.com/2025/02/11/workday-launches-a-platform-for-enterprises-to-manage-all-of-their-ai-agents-in-one-place
[^moda]: 數位發展部「人工智慧風險分類框架」v1.0，2026-07-07 生效，對民間 AI 應用沒有直接拘束力。理律法律事務所電子報，2026-07。https://www.leeandli.com/TW/NewslettersDetail/7661.htm
[^aircanada]: Moffatt v. Air Canada, 2024 BCCRT 149，2024-02-14。英屬哥倫比亞省民事仲裁庭，非上級法院判例。https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada
[^wti25]: Microsoft,〈2025: The year the Frontier Firm is born〉，Work Trend Index，2025-04-23；31 國約 31,000 名知識工作者。廠商調查。https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
[^salesforce]: Salesforce FY26 Q3 財報新聞稿，2025-12-03。廠商財報，ARR 口徑由公司定義。https://www.salesforce.com/news/press-releases/2025/12/03/fy26-q3-earnings/
[^wti26]: Microsoft Work Trend Index 2026，2026-05-05。廠商數據。https://www.microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization
[^gartner]: Gartner 新聞稿，2025-06-25。屬預測與估計，非實測。https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
