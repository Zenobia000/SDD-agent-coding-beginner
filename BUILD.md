# SmartTrip FX：跟著 Google Antigravity 做出一支能算旅費、有測試保護的小程式

這是本課第二冊，也是 SmartTrip FX 專案實戰唯一要照著走的文件。請先完成 [`ANTIGRAVITY.md`](./ANTIGRAVITY.md) 的官方元件速成，再回到這裡。你不需要先會寫程式，也不用自己決定題目或技術——本書只做同一題、走同一路、用同一組驗收標準。你要做的事很單純：**複製、貼上、執行、跟答案核對**。

看不懂某個英文詞沒關係，這份文件會在第一次出現時，用括號附上白話說明；只要看得懂括號裡的話，就能繼續往下做。

## 完成品

```text
AI 或人產生行程 JSON
          ↓
   schema 與輸入驗證
          ↓
程式計算現金 + 匯率燈號
          ↓
     terminal 輸出結果
```

你可以把它想成兩個角色分工：**AI 是那個很懂行程、幫你猜「這一攤大概要付現金」的朋友**；**程式是六親不認、只認數字的會計**，負責把朋友的猜測換算成明確的金額和燈號。AI 負責「哪些行程可能需要現金」這種判斷；程式負責加總、比例、門檻跟錯誤處理。這條分工邊界，是全書唯一要記住的核心規則。

## 在開始之前：四個你會一直看到的詞

- **終端機（Terminal）**：一個只能打字、電腦馬上照做的視窗，跟平常用滑鼠點資料夾不一樣。這本書所有指令都在這裡打。
- **執行一個命令**：把一行文字打進終端機、按 Enter，電腦就會照那行字做事，然後把結果印給你看。
- **JSON**：一種電腦看得懂的清單寫法，用 `{ }` 包資料、用 `,` 分隔欄位。第 5 章會看到實際範例，看過一次就懂。
- **Antigravity 與 `agy`**：Antigravity 是 Google 的 AI coding agent。它有兩種用法——桌面版 IDE，跟終端機版的 `agy`。兩種都能走完本書；示範命令以 `agy` 為主，因為它在哪台機器都跑得起來。

不用先背起來，走到會用到的地方，這裡都會再提醒一次。

## 本書怎麼用

每章固定五格：

1. **貼給 Antigravity**：把整段文字複製起來，貼進你已經打開 `agy` 的那個終端機視窗（或 IDE 的 Agent 對話框），按 Enter 送出。
2. **範例問答**：如果它反問你問題，不用自己想答案，直接把這裡附的建議答案複製貼上就好。
3. **你應看到**：它做完之後畫面大概會長怎樣，重點是「形狀對不對」，不用一字不差。
4. **通過**：貼一段命令去檢查有沒有做對；看到通過的樣子才能往下走，卡住就先別往前。
5. **卡住就貼**：不用自己想怎麼描述問題，直接把這段話貼回去。

### 兩個一定要先知道的 Antigravity 行為

**一、它每做一件有後果的事，都會停下來等你批准。**
要跑命令、要改檔案之前，畫面會出現一個待批准的項目。`Ctrl+K` 批准目前這一項，`Ctrl+J` 跳到還在等批准的地方。**看不懂它要做什麼，就不要批准**——先問它「你為什麼要跑這個？」再決定。

**二、Skill 有可能它自己啟動，不是只有你叫得動。**
Antigravity 平常只會看到每個 Skill 的名稱與描述；當它覺得某個 Skill 符合你的要求，就可能自己把整份內容讀進來執行。**這裡沒有「只准人呼叫」的開關**。本 repo 有 11 個會改變工作階段的 Skill（`workflow`、`setup-project`、`wayfinder`、`grill-with-docs`、`to-spec`、`to-tickets`、`implement`、`triage`、`improve-codebase-architecture`、`create-pull-request`、`handoff`）在正文第一句寫了「只在使用者明確要求時執行」，但那是寫給模型看的文字約束，不是系統強制。其餘 20 個是紀律型 Skill（`tdd`、`code-review` 這類），本來就允許模型自行啟動。

