# 第 3 章　AI-Native 企業以 AI 為前提重新設計工作，在舊流程上加工具只是起點

<p class="lede">AI-Native 說的是工作的設計方式，和用了多少工具無關：哪些事交給 AI、哪些事留給人、資料從哪裡來、結果怎麼驗收，都在流程設計時就決定好。大企業、中小企業、新創的起點不同，但要走的方向一樣。</p>

## 判斷標準只有一個：拿掉 AI，這套工作方式還成立嗎

AI-Native 目前沒有權威機構的統一定義。業界最常用的判斷方法很簡單：把 AI 拿掉，這套工作方式還說得通嗎？說得通，AI 就是外掛的功能；說不通，AI 才是工作的一部分。[^leanware] McKinsey 用「agentic organization」描述同一件事：以 AI 為前提重建工作流程，人與 AI agent 在同一個團隊裡分工。[^mck-agentic]

用兩個問題可以把企業的 AI 應用分成四類：流程有沒有重新設計？AI 在流程裡是輔助還是前提？

```exhibit
{"id": "3.1", "type": "matrix",
 "title": "沒有重新設計流程就讓 AI 接手，是最常翻車的一格",
 "x": {"label": "流程", "low": "沿用舊流程", "high": "重新設計"},
 "y": {"label": "AI 的角色", "low": "輔助", "high": "前提"},
 "cells": [
   {"title": "硬接手", "text": "流程沒改，直接讓 AI 取代人做其中一段。品質與責任問題最常在這裡爆發"},
   {"title": "AI-Native", "text": "以 AI 為前提重新設計分工、資料與驗收。回報集中在這一格", "highlight": true},
   {"title": "個人工具", "text": "員工自己用聊天工具，公司看不到、也接不住。多數企業在這裡"},
   {"title": "流程改善", "text": "重新設計流程，AI 負責其中幾個步驟。走向 AI-Native 的必經之路"}
 ],
 "source": "桑尼資料科學整理"}
```

多數企業停在左下角。從左下直接跳到左上（流程不改、直接讓 AI 接手）最誘人，因為看起來省最多人力；第 4 章的 Klarna 和澳洲聯邦銀行都是在這一格付了學費。比較穩的路線是先往右走：先把流程重新設計，再逐步讓 AI 承擔更多。

## 有回報的企業重新設計流程的比例，約是其他企業的 3 倍

McKinsey 比較了 AI 高績效者和其他企業的做法，在所有測試過的因素裡，「從根本重新設計工作流程」是和營業利益影響關聯最強的因素之一。高績效者這樣做的機率，約是其他企業的 3 倍；在多數部門裡，它們正在擴大使用 AI agent 的機率也至少是其他企業的 3 倍。[^mck]

```exhibit
{"id": "3.2", "type": "bar",
 "title": "AI 高績效者從根本重新設計流程的機率，約是其他企業的 3 倍",
 "data": [
   {"label": "其他企業", "value": 1, "display": "基準"},
   {"label": "AI 高績效者", "value": 3, "display": "約 3 倍", "highlight": true}
 ],
 "source": "McKinsey, The state of AI in 2025；約 2,000 位受訪者",
 "note": "以其他企業為基準的相對倍數"}
```

**這代表什麼**：預算的重點應該放在「改流程」，不是「買工具」。工具三個月就會被下一代取代，重新設計過的流程與累積下來的資料會留在公司裡。

## AI-Native 企業有五個共同做法，每一個都看得到、量得到

我們把研究與公開個案裡反覆出現的做法，歸納成五項。每一項都可以在公司裡直接觀察，也都對應後面的一個決策。

| 做法 | 看得到的樣子 | 依據 | 對應 |
|---|---|---|---|
| **人機分工寫進流程** | 流程圖上標明每一步由人、由 AI，還是由 AI 做、人審 | 高績效者重新設計流程的機率約 3 倍 [^mck] | 第 5 章 |
| **資料隨工作產生** | 每完成一件工作，就留下 AI 下次用得上的資料，不需要另外整理 | 複雜任務常卡在拿不到資訊 [^anthropic] | 第 5 章 |
| **數位員工有身分** | 每個 AI agent 有自己的帳號、權限與一位負責人 | Microsoft、Workday 已把 agent 當員工管理 [^agentid] | 第 7 章 |
| **執行權下放，問責集中** | 第一線可以試，每個專案有一位對結果負責的主管 | 能跨過試點的企業普遍這樣做 [^nanda] | 第 6 章 |
| **量測內建** | 上線前就定好基準線與驗收標準，AI 的表現自動被記錄 | 60% 的企業沒有任何 AI 財務指標 [^bcg-kpi] | 第 8 章 |

以下五項是本指南整理的工作假設，適合拿來檢視企業流程；它們是本指南的分析框架，不代表已由桑尼資料科學的多家客戶案例驗證。

## 同樣喊 AI-first，三家公司走出三種結局，差在人力政策和品質底線

2025 年前後，許多企業的執行長發出「AI-first」內部信。內容相近，結果差很多。

| | Shopify | Duolingo | Klarna |
|---|---|---|---|
| **做法** | 申請加人前，先說明為什麼 AI 做不到；AI 使用納入績效評核 [^shopify] | 逐步停止讓約聘人員做 AI 能做的事；招募與考核看 AI 使用 [^duolingo] | 宣稱 AI 客服相當於 700 名人力，凍結非工程招募 [^klarna] |
| **對人的影響** | 不裁員，靠自然流失，員工數一年少約 6% | 正職未裁，約聘減少 | 以凍結招募與自然流失為主 |
| **反應** | 反彈小 | 用戶與社群強烈反彈，執行長兩度出面澄清 | 品質下降，執行長承認「太看重成本」 |
| **結果** | 人數穩定下降，業務持續成長 | 一年上線 148 門新課；用戶成長放緩，但與 AI-first 的因果未證實 | 改回保證客戶隨時找得到真人 |

