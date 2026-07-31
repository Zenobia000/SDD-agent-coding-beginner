---
name: prototype
description: 建立明確標為 throwaway 的可執行 prototype，回答一個紙上無法決定的 state/logic 或 UI 問題。當使用者要 sanity-check 互動、比較介面方向或驗證狀態模型時使用。
---

# Prototype

Prototype 只回答一個設計問題，不是 production 起點。

## 選分支

- 「state/logic 是否合理？」：做最小 terminal app 或 harness，可依序觸發關鍵事件並在每步顯示完整 state。
- 「UI 應該長什麼樣？」：在同一路由提供至少三個真正不同的 variation，用 query param 或小型 switcher 切換，讓使用者直接比較。

問題不明且使用者不在線時，依周邊 code 推斷並在 artifact 第一行寫出假設。

## 規則

1. 檔名或路由明確含 `prototype`，放在接近目標 module 的位置。
2. 提供一個可複製執行的命令。
3. 預設只用 memory；若問題本身需要 persistence，使用可安全清除的 scratch 資料。
4. 不補 production error handling、abstraction、完整 tests 或 polish；只做到足以回答問題。
5. 使用者看過後記錄 question、verdict、被拒絕方案與帶回 production 的 decision。
6. 未經使用者同意不把 prototype 搬成正式 code。採納結論後，移除主分支的 throwaway artifact，或依使用者指定保存到 throwaway branch。
