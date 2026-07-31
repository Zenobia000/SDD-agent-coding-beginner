# SmartTrip FX：從一句需求到可測試 CLI

這是學生唯一要照著走的文件。全書固定同一題、同一技術路線、同一組驗收條件；你只需要複製、貼上、執行、核對。

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

AI 負責「哪些行程可能需要現金」這類判斷；程式負責加總、比例、門檻與錯誤處理。這條邊界是全書唯一核心。

## 本書怎麼用

每章固定五格：

1. **貼給 Claude**：整段複製到 Claude Code。
2. **範例問答**：Claude 若追問，直接貼建議答案。
3. **你應看到**：輸出形狀，不要求逐字相同。
4. **通過**：執行命令，通過才能往下。
5. **卡住就貼**：不用自己猜下一步。

本書支援 macOS、Linux 與 Windows WSL。終端機指令都在 repo 根目錄執行。

---

# 第 0 章｜讓 Claude 讀對規則

目標：確認環境可用，而且 Claude 知道哪些是建議、哪些是機械強制。

## 終端機

```bash
python3 --version
git --version
claude --version
git status --short
```

前三個命令都要有版本輸出；剛 clone 的 repo，最後一個命令應沒有輸出。

## 貼給 Claude

```text
先讀 CLAUDE.md、.claude/rules/engineering-workflow.md、
.claude/skills/workflow/SKILL.md 與 .claude/settings.json。

這是教材實作，固定題目是 SmartTrip FX，固定使用 Python 3.11+
standard library CLI。先不要寫 code，也不要 commit。

只用四行回答：
1. 這個 repo 要我完成什麼。
2. 哪些規則是建議。
3. 哪些操作由 hook 強制。
4. 我現在唯一的下一步。
```

## 你應看到

```text
目標：完成可測試的 SmartTrip FX CLI。
建議：依需求選用 Skills，以 vertical slice 和 TDD 前進。
強制：敏感檔案、credential 與破壞性操作會被 hook 攔截。
下一步：建立 project contract。
```

## 通過

- [ ] Claude 沒有開始寫 code。
- [ ] 它沒有提到 `frame`、`spec`、`evals`、`next` 或 `ship` 等不存在的舊 Skill。
- [ ] 下一步只有一個。

## 卡住就貼

```text
你引用了目前不存在的流程。請只根據剛讀到的實際檔案重新回答，
並用 rg 驗證你提到的 Skill 目錄真的存在。
```

---

# 第 1 章｜建立 project contract

目標：把測試命令、文件位置與安全邊界寫成後續 Skills 都讀得到的專案契約。**Project contract** 就是每個 agent 開工前共同讀取的專案說明書。

## 貼給 Claude

```text
/setup-project

使用以下課程固定值，不要讓我選技術棧：
- Runtime：Python 3.11+，只用 standard library。
- Focused test：python3 -m unittest <test_module> -v
- Full test：python3 -m unittest discover -s tests -v
- Build check：python3 -m compileall -q smarttrip_fx
- Typecheck、lint、format：未設定，不要假裝已驗證。
- Issue tracker：local markdown，放 .scratch/smarttrip-fx/issues/。
- Specs：docs/specs/。
- Git：目前分支；commit message 使用 Conventional Commits。
- Risk boundary：刪資料、force push、真實 API 呼叫、部署與外部寫入都要再次確認。

先探索 repo，分清楚「從檔案驗證的事實」和「課程固定決策」。
先預覽 docs/agents/project.md，等我確認後再寫入。不要改產品 code。
```

## 範例問答

Claude 預覽後，貼：

```text
採用這份預覽。請寫入 docs/agents/project.md，然後只回報檔案路徑與下一步。
```

## 你應看到

`docs/agents/project.md` 至少有：Quality commands、Issue tracker、Git workflow、Domain docs、Risk boundary、Verified on。

## 通過

```bash
test -f docs/agents/project.md
rg -n "Full test|python3 -m unittest|Risk boundary" docs/agents/project.md
```

兩個命令都必須 exit 0。

## 卡住就貼

```text
只修正 docs/agents/project.md。缺少的命令用「未設定」標記，
不要安裝套件，也不要把課程指定值冒充成 repo 已驗證事實。
```

---

# 第 2 章｜把需求問到沒有歧義

目標：固定產品邊界。這章不寫 code。

## 貼給 Claude

