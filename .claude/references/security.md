# 安全檢查

需要時查，不用先讀完。`review` 的安全鏡頭與 `ship` 的守門都指向這裡。

---

## 憑證

工作區：
```bash
rg -n --hidden -g '!.git' \
  -e 'sk-[A-Za-z0-9_-]{20,}' -e 'sk-ant-[A-Za-z0-9_-]{20,}' \
  -e 'ghp_[A-Za-z0-9]{30,}' -e 'AIza[A-Za-z0-9_-]{30,}' \
  -e 'AKIA[A-Z0-9]{16}' -e '-----BEGIN [A-Z ]*PRIVATE KEY-----'
```

歷史（比工作區更重要）：
```bash
git log --all --oneline --name-only --diff-filter=A -- '*.env' '*.env.*'
git log -p --all -S 'sk-' --oneline | head -40
```

翻到東西 → **先輪換那把 key**，再考慮清歷史。順序不能顛倒。

前端呼叫付費 API 一律走後端 proxy。key 進了 bundle 就是公開的。

---

## 輸入會流到哪裡

外部可控的輸入比你想的多：URL 參數、request body、header（含 `X-Forwarded-For`、`Referer`）、cookie、**上傳的檔名**（不只內容）、第三方 API 的回應、資料庫裡的舊資料。

逐一追蹤它們流到哪：

| 流向 | 風險 | 正確做法 |
|---|---|---|
| SQL | 注入 | 參數化查詢，不要字串拼接 |
| shell | 命令注入 | `subprocess` 用陣列，不用 `shell=True` |
| `eval` / `pickle` / `yaml.load` | 任意執行 | `json.loads`、`yaml.safe_load`；絕不 `eval` |
| 檔案路徑 | 路徑穿越 | 正規化後確認仍在允許目錄內 |
| HTML | XSS | 用框架預設跳脫；要放 HTML 就過白名單 |
| 伺服器發出的請求 | SSRF | 白名單網域，擋內網位址 |
| system prompt | prompt injection | 用標籤隔離，守則放 system、內容放 user |

追不到底的標「未知」，不要假設中間有人擋。

---

## 授權

**換個 id 能不能看到別人的東西**——這是最常見也最常漏的漏洞（IDOR）。

UI 上藏起來不算數。每個資源存取都要在後端檢查歸屬。

資源不存在與無權存取**都回 404**。回 403 等於告訴攻擊者「這個 id 存在」，可以拿來列舉。

其他：權限檢查是每個 endpoint 都做還是只在 UI？批次操作有逐項檢查嗎？有沒有忘了關的 debug endpoint？

---

## 認證

密碼用 bcrypt / argon2 / scrypt，不是 MD5 或 SHA1，也不是加密——**要不可逆**。慢是刻意的。

比對用常數時間函式。`==` 會洩漏「前幾個位元組對了」。

session 一定要有過期時間，而且要能一次踢掉某使用者的全部 session（改密碼、偵測到入侵時用）。

登入失敗時，帳號不存在與密碼錯誤**回同一個訊息**。分開回報等於提供帳號列舉的管道。

---

## 錯誤訊息

不要把 stack trace、SQL、內部主機名回傳給使用者。

對外訊息與對內細節分開：一個給人看且不含內部資訊，一個只進 log。

---

## 依賴

```bash
npm audit --omit=dev
pip-audit
govulncheck ./...
```

只回報 high / critical，而且只回報**你真的有用到那條路徑**的。

---

## 報告的形狀

阻擋項最多五個，每個附位置、證據（key 要遮罩）、**具體攻擊情境**（攻擊者做 X 就能拿到 Y，不是「可能有風險」）、修法。

**列出「不適用」的類別。** 這個專案沒有的風險要明講查過了，否則讀的人無法評估覆蓋範圍。

不要自動修。安全修補改錯比不改更糟。
