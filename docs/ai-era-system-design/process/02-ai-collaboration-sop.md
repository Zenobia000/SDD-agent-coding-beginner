# Process 02 — AI 協作五輪工作流

> 目的：把「AI 發散、人類收斂」落地成可重複執行的五輪流程。
> 核心：不要讓 AI 一直「說」，要讓 AI 進入結構化產出；人類只在每輪末端做決策。

---

## 五輪總覽

```
第一輪 AI 發散      →  第二輪 人類收斂  →  第三輪 AI 結構化
                                              ↓
第五輪 AI 轉開發資產  ←  第四輪 Human Gate
```

| 輪 | 主角 | 輸入 | 輸出 | 責任 |
|----|------|------|------|------|
| 1 發散 | AI | 種子簡報 | 需求假設、角色、主流程、例外、邊界、技術候選、風險、Open Questions（全標 `draft`） | AI 產，不下結論 |
| 2 收斂 | 人類 | 第一輪草稿 | 分類為 保留 / 刪除 / 待確認 | 人類決定取捨 |
| 3 結構化 | AI | 保留下來的內容 | PRD、Flow、ERD、API Contract、Test Case、ADR、Decision Log | AI 轉成結構 |
| 4 Gate | 人類 | 結構化產出 | 通過 / 退回 / 修改後通過 | 人類守 Gate |
| 5 開發資產 | AI | 已通過的 Spec | OpenAPI、DB migration、DTO、Service skeleton、Unit / Integration test、README、Runbook | AI 生成，工程師審查 |

---

## 每輪的執行要點

### 第一輪：AI 發散

Prompt 不要下「幫我設計最佳架構」，要下：

```
在以下約束下，產生 3 個架構候選方案。
每個方案需包含：
1. 適用條件  2. 優點  3. 風險
4. 不適用情境  5. 對團隊能力的要求  6. 需要人類決策的問題
```

所有產出標記 `status: draft`。並要求 AI 附上**假設清單**（見 [process/03](03-schemas-and-traceability.md)），因為 AI 最常出錯的不是語句，而是假設。

### 第二輪：人類收斂

不要逐字修 AI 文件，那很浪費時間。先做分類：

- **保留**：直接進第三輪結構化。
- **刪除**：丟到 `_discarded/`。
- **待確認**：進 Open Questions，指派 Owner 與 Due。

### 第三輪：AI 結構化

把保留內容轉成正式格式（PRD / Flow / ERD / API / Test / ADR）。此時對應跑 `/spec-it` 與 `/adr`。

### 第四輪：Human Gate

每道 Gate 只問一個關鍵問題（完整清單見 [process/04](04-human-gate-and-agent-roles.md)）。只有通過才進下一步。

### 第五輪：AI 轉開發資產

規格已收斂，AI 不會亂飛，此時價值最大。對應跑 `/tdd-cycle`、`/verify`、`/sync-it`。

---

## 文件目錄約定

避免 AI 產出污染正式規格，固定區分正式區與草稿區：

```
docs/                  # 正式文件（approved 才放）
_ai_drafts/            # AI 草稿
_research/             # 探索資料
_alternatives/         # 被比較但未採用的方案
_discarded/            # 已丟棄
```

---

## 對應 repo 的 sprint

這五輪是 [`.agents/WORKFLOW.md`](../../../.claude/skills/next/SKILL.md) 十站式 sprint 的決策視角：sprint 講「站點順序」，本流程講「每站誰發散、誰收斂、誰拍板」。