所以整本書只要看到它自己跑起你沒點名的流程，就貼這句：

```text
停。我沒有要求啟動這個 skill。請回到我上一則訊息指定的工作，先不要做別的。
```

`agy` 本身支援原生 Windows（有官方的 `install.ps1`），但**本書的驗收命令是 Unix shell**，所以 Windows 請在 WSL 裡執行。macOS 與 Linux 直接用系統終端機即可。所有終端機指令都在 repo 根目錄跑。

---

# 第 0 章｜讓 Antigravity 讀對規則

目標：先確認你電腦上該裝的工具都裝好了，再讓 Antigravity 弄懂這個專案的規則——哪些只是建議、哪些是系統會自動擋下來的強制規定。

## 終端機

一行一行貼進終端機、按 Enter：

```bash
python3 --version
git --version
agy --version
git status --short
```

這四行分別在問電腦：有沒有裝 Python（第幾版）、有沒有裝 Git（幫你保存改動記錄的工具）、有沒有裝 Antigravity CLI、這個資料夾裡有沒有還沒存檔的改動。前三個命令都要回你一行版本號才算成功（`agy --version` 會印出像 `1.1.12` 這樣一行純數字）；如果你是剛下載這個 repo，第四個命令通常什麼都不會印出來，那才是正常的。

沒印出 `agy` 版本號的話，先回 [`docs/INSTALL.md`](./docs/INSTALL.md) 把安裝與登入做完，再回來。

確認都過了，在 repo 根目錄啟動它：

```bash
agy
```

## Antigravity 會自己讀到什麼（先看懂再貼）

這個 repo 已經幫你準備好一組設定。它們不是同一種東西，被讀到的時機也不一樣：

| 檔案 | 什麼時候被讀進去 |
|---|---|
| `AGENTS.md`（根目錄） | **每次都讀**。放在 repo 根目錄的 `AGENTS.md`，對整個 repo 永遠生效，沒有開關。 |
| `.agents/rules/*.md` | 檔案開頭寫 `trigger: always_on` 的每次都讀；寫 `model_decision` 的由它自己判斷要不要讀。 |
| `.agents/skills/<名稱>/SKILL.md` | 平常**只載入名稱與描述**；被你點名、或它自己決定要用時，才把整份內容讀進來。 |
| `.agents/hooks.json` | **這份不是給模型看的**。它是系統設定，把 `.agents/hooks/guard.py` 掛在「工具真的執行之前」，該擋的直接擋掉。 |
| `.agents/agents/<名稱>/agent.md` | subagent（幫忙分工的獨立助手）定義。⚠️ workspace subagent 的官方檔案格式目前未載明，本 repo 的版本有可能載不進去，載不進去不影響本書流程。 |

先在 `agy` 裡打 `/skills` 按 Enter，確認清單裡看得到這幾個名字：`workflow`、`setup-project`、`grill-with-docs`、`to-spec`、`to-tickets`、`implement`、`code-review`、`security-review`、`commit-message`。

一個都看不到，代表 Antigravity 沒讀到 `.agents/`——多半是你不在 repo 根目錄啟動的。先 `exit` 離開，`cd` 回根目錄再開一次。

## 貼給 Antigravity

```text
先讀 AGENTS.md、.agents/rules/engineering-workflow.md、
.agents/skills/workflow/SKILL.md 與 .agents/hooks.json。

現在進入教材第二冊，固定題目是 SmartTrip FX，固定用 Python 3.11+ 的
standard library 寫一支終端機程式（CLI）。先不要寫程式，也先不要 commit（把改動存進 Git 記錄）。

用四行回答我：
1. 這一冊要我完成什麼。
2. 哪些規則只是建議，我可以自己判斷。
3. 哪些操作會被 hook（系統自動檢查）強制擋下來。
4. 我現在唯一該做的下一步是什麼。
```

## 你應看到

