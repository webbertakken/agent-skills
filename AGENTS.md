# Agent guidelines

- Skills live in `skills/<skill-name>/SKILL.md`
- Skill names must be kebab-case and match directory name
- SKILL.md requires YAML frontmatter with `name` and `description`
- Keep SKILL.md under 200 lines; split detailed content into `references/`
- Run `npx markdownlint-cli2 "**/*.md"` and `bash scripts/validate-skills.sh` before committing
