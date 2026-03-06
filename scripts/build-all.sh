#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

mapfile -t files < <(find languages/cpp -type f -name "*.cpp")

if [[ ${#files[@]} -eq 0 ]]; then
  echo "No C++ files found under languages/cpp"
  exit 0
fi

mkdir -p build

extra_flags=()
case "$(uname -s)" in
  Linux*|Darwin*)
    extra_flags+=(-pthread)
    ;;
esac

index=0
for file in "${files[@]}"; do
  output="build/check_${index}"
  echo "Compiling: $file"
  g++ -std=c++17 -Wall -Wextra -pedantic "${extra_flags[@]}" "$file" -o "$output"
  index=$((index + 1))
done

echo "Compiled $index file(s) successfully."
