# Antigravity CLI Memory 機制說明

> 這個資料夾**不存放檔案**，是給你的「使用說明」。Antigravity 的 memory 由 CLI 自己管，不在 repo 內。

---

## 什麼是 Memory？

Antigravity CLI（`agy`）繼承了 Gemini CLI 的「長期記憶」機制，跨對話保留特定資訊，不必每次重貼。

跟 `AGENTS.md` 的差別：

| 對比     | `AGENTS.md`        | Memory                  |
| ------ | ------------------ | ----------------------- |
| 存放位置   | repo 內，會 commit    | CLI 本機，不會 commit         |
| 適合放什麼  | 專案規則、團隊共識          | 個人習慣、跨專案 preference     |
| 誰會看到   | 所有 collaborator    | 只有你                     |
| 更新方式   | 編輯檔案 commit         | `/memory add` 或 `save_memory` |

---

## 三個必學指令

### 1. `/memory show` — 看 Antigravity 現在記得什麼

```
/memory show
```

會列出：
- 載入的 `AGENTS.md` 內容
- 你自己加的 memory 條目

**用途**：當你覺得「AI 好像沒讀到規則」時，先跑這個確認。

### 2. `/memory add` — 主動讓 Antigravity 記住

```
/memory add 我習慣用 pnpm 不是 npm
/memory add 這個專案的部署平台是 Cloudflare Pages
/memory add 我的時區是 Asia/Taipei
```

**用途**：個人習慣、跨對話偏好。

### 3. `/memory refresh` — 重讀 `AGENTS.md`

```
/memory refresh
```

當你**剛剛改完 `AGENTS.md`**，CLI 不會自動偵測，要手動 refresh。

---

## 該記什麼？不該記什麼？

### ✅ 適合存進 Memory

- 個人工具偏好（pnpm / yarn / npm）
- 跨專案的常用設定（時區、語言）
- 你經常忘記提的限制（「我電腦沒 Docker」）

### ❌ 不該存進 Memory

- API Key、密碼、token（這些是 secrets，會洩漏）
- 個資（電話、地址、Email）
- 一次性任務細節（這次 bug 是因為 ___）
- 專案規則（這些該寫 `AGENTS.md`，會跟著 repo 走）

---

## 從 Gemini CLI 搬過來的 memory 怎麼辦？

`agy plugin import gemini` 會把舊有 memory 條目一併搬到新位置（`~/.gemini/antigravity-cli/memory/`，過渡期沿用 `.gemini/` 路徑）。**不會遺失**，你只需要在第一次啟動 `agy` 時選「Import extensions from Gemini CLI」就好。

---

## 五歲小孩版理解

把 `AGENTS.md` 想成「公司員工守則」（大家都要遵守、釘在牆上）。
把 Memory 想成「你自己的便利貼」（只貼在你的辦公桌上、別人看不到）。

**規則寫在守則，習慣寫在便利貼。**
