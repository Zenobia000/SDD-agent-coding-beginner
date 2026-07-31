---
name: sec-scan
description: 交付前的資安掃描 —— 憑證外洩（含 git 歷史）、OWASP Top 10 高風險項、依賴漏洞、對外暴露面。產出可行動的修補清單，不是恐嚇清單。
when_to_use: 使用者說「要部署了」「上線前檢查」「安全嗎」「會不會外洩」「push 到公開 repo」，或準備跑 /ops-card、剛加了對外 API endpoint / 檔案上傳 / 使用者輸入處理。
argument-hint: [範圍，留空則掃全專案]
allowed-tools: Read, Glob, Grep, Bash
---

# /sec-scan — 交付前資安掃描

> **核心**：找出**這個專案真的會被打的地方**，不是背誦 OWASP 清單。

## 🚨 自動觸發訊號

### 強訊號
- 「要部署了」「上線前」「push 到 GitHub」「開 public repo」
- 剛加了：對外 endpoint / 檔案上傳 / 使用者輸入直接進 SQL 或 shell / 第三方 API 呼叫
- 使用者說「安全嗎」「會不會被駭」

### 反訊號
- 純前端樣式調整
- 本機一次性 script，不會部署也不會進版控

---

## 五個維度（依嚴重度排序，由上往下掃）

### ① 憑證外洩 —— 最優先，**要掃 git 歷史**

```bash
# 工作區
rg -n --hidden -g '!.git' \
  -e 'sk-[A-Za-z0-9_-]{20,}' \
  -e 'sk-ant-[A-Za-z0-9_-]{20,}' \
  -e 'ghp_[A-Za-z0-9]{30,}' \
  -e 'AIza[A-Za-z0-9_-]{30,}' \
  -e 'AKIA[A-Z0-9]{16}' \
  -e '-----BEGIN [A-Z ]*PRIVATE KEY-----'

# .env 是否曾被提交過（最常見的災難）
git log --all --oneline --name-only --diff-filter=A -- '*.env' '*.env.*' | head -20

# 歷史中的憑證（比工作區更重要 —— 刪掉檔案不會刪掉歷史）
git log -p --all -S 'sk-' --oneline | head -40
```

> **關鍵觀念**：`git rm .env` 之後 key 仍在歷史裡，公開 repo 等同外洩。
> **已經進歷史的 key，唯一正確的處理是「立刻輪換那把 key」**，不是清歷史。
> 清歷史（`filter-repo` / BFG）是善後，不是修補。

### ② 對外暴露面

- 有哪些 endpoint 不需要認證就能打？逐一列出並確認是刻意的
- 前端 bundle 裡有沒有 API key？（**前端呼叫 LLM / 付費 API 一律要走後端 proxy**）
- CORS 是不是 `*`？
- 有沒有 debug endpoint / `/admin` 忘了關？
- 錯誤訊息會不會吐出 stack trace 或 SQL 給使用者？

### ③ 輸入處理（OWASP 高風險項）

只查這個專案**真的有**的部分，沒有的直接標「不適用」：

| 風險 | 查什麼 | 正確做法 |
|---|---|---|
| **注入** | 字串拼接進 SQL / shell / eval | 參數化查詢；`subprocess` 用陣列不用 `shell=True`；**絕不 `eval`** |
| **XSS** | `innerHTML` / `dangerouslySetInnerHTML` / 樣板不跳脫 | 用框架預設跳脫；要放 HTML 就過白名單消毒 |
| **路徑穿越** | 使用者輸入拼進檔案路徑 | 正規化後檢查是否仍在允許目錄內 |
| **SSRF** | 使用者提供 URL 後由伺服器去抓 | 白名單網域；擋內網位址 |
| **Prompt injection** | 使用者內容直接進 system prompt | 用分隔標籤隔離 + 指揮鏈（守則放 system，內容放 user） |
| **反序列化** | `pickle.loads` / `yaml.load` 吃外部資料 | `yaml.safe_load`；不要 pickle 外部資料 |

### ④ 認證與授權

- 密碼有沒有雜湊？用的是 bcrypt / argon2 還是 MD5？
- session / token 過期時間設了嗎？
- **有沒有「換個 id 就能看別人資料」**（IDOR）—— 這是最常見也最常漏的
- 高風險操作（刪除、轉帳、改權限）有沒有二次確認？

### ⑤ 依賴

```bash
[ -f package.json ]     && npm audit --omit=dev
[ -f requirements.txt ] && pip-audit 2>/dev/null || echo "pip-audit 未安裝：pip install pip-audit"
[ -f go.mod ]           && govulncheck ./... 2>/dev/null
```

**只回報 high / critical**，且只回報**你真的有用到那條路徑**的。

---

## 輸出格式

```
## 判定
可以部署 / 不可部署（<N> 個阻擋項）

## 阻擋項（必須修完才能上線）

### 1. <一句話標題>
嚴重度：Critical / High
位置：<檔案:行號>
證據：已確認 —— <引用實際內容，key 要遮罩成 sk-ant-****>
攻擊情境：<具體到「攻擊者做 X 就能拿到 Y」，不要寫「可能有風險」>
修法：<可直接執行的指令或 diff>

## 建議項（可以之後修）
<最多 3 條，一行一條>

## 不適用
<這個專案沒有的風險類別，一行帶過，讓使用者知道你查過了>

## 下一步
<恰好一個動作>
```

---

## 硬規則

- ❌ **不准把 key 原文印出來** —— 一律遮罩（`sk-ant-****3f9a`），連在報告裡都不行
- ❌ **不准列「理論上可能有風險」** —— 每一條都要有具體攻擊情境
- ❌ **不准超過 5 個阻擋項** —— 超過就只列最嚴重的 5 個，並註明「修完再掃一次」
- ❌ **不准自動修改** —— 列出修法，讓使用者決定。安全修補改錯比不改更糟
- ✅ **一定要掃 git 歷史** —— 只掃工作區是最常見的假安全感
- ✅ 沒有的風險類別要**明講「不適用」**，讓使用者知道範圍

---

## 三層防線（本 skill 是第三層）

| 層 | 誰 | 什麼時候 | 擋什麼 |
|---|---|---|---|
| ① | `.claude/hooks/block-secret-write.sh` | 寫檔當下 | 明顯的憑證寫入 |
| ② | `.githooks/pre-commit` | commit 時 | 漏網的憑證、誤加的 `.env` |
| ③ | **本 skill** | 交付前 | 歷史、暴露面、邏輯漏洞、依賴 |

前兩層是機械的、便宜的；本 skill 是**需要判斷**的那一層。

---

## 相關

- 部署與維運 → `/ops-card`
- 需要第二意見 → 派 `security-auditor` subagent
- 五維度品質驗證（含 security 一項）→ `/verify`