```text
/grill-with-docs SmartTrip FX

請用一次一題的方式確認以下固定需求；能從內容直接得到答案就不要重問：

產品：SmartTrip FX，給準備去日本關西旅行的人估算要換多少日圓現金。
輸入：一個 UTF-8 JSON 檔，包含 destination、items 與 fx。
items 每筆只有 name、amount_jpy、payment。
payment 只能是 cash_only、card_ok、unknown。
fx 包含 today_twd_per_jpy 與 ma30_twd_per_jpy，使用十進位字串。

規則：
1. 現金小計 = cash_only + unknown；card_ok 不計入。
2. 加 10% 預備金後，向上取整到下一個 1000 JPY。
3. today 比 ma30 低至少 2% 為 GOOD；高至少 2% 為 WAIT；其餘 NEUTRAL。
4. 不合法 JSON、缺欄位、負金額或未知 payment 必須清楚報錯並以非 0 結束。

固定實作範圍：Python standard library CLI。
Out of scope：live LLM、即時匯率 API、Web UI、database、登入、部署。
成功：固定範例輸出 ¥9,000 與 GOOD；所有 tests 通過；完全不連網。

先檢查是否仍有真正會改變行為的歧義。沒有就整理已決定、out of scope
與可驗收結果，推薦下一個 Skill。不要寫 code。
```

## 範例問答

若 Claude 仍追問，依題意貼其中一個答案：

```text
金額規則採推薦值：unknown 保守計入現金，最後結果向上取整到 1000 JPY。
```

```text
匯率門檻採推薦值：差異剛好等於 -2% 算 GOOD，剛好等於 +2% 算 WAIT。
```

```text
錯誤輸出採推薦值：人類可讀訊息寫到 stderr，process exit code 使用 2。
```

最後貼：

```text
以上決策正確，需求已收斂。請停止訪談並推薦下一個 Skill。
```

## 你應看到

Claude 應推薦 `/to-spec`，而不是開始實作。它可以建立 domain glossary，但不能建立產品程式碼。

## 通過

- [ ] `payment` 只有三個合法值。
- [ ] 金額公式與 2% 匯率門檻沒有模糊詞。
- [ ] live API 與 Web UI 明確在 out of scope。
- [ ] 每個成功條件可以回答 pass 或 fail。

## 卡住就貼

```text
現在只找「會讓兩個工程師寫出不同行為」的未知資訊。
若沒有這種未知，停止提問並用已確認需求收斂。
```

---

# 第 3 章｜把對話變成可驗收 spec

目標：讓需求離開聊天紀錄，變成下一個 session 也能正確實作的文件。**Spec** 是描述可觀察結果與驗收條件的實作契約，不是程式碼步驟清單。

## 貼給 Claude

```text
/to-spec SmartTrip FX

用剛才已確認的需求產生 spec，目標路徑是 docs/specs/smarttrip-fx.md。
Implementation decisions 固定為：
- package：smarttrip_fx/
- public seams：recommend_cash(items)、fx_signal(today, ma30)、load_trip(path)
- CLI：python3 -m smarttrip_fx examples/kansai-3-days.json
- 只用 decimal、json、dataclasses、pathlib、argparse、unittest 等 standard library
- 範例必須輸出：現金項目 ¥5,500、不確定項目 ¥1,800、建議換匯 ¥9,000、匯率燈號 GOOD

每條 acceptance criterion 都寫成 Given / When / Then 且可 pass/fail。
先預覽 Problem、Outcome、seams、Out of scope 與 Open questions；我確認後才寫檔。
```

## 範例問答

預覽正確時貼：

```text
確認。Open questions 應為 None，請寫入 docs/specs/smarttrip-fx.md。
```

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

## 通過

```bash
test -f docs/specs/smarttrip-fx.md
rg -n "Acceptance criteria|recommend_cash|fx_signal|Out of scope|Open questions" docs/specs/smarttrip-fx.md
```

## 卡住就貼

```text
不要新增新需求。只根據已確認對話補齊可驗收 spec；任何無證據內容放進 Open questions，
但課程固定值不得重新變成問題。
```

---

# 第 4 章｜把 spec 切成三張小票

目標：每次只讓 Claude 完成一個可驗證行為，避免一口氣生成整個專案。**Ticket** 是一個乾淨 session 能獨立完成並驗證的工作單位。

## 貼給 Claude

```text
/to-tickets docs/specs/smarttrip-fx.md

使用 local tracker，固定輸出三張票：
1. .scratch/smarttrip-fx/issues/01-cash-recommendation.md
   完成 recommend_cash 與 tests。
2. .scratch/smarttrip-fx/issues/02-fx-signal.md
   完成 fx_signal 與 tests。
3. .scratch/smarttrip-fx/issues/03-cli-integration.md
   完成 load_trip、CLI、固定 example 與端到端 tests；blocked by 01、02。

每張票都要有 What to build、Acceptance criteria、Testing seam、Blocked by、Out of scope。
課程固定依 01 → 02 → 03 序列執行，不建立 worktree、不平行實作。
先預覽三張票，確認後才寫檔。
```

## 範例問答

