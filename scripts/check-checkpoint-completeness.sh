#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

checkpoint_kinds=("projects" "assessments")
languages=("cpp" "csharp" "go" "python")

main_for_language() {
  case "$1" in
    csharp) echo "main.cs" ;;
    go) echo "main.go" ;;
    python) echo "main.py" ;;
    *) echo "" ;;
  esac
}

failures=0
checkpoint_count=0

for language in "${languages[@]}"; do
  lang_root="./languages/$language"
  [[ -d "$lang_root" ]] || continue

  main_file_name="$(main_for_language "$language")"
  for kind in "${checkpoint_kinds[@]}"; do
    kind_path="$lang_root/$kind"
    [[ -d "$kind_path" ]] || continue

    while IFS= read -r checkpoint_dir; do
      checkpoint_count=$((checkpoint_count + 1))

      if [[ ! -f "$checkpoint_dir/README.md" ]]; then
        echo "Checkpoint completeness failed: $checkpoint_dir missing README.md"
        failures=1
      fi

      if [[ -n "$main_file_name" && ! -f "$checkpoint_dir/$main_file_name" ]]; then
        echo "Checkpoint completeness failed: $checkpoint_dir missing $main_file_name"
        failures=1
      fi

      if [[ "$language" == "csharp" ]]; then
        shopt -s nullglob
        csproj_files=("$checkpoint_dir"/*.csproj)
        shopt -u nullglob
        if [[ "${#csproj_files[@]}" -eq 0 ]]; then
          echo "Checkpoint completeness failed: $checkpoint_dir missing .csproj file"
          failures=1
        fi
      fi
    done < <(find "$kind_path" -mindepth 1 -maxdepth 1 -type d | sort)
  done
done

if (( checkpoint_count == 0 )); then
  echo "No checkpoint directories found for completeness validation."
  exit 1
fi

if (( failures != 0 )); then
  exit 1
fi

echo "Checkpoint completeness validation passed for $checkpoint_count checkpoint directories."
