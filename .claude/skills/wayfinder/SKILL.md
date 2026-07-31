---
name: wayfinder
description: 把超過單一 session、路線仍在迷霧中的大型工作建立成 decision map，逐張解決阻塞決策，直到能進入規格階段。
disable-model-invocation: true
argument-hint: "大型目標，或既有 map reference"
---

# Wayfinder

Wayfinder 處理「還不知道怎麼走」的大型工作，不直接建置 destination。每張 ticket 解一個 decision，不是 implementation slice；路線清楚後交給 `/to-spec`。

先讀 `docs/agents/project.md` 的 tracker。沒有設定時，使用 `.scratch/<effort>/map.md` 與 `decisions/` 本地檔案；任何外部 tracker mutation 都要先預覽並取得確認。

## Map

```markdown
# <Effort name>

## Destination
走出迷霧時會得到什麼：可寫的 spec、已定案的 decision 或可執行 migration plan。

## Notes
共同 glossary、必用 skills、constraints 與風險界線。

## Decisions so far
- [Decision title](link) — 一行結論；細節只存在 decision ticket。

## Not yet specified
- 看得見方向但現在還不能精確成問題的 fog。

## Out of scope
- 明確在 destination 外的內容與理由。
```

Map 是索引，不重複 ticket detail。人類可讀內容永遠用 linked title，不用裸 `#42` 代稱。

## Decision tickets

每張只包含一個能在新 session 回答的 `## Question`，並標類型：

- `research`（AFK）：primary-source fact finding，使用 `research`。
- `prototype`（HITL）：用可互動 artifact 提高討論 fidelity，使用 `prototype`。
- `grilling`（HITL）：產品/設計取捨，使用 `grilling` + `domain-modeling`。
- `task`（AFK/HITL）：不產出 destination，只完成會解除決策阻塞的必要動作。

Ticket 具有 blocking edges。frontier 是 open、unblocked、unclaimed tickets。無法精確寫成 question 的內容留在 fog，不要過早切票。

## 模式 A：建立 map

1. 使用 `grilling` + `domain-modeling` 先定 destination；它決定 scope。
2. breadth-first 掃描決策空間，區分已可精確的 questions 與 fog。若整條路已能在一個 session 說清楚，停止並建議 `/grill-with-docs`，不要製造 map。
3. 預覽 map、tickets、types 與 edges，核准後建立；先建 tickets 取得 identifiers，再第二輪 wiring。
4. research tickets 可平行委派，其餘不在建立 map 的 session 解決。

## 模式 B：推進 map

1. 只載入 map 低解析摘要；使用者沒指定 ticket 時取第一張 frontier。
2. 在任何工作前 claim ticket，避免並行 session 重複處理。
3. 按 type 解決，必要時按需讀相關 closed decisions，不把整張 map 灌進 context。
4. 將答案放在 ticket resolution，關閉 ticket，map 只新增 linked one-line gist。
5. 答案讓 fog 變清晰時再新增 tickets/wiring；越過 destination 的項目移到 Out of scope。

每個 session 最多解一張非 research ticket。所有決策完成、fog 清空且 destination 可直接規格化時，停止並建議 `/to-spec`；不要跳過規格直接 `/implement`。