```text
目標：完成可測試的 SmartTrip FX CLI。
建議：依需求選用 Skills，以 vertical slice 和 TDD 前進。
強制：敏感檔案、疑似 credential 與破壞性操作，會被 .agents/hooks.json 掛的 guard 擋下或退回確認。
下一步：建立 project contract。
```

（vertical slice 指「一次只做一小片可以獨立驗證的功能」；TDD 指「先寫一個測試證明還沒做到，再寫最少的程式讓測試通過」，第 5 章會實際做一次，現在看不懂沒關係。credential 指帳號密碼、API 金鑰這類不該進版控的秘密。）

## 通過

- [ ] 它沒有開始寫 code。
- [ ] 它提到的每個 Skill 名字，都在剛剛 `/skills` 的清單裡找得到（不能出現 `frame`、`spec`、`evals`、`next`、`ship` 這幾個根本不存在的名字）。
- [ ] 它講「強制」時，指得出是 `.agents/hooks.json` 或 `.agents/hooks/` 在做這件事，不是憑印象講。
- [ ] 它給的下一步只有一個，不是一堆選項。

## 卡住就貼

```text
停。你剛剛引用了不存在的流程或檔案。
請先實際跑 ls .agents/skills 與 ls .agents/rules，
只根據列出來的東西重新回答那四行。列不出來的就說「沒有這個檔案」，不要靠印象補。
```

---

# 第 1 章｜建立 project contract（幫 AI 準備一份專案說明書）

目標：幫這個專案寫一份「說明書」，把測試怎麼跑、文件放在哪裡、安全底線都寫清楚。之後不管哪個 Skill 接手，都會先讀這份說明書，不用你每次重新解釋一遍。這份說明書的正式名稱叫 **project contract**。

## 先看懂：怎麼叫得動一個 Skill

**兩種寫法都可以，選你的畫面吃得下去的那一種。**

**寫法 A（斜線）**：在 `agy` 的輸入框打 `/setup-project` 按 Enter，就是點名要它跑那個 Skill。斜線後面還可以接文字，那段文字會一起送進去當輸入——本書後面幾章都用這種寫法。
（`agy --help` 裡有一個 `--disable-slash-commands` 旗標，說明寫的是 `Disable slash command and skill expansion in print mode`——「skill 展開」被跟「斜線指令」寫在一起，所以斜線叫 skill 是可行的。但**每個版本、每種介面的實際行為可能不同**，官方文件沒有逐一列出 workspace skill 的斜線名稱。）

**寫法 B（純文字，永遠有效）**：斜線沒跳出補完清單、或送出去沒反應，就改成這樣，效果一樣：

```text
請使用 setup-project skill。
（下面接原本要貼的內容）
```

（⚠️ IDE 版的呼叫介面可能長得不太一樣；以你自己畫面上 `/skills` 列出來的名稱為準。本書每章的貼文都是寫法 A，看到不動的時候直接換成寫法 B 就好。）

## 貼給 Antigravity

```text
/setup-project

用這門課固定的答案就好，不用讓我自己選技術：
- Runtime：Python 3.11+，只用 standard library（不裝任何額外套件）。
- Focused test（只跑一小塊測試）：python3 -m unittest <test_module> -v
- Full test（跑全部測試）：python3 -m unittest discover -s tests -v
- Build check（確認程式能被讀懂、沒有語法錯）：python3 -m compileall -q smarttrip_fx
- Typecheck、lint、format：這門課沒有設定，不要假裝已經驗證過。
- Issue tracker（放任務清單的地方）：用本機 markdown 檔，放在 .scratch/smarttrip-fx/issues/。
- Specs（放規格文件的地方）：docs/specs/。
- Git：用我現在所在的分支；commit message 照 Conventional Commits 格式寫。
- Risk boundary（風險底線）：刪資料、force push、真的打 API、部署、寫到外部系統，
  這些動作做之前都要再問我一次。

先去 repo 裡確認一遍，把「你真的從檔案裡看到的事實」跟「這門課固定要求的決定」分開。
先給我一份 docs/agents/project.md 的預覽，我確認後你再真的寫進去。先不要動任何產品程式碼。
```

