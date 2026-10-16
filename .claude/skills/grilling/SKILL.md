---
name: grilling
description: 就一個計畫、決策或想法窮追不捨地拷問使用者。當使用者想壓力測試自己的思路、想被質疑一個設計，或說出 "grill"、「拷問我」、「戳破我」這類觸發語時使用。
---

# Grilling

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

**Respond in the session's language.** This file is English; the interview is not. Questions, recommendations, and the final summary follow the language the user is speaking.

## Rounds and the frontier

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled — the questions you can ask *now* without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree — settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a *later* round, not this one.

## Facts and decisions

Finding *facts* is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it — don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report — ask the rest of the frontier now. The *decisions* are the user's — put each to them and wait.

This split matters most when another skill runs this loop inside its own frame. Being told to explore is not license to answer decisions autonomously.

## Completion

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed — resolved, or explicitly deferred with a note on what would settle it later. Summarise the resolved decision tree, then stop: do not act on any of it until the user confirms you have reached a shared understanding.
