# 法務：契約初審省時間，對外的法律意見不能交給 AI

<p class="lede">法務的公開資料裡，失敗比成效多：專業法律 AI 工具在研究測試中仍有一到三成的題目出現幻覺，法院處理 AI 捏造引用的判決已經超過一千五百件。AI 適合做的是有公司範本可以對照的契約初審，把偏離條款標出來給人看。對外的法律意見、訴訟策略與最終條款，留給律師與法務。</p>

## 現況證據

**公開的可信成效數據很少。** Harvey 等法律 AI 工具與大型律所的使用數字，本書沒有查到可以核對的原始出處，不引用。

**研究**：史丹佛 RegLab 與 HAI 測試 Lexis+ AI 與 Thomson Reuters 的 AI 法律研究工具，在 200 多個法律問題上，幻覺率約 17% 到 33%。比通用的 GPT-4 低，但離零很遠。Thomson Reuters 抗議研究團隊測錯了產品，團隊之後補測。[^stanford]

**判決資料庫**：Damien Charlotin 整理的資料庫，到 2025 年底收錄 712 件法院處理 AI 幻覺內容的判決；[^bloomberg] 到 2026 年 6 月初，全球約有 1,545 到 1,600 件，美國約 1,058 件，每天新增約五到六件。[^unc]

**個案**：

- Mata v. Avianca：律師提交的書狀引用了至少 6 件 ChatGPT 捏造的判例，法官判罰 5,000 美元。法院最在意的是律師被指出問題後沒有更正。[^mata]
- Deloitte 澳洲為政府機關撰寫一份合約金額 44 萬澳幣的報告，內容出現捏造的判決引文與不存在的論文。修訂版補上「撰寫時使用 Azure OpenAI」的揭露，Deloitte 同意退還最後一期款項。[^deloitte]

**台灣**：行政院的生成式 AI 參考指引規定，AI 產出未經確認，不能當成行政決策的唯一依據。[^ey] 這條原則同樣適合企業法務。

**這代表什麼**：法律 AI 最大的風險是「看起來很專業的錯誤」。導入的重點在於每一個引用都能被人回查。

```exhibit
{"id": "法務 1", "type": "column", "unit": "件",
 "title": "法院處理 AI 捏造引用的判決，半年內增加一倍以上",
 "data": [
   {"label": "2025 年底", "value": 712},
   {"label": "2026 年 6 月初", "value": 1570, "display": "約 1,545–1,600", "highlight": true}
 ],
 "source": "Damien Charlotin AI 幻覺判例資料庫，經 Bloomberg Law（2025-12-29）與 UNC Law Library（2026-06）報導",
 "note": "全球累計件數；柱高以區間中點繪製；只計入被收錄的判決"}
```

## 先做這一件

**先做標準契約的初審：AI 對照公司的標準條款範本，把保密協議、採購合約裡偏離範本的條款標出來，附原文位置與風險等級建議，由法務決定怎麼改。**

保密協議和一般採購合約量大，公司通常已經有範本，這就是標準答案。AI 只負責找出「哪裡不一樣」，判斷能不能接受仍然由人做。初審時間與漏判率都量得到。

怎麼做：

1. 先把公司對常見條款的立場寫下來：保密期間、責任上限、管轄法院、智財歸屬，各自的可接受範圍與底線。這份文件常被稱為條款手冊。
2. AI 只輸出偏離清單，每一項附原文位置與對應的條款手冊條目，不直接改寫合約。
3. 法務照常審完，記錄 AI 漏掉的偏離與誤標的條款。
4. 漏判率連續穩定在你訂的門檻以下，再考慮讓業務或採購對低風險合約先自己跑一次初審。

怎樣算成功：每份合約的初審時間下降，法務複審發現的漏判件數維持在門檻以下，業務等待法務回覆的天數縮短。

## 不能交給 AI 的決策