## 範例問答

它給完預覽後，貼：

```text
這份預覽可以用。幫我存成 docs/agents/project.md，之後只要跟我說檔案路徑跟你建議的下一步就好。
```

寫檔案是有後果的動作，畫面會出現待批准項目。確認路徑真的是 `docs/agents/project.md` 之後，按 `Ctrl+K` 批准。

## 你應看到

`docs/agents/project.md` 至少要有這幾個區塊：Quality commands（測試怎麼跑）、Issue tracker（任務清單放哪）、Git workflow（怎麼開分支、怎麼寫 commit）、Domain docs（規格文件放哪）、Risk boundary（風險底線）、Verified on（這份說明書是根據什麼、什麼時候驗證過的）。

## 通過

```bash
test -f docs/agents/project.md
grep -nE "Full test|python3 -m unittest|Risk boundary" docs/agents/project.md
```

兩個命令都必須 exit 0——意思是「這個命令做完了、沒有出錯」。你只要看終端機有沒有跳出紅色錯誤訊息就好，沒有錯誤訊息通常就是過關。

## 卡住就貼

```text
只修正 docs/agents/project.md。缺的指令就寫「未設定」，不要自己去安裝套件，
也不要把這門課規定的固定值，寫得好像是你在 repo 裡驗證出來的事實。
```

---

# 第 2 章｜把需求問到沒有歧義（問清楚規則，不留模糊地帶）

目標：這一章只負責「把規則問到清楚」，先不要碰任何程式碼。「歧義」的意思是：同一句話，兩個工程師可能會理解成不同做法。這一章要把這種模糊全部問掉。

## 貼給 Antigravity

```text
/grill-with-docs SmartTrip FX

請一次只問我一題，確認下面這些已經固定的需求；如果答案已經寫在下面，就不用再問我一次：

產品：SmartTrip FX，幫準備去日本關西玩的人，算大概要換多少日圓現金。
輸入：一個 UTF-8 編碼的 JSON 檔案，裡面有 destination（目的地）、items（行程項目清單）跟 fx（匯率資料）。
items 裡每一筆只有三個欄位：name（名稱）、amount_jpy（日圓金額）、payment（付款方式）。
payment 只能是這三種值：cash_only（只能付現）、card_ok（可以刷卡）、unknown（不確定）。
fx 裡有 today_twd_per_jpy（今天的匯率）跟 ma30_twd_per_jpy（30 天平均匯率），
兩個都用十進位字串表示（例如 "0.2120"）。

換匯規則：
1. 現金小計 = cash_only 的金額加上 unknown 的金額；card_ok 不算進去。
2. 現金小計再加 10% 當預備金，然後無條件進位到下一個 1000 日圓（例如 8030 要進位成 9000）。
3. 今天匯率比 30 天均線低 2% 以上算 GOOD（適合換）；高 2% 以上算 WAIT（先別換）；
   其他情況算 NEUTRAL（都可以）。
4. JSON 格式錯誤、缺欄位、金額是負的，或 payment 不是上面三種值，
   程式都要印出清楚的錯誤訊息，而且要用「非 0」的結束代碼（exit code）結束。

這次固定只做：一支只用 Python standard library 寫的終端機程式（CLI）。
不做的部分：真的串 LLM、即時匯率 API、網頁介面、資料庫、登入功能、部署上線。
怎樣算成功：固定的範例輸入要算出 ¥9,000、匯率燈號 GOOD；所有測試都要通過；
全程都不能連網路。

先檢查看看還有沒有「會讓兩個工程師寫出不同做法」的模糊地帶。如果沒有了，
就幫我整理已經決定的事、不做的部分，跟怎樣算過關，然後推薦我下一步要用哪個 Skill。
先不要寫程式，也不要直接接著跑下一個 Skill。
```

最後那句要留著。Antigravity 可能會覺得「都問完了不如順手把 spec 也寫了」，就自己接著啟動 `to-spec`；這一章要的是先停在需求層。

## 範例問答

若它仍追問，依題意貼其中一個答案：

