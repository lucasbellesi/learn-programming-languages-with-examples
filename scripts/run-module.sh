#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: bash scripts/run-module.sh <module-path>"
  echo "Example: bash scripts/run-module.sh languages/cpp/01-foundations/strings"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

module_path="${1//\\//}"

if [[ ! -d "$module_path" ]]; then
  echo "Module folder not found: $module_path"
  exit 1
fi

example_file="$module_path/example/main.cpp"
if [[ ! -f "$example_file" ]]; then
  echo "Missing example file: $example_file"
  exit 1
fi

output_path="$(mktemp /tmp/run_module_XXXXXX)"
trap 'rm -f "$output_path"' EXIT

extra_flags=()
case "$(uname -s)" in
  Linux*|Darwin*)
    extra_flags+=(-pthread)
    ;;
esac

echo "Compiling example: $example_file"
g++ -std=c++17 -Wall -Wextra -pedantic "${extra_flags[@]}" "$example_file" -o "$output_path"

echo "Running example..."
"$output_path"

exercise_dir="$module_path/exercises"
if [[ -d "$exercise_dir" ]]; then
  mapfile -t exercises < <(find "$exercise_dir" -maxdepth 1 -type f -name "*.cpp" | sort)
  if [[ ${#exercises[@]} -gt 0 ]]; then
    echo
    echo "Exercises in $module_path/exercises:"
    for exercise in "${exercises[@]}"; do
      echo "- ${exercise//\\//}"
    done
  fi
fi