| 決策 | 為什麼 | 依據 |
|---|---|---|
| 對外的法律意見 | 意見出去就是公司或律師的責任 | Mata v. Avianca；Deloitte 澳洲退款 [^mata] [^deloitte] |
| 訴訟策略 | 需要判斷對方、法院與商業目標 | 屬無法回溯驗證的判斷 |
| 和解決定 | 牽涉金錢、聲譽與先例 | 屬對外具法律效力的承諾 |
| 合約的最終條款 | 簽下去就是公司的義務 | 同上 |
| 任何判例與條文的引用 | 專業工具仍有一到三成的題目出現幻覺 | 史丹佛 RegLab／HAI 研究 [^stanford] |

## 加 AI 還是重建

**在既有工具加 AI**：Lexis+ AI、Thomson Reuters 等法律資料庫已經內建 AI 研究功能，文件管理與合約管理系統也陸續加上摘要與條款比對。前提是你清楚它的錯誤率，並且規定每個引用都要人工回查原文。研究顯示，專業工具的幻覺率比通用工具低，但不是零。[^stanford]

**用 AI 重新設計流程**：把標準契約改成自助流程。業務或採購用公司範本起草，AI 檢查有沒有偏離，只有偏離的合約才進法務。法務的工作從「每份都看」變成「看例外」。前提是公司已經有寫成文字的條款手冊，而且主管同意「沒有偏離的低風險合約可以不經法務」這個授權。沒有這兩項，自助流程只會把風險搬到業務身上。

## 雷區

**引用沒有回查。** Mata 案與 Deloitte 案都是這一步沒做。[^mata] [^deloitte] 規定很簡單：每一個判例、條文、文獻，都要有人打開原文確認過，才能出現在對外文件裡。

**合約與案件資料放進未經核准的工具。** 合約常有保密條款，訴訟資料更敏感。Samsung 在 2023 年因工程師把原始碼與會議紀錄貼進 ChatGPT，暫時禁用生成式 AI。[^samsung] 法務用的 AI 工具要先確認資料不會被拿去訓練、留存可控。

**把 AI 初審當成「已經審過」。** AI 的偏離清單是給人看的起點。合約系統裡要分清楚「AI 初審完成」和「法務審核完成」兩個狀態，避免有人看到前者就簽約。

**對外文件沒有揭露 AI 的使用。** Deloitte 的修訂版事後才補上揭露。[^deloitte] 對客戶或主管機關的報告，事先決定什麼情況要揭露。

## 該量的三個指標

| 指標 | 怎麼量 | 多久看一次 |
|---|---|---|
| 每份合約的初審時間 | 從收件到初審完成，對照導入前同類合約 | 每月 |
| 漏判率 | 法務複審發現、AI 沒有標出的偏離條款數 ÷ 總偏離條款數 | 每兩週 |
| 業務等待法務回覆的天數 | 合約管理系統或請求單紀錄 | 每月 |

<div class="advice" markdown>
法務主管在導入任何 AI 之前，先花一週把條款手冊寫出來。這份文件沒有 AI 也有用，新進法務審約時有依據可以對照。有了它，AI 初審才有標準可以對照，漏判率也才算得出來。
</div>

[^stanford]: Stanford HAI，2024-05。https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries ；LawNext，2024-05。https://www.lawnext.com/2024/05/stanford-will-augment-its-study-finding-that-ai-legal-research-tools-hallucinate-in-17-of-queries-as-some-raise-questions-about-the-results/
[^bloomberg]: Bloomberg Law，2025-12-29。https://news.bloomberglaw.com/legal-ops-and-tech/ai-faked-cases-become-core-issue-irritating-overworked-judges
[^unc]: UNC Law Library,〈Handling Hallucinations: A Reflection on the Last Three Years〉，2026-06。https://library.law.unc.edu/2026/06/handling-hallucinations-a-reflection/
[^mata]: Mata v. Avianca, Inc.（SDNY，2023-06-22）。https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.
[^deloitte]: AP，經 CTV News 轉載，2025-10。https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
[^ey]: 行政院及所屬機關（構）使用生成式 AI 參考指引，2023-08；自由時報，2023-09。https://ec.ltn.com.tw/article/paper/1602420
[^samsung]: Forbes Australia，2023-05-02。https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/
