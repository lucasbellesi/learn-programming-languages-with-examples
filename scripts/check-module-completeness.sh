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

levels=("01-foundations" "02-core" "03-advanced" "04-expert")

ext_for_language() {
  case "$1" in
    cpp) echo "cpp" ;;
    csharp) echo "cs" ;;
    go) echo "go" ;;
    python) echo "py" ;;
    *) return 1 ;;
  esac
}

failures=0
module_count=0

for language in cpp csharp go python; do
  ext="$(ext_for_language "$language")"
  for level in "${levels[@]}"; do
    level_path="./languages/$language/$level"
    [[ -d "$level_path" ]] || continue

    while IFS= read -r module_dir; do
      module_count=$((module_count + 1))
      readme="$module_dir/README.md"
      example_dir="$module_dir/example"
      exercises_dir="$module_dir/exercises"
      main_file="$example_dir/main.$ext"
      exercise_01="$exercises_dir/01.$ext"
      exercise_02="$exercises_dir/02.$ext"

      if [[ ! -f "$readme" ]]; then
        echo "Module completeness failed: $module_dir missing README.md"
        failures=1
        continue
      fi

      if [[ ! -d "$example_dir" ]]; then
        echo "Module completeness failed: $module_dir missing example/ directory"
        failures=1
      fi

      if [[ ! -d "$exercises_dir" ]]; then
        echo "Module completeness failed: $module_dir missing exercises/ directory"
        failures=1
      fi

      if [[ ! -f "$main_file" ]]; then
        echo "Module completeness failed: $module_dir missing example/main.$ext"
        failures=1
      fi

      if [[ ! -f "$exercise_01" ]]; then
        echo "Module completeness failed: $module_dir missing exercises/01.$ext"
        failures=1
      fi

      if [[ ! -f "$exercise_02" ]]; then
        echo "Module completeness failed: $module_dir missing exercises/02.$ext"
        failures=1
      fi

      missing=()
      lines=()
      for heading in "${required_headings[@]}"; do
        line="$(grep -nF "$heading" "$readme" | head -n1 | cut -d: -f1 || true)"
        if [[ -z "$line" ]]; then
          missing+=("$heading")
        else
          lines+=("$line")
        fi
      done

      if [[ "${#missing[@]}" -gt 0 ]]; then
        echo "Module completeness failed: $module_dir README missing headings -> ${missing[*]}"
        failures=1
        continue
      fi

      prev=0
      for line in "${lines[@]}"; do
        if (( line < prev )); then
          echo "Module completeness failed: $module_dir README headings are out of order."
          failures=1
          break
        fi
        prev=$line
      done
    done < <(find "$level_path" -mindepth 1 -maxdepth 1 -type d | sort)
  done
done

if (( module_count == 0 )); then
  echo "No module directories found for completeness validation."
  exit 1
fi

if (( failures != 0 )); then
  exit 1
fi

echo "Module completeness validation passed for $module_count module directories."