```text
金額規則就用推薦的做法：不確定（unknown）的金額保守算進現金裡，最後的結果無條件進位到 1000 日圓。
```

```text
匯率門檻就用推薦的做法：差距剛好等於 -2% 算 GOOD，剛好等於 +2% 算 WAIT。
```

```text
錯誤輸出就用推薦的做法：給人看的錯誤訊息印到 stderr（錯誤輸出）；程式的結束代碼（exit code）用 2。
```

最後貼：

```text
以上這些決定都對，需求已經問清楚了。請不要再繼續問，直接幫我收斂結論，並推薦下一個 Skill。
```

## 你應看到

它應該**推薦**你下一步用 `/to-spec`，而不是自己開始實作、也不是自己接著把 spec 寫掉。它可以先幫忙整理名詞用法（domain glossary），但還不能動手寫產品程式碼。

## 通過

- [ ] payment 真的只剩三個合法值。
- [ ] 金額公式跟 2% 門檻講法清楚，沒有「大概」「可能」這種模糊字。
- [ ] live API 跟網頁介面（Web UI），清楚寫在不做的範圍裡。
- [ ] 每一條成功條件，都能直接回答「有做到」或「沒做到」。
- [ ] 這一章結束時，`docs/specs/` 底下還沒有任何新檔案——寫 spec 是下一章的事。

## 卡住就貼

```text
現在只找「會讓兩個工程師寫出不同行為」的未知資訊。
若沒有這種未知，停止提問並用已確認需求收斂。不要啟動其他 skill。
```

---

# 第 3 章｜把對話變成可驗收 spec（一份「怎樣算做完」的白紙黑字）

目標：讓需求離開聊天紀錄，變成下一次開新對話、別人也看得懂的文件。**Spec** 是一份寫清楚「結果要長怎樣、怎樣算過關」的文件，不是一步一步教你怎麼寫程式的教學。

## 貼給 Antigravity

```text
/to-spec SmartTrip FX

用剛才已經確認的需求，幫我生一份 spec，存到 docs/specs/smarttrip-fx.md。
下面幾個實作上的決定是固定的，不用重新討論：
- package（程式碼放的資料夾）：smarttrip_fx/
- 對外公開的三個函式（seam，也就是外部可以呼叫、也方便單獨測試的介面）：
  recommend_cash(items)、fx_signal(today, ma30)、load_trip(path)
- CLI 用法：python3 -m smarttrip_fx examples/kansai-3-days.json
- 只能用 decimal、json、dataclasses、pathlib、argparse、unittest
  這些 Python standard library，不裝任何第三方套件。
- 固定範例算出來要是：現金項目 ¥5,500、不確定項目 ¥1,800、
  建議換匯 ¥9,000、匯率燈號 GOOD。

每一條驗收條件（acceptance criteria）都要寫成「假設 Given／當 When／那麼 Then」
的格式，而且要能直接回答「過」或「不過」。
先給我看 Problem、Outcome、seams、Out of scope 跟 Open questions 的預覽，
我確認以後你再真的寫進檔案。
```

## 範例問答

預覽正確時貼：

```text
確認。Open questions 應為 None，請寫入 docs/specs/smarttrip-fx.md。
```

寫檔案的待批准項目出現時，先看它要寫的路徑對不對，再按 `Ctrl+K`。

## 你應看到

```markdown
# SmartTrip FX

## Problem
## Outcome
## User stories
## Acceptance criteria
## Implementation decisions
## Testing decisions
## Out of scope
## Open questions
None
```

各區塊白話對照：Problem（要解決的問題）、Outcome（做完之後會有什麼結果）、User stories（誰會怎麼用）、Acceptance criteria（怎樣算過關）、Implementation decisions（技術上的固定決定）、Testing decisions（打算怎麼測）、Out of scope（這次不做的部分）、Open questions（還沒決定的事——這次應該是 None，代表沒有懸而未決的問題）。

## 通過

