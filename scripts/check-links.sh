#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

broken=0

while IFS= read -r file; do
  while IFS= read -r token; do
    target="$(sed -E 's/.*\(([^)]*)\).*/\1/' <<< "$token")"
    target="$(sed -E 's/^[[:space:]]+|[[:space:]]+$//g' <<< "$target")"

    if [[ "$target" == http://* || "$target" == https://* || "$target" == mailto:* || "$target" == \#* ]]; then
      continue
    fi

    target="${target%%#*}"
    if [[ -z "$target" ]]; then
      continue
    fi

    dir="$(dirname "$file")"
    candidate="$dir/$target"

    if [[ ! -e "$candidate" ]]; then
      echo "Broken link: $file -> $target"
      broken=1
    fi
  done < <(grep -oE '\[[^]]+\]\([^)]+\)' "$file" || true)
done < <(find . -type f -name "*.md")

if [[ "$broken" -ne 0 ]]; then
  exit 1
fi

echo "No broken markdown links found."
