<!-- CLAUDE_CODE_PROJECT_TEMPLATE_V5 -->

# Claude Code 專案初始化提示

> **版本:** v5.1 | **模式:** 人類主導 | **觸發方式:** Session 啟動時自動偵測

## 給 Claude 的指令

當你（Claude）在 session 啟動時看到這個檔案，請：

1. 顯示一行訊息：「偵測到 `CLAUDE_TEMPLATE.md`，這是個未初始化的專案模板。要開始 `/task-init` 嗎？」
2. 等待使用者確認
3. 同意後執行 `/task-init`，引導完成初始化
4. **`/task-init` 完成後刪除本檔案**（避免下次 session 重複觸發）

## 給使用者的說明

這個檔案是「初始化哨兵」 — 它的存在告訴 Claude「這個專案還沒設定」。
完成初始化後會被自動刪除。

完整的初始化流程定義在：
- `.claude/commands/task-init.md`（執行邏輯）
- `.claude/templates/CLAUDE-md.template.md`（CLAUDE.md 生成範本）
- `.claude/templates/project-structures.md`（專案結構選項）

## 記憶系統規則（重要）

初始化後的專案應遵循：
- 跨 session 技術發現 → `.claude/context/<area>/`（agent 自動寫入）
- 跨 session 工作交接 → `.claude/sessions/`（`/save-session` 手動）
- 可重用 pattern → `.claude/skills/learned/`（`/learn` 手動）
- **不使用** Auto-memory（`~/.claude/projects/.../memory/`），所有記憶留在專案內

詳見 `.claude/guides/MECHANISMS.md`。

<!-- CLAUDE_CODE_INIT_END -->
