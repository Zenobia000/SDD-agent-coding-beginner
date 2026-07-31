# 循環工程專案骨架

> 一套可以直接複製走的 Claude Code 設定：**16 個 skill、4 個 subagent、4 個 command、5 個 hook、3 個 output style、9 條 rule**。
> 不上課也能用。上課的話，這是你 8 小時的工作目錄。

---

## 結論卡

| | |
|---|---|
| **做什麼** | 給你一套「AI 協作有紀律」的專案起點 |
| **核心** | 沒有評分函式不開跑；跑起來讓它跑完；收工由人決定 |
| **要花多久上手** | 5 分鐘（複製 + 開 claude + 打 `/blocks`） |
| **不必全用** | 最小集只有三個 skill，其餘刪掉是正確做法 |
| **下一步** | 見下面「三行開始」 |

---

## 三行開始

```bash
cp -r <這個資料夾> my-project && cd my-project
cp .mcp.json.example .mcp.json      # 用不到的 MCP 整段刪掉
claude
```

進去之後打 `/blocks` —— 它會看你的專案現況，告訴你下一塊該裝什麼。

---

## 裡面有什麼

```
CLAUDE.md                 ← 站立規則（每次對話都生效）
.mcp.json.example         ← 三個 MCP：context7 / playwright / figma
.githooks/                ← 機械守門：pre-commit 擋 secret、pre-push 擋 force push
docs/PRD.md               ← 你的需求規格（/spec-it 會幫你填）
tasks/                    ← backlog / 當前 sprint / 已知問題 / 回顧
.claude/
├── WORKFLOW.md           ← 15 站流程總圖（從意圖到交付）
├── SKILL-MAP.md          ← 積木怎麼接（Pre/Post 條件、典型路徑、斷層排查）
├── MCP.md                ← 外接工具：用在哪、風險是什麼
├── settings.json         ← 權限 + 5 個 hook 的註冊
├── rules/                ← 9 條硬約束
├── skills/               ← 16 塊流程積木
├── agents/               ← 4 個 subagent
├── commands/             ← 4 個編排指令
├── output-styles/        ← 3 種輸出風格
└── hooks/                ← 5 個 hook 腳本
```

---

## 核心六塊積木

其餘十塊「該專案需要時再啟用」。完整清單見 [`.claude/SKILL-MAP.md`](./.claude/SKILL-MAP.md)。

| Skill | 一句話 |
|---|---|
| `/loop` | 跑一輪四拍，改到好為止 |
| `/decide` | 給我一個建議，不要給我選項清單 |
| `/spec-it` | 一句話需求 → 七欄位 spec |
| `/eval-set` | 「做對了」變成可執行的考卷 |
| `/tdd-cycle` | 紅 → 綠 → 重構 |
| `/verify` | commit 前五維度驗證 |

---

## 五個 hook 在幫你擋什麼

這些是**機械層**——寫進 `CLAUDE.md` 的規則約有 ~70% 順從率，不可逆的操作不能賭那 30%。

| Hook | 時機 | 擋 / 做什麼 |
|---|---|---|
| `inject-station.sh` | 每次送出訊息 | 注入「你在第幾站、第幾拍」 |
| `block-dangerous-bash.sh` | 執行指令前 | `rm -rf`、force push、`reset --hard`、在 main 上 commit |
| `block-secret-write.sh` | 寫檔前 | 寫 `.env`、硬編碼的 API key |
| `autoformat.sh` | 寫檔後 | 自動跑 formatter |
| `remind-verify.sh` | 回合結束 | 有未提交改動卻沒跑 `/verify` 時提醒一次 |

想自己改一個？→ [`docs/authoring/04-write-a-hook.md`](../../docs/authoring/04-write-a-hook.md)

---

## 三種輸出風格

用 `/config` → Output style 切換（`/output-style` 指令已在 v2.1.91 移除）。

| 風格 | 什麼時候用 |
|---|---|
| **ADHD** | 你只想要結論和下一步 |
| **Dev Decision** | 選型 / debug / 架構決策 |
| **Teaching** | 上課、帶新人 |

---

## 不必全用

**Solo dev 的最小集是三個**：`/spec-it` + `/tdd-cycle` + `/commit-msg`。

刪掉用不到的是**正確做法**，不是偷懶：

```bash
rm -rf .claude/skills/ui-spec     # 純 CLI 工具沒有介面
rm -rf .claude/skills/retro       # 一次性小工具不需要回顧
rm -rf .claude/skills/adr         # 沒有架構選擇要記錄
```

**留著沒在用的 skill，會讓 AI 在錯的時機建議它們。**

---

## 常見問題

**Q：我打 `/spec-it` 沒反應？**
A：① 確認 `.claude/skills/spec-it/SKILL.md` 在 ② 打 `/context` 看載入狀況 ③ 重開 `claude`。

**Q：小調整也要跑全套嗎？**
A：不用。判準是**有沒有行為改變**。有 → 至少 `/spec-it`（精簡）+ `/tdd-cycle`；純樣式 / typo → 直接改。

**Q：AI 一直建議我跑 skill，很煩。**
A：兩個方法 ——
① 這個 session：說「不要建議任何 skill，我自己來」
② 永久：刪掉用不到的 skill 目錄（最乾淨的方法）

**Q：`skills/` 和 `commands/` 差在哪？**
A：兩者都產生 `/<name>`。skill 是目錄、可帶附件、可被 AI 自動載入；command 是單檔、通常由你主動打。
完整判斷 → [`docs/authoring/07-choose-which.md`](../../docs/authoring/07-choose-which.md)

**Q：ADR 我寫了再也沒看，有用嗎？**
A：有。**ADR 的價值在「未來的 AI session 會自動讀到」**，不是給你看的。
3 個月後 AI 會 reference 過去的決策，不會推翻它。

**Q：這套跟其他 AI coding 設定差在哪？**
A：多數設定在教「怎麼叫 AI 做事」。這套在教「怎麼判斷 AI 做對了沒」——
差別就在 `/eval-set` 和 `rules/08-loop-first.md`。

---

## 下一步

打開 [`.claude/WORKFLOW.md`](./.claude/WORKFLOW.md)，看你的專案該從第幾站開始。
