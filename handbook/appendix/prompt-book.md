# 課堂提示詞

D1 在獨立練習資料夾；D2 在 LeaveBot 根目錄。

# D1 通用操作提示詞

## d1-read｜唯讀認識練習資料夾
```text
只讀目前練習資料夾，告訴我已有什麼、如何在瀏覽器開啟。這是D1獨立練習，不是LeaveBot；不修改檔案，不讀其他專案資料。
```

## d1-1｜一次提示做作品
```text
請直接完成我接下來貼的題目，使用目前獨立資料夾。遵守題目附的素材、時間與驗收要求；不要只寫計畫。由我計時，允許你自行執行與修正，未驗證事項如實回報。
```

## d1-2｜補上下文再比較
```text
在另一個新資料夾做同一題，沿用相同時間、工具與模型。本次新增的參考圖、素材和明確限制如下：＜填入＞。不要讀第一版原始碼。完成後與第一版按相同條件比較，記下這次變動了哪些輸入。
```

## d1-3｜修一個問題
```text
我看到：＜實際畫面或重現步驟＞。我期待：＜可觀察的結果＞。
先找出差異與原因，再只修這一件事。實際開啟並驗證；沒有瀏覽器工具就列出我要操作的步驟，不假裝已通過。
```

## d1-4｜回顧 AI 自行做的假設
```text
列出這次作品裡我沒有明確指定、由你自行決定的事項。每項附畫面或檔案依據，讓我選擇保留、修改或不做。這一步只討論，不修改檔案；等我確認再整理PRD。
```

## d1-5｜今天收斂到 PRD
```text
根據剛才已確認的決策，將這個作品整理成目前練習資料夾內的 prd.md。
包含目標使用者、問題、核心流程、這次做與不做的範圍、至少三條 Given/When/Then 驗收條件（至少一條失敗情境）與待決事項。
這是D1簡版，不使用LeaveBot專案模板或公司規則。不補未確認需求，不寫程式，不畫流程圖。
```

# 卡 A｜需求訪談與 Brief

技能：`grill-with-docs`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/grill-with-docs
先讀 @AGENTS.md、@course/WORKFLOW.md、@course/LEAVEBOT.md。
這是第二天表單主線。依 @course/templates/01-brief.md 協助我們整理最小 Brief。
已固定的技術與功能不重問；訪談只聚焦理由是否必填與長度、過去日期、重複送出回饋，最多兩輪。
每題給建議，等我們回答，不自行定案。課堂建議是理由選填最多200字、接受過去日期、不自動去重但送出期間鎖住按鈕；只有我們確認後才採用。
共識確認後寫 docs/01-brief.md，三項決策附在同檔。未決且影響核心流程時明列並由講師決定，不開始寫程式。
```

# 卡 B｜寫成最小 PRD

技能：`to-spec`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/to-spec
依 @course/WORKFLOW.md、@docs/01-brief.md 與剛才已確認的決策，使用 @course/templates/02-prd.md 產出 docs/02-prd.md。
只處理 PRD：2–3個故事、AC不超過10，至少涵蓋成功送出、拒絕輸入不存檔、查看自己的假單。已確認的理由、日期與重複送出規則要寫得可判斷。
不加入主管核准、額度或LLM解析。不建立尚未進行的SRS與設計文件。
不要替我們補未決問題；完成後列出需要人工審查的AC。
```

# 卡 C｜從 AC 到系統規則

技能：`to-spec`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/to-spec
讀 @course/LEAVEBOT.md、@docs/02-prd.md，依 @course/templates/03-srs.md 產出 docs/03-srs.md。
每條FR引用AC；FR不超過10。確認必填、合法員工與假別、反向日期、半天限單日工作日、扣週末、零工作日拒絕、pending狀態由後端決定，以及員工列表隔離。
產品細節依已確認決策；出現矛盾就列出，不擅自選邊。
不重建PRD、不寫程式。列出未被SRS承接的AC。
```

# 卡 D｜用 Archify 檢查流程

技能：`archify`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/archify
讀 @docs/03-srs.md，把員工提交請假的流程畫成 workflow，輸出 diagrams/submit-leave.html，保留來源候選檔與工具實際驗證結果。
包含選員工、填表、送出、後端驗證、錯誤回饋且不存檔、存成pending、我的假單顯示結果。只畫SRS裡已定的行為，不自行加核准或LLM。
使用本repo的Archify工具與交付流程。完成後回報實際檔案路徑與通過／未通過的檢查。
若Node、工具或瀏覽器條件不足，明確回報原因，改在 docs/03-srs.md 的流程圖區寫 Mermaid；不要假裝已產出HTML。
我們會對照SRS逐一審圖，未確認前不修改需求。
```

# 卡 E｜最小 SAD 與 SDS

