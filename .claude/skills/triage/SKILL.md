---
name: triage
description: 對外部進來的 bug reports、feature requests 與 PR 做狀態機式 triage，補足重現資訊並判斷是否可交給 agent。
disable-model-invocation: true
argument-hint: "issue/PR reference，或留空查看 queue"
---

# Triage

只 triage 外部進來、尚未整理的工作。`/to-tickets` 產生的 tickets 已可執行，不要再走本流程。

先讀 `docs/agents/project.md` 的 issue tracker 設定。沒有設定時採 read-only 探索並建議 `/setup-project`；不要猜外部 mutation 命令。

## Canonical roles

- `needs-triage`：尚未判讀。
- `needs-info`：缺少一個能改變判斷的關鍵資訊。
- `ready-for-agent`：範圍、重現/驗收與風險足以讓 agent 執行。
- `ready-for-human`：需要產品決策、權限、production 操作或不可逆取捨。
- `wontfix`：重複、無法重現、超出產品範圍或成本不合理，且理由已記錄。

每個 item 同時只能有一個 canonical role。

## 查看 queue

列出目前需要人處理的 items，依 role 分組；每項只顯示名稱、連結、目前缺口與建議下一狀態。不修改 tracker。

## Triage 單一 item

1. 讀完整 body、comments、linked PR/issue 與相關 code/history。
2. 判斷 request 是 bug、feature、support、duplicate 或無效輸入。
3. Bug 必須有最小重現、expected/actual、環境與可執行 feedback loop；feature 必須有 observable outcome、acceptance 與 out of scope。
4. 缺資訊時只問最能收斂的一題，使用 needs-info template；不要丟問卷。
5. 建議下一 role、理由與要新增的 notes。使用者確認後才更新外部 tracker。

`ready-for-agent` 不是「描述很長」，而是 fresh session 能從 issue 建立明確紅綠訊號。任何需要 human preference 的決策仍為 `ready-for-human`。
