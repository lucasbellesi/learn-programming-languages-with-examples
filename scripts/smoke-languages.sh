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

xml_escape() {
  local value="$1"
  value="${value//&/&amp;}"
  value="${value//\"/&quot;}"
  value="${value//</&lt;}"
  value="${value//>/&gt;}"
  printf '%s' "$value"
}

build_csharp_exercise() {
  local exercise_path="$1"
  local temp_root="$2"
  local index="$3"
  local project_dir="$temp_root/exercise-$index"
  local escaped_path

  escaped_path="$(xml_escape "$(realpath "$exercise_path")")"
  mkdir -p "$project_dir"

  cat > "$project_dir/exercise-check.csproj" <<EOF
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>disable</ImplicitUsings>
    <Nullable>disable</Nullable>
    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="$escaped_path" Link="Program.cs" />
  </ItemGroup>
</Project>
EOF

  dotnet build "$project_dir/exercise-check.csproj" --nologo --verbosity quiet >/dev/null
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
require_cmd realpath

tmp_dir=""
csharp_exercise_tmp_dir=""
cleanup() {
  [[ -n "${tmp_dir:-}" ]] && rm -rf "$tmp_dir"
  [[ -n "${csharp_exercise_tmp_dir:-}" ]] && rm -rf "$csharp_exercise_tmp_dir"
}
trap cleanup EXIT

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
"$PYTHON_BIN" languages/python/03-advanced/constructors-and-invariants/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/03-advanced/copy-and-move-semantics/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/03-advanced/inheritance-and-polymorphism/example/main.py >/dev/null
"$PYTHON_BIN" languages/python/03-advanced/templates-basics/example/main.py >/dev/null
printf '0\n2\nAna Smith\n101\n91\nBob Lee\n77\n' | "$PYTHON_BIN" languages/python/projects/01-foundations/main.py >/dev/null
printf '3\nAna Smith\n91\nBob Lee\n55\nCarla Mendez\n88\n' | "$PYTHON_BIN" languages/python/assessments/01-foundations/main.py >/dev/null
(
  cd languages/python/projects/02-core
  cat > smoke-input.txt <<'EOF'
Ana Smith 91
Bob Lee 77
InvalidRow
Carla Mendez 88
EOF
  printf '%s\n' "$(pwd)/smoke-input.txt" | "$PYTHON_BIN" main.py >/dev/null
  [[ -f report.txt ]]
  rm -f smoke-input.txt report.txt
)
(
  cd languages/python/assessments/02-core
  printf '91\n88\n72\n105\n60\n-1\n' | "$PYTHON_BIN" main.py >/dev/null
  [[ -f core_assessment_report.txt ]]
  rm -f core_assessment_report.txt
)

echo "[3/6] Go compile check..."
tmp_dir="$(mktemp -d)"

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
go run languages/go/03-advanced/constructors-and-invariants/example/main.go >/dev/null
go run languages/go/03-advanced/copy-and-move-semantics/example/main.go >/dev/null
go run languages/go/03-advanced/inheritance-and-polymorphism/example/main.go >/dev/null
go run languages/go/03-advanced/templates-basics/example/main.go >/dev/null
printf '0\n2\nAna Smith\n101\n91\nBob Lee\n77\n' | go run languages/go/projects/01-foundations/main.go >/dev/null
printf '3\nAna Smith\n91\nBob Lee\n55\nCarla Mendez\n88\n' | go run languages/go/assessments/01-foundations/main.go >/dev/null
(
  cd languages/go/projects/02-core
  cat > smoke-input.txt <<'EOF'
Ana Smith 91
Bob Lee 77
InvalidRow
Carla Mendez 88
EOF
  printf '%s\n' "$(pwd)/smoke-input.txt" | go run main.go >/dev/null
  [[ -f report.txt ]]
  rm -f smoke-input.txt report.txt
)
(
  cd languages/go/assessments/02-core
  printf '12 17 31 77 91 105 64 -3 88 -1\n' | go run main.go >/dev/null
  [[ -f core_assessment_report.txt ]]
  rm -f core_assessment_report.txt
)

echo "[5/6] C# build check..."
while IFS= read -r project; do
  dotnet build "$project" --nologo --verbosity quiet
done < <(find languages/csharp -type f -name "*.csproj" | sort)

csharp_exercise_tmp_dir="$(mktemp -d)"
exercise_idx=0
while IFS= read -r exercise; do
  build_csharp_exercise "$exercise" "$csharp_exercise_tmp_dir" "$exercise_idx"
  exercise_idx=$((exercise_idx + 1))
done < <(find languages/csharp -type f -path "*/exercises/*.cs" | sort)

echo "[6/6] C# runtime smoke..."
dotnet run --project languages/csharp/01-foundations/functions/example/functions-example.csproj >/dev/null
dotnet run --project languages/csharp/01-foundations/formatted-output-and-iomanip/example/formatted-output-and-iomanip-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/algorithms-basics/example/algorithms-basics-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/sorting-and-searching/example/sorting-and-searching-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/maps-and-frequency-counting/example/maps-and-frequency-counting-example.csproj >/dev/null
dotnet run --project languages/csharp/02-core/error-handling-and-defensive-programming/example/error-handling-and-defensive-programming-example.csproj >/dev/null
dotnet run --project languages/csharp/03-advanced/structs-and-classes/example/structs-and-classes-example.csproj >/dev/null
dotnet run --project languages/csharp/03-advanced/constructors-and-invariants/example/constructors-and-invariants-example.csproj >/dev/null
dotnet run --project languages/csharp/03-advanced/copy-and-move-semantics/example/copy-and-move-semantics-example.csproj >/dev/null
dotnet run --project languages/csharp/03-advanced/inheritance-and-polymorphism/example/inheritance-and-polymorphism-example.csproj >/dev/null
dotnet run --project languages/csharp/03-advanced/templates-basics/example/templates-basics-example.csproj >/dev/null
printf '0\n2\nAna Smith\n101\n91\nBob Lee\n77\n' | dotnet run --project languages/csharp/projects/01-foundations/foundations-project.csproj >/dev/null
printf '3\nAna Smith\n91\nBob Lee\n55\nCarla Mendez\n88\n' | dotnet run --project languages/csharp/assessments/01-foundations/assessment-01-foundations.csproj >/dev/null
(
  cd languages/csharp/projects/02-core
  cat > smoke-input.txt <<'EOF'
Ana Smith 91
Bob Lee 77
InvalidRow
Carla Mendez 88
EOF
  printf '%s\n' "$(pwd)/smoke-input.txt" | dotnet run --project core-project.csproj >/dev/null
  [[ -f report.txt ]]
  rm -f smoke-input.txt report.txt
)
(
  cd languages/csharp/assessments/02-core
  printf '12 17 31 77 91 105 64 -3 88 -1\n' | dotnet run --project assessment-02-core.csproj >/dev/null
  [[ -f core_assessment_report.txt ]]
  rm -f core_assessment_report.txt
)

echo "Multi-language smoke checks passed."