技能：`to-architecture`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/to-architecture
讀 @docs/02-prd.md、@docs/03-srs.md、@course/STACK.md 與剛才確認的流程。
依 @course/templates/04-sad.md、@course/templates/05-sds.md 產出 docs/04-sad.md、docs/05-sds.md。
系統固定為FastAPI提供HTML/CSS/原生JavaScript、後端API、SQLite。定清員工資料、送出與依員工列出假單的API，包含錯誤碼、資料欄位與公開模組接縫。
寫清天數由程式算、pending不能由客戶端指定、測試資料庫與固定時鐘的注入方式；先登記API最後掛靜態頁。
有真正取捨才寫ADR，不湊圖或文件篇幅。核心決策未定先問，不寫程式。回報沒有設計落點的FR/NFR。
```

# 卡 F｜測試計畫與人工預期結果

技能：`to-test-plan`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/to-test-plan
讀 @docs/02-prd.md 至 @docs/05-sds.md，依 @course/templates/06-test-plan.md 建立 docs/06-test-plan.md。
先提出6–12個代表TC供我們審預期結果：成功、必填、反向日期、半天、週末、員工隔離、狀態與天數不信任客戶端。預期值來自規格與人工算例，不呼叫實作函式計算答案。
案例以API驗收與必要單元測試為主，另列人工畫面流程。沒有測試證據先標未執行。
這次沒有LLM功能，不建立模型eval或注入評測。
若風險無法在案例預算內覆蓋，指出缺口讓講師決定範圍。人確認後才寫入。
```

# 卡 G｜拆骨架與表單兩張票

技能：`to-tickets`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/to-tickets
依 @course/WORKFLOW.md、@docs/05-sds.md、@docs/06-test-plan.md，按今天的時間拆兩張主線票：
issues/000-skeleton.md：照STACK建立套件、FastAPI、靜態首頁、GET /api/health與health測試，不寫請假邏輯。
issues/001-submit-leave.md：表單→後端驗證→SQLite→我的假單，逐個TC做TDD。
每張寫成果、TC或骨架檢查、驗收指令、所讀規格段落與真正依賴；業務TC歸001。列出建置前提與估計大小，若兩張的範圍過大先報告。
只規劃基本範圍；進階挑戰由我們要求後另開票。先給我們審清單，再寫檔。
建立 docs/LESSONS.md（依同名模板）並在AGENTS.md的本專案段補已確認的必要規則，不覆蓋原有課程邊界。
```

# 卡 H｜一張票一個對話，逐個行為實作

技能：`implement`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/implement
先完成 @issues/000-skeleton.md，遵守 @AGENTS.md 與 @course/STACK.md。使用專案虛擬環境，讓首頁讀到 /api/health，跑health測試，實際啟動並回報網址。這一步不寫請假邏輯，完成後停止，等待我們驗收。

```

骨架驗收後，另開新對話再貼第二段：

```text
/implement
讀 @issues/001-submit-leave.md 與它引用的規格。依 /tdd 一次一個行為，第一個業務測試先跑出預期原因的紅燈，停下讓我們確認，再做綠燈。後續按同樣循環完成。
每個測試標TC與需求編號；資料庫用暫存位置。不能改測試放寬條件。完成後跑完整pytest、操作核心流程、回填追溯表與實際偏差。
Windows用 .venv\Scripts\python.exe；macOS/Linux用 .venv/bin/python。不假裝已啟用虛擬環境。
不要自動commit或push，未驗證項明確列出。
```

# 卡 I｜有證據的除錯

技能：`diagnosing-bugs`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/diagnosing-bugs
先讀 @AGENTS.md 與 @docs/06-test-plan.md。以下是本組的失敗指令、完整輸出與重現步驟：
＜貼真實錯誤；沒有就先由講師在獨立練習分支製造可還原的錯誤，不憑空假設＞
先分清環境問題、規格矛盾或實作錯誤。建立能穩定重現的檢查，一次只驗一個原因。
修實作前讓我們看到失敗證據，修復後跑相關與完整測試。不得放寬測試以求通過。
記錄原因、修改與實際結果，不能重現或未驗證就如實標明。
```

# 卡 J｜變更需求先分析影響

技能：`grill-with-docs`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/grill-with-docs
變更需求：將理由長度上限從200字改為100字（若本組原本不同，先指出差異並由講師確認）。
讀 @docs/02-prd.md 至 @docs/06-test-plan.md，先列出受影響的AC、FR、API驗證、畫面、TC與程式位置。這一步先不改程式，讓我們確認。
確認後更新規格與案例，建立 issues/002-reason-limit.md。再由我們另開新對話，以 /implement 執行這張變更票。
要先新增101字理由會被拒絕且不存檔的測試，看它在舊實作失敗，再改程式。原本有效的測試仍須通過；若測試期待因規格變更需修訂，先列明依據由人確認。
```

# 卡 K｜交付檢查與操作展示

技能：`code-review`。先讀 [WORKFLOW](../WORKFLOW.md)，只處理這個階段。

```text
/code-review
審查本組指定的工作範圍：＜填基準SHA／分支，或明確指定目前已暫存及未暫存的改動＞。
對照 @AGENTS.md、已確認規格、工作票與 @docs/06-test-plan.md，分別檢查規範與需求是否做到。
執行完整pytest；實際走一次成功送出、拒絕不存檔、重新整理及換員工流程；沒瀏覽器工具就列給我們人工操作，不宣稱已驗證。
抽查一條AC→FR→API→TC→測試斷言與結果，檢查沒有金鑰或資料庫被加入版控。
在 docs/DELIVERY.md 記錄啟動指令、實際環境版本、測試與人工驗收證據、未完成項。修正阻擋交付的問題後再驗證。
先給出審查結果，不自行commit或push；由小組確認並明確加入本次檔案保存版本。
```
