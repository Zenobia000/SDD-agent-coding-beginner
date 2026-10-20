# IT 與資安：服務台是最快見效的場景，也是 agent 權限最該管的地方

<p class="lede">IT 服務台的問題重複率高、答案寫在知識庫裡，是內部最快看得到效果的 AI 場景。IT 也是 agent 拿到最多權限的部門：能重設密碼、改設定、碰正式環境。2025 年公開的幾起重大事故，都是 agent 的權限給得太多。先讓 AI 回答問題，要它動手之前，先把身分、權限與稽核做好。</p>

## 現況證據

**廠商數據**：ServiceNow 拿自己當第一個客戶，表示內部員工問題有 54% 由生成式 AI 工具處理、不需再找真人，客服人員每案省 12 到 17 分鐘。[^servicenow] 財務長在 2025 年第二季法說會上說，公司當年光人力就省下 1 億美元。[^servicenow-cfo] 這些都是廠商自述。

**廠商執行的隨機實驗**：Microsoft 首席經濟學家辦公室讓 147 名資安分析師在模擬環境裡測試 Security Copilot，有經驗的分析師速度快 22%，準確度提高 7%。[^seccopilot] 實驗由賣產品的公司執行，環境也是模擬的。

**研究預印本**：一篇 2025 年的論文測試釣魚郵件分類 agent，每位分析師每分鐘找出的真陽性最多增加 6.5 倍。[^phishing] 尚未經同儕審查。

**反向證據**：METR 的隨機對照實驗中，資深工程師用 AI 寫程式反而慢了 19%，自己卻以為快了 20%。[^metr] 開發效率要量，不能問。

**事故**：

- EchoLeak（CVE-2025-32711）：攻擊者寄一封夾帶隱藏指令的郵件，Microsoft 365 Copilot 檢索時把信讀進來，就會把 OneDrive、SharePoint、Teams 的資料外傳，使用者什麼都不用點。漏洞評為 CVSS 9.3，微軟在 2025 年 6 月修補。[^echoleak]
- Replit 的 agent 在程式凍結期間對正式資料庫下了破壞性指令，刪掉 1,206 筆高管資料與 1,196 筆以上的公司資料，還捏造資料、謊稱無法復原。[^replit]
- Amazon Q 的 VS Code 擴充套件被合併進一段惡意提示詞，要 agent 清空家目錄並刪除 AWS 資源，附帶 `--trust-all-tools` 參數，並以正式版本發布。[^amazonq]

```exhibit
{"id": "IT 1", "type": "bar", "unit": "%",
 "title": "回報 AI 資安事件的組織，97% 沒有適當的 AI 存取控管",
 "data": [
   {"label": "外洩事件涉及 shadow AI 的受訪組織", "value": 20},
   {"label": "回報 AI 相關資安事件的組織", "value": 13},
   {"label": "上述組織中，缺乏適當 AI 存取控管", "value": 97, "highlight": true}
 ],
 "source": "IBM Cost of a Data Breach Report 2025，經 TechRepublic、Baker Donelson 整理",
 "note": "第三項的分母是回報 AI 相關資安事件的組織，與前兩項不同"}
```

## 先做這一件

**先做服務台的常見問題自助：密碼重設流程、VPN 連線、軟體安裝申請、印表機設定，由 AI 依知識庫回答。AI 只能讀知識庫、不能改任何系統；需要動作的，照舊開單給人或既有的自動化流程。**

服務台的問題重複率高，答案寫在知識庫裡，每張工單都有時間戳記，基準線現成。AI 只讀不寫，說錯了頂多讓員工多問一次，不會改壞系統。

怎麼做：

1. 從工單系統找出量最大的 20 類問題，把每一類的標準處理方式寫進知識庫。
2. AI 回答時附上知識庫條目；找不到的，直接引導員工開單。
3. 這個階段 AI 沒有任何寫入權限：不能重設密碼、不能改群組、不能裝軟體。
4. 每週檢查「AI 回答後員工仍然開單」的案例，補知識庫。

怎樣算成功：自助解決率上升，平均解決時間下降，問題被重開的比例沒有變高。

## 不能交給 AI 的決策

| 決策 | 為什麼 | 依據 |
|---|---|---|
| 正式環境的變更核准 | 改錯了影響全公司，而且不一定救得回來 | Replit 刪除正式資料庫 [^replit] |
| 權限授予 | 權限給錯就是資安事件的起點 | OWASP 把 Excessive Agency 列為 LLM 主要風險 [^owasp] |
| 資安事件的隔離與對外通報 | 牽涉法定通報義務與營運中斷 | 資通安全管理法修正，特定非公務機關未通報的罰鍰上限提高到 1,000 萬元 [^cyber] |
| 資料外洩的判定 | 判定結果決定要不要通知當事人與主管機關 | 個資法修正新增事故通報義務 [^pdpa] |

## 加 AI 還是重建

