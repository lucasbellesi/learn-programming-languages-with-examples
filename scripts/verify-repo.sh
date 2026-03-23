#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[1/5] Checking markdown links..."
bash ./scripts/check-links.sh

echo "[2/5] Checking README structure..."
bash ./scripts/check-readme-structure.sh

echo "[3/5] Checking module completeness..."
bash ./scripts/check-module-completeness.sh

echo "[4/5] Checking checkpoint completeness..."
bash ./scripts/check-checkpoint-completeness.sh

echo "[5/5] Compiling C++ files..."
bash ./scripts/build-all.sh

echo "Repository verification completed successfully."
