# Prompt：上線給朋友看

> 專案在本機跑得起來了，想放到網路上讓朋友打開網址就能用時用。

---

## 推薦方案：Cloudflare Pages（最簡單，免費）

### 模板（複製這段）

```
我的專案已經通過 /verify、本機可以跑。
現在我想把它部署上線，讓人用網址就能打開。

請幫我用「Cloudflare Pages」部署，因為它免費、快、不用信用卡。

請給我「逐步操作指引」，包含：

1. 我要先做什麼準備（要不要註冊帳號？要不要裝什麼工具？）
2. 一步一步的操作（每步驟告訴我「點哪個按鈕、輸入什麼」）
3. 部署完之後我會拿到什麼網址
4. 之後我改了 code，要怎麼更新線上版本

注意：
- API Key / secret 一律走環境變數，**不要**進前端 bundle 或 commit
- 我不要用需要信用卡的服務
- 如果有後端，請一併說明後端怎麼部署、環境變數怎麼設
- 每個 git / CLI 指令請完整寫出並解釋它在做什麼

請開始。
```

---

## 部署前自我檢查

- [ ] `/verify` 全綠（format / lint / type / test+coverage / security）
- [ ] `/sec-scan` 通過——無 secret 寫死、無 placeholder、`.gitignore` 覆蓋 `.env`
- [ ] `/sync-it` 無 drift——部署的 code 與 PRD / api-contract 一致

---

## ⚠️ API Key 安全（循環工程 正解）

**絕不把 API Key 寫進前端 code 上線**——公開 = 被盜刷。正解依架構：

**有後端**（循環工程 專案多數情況）：
- API Key 放部署平台的 **Environment Variables**（Cloudflare/Vercel 後台設定）
- 前端呼叫自己的後端 `/api/...`，後端代呼叫 LLM，金鑰不出後端

**純靜態無後端**（小工具）：
- 用 serverless function（Cloudflare Workers / Pages Functions）當 proxy
- 金鑰放 Workers 的 environment variables，前端只打自己的 function endpoint

**要 AI 幫你改？貼這句**：
```
我要上線了，請幫我把 API Key 改成走後端 / serverless proxy（環境變數讀取），
不要讓金鑰出現在前端 bundle。改完跑 /sec-scan 確認。
```