```bash
test -f docs/specs/smarttrip-fx.md
grep -nE "Acceptance criteria|recommend_cash|fx_signal|Out of scope|Open questions" docs/specs/smarttrip-fx.md
```

## 卡住就貼

```text
不要新增新需求。只根據已確認對話補齊可驗收 spec；任何無證據內容放進 Open questions，
但課程固定值不得重新變成問題。
```

---

# 第 4 章｜把 spec 切成三張小票（拆成三個一次做得完的小任務）

目標：每次只讓 Antigravity 完成一個可驗證的行為，避免一口氣生出整個專案。**Ticket** 只是一份 markdown 檔案，不是要你去哪個平台開真的工單。它的重點是：一次開一個乾淨的新對話，也能獨立做完、獨立驗證。

## 貼給 Antigravity

```text
/to-tickets docs/specs/smarttrip-fx.md

用本機的任務清單（local tracker），固定切成三張票：
1. .scratch/smarttrip-fx/issues/01-cash-recommendation.md
   做完 recommend_cash 跟它的測試。
2. .scratch/smarttrip-fx/issues/02-fx-signal.md
   做完 fx_signal 跟它的測試。
3. .scratch/smarttrip-fx/issues/03-cli-integration.md
   做完 load_trip、CLI、固定的範例檔，以及從頭到尾的整合測試；
   這張票要等 01、02 都做完才能開始（blocked by 01、02）。

每張票都要寫：What to build（要做什麼）、Acceptance criteria（怎樣算過關）、
Testing seam（要測哪個功能點）、Blocked by（要等哪張票先做完）、Out of scope（不做什麼）。
這門課固定照 01 → 02 → 03 的順序做，不要開 worktree，也不要平行做，
也不要切完票就自己接著開始實作。
先給我看三張票的內容，我確認後你再真的寫進檔案。
```

## 範例問答

```text
切分正確。請照剛剛指定的檔名寫入三張 tickets，先不要開始做。
```

## 你應看到

```text
.scratch/smarttrip-fx/issues/
├── 01-cash-recommendation.md
├── 02-fx-signal.md
└── 03-cli-integration.md
```

## 通過

```bash
find .scratch/smarttrip-fx/issues -maxdepth 1 -type f -name '*.md' | sort
```

跑出來的結果一定要剛好三個檔案，而且第 03 張要清楚寫著被 01、02 擋住（blocked by）。此時 `smarttrip_fx/` 應該還不存在——這一章不寫任何程式。

## 卡住就貼

```text
不要按 model、service、tests 做水平切分。回到使用者可觀察行為，
並嚴格使用教材指定的三個檔名與 dependency。切完就停，不要接著實作。
```

---

# 第 5 章｜一張票一次完成（實際跑三次「先讓它失敗，再讓它成功」）

目標：實際跑三次 red → green → review，而不是一次生成所有檔案。**TDD** 的意思是：先寫一個一定會失敗的測試，證明「這個功能現在真的還沒做出來」（這叫紅燈 / RED），再寫剛好夠用的程式讓測試通過（這叫綠燈 / GREEN），最後把程式整理乾淨（refactor），但不能改變原本的行為。

這一章 Antigravity 會頻繁要求批准：建檔案、改檔案、跑 `python3 -m unittest`。**跑測試的命令請放心批准，那是這一章的重點**；但每次它要改檔案時，先看一眼路徑有沒有跑到票的範圍外。`Ctrl+J` 跳到待批准處，`Ctrl+K` 批准當前這一項。

（`agy` 有 `--mode accept-edits` 可以讓它自動套用檔案修改；本書刻意不用，因為「你看著它一步步做」正是這一章要練的東西。）

## 5.1 現金計算

### 貼給 Antigravity

```text
/implement .scratch/smarttrip-fx/issues/01-cash-recommendation.md

只做票 01 這一張，先講清楚這次的範圍、怎樣算過關（acceptance criteria）、
要測哪個功能點（testing seam），並記住現在這個版本（HEAD）當作基準點。
接著用 unittest 跑一次：寫一個測試 → 讓它先失敗（RED） →
寫最少的程式讓它通過（GREEN） → 再整理程式碼（refactor）。
不要順便做 fx、JSON 解析器或 CLI 這些其他票的事。先不要 commit。
```

