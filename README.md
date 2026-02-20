# Agent skills

Reusable skills for Claude Code and OpenCode.

## Skills

| Skill | Description |
| --- | --- |
| [context-optimizer](skills/context-optimizer/SKILL.md) | Audit context window usage and get actionable recommendations to reduce waste |
| [session-reset](skills/session-reset/SKILL.md) | Preserve session state to PROMPT.md, tear down agents, and restore after /clear |

## Installation

### Claude Code (plugin)

Load directly from the repo:

```bash
claude --plugin-dir ./agent-skills
```

Skills are available as `/webber:context-optimizer` and `/webber:session-reset`.

### Claude Code (manual)

Copy individual skills into `~/.claude/skills/`:

```bash
cp -r skills/context-optimizer ~/.claude/skills/
```

Available as `/context-optimizer` (no namespace prefix).

### OpenCode

Copy into `~/.config/opencode/skills/` or `.opencode/skills/` in your project:

```bash
cp -r skills/context-optimizer ~/.config/opencode/skills/
```

## Development

Requires [lefthook](https://github.com/evilmartians/lefthook) for pre-commit hooks:

```bash
lefthook install
```

Pre-commit runs markdownlint and skill validation in parallel.
