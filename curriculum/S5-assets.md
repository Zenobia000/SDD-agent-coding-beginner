# S5 方法變資產

## 結論卡

| | |
|---|---|
| **做什麼** | 把你今天重複講第三次的話，變成 hook / command 資產 |
| **為什麼** | **會用是使用者，會寫才是工程師**——這是全天唯一教「寫」的一站 |
| **產出** | 一個你自己改過的 hook + 一個你自己寫的 command |
| **下一步** | 跑 `/gate` 確認 S5 過關 |

**這一站對「資產」跑一輪四拍。**

---

## 課堂 15 分鐘版

**老師講**（5 分）：

1. 判斷訊號：**同樣的話你已經跟 AI 講第 3 次了** → 該包成資產
2. 六種資產，差別只在**誰觸發、什麼時候生效、能不能被違反**
3. 課堂只動手做兩種（hook + command），其餘四種複製成品，回家照 `docs/authoring/` 展開

**學生做**（40 分）：改一個 hook（20）+ 寫一個 command（20）。

老師巡場的重點：**確認每個人都親手跑過一次 hook 被觸發的樣子。**
沒有親眼看到 hook 擋下東西的人，不會相信機械層是真的。

---

## 動手

1. 挑一件今天重複做的事，寫下來
   ```
   我今天重複講了 3 次的話是：______________
   ```

2. 改一個 hook —— 在 `block-dangerous-bash.sh` 加一條你自己的規則
   ```bash
   # 開啟 .claude/hooks/block-dangerous-bash.sh
   # 在 ④ 後面加一段，例如擋掉直接改 .env
   ```

3. **實測你的 hook**（這步不能跳）
   ```bash
   echo '{"tool_input":{"command":"<你要擋的指令>"}}' \
     | bash .claude/hooks/block-dangerous-bash.sh
   ```
   應該印出 `permissionDecision: "deny"`。

4. 重開 `claude`，在對話裡真的觸發一次，確認擋得下來

5. 寫一個 command —— 建 `.claude/commands/<你的名字>.md`
   ```markdown
   ---
   description: <一句話，會出現在 / 選單>
   argument-hint: [參數提示]
   ---

   # 這個指令要做什麼

   ## 步驟
   1. …

   ## 硬規則
   - ❌ 不准 …
   ```

6. 重開 `claude`，打 `/<你的名字>` 確認會動

---

## 閘門

- [ ] `block-dangerous-bash.sh` 有你自己加的規則
- [ ] 用 `echo '{...}' | bash` 實測過，有印出 deny
- [ ] 在對話中真的被觸發過一次
- [ ] `.claude/commands/` 有一個你寫的新檔
- [ ] 打 `/<你的名字>` 有反應

---

## 我做對了嗎

對照 [`../labs/reference-project/S5/expected/`](../labs/reference-project/S5/expected/)：

- `my-hook.patch` —— 老師加的規則長什麼樣
- `my-command.md` —— 老師寫的 command

**這一站不比內容，比「你的東西真的會動嗎」**。

| 症狀 | 原因 | 修法 |
|---|---|---|
| hook 沒被觸發 | 沒重開 `claude`（hook 在啟動時載入） | 重開 |
| hook 報錯 | JSON 解析失敗 | 用 `bash -x` 跑看看哪一行 |
| `/我的指令` 找不到 | frontmatter 格式錯，或沒重開 | 檢查 `---` 有沒有成對 |
| command 有反應但行為不對 | 指令寫得太模糊 | 加「硬規則」段，寫 ❌ 不准做什麼 |

---

## 回家展開版

### 六種資產的決策表（這張表是本站的核心）

| 資產 | 誰觸發 | 何時生效 | 能被違反嗎 | 適合放什麼 |
|---|---|---|---|---|
| **CLAUDE.md** | 自動 | 每次對話 | ✅ 約 70% 順從 | 專案慣例、角色、必讀清單 |
| **rule** | 由 CLAUDE.md 引用 | 每次對話 | ✅ 同上 | 硬約束的說明與理由 |
| **skill** | 你打 `/x` 或 AI 判斷 | 需要時載入 | ✅ | 多步驟流程、有附件的程序 |
| **command** | 你打 `/x` | 需要時載入 | ✅ | 單檔的固定動作 |
| **subagent** | AI 判斷要派 | 需要時 | ✅ | 要獨立 context 或獨立視角的工作 |
| **hook** | **系統** | 特定事件 | ❌ **不能** | 不可逆操作的攔截、狀態注入、自動化 |

