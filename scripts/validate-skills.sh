#!/usr/bin/env bash
# Validate all skills in the skills/ directory.
# Checks: SKILL.md exists, has frontmatter with name + description,
# name is kebab-case, name matches directory name, body is non-empty.
set -euo pipefail

SKILLS_DIR="skills"
failed=0
checked=0

if [ ! -d "$SKILLS_DIR" ]; then
  echo "ERROR: $SKILLS_DIR/ directory not found"
  exit 1
fi

for skill_dir in "$SKILLS_DIR"/*/; do
  [ -d "$skill_dir" ] || continue
  dir_name=$(basename "$skill_dir")
  skill_md="$skill_dir/SKILL.md"
  errors=()
  checked=$((checked + 1))

  if [ ! -f "$skill_md" ]; then
    errors+=("SKILL.md not found")
  else
    content=$(cat "$skill_md")

    # Check frontmatter exists
    if [[ "$content" != ---* ]]; then
      errors+=("no YAML frontmatter found")
    else
      # Extract name field
      name=$(sed -n '/^---$/,/^---$/p' "$skill_md" | grep -E '^name:' | head -1 | sed 's/^name:[[:space:]]*//')
      if [ -z "$name" ]; then
        errors+=("missing 'name'")
      else
        # Check kebab-case
        if ! echo "$name" | grep -qE '^[a-z0-9-]+$'; then
          errors+=("name '$name' must be kebab-case")
        fi
        # Check name matches directory
        if [ "$name" != "$dir_name" ]; then
          errors+=("name '$name' does not match directory '$dir_name'")
        fi
      fi

      # Check description field
      description=$(sed -n '/^---$/,/^---$/p' "$skill_md" | grep -E '^description:' | head -1)
      if [ -z "$description" ]; then
        errors+=("missing 'description'")
      fi

      # Check body is non-empty (content after second ---)
      body=$(sed '1,/^---$/!d' "$skill_md" | wc -l)
      total_lines=$(wc -l < "$skill_md")
      frontmatter_end=$((body + 1))
      body_content=$(tail -n +"$frontmatter_end" "$skill_md" | sed '/^$/d' | head -1)
      if [ -z "$body_content" ]; then
        errors+=("SKILL.md body is empty")
      fi
    fi
  fi

  if [ ${#errors[@]} -eq 0 ]; then
    echo "  PASS  $dir_name"
  else
    echo "  FAIL  $dir_name"
    for error in "${errors[@]}"; do
      echo "          - $error"
    done
    failed=$((failed + 1))
  fi
done

if [ "$checked" -eq 0 ]; then
  echo "ERROR: no skills found in $SKILLS_DIR/"
  exit 1
fi

echo ""
echo "$checked skills checked, $failed failed"
exit $((failed > 0 ? 1 : 0))
