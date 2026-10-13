# 模板庫

> 上課時用，回公司也能直接帶走。每一份都是**填空題**，`＜＞` 是要換掉的地方，`💡` 是提示。

| 檔案 | 什麼時候用 | 對應課程 |
|---|---|---|
| [`1_requirements_template.md`](./1_requirements_template.md) | 寫需求：痛點、User Story、驗收條件、待決事項 | Day 1 單元 4 |
| [`2_architecture_template.md`](./2_architecture_template.md) | 寫架構：系統邊界、AI 與規則的分工、ERD、API、技術決策 | Day 2 單元 6 |
| [`agent-rules/AGENTS.safe.md`](./agent-rules/AGENTS.safe.md) | 專案大腦：**通用安全模式**（套件、秘密、輸入驗證、AI 輸出） | Day 2 單元 7 |
| [`agent-rules/AGENTS.tdd.md`](./agent-rules/AGENTS.tdd.md) | 專案大腦追加：**TDD 強制模式**（先紅燈、不准改測試） | Day 3 單元 11 |
| [`hooks/`](./hooks/) | 把紅線從文字規則變成「做不到」 | Day 2 單元 7、Day 3 |

---

## 怎麼用

**規格模板**：複製到你的專案根目錄，去掉檔名的 `_template`。可以自己填，也可以讓 AI 照著格式填：

```text
用 @2-templates/1_requirements_template.md 的格式，
根據我們剛剛的討論產出 1_requirements.md。
模板裡的 💡 提示是寫給你的規則，要遵守，但不要出現在產出裡。
沒討論到的欄位，放進「待決事項」，不要替我決定。
```

**專案大腦**：

| 你用的是 | 怎麼放 |
|---|---|
| Codex | 複製成專案根目錄的 `AGENTS.md` |
| Claude Code | 同上，再建一個 `CLAUDE.md`，內容只有一行 `@AGENTS.md` |
| 兩個都用 | 同上，一份 `AGENTS.md` 兩邊共用 |

要 TDD 強制模式，就把 `AGENTS.tdd.md` 的內容接在 `AGENTS.safe.md` 後面。

---

## 這些模板刻意不做的事

- **不給範例答案。** 模板裡只有格式與提示，沒有填好的請假系統範例。填好的範例會被直接照抄，而你的公司規則和範例不一樣。
- **不求完整。** 模板只列這門課用得到的段落。真實專案需要更多段落時，自己加；用不到的段落，刪掉。
- **不寫無法檢查的規則。** 像「請寫出高品質的程式碼」這種句子，AI 讀了也不知道怎麼做，你也不知道它做到了沒。
