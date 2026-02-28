---
name: session-reset
description: >-
  Reset the session while preserving context. Commits changes, writes a slim
  PROMPT.md with session-specific state (current task, method, progress), tears
  down any active team, then guides the user through /clear and context
  restoration. Use when the context window is getting large, the session needs a
  fresh start, or when switching focus. Also use when user says "reset", "fresh
  start", "save and clear", or "write prompt".
---

# Session reset

Preserve session-specific state in PROMPT.md across a /clear, then restore afterwards.

PROMPT.md captures **only session-specific state** — current task, method, and progress. Persistent knowledge (user preferences, codebase patterns, dev quirks, workflow lessons) is handled separately by auto-memory and must NOT be included in PROMPT.md.

## Workflow

### 1. Commit and push

Check `git status` for uncommitted changes. If there are any:

**Security check** — before staging, scan changed files for secrets. Flag and exclude any files matching
common sensitive patterns (`.env*`, `*.key`, `*.pem`, `credentials.*`, `*secret*`, `*.token`). Warn
the user if any are found and never stage them without explicit confirmation.

Then ask the user:

- **Commit and push** — stage safe changes, commit with a concise message, and push to the current branch
- **Commit only** — stage and commit without pushing
- **Skip** — leave changes as-is

If the user chooses to commit, use `/commit`. If they also want to push, push after the commit succeeds.

If the working tree is already clean, tell the user "Working tree is clean — nothing to commit." and move on.

### 2. Write PROMPT.md

Generate PROMPT.md at the **project root** by reviewing the current session state. PROMPT.md is ephemeral and must **never** be committed.

```markdown
# PROMPT.md

## Current task
<!-- What we're working on - the goal, feature, or fix -->

## Method
<!-- Which workflow/approach is active (e.g. OpenSpec, manual, etc.) -->
<!-- Include any active change IDs, branch names, or tracking references -->

## Progress
<!-- Where we are in the process -->
<!-- What's done, what's in flight, what's next -->
<!-- Any blocking issues or open questions -->
```

Guidelines:

- **Do NOT include** user preferences, codebase patterns, dev quirks, or general knowledge — auto-memory handles that
- **Do include** task-specific context: current branch, active OpenSpec change, what's done, what's next, blocking issues
- Be specific and actionable — include file paths, branch names, change IDs, and concrete references
- Keep it concise — typically 20-40 lines

### 3. Tear down team (if active)

If a team is active (check for team config in `$CONFIG_DIR/teams/`):

1. Read the team config to discover all active members
2. List the active members to the user and confirm they want to tear down the team
3. Send `shutdown_request` to each teammate
4. Wait for confirmations
5. Delete the team with `TeamDelete`

If no team is active, tell the user "No active team — skipping teardown." and move on.

### 4. Guide the user

After teardown, output this message exactly:

```
Session state saved to PROMPT.md. All agents shut down.

Run `/clear` now, then tell me: **read PROMPT.md**
```

### 5. Restore (post-clear)

When the user says "read PROMPT.md" after a /clear:

1. Read PROMPT.md from the project root
2. Summarise the restored context to the user
3. Resume work based on the progress section
