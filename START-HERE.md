# START HERE

> 這份文件一次只給你**一件事**。不要往下滑找別的，做完當下這件再回來。

---

## 你現在要做的事

**打開終端機，跑這三行。**

```bash
cp -r templates/claude_project_template my-first-loop
cd my-first-loop
claude
```

跑起來了 → 跳到 [S0 開機](./curriculum/S0-boot.md)。
`claude: command not found` → 先看 [安裝](./docs/setup/01-claude-code.md)（10–20 分鐘）。
沒有訂閱、想用免費的 → [三條免費路線](./docs/setup/02-free-routes.md)（15–40 分鐘，看你選哪條）。

---

## 今天會發生什麼（30 秒版）

你會跑 **八站**。每一站的結構都一樣：

```
讀結論卡（30 秒）→ 動手 → 打 /gate → 通過就進下一站
```

`/gate` 會告訴你「通過 / 缺什麼 / 下一步」。**不通過就別往前走**，卡住的成本比重做低。

---

## 八站地圖

只看你現在那一格，其他先不用管。

| | 站 | 你會做出 | 大概多久 |
|---|---|---|---|
| ☐ | [**S0 開機**](./curriculum/S0-boot.md) | 能跑的 `claude` + 專案骨架 | 30 分 |
| ☐ | [**S1 問對問題**](./curriculum/S1-frame.md) | `decision-card.md` | 55 分 |
| ☐ | [**S2 定契約**](./curriculum/S2-contract.md) | `docs/PRD.md` + `evals/eval-set.md` | 55 分 |
| ☐ | [**S3 先跑通**](./curriculum/S3-prototype.md) | 一個會動的 v0 | 40 分 |
| ☐ | [**S4 迴圈開工**](./curriculum/S4-loop.md) | v1 + 綠燈測試 | 90 分 |
| ☐ | [**S5 方法變資產**](./curriculum/S5-assets.md) | 你自己改過的 hook + command | 55 分 |
| ☐ | [**S6 積木裝配**](./curriculum/S6-blocks.md) | 全端 v2 | 45 分 |
| ☐ | [**S7 守門與交付**](./curriculum/S7-ship.md) | 資安報告 + 公開網址 | 25 分 |

做完一站就把 ☐ 塗掉。**看得到進度，比記得住進度重要。**

---

## 卡住的時候

按這個順序，**不要跳**：

1. **重讀那一站的「閘門」** —— 通常是你漏了其中一條
2. **打 `/gate`** —— 它會直接告訴你缺什麼
3. **對照老師的成品** —— `labs/reference-project/S<n>/expected/`
4. **打 `/explain-code`** —— 看不懂 AI 寫了什麼的時候用
5. **舉手 / 開 issue** —— 卡超過 10 分鐘就別自己撐

> **卡關不是你的問題，是這份教材的問題。**
> 卡住請開 issue 告訴我們卡在第幾步——這是最有價值的回饋。

---

## 三個今天會一直用到的東西

**① 循環工程四拍** —— 每一站都在跑這個
```
劃邊界 → 放它跑 → 打分數 → 收判斷
```

**② `/gate`** —— 每站結束打一次，判斷能不能往前

**③ 「已確認 / 推測 / 未知」** —— AI 講的每句話，你要能分辨它屬於哪一級

其他名詞（skill、hook、subagent、MCP…）**今天用到才學**，現在不用背。

---

## 給沒有時間跑完整天的人

只有 2 小時 → 跑 **S0 + S1 + S2**。
拿到 `decision-card.md` 和 `PRD.md` 就有收穫了——**問對問題本身就是產出**。

只有 4 小時 → 跑 **S0–S4**。你會有一個測試綠燈的 v1。

想直接拿工具不上課 → 回 [README 第三個入口](./README.md#三我只想拿那套-claude工程師)。

---

## 下一步

打開 [S0 開機](./curriculum/S0-boot.md)。
