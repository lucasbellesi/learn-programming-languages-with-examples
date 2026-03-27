#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

required_headings=(
  "## Quick Run"
  "## Topics Covered"
  "## Common Pitfalls"
  "## Exercise Focus"
  "### Exercise Specs"
  "## Checkpoint"
)

languages=("cpp" "csharp" "go" "python")
levels=("01-foundations" "02-core" "03-advanced" "04-expert")

heading_line_number() {
  local heading="$1"
  local file="$2"
  grep -nE "^[[:space:]]{0,3}${heading}[[:space:]]*$" "$file" | head -n1 | cut -d: -f1 || true
}

module_readmes=()
for language in "${languages[@]}"; do
  for level in "${levels[@]}"; do
    level_path="./languages/$language/$level"
    [[ -d "$level_path" ]] || continue
    while IFS= read -r module_dir; do
      readme="$module_dir/README.md"
      [[ -f "$readme" ]] && module_readmes+=("$readme")
    done < <(find "$level_path" -mindepth 1 -maxdepth 1 -type d | sort)
  done
done

if [[ "${#module_readmes[@]}" -eq 0 ]]; then
  echo "No module README files found for validation."
  exit 1
fi

failed=0

for file in "${module_readmes[@]}"; do
  missing=()
  lines=()

  for heading in "${required_headings[@]}"; do
    line="$(heading_line_number "$heading" "$file")"
    if [[ -z "$line" ]]; then
      missing+=("$heading")
    else
      lines+=("$line")
    fi
  done

  if [[ "${#missing[@]}" -gt 0 ]]; then
    echo "README structure failed: $file missing -> ${missing[*]}"
    failed=1
    continue
  fi

  prev=0
  for line in "${lines[@]}"; do
    if (( line < prev )); then
      echo "README structure failed: $file required headings are out of order."
      failed=1
      break
    fi
    prev=$line
  done
done

if (( failed != 0 )); then
  exit 1
fi

echo "README structure validation passed for ${#module_readmes[@]} module files."
