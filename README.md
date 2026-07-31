# 循環工程

一套可以直接開工的 Claude Code 設定，加上教它怎麼來的課程。

```bash
git clone <this-repo> my-project && cd my-project
cp .mcp.json.example .mcp.json     # 用不到的整段刪掉
claude
```

進去打 `/next`，它會看你的專案現況給一個建議。**然後就可以開始做東西了。**

---

## 這裡沒有必經的關卡

`.claude/skills/` 裡有八個技能。它們是**參考書，不是流程圖**——任何順序取用，也可以完全不用。

| Skill | 什麼時候翻它 |
|---|---|
| `frame` | 題目還很模糊，想先問清楚再動手 |
| `spec` | 要定介面、資料結構、或別人要接的東西 |
| `evals` | 改了幾輪還在原地，或講不出「怎樣算變好」 |
| `tdd` | 要寫新功能或修 bug |
| `review` | 要 commit / 開 PR / 重構 |
| `ship` | 要部署或交給別人維護 |
| `decide` | 卡在選擇，或找不到根因 |
| `next` | 不知道現在該做什麼 |

領域知識放在 `.claude/references/`（資料層、介面、安全、維運、架構），**需要時再讀**。

---

## 唯一「你沒得選」的部分

五個 hook 擋的是不可逆的事：遞迴刪除、force push、`reset --hard`、在保護分支 commit、把 secret 寫進檔案。

寫進文件的規則大約有七成順從率。不可逆的操作不能賭剩下那三成——所以它們在 `.claude/hooks/`，不在建議裡。

**其餘全部是建議。**

---

## 課程

同一個 repo 也是一份 8 小時的課，教這套設定背後的判斷。

八站 `S0`–`S7`，主軸是**循環工程四拍**：劃邊界 → 放它跑 → 打分數 → 收判斷。
第一拍就是那三個問題（動哪些檔案、什麼算變好、幾輪後停），一天對六個不同對象各跑一次。

| | |
|---|---|
| 學員入口 | [`START-HERE.md`](./START-HERE.md) |
| 講師入口 | [`curriculum/instructor/prep.md`](./curriculum/instructor/prep.md) |
| 老師的完整成品 | [`labs/reference-project/`](./labs/reference-project/) |
| 可複製的積木 | [`labs/blocks/`](./labs/blocks/)（5 塊，47 個測試） |

**不上課也能用這套設定。** 課程只是解釋它為什麼長這樣。

---

## 想自己寫這些東西

`docs/authoring/` 有六種資產的撰寫指南：CLAUDE.md、rule、skill、command、hook、subagent，
外加一份[決策樹](./docs/authoring/07-choose-which.md)告訴你同一個需求該做成哪一種。

**會用是使用者，會寫才是工程師。**

---

## 結構

```
.claude/            skills / references / hooks / agents / rules / output-styles
docs/               setup（安裝與免費路線）· authoring（怎麼寫）· concepts（讀本）
curriculum/         八站課程 + 講師手冊 + 教具
labs/               參照專案 + 可複製積木
tasks/              backlog / 當前工作 / 已知問題
```

---

## 沒有 Claude Code 訂閱

[`docs/setup/02-free-routes.md`](./docs/setup/02-free-routes.md) 有三條路線與各自的代價。
先用官方免費額度試，多半夠。

---

## 授權

MIT。可商用、可改編，保留作者標示即可。

**這些設定是拿來改的。** 刪掉用不到的 skill 是正確做法，不是偷懶。