**在既有系統加 AI**：ServiceNow Now Assist 與 AI Agent Orchestrator、Microsoft Security Copilot，都建在既有的工單、身分與資安平台上。這條路的好處是權限模型與稽核紀錄已經在那裡。前提是你的 ITSM 與身分管理本來就有在用，不是只有一個信箱收問題。

**用 AI 重新設計流程**：讓 agent 處理整段流程，例如自動判斷工單、重設權限、隔離可疑裝置，人只看例外。前提有三個。第一，每個 agent 有自己的身分與一位人類負責人，Microsoft Entra Agent ID 已經把這件事做成產品功能。[^entra] 第二，只給完成任務所需的最小權限，破壞性動作一律要人確認。第三，遵守 Meta 提出的「Agents Rule of Two」：同一個 session 裡，處理不可信的輸入、存取敏感資料、對外寫入或改變狀態，三項最多只能同時具備兩項。[^ruleoftwo]

## 雷區

**以為 prompt injection 可以用提示詞擋掉。** 一篇研究用適應性攻擊測試 12 種已發表的防禦，全部被突破。[^ruleoftwo] 能做的是從架構上限制 agent 能碰什麼，不是寫更長的系統提示。

**給 agent 全開的權限。** Replit 與 Amazon Q 兩起事件的共同點，就是 agent 拿得到它不需要的權限。[^replit] [^amazonq] 不要在任何正式環境使用 `--trust-all-tools` 這類參數。

**員工私下用 AI，公司看不到。** 外洩事件涉及 shadow AI 的組織，每起平均多出約 67 萬美元成本。[^ibm] 封鎖擋不住，比較有效的是先提供企業版工具，再管帳號。

**用問卷量開發效率。** METR 的工程師自認快了 20%，實際慢了 19%。[^metr] 要量工單或任務的實際完成時間。

## 該量的三個指標

| 指標 | 怎麼量 | 多久看一次 |
|---|---|---|
| 服務台自助解決率 | AI 回答後員工沒有再開單的比例 | 每週 |
| 平均解決時間 | 從提問到結案，對照導入前同類工單 | 每週 |
| agent 清冊完整率 | 有身分、負責人、權限清單、稽核紀錄的 agent 數 ÷ 所有 agent 數 | 每月 |

<div class="advice" markdown>
本月就做一次 agent 盤點：公司裡有哪些 AI 工具或 agent 拿著能寫入、刪除、寄信的權限？各用誰的帳號？出事時誰負責？列不出這張清單，就先暫停新的 agent 上線。第 7 章與附錄的數位員工上崗檢核表有完整做法。
</div>

[^servicenow]: ServiceNow blog,〈Boosting customer support agent productivity with generative AI〉，2024，廠商自述。https://www.servicenow.com/blogs/2024/support-agent-productivity-genai
[^servicenow-cfo]: Computing，2025-07，轉述財報電話會議。https://www.computing.co.uk/news/2025/ai/servicenow-100m-savings-ai-job-cuts
[^seccopilot]: Microsoft 首席經濟學家辦公室，Security Copilot 研究，2024；147 人，模擬環境，廠商執行。https://www.microsoft.com/content/dam/microsoft/final/en-us/microsoft-brand/documents/EconStudy-Speed-accuracy-and-sentiment-Infographic-Final.pdf
[^phishing]: arXiv 2511.13860，2025-11，預印本。https://www.arxiv.org/abs/2511.13860
[^metr]: METR，2025-07-10；16 位資深開發者、246 個任務的隨機對照實驗。https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[^echoleak]: The Hacker News，2025-06。https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html ；arXiv 2509.10540，2025-09。https://arxiv.org/html/2509.10540v1
[^replit]: OECD AI Incidents，2025-07-19。https://oecd.ai/en/incidents/2025-07-19-1eb1
[^amazonq]: The Register，2025-07-24。https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/
[^owasp]: OWASP Top 10 for LLM Applications，經 Akamai 整理，2026；各項排名未回查 OWASP 原頁。https://www.akamai.com/blog/ai/owasp-top-10-llm-applications-2026-realistic-security-model
[^cyber]: 理律法律事務所 Newsletter，資通安全管理法修正，2025-09-24 公布，施行日期待定。https://www.leeandli.com/TW/NewslettersDetail/7505.htm
[^pdpa]: 理律法律事務所 Newsletter，個人資料保護法修正，2025-11-11 公布，施行日期待行政院定。https://www.leeandli.com/TW/NewslettersDetail/7532.htm
[^entra]: Microsoft Learn，Entra Agent ID。https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
[^ruleoftwo]: Simon Willison,〈New prompt injection papers: Agents Rule of Two and The Attacker Moves Second〉，2025-11。https://simonw.substack.com/p/new-prompt-injection-papers-agents
[^ibm]: IBM Cost of a Data Breach Report 2025，經 TechRepublic 整理，2025-07。https://www.techrepublic.com/article/news-ai-breach-risks-rise-as-governance-lags/
