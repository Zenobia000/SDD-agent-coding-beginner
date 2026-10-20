<div class="part" markdown>
<span class="kicker">第一部　判斷</span>

**公司現在在哪裡，為什麼卡住，要往哪裡去**

第 1–3 章
</div>

# 第 1 章　AI 的能力已經到位，多數企業的帳上還看不到回報

<p class="lede">用 AI 的企業很多，從 AI 拿到回報的企業很少。差距不在模型，而在企業有沒有改變工作的方式。這個差距會累積，越晚動手，要補的越多。</p>

## 近九成組織在用 AI，讓營業利益多出 5% 以上的約只有 6%

McKinsey 2025 年調查約 2,000 位企業主管：88% 的組織已經在至少一個部門用 AI，比前一年的 78% 再往上。可是把 AI 帶來的營業利益（EBIT）做到 5% 以上、而且自認有顯著價值的「高績效者」，大約只占 6%。[^mck]

BCG 同年的調查得到相近的結論：只有 5% 的企業從 AI 拿到規模化的價值，60% 幾乎看不到營收或成本上的效益。[^bcg-gap]

```exhibit
{"id": "1.1", "type": "bar", "unit": "%",
 "title": "近九成組織在用 AI，讓營業利益多出 5% 以上的約只有 6%",
 "data": [
   {"label": "至少一個部門使用 AI", "value": 88},
   {"label": "AI 貢獻 5% 以上營業利益（高績效者）", "value": 6, "highlight": true}
 ],
 "source": "McKinsey, The state of AI in 2025，1,993 位受訪者、105 國",
 "note": "高績效者：AI 貢獻 5% 以上 EBIT，且自評價值顯著"}
```

**這代表什麼**：「有沒有在用 AI」已經不是區分企業的指標，大家都在用。分水嶺在於「AI 有沒有改變公司的帳」。

## 台灣的落差更大：員工早就在用，公司還沒接手

2024 年，台灣有 84% 的知識工作者已經在工作上用生成式 AI。[^ms] 到了 2026 年，企業端的調查顯示，有 61.8% 的 AI 使用發生在公司管控之外，把 AI 整合進核心流程的企業只有 6.6%。[^aif]

```exhibit
{"id": "1.2", "type": "bar", "unit": "%",
 "title": "台灣員工早就在用 AI，把 AI 接進核心流程的企業很少",
 "data": [
   {"label": "知識工作者在工作上用生成式 AI（2024）", "value": 84},
   {"label": "AI 使用在公司管控之外（2026）", "value": 61.8},
   {"label": "企業把 AI 整合進核心流程（2026）", "value": 6.6, "highlight": true}
 ],
 "source": "Microsoft 台灣工作趨勢指數 2024；人工智慧科技基金會 2026 台灣產業 AI 化大調查（228 家企業）",
 "note": "三個數字來自不同調查、母體不同，只用來看方向，不直接相減"}
```

**這代表什麼**：台灣的問題不是員工不會用，是公司沒有接手。員工自己找工具、自己摸索，用得好的經驗留在個人身上，用出問題的風險公司也看不到。

## 有硬證據的效益集中在量大、有標準答案的工作，新手受益最多

AI 帶來生產力，這件事有嚴謹的研究支持，但效益很不平均。

最常被引用的是史丹佛與 MIT 學者對 5,179 名客服人員的研究：導入生成式 AI 助理後，每小時解決的問題平均多了 14%；資歷淺、技能較低的人多了 34%，資深人員幾乎沒有變化。[^brynjolfsson] 原因是 AI 把資深人員的做法傳給了新人。

```exhibit
{"id": "1.3", "type": "column", "unit": "%",
 "title": "AI 客服助理讓每小時解決件數平均增加 14%，新手增加 34%",
 "data": [
   {"label": "全體平均", "value": 14},
   {"label": "新手與低技能者", "value": 34, "highlight": true},
   {"label": "資深人員", "value": 0, "display": "約 0"}
 ],
 "source": "Brynjolfsson, Li & Raymond, Quarterly Journal of Economics, 2025；5,179 名客服人員"}
```

**這代表什麼**：先導入的地方，應該是工作量大、做法有標準、新人多或流動率高的單位。期待 AI 讓最資深的專家變得更強，目前證據不多。

## AI 的能力邊界參差不齊，用在邊界外反而更容易出錯

哈佛與 BCG 讓 758 名顧問隨機分組做兩類任務。[^jagged] 在 AI 擅長的任務上，用 AI 的人完成更多工作、速度快約四分之一、品質評分高約三成。到了 AI 不擅長的任務，結果反過來：

```exhibit
{"id": "1.4", "type": "column", "unit": "%",
 "title": "在 AI 不擅長的任務上，用了 AI 的顧問答對率反而下降",
 "data": [
   {"label": "沒有用 AI", "value": 84.5},
   {"label": "用 AI", "value": 70.6},
   {"label": "用 AI，且受過提示訓練", "value": 60, "highlight": true}
 ],
 "source": "Dell'Acqua 等，Organization Science 37(2)，2026；758 名 BCG 顧問",
 "note": "任務為品牌策略個案，答案需要結合訪談內容判斷"}
```

