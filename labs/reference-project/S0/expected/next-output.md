# `/next` 的預期輸出（節錄）

對照重點：**八個 skill 名稱都要出現**。建議內容會依你的專案現況不同。

---

## 八個 skill

```
frame   題目還很模糊，想先問清楚再動手
spec    要定介面、資料結構、或別人要接的東西
evals   改了幾輪還在原地，或講不出「怎樣算變好」
tdd     要寫新功能或修 bug
review  要 commit / 開 PR / 重構
ship    要部署或交給別人維護
decide  卡在選擇，或找不到根因
next    不知道現在該做什麼（你剛打的這個）
```

## 領域參考

```
references/data.md          資料層與管線
references/ui.md            介面與六種狀態
references/security.md      安全檢查
references/ops.md           部署與維運
references/architecture.md  架構與重構
```

## 可以派出去的工作

```
explorer            在陌生 code 裡找東西
test-writer         為既有 code 補測試
reviewer            獨立視角的審查
security-auditor    高風險改動的深度推演
```

## S0 時的預期建議

```
你現在有：一套完整的 .claude/，但還沒有題目
你現在缺：一個框好的問題

建議：frame
為什麼：後面所有技能都需要一個「要做什麼」當輸入

下一步：說一句你想解決的痛點，我們開始
```

---

## 沒看到這些的話

| 症狀 | 原因 |
|---|---|
| 完全沒反應 | 你不在 repo 根目錄開的 `claude` |
| 只列出幾個 | `.claude/skills/` 不完整，重新 clone |
| 說找不到 `/next` | `.claude/skills/next/SKILL.md` 不存在 |

---

## 一個容易誤解的地方

`/next` 給的是**建議**，不是指令。

你完全可以無視它直接開始寫 code——**這套設定沒有必經的關卡**。
它存在的意義是「不知道下一步時有個地方問」，不是「每一步都要先問過它」。
