# Agent skills

My reusable agent skills.

Documentation at <https://skills.sh/?q=webbertakken/>

## Installation (individual skills)

```console
npx skills add https://github.com/webbertakken/agent-skills
```

You should see

```console

███████╗██╗  ██╗██╗██╗     ██╗     ███████╗
██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝
███████╗█████╔╝ ██║██║     ██║     ███████╗
╚════██║██╔═██╗ ██║██║     ██║     ╚════██║
███████║██║  ██╗██║███████╗███████╗███████║
╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝

┌   skills
│
◇  Source: https://github.com/webbertakken/agent-skills.git
│
◇  Repository cloned
│
◇  Found 3 skills
│
◆  Select skills to install (space to toggle)
│  ◼ context-optimizer (Audit and optimise context window usage for AI coding tools...)
│  ◼ session-reset (Reset the session while preserving context. Commits chang...)
│  ◼ session-start (Start team, run dev servers, and read PROMPT.md if present...)
└

```

## Development

Requires [lefthook](https://github.com/evilmartians/lefthook) for pre-commit hooks:

```console
lefthook install
```

Pre-commit runs markdownlint and skill validation in parallel.

## License

[MIT License](./LICENSE)