### 你應看到

至少有 `smarttrip_fx/` 的計算模組與 `tests/test_cash_recommendation.py`，而且回報中包含實際跑過的 RED 與 GREEN 命令。**它必須真的讓你看到一次失敗的測試輸出**；只說「我先寫了測試，它會失敗」不算數。

### 通過

```bash
python3 -m unittest tests.test_cash_recommendation -v
```

## 5.2 匯率燈號

### 貼給 Antigravity

```text
/implement .scratch/smarttrip-fx/issues/02-fx-signal.md

只做票 02 這一張。用 Decimal（精準計算用的型別，不會有浮點數誤差）
比較 today 跟 ma30，一定要明確測到 -2%、+2% 跟中間值這幾個邊界情況。
沿用票 01 已經定好的程式結構（package shape），不要改到現金計算的行為。先不要 commit。
```

### 通過

```bash
python3 -m unittest tests.test_fx_signal -v
```

## 5.3 JSON 與 CLI 串接

### 貼給 Antigravity

```text
/implement .scratch/smarttrip-fx/issues/03-cli-integration.md

只做票 03 這一張。建立 examples/kansai-3-days.json，內容固定是：
- Airport bus：2300 日圓，cash_only
- Fushimi souvenir：1800 日圓，unknown
- Hotel：24000 日圓，card_ok
- Nishiki market：3200 日圓，cash_only
- today_twd_per_jpy：0.2120
- ma30_twd_per_jpy：0.2180

CLI 跑成功的時候，畫面上一定要有：
目的地 Kansai、現金項目 ¥5,500、不確定項目 ¥1,800、
建議換匯 ¥9,000、匯率燈號 GOOD。

針對「JSON 格式錯誤」「缺欄位」「金額是負的」「payment 不是合法值」這四種情況，
都要寫測試檢查程式的對外行為。不要連網路、不要加第三方套件、先不要 commit。
```

### 你應看到

```text
smarttrip_fx/
tests/
examples/kansai-3-days.json
```

檔案可以比這些多，但不能出現 Web framework、database 或 live API client。

### 通過

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q smarttrip_fx
python3 -m smarttrip_fx examples/kansai-3-days.json
```

最後一個命令應包含：

```text
目的地: Kansai
現金項目: ¥5,500
不確定項目: ¥1,800
建議換匯: ¥9,000
匯率燈號: GOOD
```

這幾個數字是本書唯一的最終驗收訊號。對不上就不要往下走。

## 卡住就貼

```text
先停止加功能。只比對目前 ticket、docs/specs/smarttrip-fx.md 與失敗測試，
指出一個主要假設、最小可推翻檢查與下一個動作。同一路徑不要嘗試第四次。
```

---

# 第 6 章｜用證據收尾（review 一遍、確認沒問題再存檔）

目標：review 完整 working tree、修阻擋問題、再產生 commit。**Working tree** 指你電腦裡目前「還沒存進 Git 記錄」的所有檔案改動。雙軸 review 會分開檢查工程品質（Standards）跟符不符合規格（Spec）。

## 先自己看一眼改了什麼

review 之前，先自己掃過一遍。最穩的做法是另外開一個終端機視窗跑：

```bash
git status --short
git diff
git diff --stat
```

（`agy` 也有 `/diff` 可以在對話裡看改動，⚠️ 這個指令列在官方 CLI 說明裡，本課未在無桌面環境實測過。看不到就用上面的 `git diff`，結果一樣。）

## 貼給 Antigravity：雙軸 review

```text
/code-review HEAD

