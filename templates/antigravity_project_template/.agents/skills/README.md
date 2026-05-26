# Agent Skills（進階，可以先跳過）

> 初學者先把 `AGENTS.md` 跟基本對話用熟，再回來看這份。
> Skill 與 MCP 的差別請看 [`../SKILLS.md`](../SKILLS.md) — 那份才是完整教學。
> 這份只是「資料夾本身的快速使用說明」。

---

## 這個資料夾在幹嘛

Antigravity CLI（`agy`）啟動時會掃描 `.agents/skills/`，把每個檔案 / 子資料夾當成一個 Skill 載入。

Skill 是**程序性知識**：你每次都要跟 AI 講「請每次都先 ___」的那種流程，包裝成 markdown 後 AI 會在對的情境下自動翻書照做。**同一份 Skill 也是 slash command**——你可以打 `/skill-name` 手動觸發。

完整原語對照與設計哲學在 [`../SKILLS.md`](../SKILLS.md)。

---

## 資料夾結構

```
.agents/skills/
├── README.md                 ← 你正在看的這份
├── check-key.md              ← 單檔 Skill = /check-key（部署前安全檢查）
└── explain-code/             ← 資料夾 Skill = /explain-code（架構師視角講解）
    └── SKILL.md
```

**為什麼只附 2 個？** 實用主義設計：只留「模型本能彌補不了」的 skill。Vibe Coding「先列計畫」流程已在 [`../../AGENTS.md`](../../AGENTS.md) 第 3 章明寫，現代 SOTA 模型會自動遵守，不需要另外做成 slash command。其他常見 skill（`/test`、`/explain`、`/git:commit` 等）的範例放在 [`../SKILLS.md`](../SKILLS.md) 最末「範例庫」段——**你需要時再複製貼到這裡**。

**鐵則**：
- 檔名（去掉 `.md`）= Skill 名 / slash command 名
- 子資料夾名 = namespace（用冒號分隔，例：`/git:commit`）
- 資料夾形式必須有 `SKILL.md`
- 開頭必須有 `name` + `description` 的 YAML frontmatter

---

## 快速建立一個新 Skill

### 形式 A：單檔（最簡單）

```bash
cat > .agents/skills/my-new-skill.md <<'EOF'
---
name: my-new-skill
description: Use when ___ 觸發場景描述，寫具體一點，AI 才找得到.
---

# My New Skill

當使用者要 ___ 時，照以下流程：

1. 第一步
2. 第二步
3. 第三步
EOF
```

存檔後**重啟 CLI**（skill 在啟動時掃描，不熱載）。可打 `/my-new-skill` 手動觸發，或讓 AI 看 description 自動翻。

### 形式 B：資料夾（要附檔案時）

```bash
mkdir -p .agents/skills/my-new-skill
touch .agents/skills/my-new-skill/SKILL.md
# 再把 examples/、checklist.md 等附件放同資料夾
```

---

## 本模板附了哪幾個範例

| Skill | 觸發 | 用途 |
|---|---|---|
| `check-key.md` | `/check-key` | 部署前檢查 API Key 設定 / 外洩風險 |
| `explain-code/` | `/explain-code` | 架構師視角 × 🟢🟡🔴 紅綠燈 × 導師教學 |

**測試方法**：重啟 `agy` 後直接打 `/check-key`、`/explain-code`，看 skill 是否觸發。

**想加更多 skill？** 看 [`../SKILLS.md`](../SKILLS.md) 末尾的「範例庫」段，有 `/test`、`/explain`、`/git:commit` 三個常見範例可以複製。

---

## 建議的初學者 Skill 清單

不用一次全建，遇到「同樣的話我已經跟 AI 講第 3 次了」再包成 Skill。

| Skill 名 | 觸發場景 | 對應 Vibe Coding 步驟 |
|---|---|---|
| `explain-code` | 「解釋這段」 | 任何步驟（debug 用） |
| `prd-rewrite` | 「我要寫 PRD」 | 第 1 步重述需求 |
| `pre-commit-review` | 「我寫完了」 | 第 3 步寫完後 |
| `check-key` | 部署前 / 怕金鑰外洩 | 第 4 步驗證 |

---

## 安全注意事項（重要）

Skill 會被 AI 當 system instruction 直接執行，且**會跟著 git 走、團隊都看得到**：

- ❌ 不要在 Skill 內塞 secret（API key、token、密碼）
- ❌ 不要寫絕對路徑（`/Users/sunny/...` 換台機器就壞）
- ❌ 不要寫破壞性指令當預設行為（「直接刪 ___」改成「列出選項等使用者確認」）
- ✅ 單一 Skill 不要超過 200 行 — 超過就拆或抽附件
- ✅ description 寫具體場景，不要寫「helper」「utility」這種空泛詞

更詳細的安全規則見 [`../SKILLS.md`](../SKILLS.md) 的「安全與品質規則」段。

---

## 與 user-level skills 的關係

Antigravity CLI 會掃兩個位置：

| 位置 | 適合放 | 跟 git 走嗎 |
|---|---|---|
| `<project>/.agents/skills/` ← **你在這裡** | 專案專屬流程 | ✅ 會 |
| `~/.gemini/antigravity-cli/skills/` | 跨專案的個人習慣 | ❌ 不會 |

跨專案會用到的 Skill 移到 user-level，避免每個專案複製一份。
