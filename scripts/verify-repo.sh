#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[1/2] Checking markdown links..."
bash ./scripts/check-links.sh

echo "[2/2] Compiling C++ files..."
bash ./scripts/build-all.sh

echo "Repository verification completed successfully."