Spec source（規格來源）：docs/specs/smarttrip-fx.md。
請把 HEAD 之後、整個 working tree 的改動都看過一遍，包含還沒 commit 的（staged）、
連 git add 都還沒做的（unstaged），還有全新的檔案（untracked）。
Standards 這一軸檢查正確性、錯誤處理跟測試品質；
Spec 這一軸檢查有沒有漏做、做錯，或做了規格以外的東西（scope creep）。
只列出真的有具體失敗情境的問題（findings），先不要動任何檔案。
```

（這個 skill 會試著把兩軸交給獨立的 subagent 分別看。⚠️ workspace subagent 的官方檔案格式目前未載明，載不進去時它會改成在同一個 context 裡分兩段做——結論一樣要看，只是隔離度較低。）

若有 blocking finding，貼：

```text
依照 review 給的證據，只修真的會擋路的問題（blocking findings）。
一次修一個，修完馬上重跑最小範圍的測試；全部修完後再跑一次完整測試跟同一個 review。
不要順便擴大範圍去改別的東西。
```

## 貼給 Antigravity：安全檢查

```text
/security-review

範圍是目前 SmartTrip FX 的 working tree。重點檢查：外部傳進來的 JSON、
檔案路徑、錯誤訊息、資源耗用，還有會不會不小心讀到不該讀的敏感檔案。
只回報「有辦法用程式碼證明真的存在」的攻擊路徑，先不要動任何檔案。
```

## 通過

```bash
python3 -m unittest discover -s tests -v
python3 -m compileall -q smarttrip_fx
git diff --check
git status --short
```

tests 必須全綠、compile 與 diff check 必須 exit 0。`git status` 此時有檔案是正常的，因為還沒 commit。

## 建立本地 commit

```bash
git add -A
```

貼給 Antigravity：

```text
/commit-message

根據 staged diff 檢查這次改動夠不夠原子（atomic），
給我一個符合 Conventional Commit 格式的 subject。先不要 commit、也不要 push。
```

`commit` 跟 `push` 是有後果的操作，這門課固定由你自己在終端機執行——它就算提議要幫你跑，也不要批准。若 staged diff 只有本書產物，直接自己執行：

```bash
git commit -m "feat(smarttrip): build deterministic cash recommendation CLI"
git status --short
```

最後一個命令應沒有輸出。到這裡，你已經完成一個有 spec、tickets、tests、review 與可執行入口的專案。

## 卡住就貼

```text
不要用「看起來沒問題」結案。請列出實際跑過的命令、exit code、未驗證事項，
以及目前唯一阻止 commit 的問題。
```

---

# 第 7 章｜把方法帶去下一個專案

你剛才不是背七個步驟，而是反覆做同一件事：

```text
固定邊界 → 產生一小片 → 用同一個判準驗證 → 人決定是否繼續
```

| 需要 | 使用的 Skill | 產出 |
|---|---|---|
| 不知道該走哪條路 | `/workflow` | 幫你推薦一條路 |
| 需求還有模糊地帶 | `/grill-with-docs` | 把決定問清楚 |
| 要把對話變成白紙黑字 | `/to-spec` | 一份可以拿去驗收的 spec |
| 工作要分好幾次做完 | `/to-tickets` | 有先後順序的任務卡 |
| 要做完一個功能 | `/implement` | 一片測試保護過的功能 |
| 準備要交出去 | `/code-review`、`/security-review` | 具體的檢查證據跟問題清單 |
| 要寫 commit message | `/commit-message` | 一句對得起 staged diff 的 subject |

要把這套帶去下一個專案，只要複製兩樣東西：根目錄的 `AGENTS.md`，跟整個 `.agents/` 資料夾。Antigravity 只讀這兩處；`.agents/hooks.json` 裡的相對路徑是以 `.agents/` 為基準，整包搬過去就會繼續生效。

下一個專案只先貼這一句：

```text
/workflow 我想完成 <一句話目標>。先讀 repo 現況，只推薦一條路並說明翻盤條件。
```

（翻盤條件的意思是：如果之後發現了什麼新狀況，原本推薦的做法就該換掉——先問清楚這個，比盲目照做安全。）

建議先把這整套流程原封不動地再走一次，練熟了以後，再考慮加 live LLM adapter、Web UI 或即時匯率 API 這些真正的複雜度。一次只加一種新東西，不要一次全加。
