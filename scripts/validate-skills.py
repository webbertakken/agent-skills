#!/usr/bin/env python3
"""Validate all skills in the skills/ directory."""

import re
import sys
from pathlib import Path

import yaml

SKILLS_DIR = Path("skills")
ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}


def validate_skill(skill_path: Path) -> tuple[bool, list[str]]:
    """Validate a single skill directory. Returns (passed, errors)."""
    errors: list[str] = []
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return False, ["SKILL.md not found"]

    content = skill_md.read_text(encoding="utf-8")

    if not content.startswith("---"):
        return False, ["no YAML frontmatter found"]

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False, ["invalid frontmatter format"]

    try:
        frontmatter = yaml.safe_load(match.group(1))
        if not isinstance(frontmatter, dict):
            return False, ["frontmatter must be a YAML dictionary"]
    except yaml.YAMLError as exc:
        return False, [f"invalid YAML: {exc}"]

    unexpected = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected:
        errors.append(f"unexpected frontmatter keys: {', '.join(sorted(unexpected))}")

    name = frontmatter.get("name", "")
    if not name:
        errors.append("missing 'name'")
    elif not isinstance(name, str):
        errors.append(f"'name' must be a string, got {type(name).__name__}")
    else:
        name = name.strip()
        if not re.match(r"^[a-z0-9-]+$", name):
            errors.append(f"name '{name}' must be kebab-case")
        elif name.startswith("-") or name.endswith("-") or "--" in name:
            errors.append(f"name '{name}' has invalid hyphens")
        if len(name) > 64:
            errors.append(f"name too long ({len(name)} chars, max 64)")
        if name != skill_path.name:
            errors.append(f"name '{name}' does not match directory '{skill_path.name}'")

    description = frontmatter.get("description", "")
    if not description:
        errors.append("missing 'description'")
    elif not isinstance(description, str):
        errors.append(f"'description' must be a string, got {type(description).__name__}")
    else:
        if len(description.strip()) > 1024:
            errors.append(f"description too long ({len(description.strip())} chars, max 1024)")

    body = content[match.end() :].strip()
    if not body:
        errors.append("SKILL.md body is empty")

    return len(errors) == 0, errors


def main() -> None:
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: {SKILLS_DIR}/ directory not found")
        sys.exit(1)

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not skill_dirs:
        print(f"ERROR: no skills found in {SKILLS_DIR}/")
        sys.exit(1)

    failed = 0
    for skill_dir in skill_dirs:
        passed, errors = validate_skill(skill_dir)
        if passed:
            print(f"  PASS  {skill_dir.name}")
        else:
            print(f"  FAIL  {skill_dir.name}")
            for error in errors:
                print(f"          - {error}")
            failed += 1

    print(f"\n{len(skill_dirs)} skills checked, {failed} failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
