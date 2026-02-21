# Agent skills

My reusable agent skills.

Documentation at https://skills.sh/?q=webbertakken/

## Installation (individual skills)

```bash
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
◇  Found 2 skills
│
◆  Select skills to install (space to toggle)
│  ◻ context-optimizer (Audit and optimise Claude Code context window usage. Esti...)
│  ◻ session-reset
└

```

## Alternative installation (Claude plugin)

Add the repository to your plugin marketplace

```bash
/plugin marketplace add webbertakken/agent-skills
```

Install the skills you want from the marketplace

```
/plugin install webber@webbertakken
```

## Development

Requires [lefthook](https://github.com/evilmartians/lefthook) for pre-commit hooks:

```bash
lefthook install
```

Pre-commit runs markdownlint and skill validation in parallel.

## License

[MIT License](./LICENSE)
