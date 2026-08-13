---
name: diagram
description: 依受眾與情境挑選最合適的圖表並繪製，缺資訊時先畫草稿再問。當使用者要畫「架構圖」「泳道圖」「流程圖」「甘特圖」「時序圖」「循序圖」「ERD」「技術堆疊」「WBS」「網路架構圖」「部署圖」「里程碑」，或要為「會報」「簡報」「標案文件」準備圖表，或說「畫個圖」「用圖表呈現」時使用。
---

# Diagram

Pick the right representation for the audience, then draw it. Selection logic is
grounded in Taiwanese project-reporting practice (會報): the audience's concern
picks the diagram — not the catalogue of what you can draw. Producing every
diagram for everyone is the classic failure mode.

## 1. Pick by audience

First fork is **who will look at this**. Ask via AskUserQuestion when unclear.

| Audience | Their concern | Reach for |
| --- | --- | --- |
| 主管／客戶 (execs, clients) | schedule, shape, cost, why-do-this | Gantt, milestone chart, informal architecture block diagram, executive one-pager (高階總覽圖) |
| 標案／文件審查 (tender & document review) | responsibility, coverage, compliance | swimlane, network/deployment diagram, WBS |
| 工程師 (engineers) | contracts, data, interactions | sequence, use case, ERD, tech stack |

**Fourth exit — not a diagram.** Inventory and comparison questions are answered
by a markdown table or matrix, not a picture: system portfolios, capability ×
application coverage, baseline-vs-target gap grids. Offer the table; drawing it
would only blur it.

The **executive one-pager** is the consulting-style opening slide: horizontal
narrative bands read top-down as a pitch (e.g. 挑戰 → 目標 → 方案全貌 → 效益).
The band *skeleton* is the genre; what each band contains comes from the
audience's actual concerns, never from a fixed template. It is dense by
design — follow STYLE.md's executive one-pager section, not the projection
tiers.

For exec/client diagrams, be **deliberately imprecise**: high-level blocks, no
protocol names, no internal components. Precision there is noise, abstraction is
respect.

Vocabulary: say 技術堆疊, not 系統堆疊圖 — the latter is not a practitioner
term. C4 and TOGAF are discussed in Taiwan but rarely used in reporting; apply
them only when the user names them.

## 2. Pick the medium

| Diagram | Medium |
| --- | --- |
| Flow, swimlane, sequence, use case, ERD, Gantt, milestone | Mermaid |
| Architecture blocks, tech stack, network/deployment, WBS, executive one-pager | SVG |

- **Mermaid** — structure-heavy, cheap to revise, renders in markdown/artifacts.
- **SVG** — slide-bound diagrams that must look good projected and screenshot
  cleanly into PowerPoint: white ground, no interactive elements.

Both media follow [`STYLE.md`](STYLE.md) — read it before drawing. For SVG,
**load the `/svg-palette` skill via the Skill tool — mandatory** before choosing
any color; user-named brand colors override its default per its mapping rule.
When the harness offers `dataviz` or `artifact-diagramming` skills, follow their
rendering mechanics for charts and artifact SVGs; without them, STYLE.md is
self-sufficient — never block on their absence.

## 3. Draft first, then ask

Never interrogate against a blank page. Draw v1 from what is already known
(codebase, conversation, docs), mark every guess **on the diagram** (`?` suffix
or a dashed "假設" node), then ask about the marks. Closed choices (audience,
venue, orientation) go through AskUserQuestion; open facts are asked in prose.

**Gantt/milestone data** is schedule data the codebase cannot yield: pull the
issue tracker first (`gh issue list`, milestones, due dates — see
`docs/agents/issue-tracker.md` when present), draft from that, mark gaps `?`,
then ask. Only when there is no tracker at all does the schedule come entirely
from the user.

Iterate until no marks remain — an unresolved `?` on a delivered diagram is a
guess shipped as a fact.

## 4. Deliver

- Mermaid: fenced block in chat or the target markdown file. Apply the init
  directive from STYLE.md — the default font has no CJK and the default size is
  too small for slides.
- SVG: write the file, render via artifact when the user wants to view or
  screenshot it. viewBox and margins per STYLE.md.
- Labels: Traditional Chinese by default, tech nouns stay English
  (`訂單服務 Order Service`, `PostgreSQL`). All-English is fine when the
  audience is engineers.
- Before handing anything over, run STYLE.md's per-diagram checklist — it is
  the single list of what every delivered diagram must carry.
