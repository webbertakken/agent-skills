---
name: context-optimizer
description: >-
  Audit and optimise Claude Code context window usage. Estimates token breakdown,
  identifies waste (duplicate skills, overlapping rules, bloated agent files, dirty git
  status, MCP server overhead), and provides actionable recommendations with projected
  savings. Use when the user says "context checkup", "reduce context", "check context",
  "context audit", "how big is my context", or when sessions feel sluggish.
---

# Context optimizer

Audit the current session's context window and produce actionable recommendations to reduce waste.

## Process

### 1. Estimate token usage

Read the following sources and estimate token counts (1 token ~ 4 characters / 0.75 words):

| Source | Where to find it |
|---|---|
| Global CLAUDE.md | `~/.claude/CLAUDE.md` |
| Project CLAUDE.md / AGENTS.md | Repo root `CLAUDE.md`, `AGENTS.md` |
| Skill metadata | Count skills listed in the system reminder |
| Git status snapshot | Run `git status` and measure output |
| MCP server tool definitions | Check `~/.claude/mcp.json` — each server injects tool schemas every turn |
| Conversation history | Estimate from turn count and average turn length |

Present a summary table:

```
Context usage estimate
--------------------------------------------
System prompt + tools     ~X,XXX tokens
  CLAUDE.md (global)        ~X,XXX
  AGENTS.md (project)       ~X,XXX
  Skill metadata (N skills) ~X,XXX
  MCP tool schemas          ~X,XXX
Git status snapshot       ~X,XXX tokens
Conversation so far       ~X,XXX tokens
--------------------------------------------
Total                     ~XX,XXX tokens
```

### 2. Run checks

Run each check below. For every finding, note the estimated token saving.

#### 2a. Duplicate skills

Glob `~/.claude/skills/*/SKILL.md` and `.claude/commands/**/*.md`. Flag skills with overlapping
descriptions or that are aliases of the same workflow (e.g. `openspec-*` vs `opsx:*`).

#### 2b. Overlapping rules (global vs project)

Compare `~/.claude/CLAUDE.md` with the project's `CLAUDE.md` / `AGENTS.md`. Flag rules that appear
in both — these are injected twice per turn. List each redundant section with its approximate token
cost.

#### 2c. Agent file length

If either `~/.claude/CLAUDE.md` or `AGENTS.md` exceeds 250 lines, recommend compressing without
losing important rules. Suggest:

- Remove examples that illustrate obvious patterns (Claude already knows these)
- Collapse verbose explanations into one-liners
- Move reference-heavy sections to files loaded on demand

Explain progressive disclosure: Claude Code loads instructions in layers — metadata always, body
when triggered, references on demand. Rules in agent files are "always loaded", so every line costs
tokens on every turn. Content that's only needed sometimes should live in separate files that Claude
reads when relevant (self-discovery).

#### 2d. MCP server overhead

Check `~/.claude/mcp.json` for configured servers. Each server injects its full tool schema into
context every turn. Flag servers whose tools overlap with:

- Built-in tools (Read, Write, Edit, Glob, Grep, Bash, WebFetch, WebSearch)
- Installed skills that cover the same workflow

Recommend disabling redundant MCP servers or replacing them with lighter skills/CLI tools.

#### 2e. Git status hygiene

Run `git status --porcelain` and count entries. Flag:

- **Dirty working tree with 20+ changes** — suggest committing WIP to a feature branch
- **Stale untracked files** — `PROMPT.md` from previous session resets, temp files, build artefacts
- **Staged deletions not committed** — files removed from disk but still tracked

#### 2f. Agent communication file bloat

Check for team communication files (e.g. `~/.claude/teams/*/`) that accumulate during long
sessions. Flag files that have grown large.

#### 2g. SKILL.md body size / reference inlining

Scan `~/.claude/skills/*/SKILL.md` for bodies exceeding 200 lines. Flag skills that embed detailed
reference content (schemas, long examples, lookup tables) that could be split into `references/`
files for progressive disclosure.

#### 2h. Session length check

If the conversation appears to exceed ~200k tokens (very long sessions with many agent turns),
recommend running `/session-reset` to preserve context and start fresh. Agent effectiveness
degrades significantly above 200-500k tokens.

### 3. Present recommendations

Group findings by impact (high / medium / low) based on estimated token savings. For each:

- What: the issue
- Cost: estimated tokens wasted per turn
- Fix: specific action to take
- Projected saving: tokens recovered

End with a **before/after summary**:

```
Projected savings
--------------------------------------------
Before (current)          ~XX,XXX tokens
Duplicate skills            -X,XXX
Overlapping rules           -X,XXX
MCP server overhead         -X,XXX
Git status cleanup          -X,XXX
Agent file compression      -X,XXX
Skill body splitting        -X,XXX
--------------------------------------------
After (projected)         ~XX,XXX tokens
Saving                    ~XX,XXX tokens (XX%)
```

### 4. Offer to fix

For issues with straightforward fixes, offer to execute them:

- Stage git deletions
- Remove stale untracked files
- Disable redundant MCP servers in `mcp.json`

Always confirm before making changes.