**最重要的一欄是「能被違反嗎」。**

```
所有東西都是「請 AI 遵守」，只有 hook 是「AI 沒得選」。
    ↓
不可逆的事情（刪資料、force push、外洩 secret）→ 一律用 hook
其他 → 用 rule / skill 就好
```

### 該做成哪一種？決策樹

```
這件事需要在特定事件自動發生嗎（不管 AI 想不想）？
├─ 是 → hook
└─ 否 ↓
   這是一套我要跟著走的多步驟流程嗎？
   ├─ 是 → 需要附件（範本、腳本）嗎？
   │        ├─ 是 → skill（目錄形式）
   │        └─ 否 → command（單檔）
   └─ 否 ↓
      這件事會產生一堆我不想看的中間資訊嗎？
      ├─ 是 → subagent
      └─ 否 ↓
         這是「每次都該知道」的專案事實嗎？
         ├─ 是 → CLAUDE.md / rule
         └─ 否 → 不用做成資產，直接講就好
```

完整版含各自的寫法範本 → [`../docs/authoring/07-choose-which.md`](../docs/authoring/07-choose-which.md)

### skill 和 command 已經合併了

**這是常見的過時知識**：`.claude/commands/deploy.md` 和
`.claude/skills/deploy/SKILL.md` **都會產生 `/deploy`**，行為一樣。

skill 多的是：
- 可以帶附件目錄（範本、腳本）
- frontmatter 能控制「誰能觸發」（`disable-model-invocation`、`user-invocable`）
- 可以被 AI 自動載入

**所以**：單純的固定動作 → command 就好；有範本或要 AI 自動觸發 → skill。

### Hook 的五種事件

| 事件 | 時機 | 典型用途 |
|---|---|---|
| `UserPromptSubmit` | 你送出訊息時 | **注入**狀態、加背景資訊 |
| `PreToolUse` | 工具執行前 | **擋**危險操作 |
| `PostToolUse` | 工具執行後 | **自動化**（格式化、檢查） |
| `Stop` | 回合結束 | **收尾**提醒 |
| `SessionStart` | session 開始 | 載入環境資訊 |

**契約**（所有 hook 共通）：
```
stdin  : JSON（含 tool_name / tool_input / session_id 等）
exit 0 : 通過。stdout 若是特定 JSON 會被解讀為決策
exit 2 : 阻擋。stderr 內容回饋給 Claude
```

`PreToolUse` 擋東西的兩種寫法：
```bash
# 寫法 A：exit 2 + stderr
echo "不准這樣做" >&2; exit 2

# 寫法 B：exit 0 + JSON（推薦，訊息更清楚）
jq -n '{hookSpecificOutput:{hookEventName:"PreToolUse",
        permissionDecision:"deny",permissionDecisionReason:"理由"}}'
```

### 寫 hook 的三個坑

1. **忘記重開** —— hook 在 session 啟動時載入，改完要重開
2. **沒處理空值** —— `jq -r '.x // empty'` 加預設，不然會拿到字串 `"null"`
3. **正則太寬** —— 擋 `rm` 結果連 `npm run rm-cache` 都擋掉。**寫完一定要測放行的案例**

### 寫 skill 的三個坑

1. **description 太空泛** —— 寫「helper」「utility」AI 找不到。要寫**觸發場景**
2. **太長** —— 超過 200 行就該拆或抽附件到同目錄
3. **沒有「不要觸發」的情況** —— 只寫何時用，AI 會過度觸發

### 安全提醒

Skill 和 hook 會被當指令執行，而且**跟著 git 走、團隊都看得到**：

- ❌ 不要在裡面塞 secret
- ❌ 不要寫絕對路徑（`/Users/sunny/...` 換台機器就壞）
- ❌ 不要寫破壞性指令當預設行為
- ✅ 用 `${CLAUDE_PROJECT_DIR}` 而不是硬寫路徑

**裝第三方 skill 前先讀它的 `SKILL.md` 和 scripts**——那是別人的程式碼。

---

## 下一步

打 `/gate`。通過後打開 [`S6-blocks.md`](./S6-blocks.md)。
