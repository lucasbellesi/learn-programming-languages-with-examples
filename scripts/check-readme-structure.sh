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

mapfile -t module_readmes < <(find ./languages -type f -path "*/01-foundations/*/README.md" | sort)

if [[ "${#module_readmes[@]}" -eq 0 ]]; then
  echo "No module README files found for validation."
  exit 1
fi

failed=0

for file in "${module_readmes[@]}"; do
  missing=()
  lines=()

  for heading in "${required_headings[@]}"; do
    line="$(grep -nF "$heading" "$file" | head -n1 | cut -d: -f1 || true)"
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
