# API Contract Template

> **Layer 2 spec（介面層）— 系統邊界的合約**
> 大廠對標：**OpenAPI 3.0**（業界標準）+ **Stripe-style Error Conventions**（最被引用的錯誤設計）+ **Google API Design Guide**（命名/分頁）
> 寫作時機：任何新增 / 修改 endpoint 時。**先寫合約、後寫實作**。
> 觸發 skill：`/spec-it`（生草稿）、`/sync-it`（同步漂移）

---

## 1. API Design Principles（採用 Google API Design Guide）

| 原則 | 落實方式 |
|---|---|
| **Resource-oriented** | URL 以名詞為主：`/articles`、`/articles/{id}/summary` |
| **Consistent verbs** | GET（讀）/ POST（建）/ PATCH（部分更新）/ PUT（取代）/ DELETE（刪） |
| **Plural nouns** | `/articles` 而非 `/article` |
| **kebab-case URL** | `/api/news-articles` 而非 `/newsArticles` |
| **snake_case body** | JSON field 用 `created_at` 而非 `createdAt`（或全專案統一一種） |
| **Versioning** | URL prefix：`/v1/articles`、`/v2/articles` |

---

## 2. Authentication

```http
Authorization: Bearer <api_key>
```

或：

```http
X-API-Key: <api_key>
```

**選 1 種、全 API 一致**。不要混用。

---

## 3. Common Response Envelope（採 Stripe 風格）

### 成功回應

```json
{
  "object": "article_summary",
  "data": {
    "id": "sum_abc123",
    "summary": "...",
    "word_count": 95,
    "created_at": "2026-05-27T11:30:00Z"
  }
}
```

### List 回應（含 cursor pagination — Google 推薦）

```json
{
  "object": "list",
  "data": [ ... ],
  "has_more": true,
  "next_cursor": "cursor_xyz789"
}
```

### 錯誤回應（Stripe-style）

```json
{
  "error": {
    "type": "invalid_request_error",
    "code": "input_too_long",
    "message": "Article content exceeds 10000 characters.",
    "param": "content",
    "doc_url": "https://docs.example.com/errors/input_too_long"
  }
}
```

---

## 4. Standard Error Types（Stripe 分類）

| HTTP | error.type | 何時用 |
|---|---|---|
| 400 | `invalid_request_error` | request 格式錯、缺欄位、欄位型別錯 |
| 401 | `authentication_error` | API key 缺失 / 失效 |
| 403 | `permission_error` | 已認證但無權限 |
| 404 | `not_found_error` | 資源不存在 |
| 409 | `conflict_error` | 與當前 state 衝突 |
| 429 | `rate_limit_error` | 超過配額 |
| 500 | `api_error` | server 內部錯（不暴露細節） |
| 503 | `service_unavailable` | 下游 service（如 LLM provider）掛掉 |

---

## 5. Endpoint List

| Method | Path | 用途 | Auth | 對應 US |
|---|---|---|---|---|
| POST | `/v1/summaries` | 建立摘要 | 必要 | US-001 |
| GET | `/v1/summaries/{id}` | 取得摘要 | 必要 | US-002 |
| GET | `/v1/summaries` | 列出歷史 | 必要 | US-003 |
| DELETE | `/v1/summaries/{id}` | 刪除摘要 | 必要 | US-004 |

---

## 6. Endpoint Schema（每個 endpoint 一段）

### POST /v1/summaries

**Request：**

```json
{
  "content": "string, required, 100-10000 chars",
  "target_language": "string, optional, default='zh-TW', enum=['zh-TW','en','ja']",
  "max_words": "integer, optional, default=100, range=[50,300]"
}
```

**Response 200：**

```json
{
  "object": "summary",
  "data": {
    "id": "sum_xxxxx",
    "summary": "string",
    "word_count": "integer",
    "source_language": "string (auto-detected)",
    "target_language": "string",
    "created_at": "ISO 8601 timestamp"
  }
}
```

**Response 400：** `invalid_request_error` — content 太短 / 太長 / 缺失
**Response 429：** `rate_limit_error` — 每分鐘超過 10 次
**Response 503：** `service_unavailable` — LLM provider 掛掉

**對應 BDD scenarios：** `tests/summary.feature` 的 Scenario 1-4

---

## 7. Rate Limiting

```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 42
X-RateLimit-Reset: 1716800000
```

超過配額時回 429 + `Retry-After: 30` header。

---

## 8. Versioning Policy

- 新版 = 新 URL prefix（`/v2/...`），舊版至少維持 6 個月
- Breaking change 必開新版本：移除欄位、改欄位型別、改 endpoint URL、改 auth 機制
- Non-breaking change 可直接加在現有版本：新增 optional 欄位、新增 endpoint、新增 enum 值

---

## 9. Idempotency（建議高風險 endpoint 加）

```http
Idempotency-Key: <client-generated-uuid>
```

POST 同一個 idempotency key 兩次 → 第二次直接回第一次的結果，不重複處理。
**只對「會產生副作用」的 endpoint 啟用**（建立、扣款、發送）。

---

## 10. Deprecation Process

廢棄 endpoint 時：

1. 回應加 `Deprecation: true` header 與 `Sunset: <date>` header
2. 在 `docs/CHANGELOG.md` 寫明
3. 文件加 `deprecated: true` frontmatter
4. **至少 3 個月後**才實際移除

---

## 寫作檢查清單

- [ ] 所有 endpoint 用名詞 + 動詞分離（不是 `/getArticle`）
- [ ] 統一一種 Auth 機制
- [ ] Response envelope 一致（success / error / list 三種）
- [ ] 每個 endpoint 有對應 user story
- [ ] 每個 endpoint 有對應 BDD scenario
- [ ] 錯誤類型用 Stripe 標準
- [ ] 列出已知的 rate limit
- [ ] Breaking change 有明確 versioning 計畫
