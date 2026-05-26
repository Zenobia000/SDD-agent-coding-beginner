# Gemini CLI Memory 機制說明

> 這個資料夾**不存放檔案**，是給你的「使用說明」。Gemini 的 memory 由 CLI 自己管，不在 repo 內。

---

## 什麼是 Memory？

Gemini CLI 有一套「長期記憶」機制，跨對話保留特定資訊，不必每次重貼。

跟 `GEMINI.md` 的差別：

| 對比     | `GEMINI.md`        | Memory                  |
| ------ | ------------------ | ----------------------- |
| 存放位置   | repo 內，會 commit    | CLI 本機，不會 commit         |
| 適合放什麼  | 專案規則、團隊共識          | 個人習慣、跨專案 preference     |
| 誰會看到   | 所有 collaborator    | 只有你                     |
| 更新方式   | 編輯檔案 commit         | `/memory add` 或 `save_memory` |

---

## 三個必學指令

### 1. `/memory show` — 看 Gemini 現在記得什麼

```
/memory show
```

會列出：
- 載入的 `GEMINI.md` 內容
- 你自己加的 memory 條目

**用途**：當你覺得「AI 好像沒讀到規則」時，先跑這個確認。

### 2. `/memory add` — 主動讓 Gemini 記住

```
/memory add 我習慣用 pnpm 不是 npm
/memory add 這個專案的部署平台是 Cloudflare Pages
/memory add 我的時區是 Asia/Taipei
```

**用途**：個人習慣、跨對話偏好。

### 3. `/memory refresh` — 重讀 `GEMINI.md`

```
/memory refresh
```

當你**剛剛改完 `GEMINI.md`**，CLI 不會自動偵測，要手動 refresh。

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
- 專案規則（這些該寫 `GEMINI.md`，會跟著 repo 走）

---

## 五歲小孩版理解

把 `GEMINI.md` 想成「公司員工守則」（大家都要遵守、釘在牆上）。
把 Memory 想成「你自己的便利貼」（只貼在你的辦公桌上、別人看不到）。

**規則寫在守則，習慣寫在便利貼。**
