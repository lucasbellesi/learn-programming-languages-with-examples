#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

require_cmd() {
  local name="$1"
  if ! command -v "$name" >/dev/null 2>&1; then
    echo "Required command not found: $name"
    exit 1
  fi
}

if command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
else
  echo "Required command not found: python or python3"
  exit 1
fi

require_cmd go
require_cmd dotnet

echo "[1/6] Python syntax check..."
"$PYTHON_BIN" -m compileall -q languages/python

echo "[2/6] Python runtime smoke..."
"$PYTHON_BIN" languages/python/01-foundations/functions/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/01-foundations/formatted-output-and-iomanip/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/02-core/algorithms-basics/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/02-core/sorting-and-searching/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/02-core/maps-and-frequency-counting/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/02-core/error-handling-and-defensive-programming/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/03-advanced/structs-and-classes/example/main.py >/dev/null

echo "[3/6] Go compile check..."
tmp_dir="$(mktemp -d)"
cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

idx=0
while IFS= read -r file; do
  go build -o "$tmp_dir/go_build_$idx" "$file"
  idx=$((idx + 1))
done < <(find languages/go -type f -name "*.go" | sort)

echo "[4/6] Go runtime smoke..."
go run languages/go/01-foundations/functions/example/main.go >/dev/null
go run languages/go/01-foundations/formatted-output-and-iomanip/example/main.go >/dev/null
go run languages/go/02-core/algorithms-basics/example/main.go >/dev/null
go run languages/go/02-core/sorting-and-searching/example/main.go >/dev/null
go run languages/go/02-core/maps-and-frequency-counting/example/main.go >/dev/null
go run languages/go/02-core/error-handling-and-defensive-programming/example/main.go >/dev/null
go run languages/go/03-advanced/structs-and-classes/example/main.go >/dev/null

echo "[5/6] C# build check..."
while IFS= read -r project; do
  dotnet build "$project" --nologo --verbosity quiet
done < <(find languages/csharp -type f -name "*.csproj" | sort)

echo "[6/6] C# runtime smoke..."
dotnet run --project languages/csharp/01-foundations/functions/example/functions-example.csproj >/dev/null
dotnet run --project languages/csharp/01-foundations/formatted-output-and-iomanip/example/formatted-output-and-iomanip-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/algorithms-basics/example/algorithms-basics-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/sorting-and-searching/example/sorting-and-searching-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/maps-and-frequency-counting/example/maps-and-frequency-counting-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/error-handling-and-defensive-programming/example/error-handling-and-defensive-programming-example.csproj >/dev/null
dotnet run --project languages/csharp/03-advanced/structs-and-classes/example/structs-and-classes-example.csproj >/dev/null

echo "Multi-language smoke checks passed."
