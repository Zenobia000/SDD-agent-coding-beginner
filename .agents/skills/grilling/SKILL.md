---
name: grilling
description: 提供一次一題、沿決策樹推進的深度訪談紀律，用來挑戰計畫、釐清需求分支與定義 out of scope。當使用者要求挑戰想法或做需求訪談，或 `grill-with-docs`、`wayfinder`、`improve-codebase-architecture` 等 skill 需要一個決策迴圈時使用。這是可被其他 skill 內嵌的紀律層，不是獨立的產出流程。
---
# Grilling

這是給其他 skill 內嵌使用的訪談紀律，本身不產出 spec、ticket 或程式碼。

沿決策樹逐一訪談，直到雙方對目標、限制、失敗情境與 out of scope 有共同理解。

- 一次只問一題並等待回答；每題先提供推薦答案、理由與會翻盤的條件。
- 先解會阻擋其他問題的上游決策，再走下游分支。
- 可以從 filesystem、code、設定、log 或官方來源取得的事實自行查，不拿來問使用者。
- 產品偏好、風險容忍、不可逆取捨與優先順序屬於使用者；不得代答。
- 答案暴露新分支時，把它加到未決清單；分支失去意義時明確關閉。
- 定期重述已決定、未決與 out of scope，讓使用者能糾正誤解。
- 使用者確認共同理解前，不實作、不發布、不做外部變更。

結束時輸出精簡 decision record：目標、決策、驗收訊號、out of scope、open questions、建議下一步。
