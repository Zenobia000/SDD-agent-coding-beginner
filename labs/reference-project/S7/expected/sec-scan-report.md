# `/sec-scan` 報告 — rate-digest

> 對照重點：**有沒有掃 git 歷史**，以及**有沒有「不適用」那一段**。
> 只講壞消息的報告，你無法評估它查了多少。

---

## 判定

**可以部署（0 個阻擋項）**

---

## 阻擋項

無。

---

## 建議項（可以之後修）

1. `requirements.txt` 沒有鎖版本（`requests` 沒寫 `==`）—— 供應鏈風險
2. SQLite 檔案權限是 644，建議改 600
3. cron log 會保留完整 URL，含 query string —— 目前沒有敏感參數，但要注意

---

## 五個維度的實際結果

### ① 憑證外洩 ✅

**工作區**
```bash
$ rg -n --hidden -g '!.git' -e 'sk-[A-Za-z0-9_-]{20,}' -e 'AIza[A-Za-z0-9_-]{30,}' \
     -e 'ghp_[A-Za-z0-9]{30,}' -e 'AKIA[A-Z0-9]{16}'
（無結果）
```

**git 歷史 ★（這段最重要，最常被跳過）**
```bash
$ git log --all --oneline --name-only --diff-filter=A -- '*.env' '*.env.*'
（無結果 —— .env 從未被提交過）

$ git log -p --all -S 'sk-' --oneline | head
（無結果）
```

> **已確認**：`.env` 從未進過版控，歷史中無憑證。
>
> **為什麼一定要掃歷史**：`git rm .env` 之後 key 仍在歷史裡。
> 公開 repo 等同外洩。**已經進歷史的 key，唯一正確的處理是立刻輪換那把 key**，
> 不是清歷史 —— 清歷史是善後，不是修補。

### ② 對外暴露面 — **不適用**

這個專案是 cron 執行的本機 script，**沒有對外 endpoint**。
沒有 CORS、沒有認證、沒有 debug endpoint 的問題。

### ③ 輸入處理 ✅

| 風險 | 狀態 |
|---|---|
| 注入 | ✅ SQLite 全用參數化查詢（`?` 佔位符），`grep -n 'execute(f"' src/` 無結果 |
| XSS | **不適用** —— 沒有 HTML 輸出 |
| 路徑穿越 | ✅ 檔案路徑全部來自設定檔常數，不接受外部輸入 |
| SSRF | ✅ **來源 URL 寫死在 `config/sources.yaml`，不接受執行期指定**（PRD Constraints 第 1 條） |
| 反序列化 | ✅ 用 `yaml.safe_load`，不是 `yaml.load` |

> SSRF 這條是設計時就擋掉的 —— 決策卡的「不做任意網站的通用爬蟲」
> 不只是範圍控制，**同時也是安全決策**。

### ④ 認證與授權 — **不適用**

單使用者本機工具，沒有登入、沒有多租戶、沒有 IDOR 的可能。

### ⑤ 依賴 ✅

```bash
$ pip-audit
No known vulnerabilities found
```

---

## 我沒能驗證的

- **上游三個網站的 TLS 憑證是否被中間人替換** —— 目前用 `requests` 預設驗證，
  沒有 pinning。查證方式：加一個測試比對憑證指紋。
  **未修的理由**：抓的是公開匯率，不是機密資料，風險可接受。

---

## 三層防線的分工（這次各擋到什麼）

| 層 | 這次擋到什麼 |
|---|---|
| ① `block-secret-write.sh` hook | S4 時擋下一次 —— AI 想把測試用的假 key 寫進 `config.py` |
| ② `.githooks/pre-commit` | 沒觸發 |
| ③ **本次掃描** | 沒發現阻擋項，但確認了歷史乾淨 |

**第一層擋掉的那次，就是沒有 hook 的話會外洩的那次。**
