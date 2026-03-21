#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[1/4] Checking markdown links..."
bash ./scripts/check-links.sh

echo "[2/4] Checking README structure..."
bash ./scripts/check-readme-structure.sh

echo "[3/4] Checking module completeness..."
bash ./scripts/check-module-completeness.sh

echo "[4/4] Compiling C++ files..."
bash ./scripts/build-all.sh

echo "Repository verification completed successfully."
