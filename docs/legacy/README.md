# 退役內容存檔

這裡放的是重構前的教材與設定，**只讀，不維護**。

保留的理由：用舊版開過課的人需要對照；有些內容（例如 AGENTS.md 方法論）
在新版被拆散到多處，想看完整論述時這裡還有。

## 有什麼

| 內容 | 原本是什麼 | 現在對應到哪 |
|---|---|---|
| `_source/core_curriculum.md` | M0–M5 一日工作坊核心教案 | `curriculum/README.md` + `instructor/prep.md` |
| `_source/teaching_plan.md` | 8 小時逐段流程 | `curriculum/S*.md` + `instructor/timing.md` |
| `_source/slides_outline.md` | 52 張投影片大綱 | `curriculum/slides/`（待重製） |
| `_source/AGENTS-GUIDE.md` | 怎麼寫 AGENTS.md 的方法論 | `docs/authoring/00-write-a-claude-md.md` |
| `_source/SKILLS.md` | Skill 完整教學 | `docs/authoring/02-write-a-skill.md` |
| `_source/SUBAGENTS.md` | Subagent 教學 | `docs/authoring/05-write-a-subagent.md` |
| `_source/HANDBOOK.md` | 模板使用手冊 | `README.md` + `.claude/skills/next/` |
| `_source/ai_ready_repo_blueprint.md` | 模板設計哲學 | `docs/authoring/README.md` |
| `_source/prompts/` | 四份對話開場白模板 | 併入對應 skill |
| `_source/check-key.md` | 部署前金鑰檢查 | `.claude/references/security.md` |
| `_source/terminal_configuration.md` | 終端機工作站設定 | 已淘汰（Antigravity 時代） |
| `_source/種子簡報.md` | SmartTrip FX 種子簡報 | `labs/reference-project/` |

## 兩個主要的退役框架

**STRIKE 提示詞戰法** —— 六字訣的 prompt 框架。退役理由：新版主張
「問對問題與架構設計比寫 prompt 值錢」，而 STRIKE 的位置被
CTCO 四格 + 七欄位 spec 取代（後者的 Success criteria 能直接接考卷，
STRIKE 沒有這條線）。內容在 `_source/core_curriculum.md` §7 框架 2。

**Antigravity（`agy`）工具鏈** —— Google 的 agent-first IDE 與 CLI。
退役理由：工具收斂到 Claude Code 一個，把省下的時間拿去教流程。
方法本身（AGENTS.md 慣例、MCP、Skills）在新版都還在，只是換了平台。

## 這裡的連結會壞

`_source/` 裡的相對連結指向已經不存在的路徑。**這是刻意的** ——
修好它們等於維護退役內容，而那會讓人以為它還在支援。

需要看原始樣貌時，用 git 歷史：

```bash
git log --oneline --all -- templates/antigravity_project_template
git show <commit>:templates/antigravity_project_template/AGENTS.md
```
