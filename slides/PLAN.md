# SmartTrip FX／Antigravity｜開場 11 頁定稿

與 `claude` 分支共用同一套情境與流水線心智模型；口白與教材名稱改為 Antigravity（`agy`、`ANTIGRAVITY.md`、`.agents/`）。

> 圖檔由 Claude 線移植：畫面文字若仍寫 Claude Code／CLAUDE-CODE.md，課堂改念 **Antigravity／ANTIGRAVITY.md** 即可，結構不變。

## 設計系統

| 項目 | 決定 |
|---|---|
| 色 | 冷灰綠紙 `#E4E7E3`、鱷霧綠 `#6B7F6A`、冷青灰 `#5F7A7A`、沙陶 `#C4B8A8`、炭褐字 `#3A3735` |
| 對撞 | 對上一代暖玫瑰貓：這代更冷、偏探險 |
| 吉祥物 | 霧綠黏土鱷（沙陶肚）——帶路同伴 |
| 禁止 | Logo、高飽和色、整頁表格、紫霓虹 |

## 頁序與職分

| # | 檔名 | 標題 | 學生帶走一句 | 視覺 |
|---|---|---|---|---|
| 1 | `slide-01-situation-night.png` | 出國前那個晚上 | 錢包不厚，最怕換錯日圓現金 | 夜燈／薄皮夾；鱷看著「要換多少？」 |
| 2 | `slide-02-situation-pains.png` | 痛點不是旅遊 App | 分不清付現、unknown、匯率時機 | 三張痛點卡 |
| 3 | `slide-03-situation-bridge.png` | 所以我們不一次生完 | 模糊願望 → 可驗收數字 | 左模糊／右 ¥9,000+GOOD |
| 4 | `slide-04-vs-nocode.png` | 跟上一段差在哪 | No-code 練想清楚；這裡練 Agent 一小步建 repo | 左右對切（口白：Antigravity） |
| 5 | `slide-05-small-steps.png` | 這堂課在練什麼 | 一小步對話，不是一次生成 | 問→文件→票→紅→綠→下一片 |
| 6 | `slide-06-agent-loop.png` | 你跟 AI 怎麼分工 | AI 跑 loop；你給目標／邊界／驗收 | 四格 loop |
| 7 | `slide-07-components.png` | 元件怎麼互相接力 | Skill 按需、AGENTS.md／Rules 常駐、Agent 隔離、Hook 硬擋 | 軌道關係圖（對應 `.agents/`） |
| 8 | `slide-08-layers.png` | 為什麼要分層 | 不能全塞進一份 prompt | 常駐／按需／強制（Hook） |
| 9 | `slide-09-pipeline.png` | SmartTrip 流水線 | 一次只推一格 | contract→grill→spec→tickets→TDD→review→commit |
| 10 | `slide-10-artifacts.png` | 過程會長什麼文件 | 對話會消失，文件留下 | project.md／spec／issues／tests |
| 11 | `slide-11-start.png` | 今天怎麼開始 | 先 `ANTIGRAVITY.md` 再 `BUILD.md`；下階段才寫 skill | 清單＋預告（口白改書名） |

## 節奏

約 15–18 分鐘講完 → 進 `ANTIGRAVITY.md`。投影片不取代兩冊教材。
