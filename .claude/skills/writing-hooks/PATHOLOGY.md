# Hook Pathology and Skeletons

Evidence base for [SKILL.md](SKILL.md)'s rules, extracted 2026-08-06 from a real project's `.claude/` after ~2 weeks of operation: 6 hooks, 2,929 lines of hook log, and **zero** interceptions. Every number below was measured against those logs.

## The three rot modes

All three share one root cause: nothing verified the hook's own health. All three went unnoticed until an audit.

### Mode A — wrong JSON field: 100% idle

```bash
# ❌ the hook read:
USER_INPUT=$(echo "$INPUT" | jq -r '.content // .message // ""')
# UserPromptSubmit's field is `prompt` — USER_INPUT was always empty
```

Measured: 84 firings, **0** entries into any processing branch. Meanwhile the hook printed "hook fired / hook done" into context every time — a hook with no working function using its only output to convince everyone it works. Status broadcasts are not just waste; they are active deception.

### Mode B — the rule expired, the hook still guards it

A blocking hook (exit 2 power) guarded paths deleted in an architecture rewrite, and its stderr message directed the model to a directory that no longer existed, citing an ADR already superseded. Measured: **0** blocks logged, ever. Only luck — the watched path prefix was deleted too, so the condition never fired. Had it fired, it would have authoritatively steered the model into a dead directory. This mode is worse than A because it carries authority.

### Mode C — gated on a file that does not exist

Two hooks wrapped their main logic in `[ -f "$DIR/project.json" ]` — and that file was never created. The elaborate "review checkpoint" UI behind the gate displayed **0** times; one hook still executed the dead conditional 673 times. Insidious because it looks like graceful degradation ("skip if not initialized") while the feature has simply never been live.

**The countermeasure for all three is the same**: a fixture-fed test per hook, asserting decisions (Mode A dies on the first assertion), plus re-running it on every PR (Modes B and C surface the day the world changes underneath).

## The four-layer skeleton

Cheapest guard first; the expensive read happens only after every gate passes. Stderr on block tells the model what to do instead — never only what is forbidden.

```bash
#!/usr/bin/env bash
# PreToolUse: Write|Edit — exit 0 allow, exit 2 block (stderr goes back to the model)
INPUT=$(cat)

# 1. Dependency absent → fail open, leave a trace
command -v jq >/dev/null 2>&1 || { log "jq missing, off duty"; exit 0; }

TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // ""')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')

# 2. Wrong tool → out (the matcher may be broader than you think)
case "$TOOL_NAME" in Write|Edit) ;; *) exit 0 ;; esac

# 3. Path outside jurisdiction → out (cover absolute AND relative forms)
case "$FILE_PATH" in *"/agent/"*|"agent/"*) ;; *) exit 0 ;; esac

# 4. Only now read content — Write carries .content, Edit carries .new_string;
#    checking one of the two leaves a back door
CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // .tool_input.new_string // ""')

if <violation>; then
  log "BLOCK: $FILE_PATH"
  echo "🔒 <rule name>: <one line why>" >&2
  echo "<what to do instead, with a live authority reference>" >&2
  exit 2
fi
exit 0
```

The authority reference in the stderr message is itself a rot surface (Mode B): when the ADR or directory it cites is retired, the hook starts lying with authority. Keep such references minimal, and let the hook's test pin the message.

## Observability patterns

From the one well-built hook in the source project (an agent-activity logger). Worth copying when you build an observer:

- **One script, both events** — `PreToolUse` and `PostToolUse` point at the same file; branch on `.hook_event_name`, pair records via `tool_use_id`.
- **Early exit** — `[ "$TOOL_NAME" != "Agent" ] && exit 0` even though the matcher should guarantee it; matchers drift.
- **Truncate, but record the original length** — `"...[truncated, total ${#PROMPT} chars]"`; how much was cut is itself signal.
- **Build JSON with `jq -nc --arg`, never string concatenation** — prompts contain quotes and newlines as a matter of course. The `-c` flag matters: default pretty-print turned one `.jsonl` into 347 physical lines holding 33 objects, silently breaking every line-based tool (`wc -l`, `tail`, `grep`, log rotation). A file extension is a promise; tools' defaults do not keep it for you. After writing the first record, `wc -l` must equal the object count.

What such a log buys: the source project *defined* 15 specialized agents, and the log showed 76% of real calls used `general-purpose` — a fact nobody knew and the strongest possible argument for deleting agent definitions. Observers do not change behavior; they reveal that what you think you use and what you actually use differ.
