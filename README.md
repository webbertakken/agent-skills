# Agent skills

Reusable skills for OpenCode and Claude Code.

## Skills

| Skill | Description |
| --- | --- |
| [context-optimizer](skills/context-optimizer/SKILL.md) | Audit context window usage and get actionable recommendations to reduce waste |
| [session-reset](skills/session-reset/SKILL.md) | Preserve session state to PROMPT.md, tear down agents, and restore after /clear |

## Installation

### OpenCode

Copy into `~/.config/opencode/skills/` or `.opencode/skills/` in your project:

```bash
cp -r skills/context-optimizer ~/.config/opencode/skills/
```

### Claude Code (plugin)

Run these inside a Claude Code session:

```text
/plugin marketplace add webbertakken/agent-skills
/plugin install webber@webbertakken
```

Skills are available as `/webber:context-optimizer` and `/webber:session-reset`.

### Claude Code (manual)

Copy individual skills into `~/.claude/skills/`:

```bash
cp -r skills/context-optimizer ~/.claude/skills/
```

Available as `/context-optimizer` (no namespace prefix).

## Development

Requires [lefthook](https://github.com/evilmartians/lefthook) for pre-commit hooks:

```bash
lefthook install
```

Pre-commit runs markdownlint and skill validation in parallel.