三家都在用 AI，差別在兩件事：**人力政策是「控制增量」還是「削減存量」**，以及**有沒有先定好品質底線**。第 4 章會把這兩件事寫成具體做法。

## 大企業、中小企業、新創的起點不同，各有一條最短的路

企業規模不同，AI 採用率差很多。OECD 統計，大企業的 AI 使用率約 40%，小企業約 11.9%；[^oecd] 美國人口普查局的資料也顯示，250 人以上的企業有 37% 在用，4 人以下的不到兩成。[^census] OECD 同時提醒，控制了既有的數位能力之後，用 AI 的企業生產力優勢會大幅縮小，也就是說，本來數位化做得好的企業，才比較容易從 AI 得到好處。

```exhibit
{"id": "3.3", "type": "bar", "unit": "%",
 "title": "大企業的 AI 使用率約是小企業的三倍以上",
 "data": [
   {"label": "大企業", "value": 40},
   {"label": "小企業", "value": 11.9, "highlight": true}
 ],
 "source": "OECD，AI adoption by small and medium-sized enterprises，2025-12"}
```

| | 大企業 | 中小企業與傳統產業 | 新創 |
|---|---|---|---|
| **優勢** | 資料、資本、客戶信任；可以先拿自己當第一個客戶 | 決策鏈短，老闆一句話就能改流程；現成軟體已內建 AI | 從第一天就以 AI 為前提設計流程與人力 |
| **常見陷阱** | 試點最多、上線最慢；對外宣言溝通不當引發反彈 | 資料還沒數位化；沒有 AI 人才；不知道從哪裡開始 | 營收成長快，但模型成本侵蝕毛利 |
| **最短的路** | 選一個核心流程徹底重新設計，用「控制增量」的人力政策，先建 agent 治理 | 先把一個流程數位化，挑一個量大、有標準答案的後勤工作，用平台內建的 AI | 維持小團隊，讓產品本身承載 AI 的槓桿，及早證明獲利 |

新創的人均產值確實驚人：瑞典的 Lovable 以 45 名全職員工、上線八個月達到年化營收 1 億美元；[^lovable] Gamma 以約 50 人做到年化營收 1 億美元並且獲利。[^gamma] 這些數字是公司自己公布的年化營收，不是經過審計的財報。大企業無法直接複製這樣的人數比例，可以學的是它們設計工作的方式：工程師用 AI 寫大部分的程式，中階管理層很少，產品本身就是 AI 的槓桿。

**討論題**：請挑一個你熟悉的企業或部門，對照上面的五項做法，找出它最成熟的一項，以及下一個最該補強的地方。這是分析練習，不是本團隊的客戶案例。

[^leanware]: Leanware,〈What is an AI-native company〉，未標日期，屬業界觀點。https://leanware.co/insights/ai-native-companies-definition-strategic-framework
[^mck-agentic]: McKinsey,〈The agentic organization: Contours of the next paradigm for the AI era〉，2025。https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era
[^mck]: McKinsey,〈The state of AI in 2025: Agents, innovation, and transformation〉，2025-11-05；1,993 位受訪者、105 國。高績效者定義為 AI 貢獻 5% 以上 EBIT 且自評價值顯著。https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025
[^anthropic]: Anthropic Economic Index，2025-09-15。https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
[^agentid]: Microsoft Learn，Entra Agent ID。https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id ；TechCrunch，Workday agent 管理平台，2025-02-11。https://techcrunch.com/2025/02/11/workday-launches-a-platform-for-enterprises-to-manage-all-of-their-ai-agents-in-one-place
[^nanda]: MIT NANDA,〈The GenAI Divide: State of AI in Business 2025〉，受訪者自述。https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
[^bcg-kpi]: BCG，2025-01，1,803 位高階主管。https://www.bcg.com/press/15january2025-ai-optimism-autonomous-agents
[^shopify]: TechCrunch，2025-04-07。https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/ ；員工數 2024 年底約 8,100 人、2025 年底約 7,600 人，依 Shopify 向 SEC 申報之年報（10-K）。
[^duolingo]: Mind the Product，2025-04-28。https://www.mindtheproduct.com/duolingo-announces-ai-first-strategy/ ；Fortune，2025-08-18。https://fortune.com/2025/08/18/duolingo-ceo-admits-controversial-ai-memo-did-not-give-enough-context-insists-company-never-laid-off-full-time-employees ；148 門課依公司財報轉述，Nasdaq，2026。https://www.nasdaq.com/articles/duolingos-ai-first-strategy-data-secures-dominance-ed-tech
[^klarna]: Klarna 新聞稿，2024-02-27。https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ ；Fortune，2025-05-09。https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/
[^oecd]: OECD,〈AI adoption by small and medium-sized enterprises〉，2025-12，經第三方託管之 PDF。https://assets.geteasy.ai/internal/files/oecd-report-ai-adoption-by-small-and-medium-sized-enterprises.pdf
[^census]: U.S. Census Bureau，2026-05。https://census.gov/library/stories/2026/05/ai-use-businesses.html
[^lovable]: TechCrunch，2025-07-23。https://techcrunch.com/2025/07/23/eight-months-in-swedish-unicorn-lovable-crosses-the-100m-arr-milestone
[^gamma]: The Next Web。https://thenextweb.com/news/gamma-grant-lee-profitable-ai-startup