```text
切分正確。請依指定檔名寫入三張 tickets，不要開始實作。
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

輸出必須剛好三個檔案，且第 03 張明確被 01、02 阻擋。

## 卡住就貼

```text
不要按 model、service、tests 做水平切分。回到使用者可觀察行為，
並嚴格使用教材指定的三個檔名與 dependency。
```

---

# 第 5 章｜一張票一次完成

目標：實際跑三次 red → green → review，而不是一次生成所有檔案。**TDD** 是先用失敗測試證明缺少行為，再寫最小實作讓它通過。

## 5.1 現金計算

### 貼給 Claude

```text
/implement .scratch/smarttrip-fx/issues/01-cash-recommendation.md

只完成 ticket 01。先固定 scope、acceptance criteria、testing seam 與 HEAD fixed point，
再用 unittest 跑一個 test → RED → 最小實作 → GREEN → refactor。
不要順手做 fx、JSON parser 或 CLI。不要 commit。
```

### 你應看到

至少有 `smarttrip_fx/` 的計算模組與 `tests/test_cash_recommendation.py`，而且回報中包含實際 RED 與 GREEN 命令。

### 通過

```bash
python3 -m unittest tests.test_cash_recommendation -v
```

## 5.2 匯率燈號

### 貼給 Claude

```text
/implement .scratch/smarttrip-fx/issues/02-fx-signal.md

只完成 ticket 02。用 Decimal 比較 today 與 ma30，明確測試 -2%、+2% 與中間值邊界。
沿用 ticket 01 的 package 形狀，不改現金計算行為。不要 commit。
```

### 通過

```bash
python3 -m unittest tests.test_fx_signal -v
```

## 5.3 JSON 與 CLI 串接

### 貼給 Claude

```text
/implement .scratch/smarttrip-fx/issues/03-cli-integration.md

只完成 ticket 03。建立 examples/kansai-3-days.json，固定資料為：
- Airport bus：2300 JPY，cash_only
- Fushimi souvenir：1800 JPY，unknown
- Hotel：24000 JPY，card_ok
- Nishiki market：3200 JPY，cash_only
- today_twd_per_jpy：0.2120
- ma30_twd_per_jpy：0.2180

CLI 成功輸出必須包含：
目的地 Kansai、現金項目 ¥5,500、不確定項目 ¥1,800、
建議換匯 ¥9,000、匯率燈號 GOOD。

為 invalid JSON、缺欄位、負金額與未知 payment 寫公開行為 tests。
不要接網路、不要新增第三方 dependency、不要 commit。
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

## 卡住就貼

```text
先停止加功能。只比對目前 ticket、docs/specs/smarttrip-fx.md 與失敗測試，
指出一個主要假設、最小可推翻檢查與下一個動作。同一路徑不要嘗試第四次。
```

---

# 第 6 章｜用證據收尾

目標：review 完整 working tree、修阻擋問題、再產生 commit。**Working tree** 是目前尚未全部 commit 的檔案狀態；雙軸 review 會分開檢查工程品質與 spec 符合度。

## 貼給 Claude：雙軸 review

```text
/code-review HEAD

Spec source：docs/specs/smarttrip-fx.md。
請審查 HEAD 之後的完整 working tree，包含 staged、unstaged 與 untracked files。
Standards 軸檢查正確性、錯誤路徑與測試品質；Spec 軸檢查漏做、做錯與 scope creep。
只列有具體失敗情境的 findings，不要修改檔案。
```

若有 blocking finding，貼：

```text
依 review 證據只修 blocking findings。每次修一個，重跑最窄測試；
完成後再跑 full test 與同一個 review。不要擴大 scope。
```

## 貼給 Claude：安全檢查

```text
/security-review

Scope 是目前 SmartTrip FX working tree。重點檢查外部 JSON、檔案路徑、錯誤訊息、
資源耗用與是否意外讀取敏感檔案。只回報可由 code 證明的攻擊路徑，不要修改檔案。
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

貼給 Claude：

```text
用 commit-message 根據 staged diff 檢查原子性，給我一個 Conventional Commit subject。
不要 commit、不要 push。
```

若 staged diff 只有本書產物，可直接執行：

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
| 不知道該走哪條路 | `/workflow` | 一條建議路徑 |
| 需求仍有歧義 | `/grill-with-docs` | 已確認決策 |
| 對話要變成契約 | `/to-spec` | 可驗收 spec |
| 工作超過一個 session | `/to-tickets` | 有 dependency 的 tickets |
| 完成一個行為 | `/implement` | tested vertical slice |
| 準備交付 | `code-review`、`security-review` | 證據與 findings |

下一個專案只先貼這一句：

```text
/workflow 我想完成 <一句話目標>。先讀 repo 現況，只推薦一條路並說明翻盤條件。
```

先把同一條路再走一次，再考慮 live LLM adapter、Web UI 或即時匯率 API。一次只新增一種複雜度。
