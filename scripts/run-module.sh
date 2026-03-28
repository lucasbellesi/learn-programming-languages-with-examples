#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: bash scripts/run-module.sh <module-path>"
  echo "Example: bash scripts/run-module.sh languages/cpp/01-foundations/strings"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
else
  echo "Required command not found: python or python3"
  exit 1
fi

"$PYTHON_BIN" ./scripts/automation.py run-module --module-path "$1"