受過提示訓練的那一組錯得最多，因為他們更相信 AI 的答案。

**這代表什麼**：哪些工作交給 AI，要靠事先的判斷和事後的驗收，不能靠員工的感覺。邊界會隨著模型更新移動，所以這個判斷要定期重做。

## 覺得變快不等於真的變快，沒有基準線的試點會誤判成效

研究機構 METR 找了 16 位資深開源工程師，在 246 個真實任務上隨機決定可不可以用 AI。[^metr] 工程師事前預期 AI 會讓自己快 24%，事後也覺得快了 20%；實際量出來，用 AI 的任務慢了 19%。

```exhibit
{"id": "1.5", "type": "bar", "unit": "%",
 "title": "資深工程師覺得 AI 讓自己快了 20%，實測慢了 19%",
 "data": [
   {"label": "主觀估計的工時變化", "value": -20},
   {"label": "實際量測的工時變化", "value": 19, "highlight": true}
 ],
 "source": "METR，2025-07-10；16 位資深開發者、246 個任務的隨機對照實驗",
 "note": "相對無 AI 的工時；負值代表省時，正值代表更耗時。研究對象是熟悉自己程式碼庫的資深工程師，不代表所有人與所有工作"}
```

**這代表什麼**：靠問卷問員工「有沒有變快」，會得到過度樂觀的答案。每個試點都要先量沒有 AI 時的基準線，上線後用同一把尺再量一次。第 8 章會講怎麼量。

## 落差會累積：還在實驗與試點階段的企業，財務表現低於同業

MIT 資訊系統研究中心（CISR）把 721 家企業依 AI 成熟度分成四個階段，再比較各階段企業的財務表現。[^cisr]

```exhibit
{"id": "1.6", "type": "column", "unit": "個百分點",
 "title": "停在前兩個階段的企業營收成長低於同業，走到後兩個階段的高於同業",
 "data": [
   {"label": "① 實驗與準備（28%）", "value": -12.6},
   {"label": "② 試點與建立能力（34%）", "value": -3.5},
   {"label": "③ 發展 AI 工作方式（31%）", "value": 11.3},
   {"label": "④ AI Future Ready（7%）", "value": 17.1, "highlight": true}
 ],
 "source": "MIT CISR Enterprise AI Maturity Model，2024-12；721 家企業，括號內為各階段企業占比",
 "note": "營收成長相對同產業平均；資料來自 2022 年調查，以分析式 AI 為主；相關不等於因果"}
```

六成以上的企業還停在前兩個階段。這組資料不能證明「導入 AI 讓企業成長」，比較可能的解讀是：管理得好的企業比較早把 AI 用進工作，而 AI 又讓它們的優勢繼續擴大。

**這代表什麼**：等 AI 更成熟再開始，代價會越來越高。領先的企業每多跑一季，就多一季的流程經驗與資料，這兩樣東西買不到。

<div class="advice" markdown>
先回答三個問題，判斷你的公司在哪裡：

1. 公司裡有多少人在用 AI？其中多少是用公司提供的工具？
2. 有沒有任何一個流程，因為 AI 而重新設計過、而且量得出前後差別？
3. AI 有沒有出現在任何一個部門的 KPI 裡？

三題都答不出來，你的公司在第一階段。第 9 章有完整的自評方法。
</div>

**可帶回團隊討論**：公司買了多少 AI 授權？每週實際使用的人有多少？哪些工作因此改變，哪些只是多了一個工具？先用這三個問題盤點現況，再對照本章的市場數據。

[^mck]: McKinsey,〈The state of AI in 2025: Agents, innovation, and transformation〉，2025-11-05；1,993 位受訪者、105 國。高績效者定義為 AI 貢獻 5% 以上 EBIT 且自評價值顯著。https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025
[^bcg-gap]: BCG,〈The Widening AI Value Gap〉，2025-09-30。https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings
[^ms]: Microsoft 台灣，2024 工作趨勢指數，2024-06-20。https://news.microsoft.com/zh-tw/ms-wti-ai/
[^aif]: 人工智慧科技基金會，2026 台灣產業 AI 化大調查，228 家企業，樣本偏向較積極的企業。經理人，2026-05-04。https://www.managertoday.com.tw/articles/view/72095 ；CIO Taiwan，2026-04-30。https://www.cio.com.tw/111644/
[^brynjolfsson]: Brynjolfsson, Li & Raymond,〈Generative AI at Work〉，Quarterly Journal of Economics 140(2)，2025。https://arxiv.org/abs/2304.11771
[^jagged]: Dell'Acqua 等,〈Navigating the Jagged Technological Frontier〉，Organization Science 37(2)，2026-03；working paper 2023-09。HBS 摘要：https://aiinstitute.hbs.edu/back-to-the-beginnings-of-ai-at-work/
[^metr]: METR,〈Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity〉，2025-07-10。https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
[^cisr]: Weill, Woerner & Sebastian, MIT CISR,〈Enterprise AI Maturity Model〉，2024-12。https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian
