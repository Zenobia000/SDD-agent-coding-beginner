# Agent Skills（進階，可以先跳過）

> 初學者先把 `GEMINI.md` 跟基本對話用熟，再回來看這份。
> Skill / Command / MCP 三者的差別請看 [`../SKILLS.md`](../SKILLS.md) — 那份才是完整教學。
> 這份只是「資料夾本身的快速使用說明」。

---

## 這個資料夾在幹嘛

Gemini CLI 啟動時會掃描 `.gemini/skills/`，把每個子資料夾當成一個 Skill 載入。
Skill 是**程序性知識**：你每次都要跟 AI 講「請每次都先 ___」的那種流程，包裝成 markdown 後 AI 會在對的情境下自動翻書照做。

跟 `commands/` 的差別一句話：

| | 觸發方式 | 何時用 |
|---|---|---|
| **Skill** | AI 看 description **自動匹配** | 你希望 AI「在對的時候自己想到該做」 |
| **Command** | 你**手動**打 `/xxx` | 你希望「打一句就跑」的固定動作 |

完整對照表在 [`../SKILLS.md`](../SKILLS.md)。

---

## 資料夾結構

```
.gemini/skills/
├── README.md                 ← 你正在看的這份
└── explain-code/             ← 一個 Skill = 一個資料夾
    └── SKILL.md              ← 主檔（必須）
```

**鐵則**：
- 資料夾名 = Skill 名（用小寫 kebab-case，例：`pre-commit-review`）
- 資料夾內必須有 `SKILL.md`
- `SKILL.md` 開頭必須有 `name` + `description` 的 YAML frontmatter
- 附件（範例、checklist、script）放同資料夾，用相對路徑引用

---

## 快速建立一個新 Skill

```bash
# 1. 建資料夾
mkdir -p .gemini/skills/my-new-skill

# 2. 建 SKILL.md
touch .gemini/skills/my-new-skill/SKILL.md
```

`SKILL.md` 最小範本：

```markdown
---
name: my-new-skill
description: Use when ___ 觸發場景描述，寫具體一點，AI 才找得到.
---

# My New Skill

當使用者要 ___ 時，照以下流程：

1. 第一步
2. 第二步
3. 第三步
```

存檔後**重啟 CLI**（skill 在啟動時掃描，不熱載）。

---

## 範例 Skill：`explain-code/`

這個資料夾附了一個現成 Skill `explain-code`，是 [`../SKILLS.md`](../SKILLS.md) 教學裡示範的成果。

**測試方法**：重啟 CLI 後問：

```
你能解釋一下 index.html 在做什麼嗎？
```

如果 skill 正確被觸發，AI 會：
- ✅ 先問你想要的解釋深度（初學者 / 中等 / 深入）
- ✅ 用 `read_file` 真的讀檔
- ✅ 分段講解、標 file:line
- ✅ 點出值得注意的設計決策

如果沒被觸發，看 [`../SKILLS.md`](../SKILLS.md) 的「除錯」段落。

---

## 建議的初學者 Skill 清單

不用一次全建，遇到「同樣的話我已經跟 AI 講第 3 次了」再包成 Skill。

| Skill 名 | 觸發場景 | 對應 Vibe Coding 步驟 |
|---|---|---|
| `explain-code` | 「解釋這段」 | 任何步驟（debug 用） |
| `prd-rewrite` | 「我要寫 PRD」 | 第 1 步重述需求 |
| `plan-before-code` | 「我要做 ___」 | 第 2 步列計畫 |
| `pre-commit-review` | 「我寫完了」 | 第 3 步寫完後 |
| `test-helper` | 「怎麼測？」 | 第 4 步帶測試 |

---

## 安全注意事項（重要）

Skill 會被 AI 當 system instruction 直接執行，且**會跟著 git 走、團隊都看得到**：

- ❌ 不要在 SKILL.md 內塞 secret（API key、token、密碼）
- ❌ 不要寫絕對路徑（`/Users/sunny/...` 換台機器就壞）
- ❌ 不要寫破壞性指令當預設行為（「直接刪 ___」改成「列出選項等使用者確認」）
- ✅ 單一 Skill 不要超過 200 行 — 超過就拆或抽附件
- ✅ description 寫具體場景，不要寫「helper」「utility」這種空泛詞

更詳細的安全規則見 [`../SKILLS.md`](../SKILLS.md) 的「安全與品質規則」段。

---

## 與 user-level skills 的關係

Gemini CLI 會掃兩個位置：

| 位置 | 適合放 | 跟 git 走嗎 |
|---|---|---|
| `<project>/.gemini/skills/` ← **你在這裡** | 專案專屬流程 | ✅ 會 |
| `~/.gemini/skills/` | 跨專案的個人習慣 | ❌ 不會 |

跨專案會用到的 Skill 移到 user-level，避免每個專案複製一份。
