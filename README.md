# Agent skills

Reusable skills for Claude Code.

## Skills

| Skill | Description |
| --- | --- |
| [context-optimizer](skills/context-optimizer/SKILL.md) | Audit context window usage and get actionable recommendations to reduce waste |
| [session-reset](skills/session-reset/SKILL.md) | Preserve session state to PROMPT.md, tear down agents, and restore after /clear |

## Installation

Copy a skill folder into `~/.claude/skills/`:

```bash
cp -r skills/context-optimizer ~/.claude/skills/
```

The skill will be available as `/context-optimizer` in your next Claude Code session.

## Development

Requires [lefthook](https://github.com/evilmartians/lefthook) for pre-commit hooks:

```bash
lefthook install
```

Pre-commit runs markdownlint and skill validation in parallel.
