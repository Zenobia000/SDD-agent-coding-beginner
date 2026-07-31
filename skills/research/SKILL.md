---
name: research
description: 對技術問題查找高可信 primary sources，並把帶引用的結論保存成 Markdown artifact。當使用者要研究 API、套件、標準、相容性或需要把閱讀工作隔離到背景 context 時使用。
---

# Research

把研究工作交給背景 subagent，讓主 session 可以繼續。agent 的任務：

1. 先把問題改寫成可驗證的研究問題與時間/版本邊界。
2. 優先官方文件、標準、source code、release notes、first-party API 與原始論文；技術結論不能只依賴二手文章。
3. 每個會影響決策的 claim 都附直接來源 URL、版本或 commit；明確區分來源事實與推論。
4. 記錄互相矛盾的來源、未知與會讓結論翻盤的條件。
5. 寫成單一 Markdown 檔，位置依 `docs/agents/project.md` 或既有 research convention；沒有慣例時使用 `.scratch/research/<slug>.md`。

回報 artifact 路徑與三行結論。研究提供決策材料，不替使用者做不可逆選擇，也不直接實作。
