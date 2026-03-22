$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

Write-Host "[1/6] Python syntax check..."
python -m compileall -q languages/python

Write-Host "[2/6] Python runtime smoke..."
python languages/python/01-foundations/functions/example/main.py | Out-Null
python languages/python/01-foundations/formatted-output-and-iomanip/example/main.py | Out-Null
python languages/python/02-core/algorithms-basics/example/main.py | Out-Null
python languages/python/02-core/sorting-and-searching/example/main.py | Out-Null
python languages/python/02-core/maps-and-frequency-counting/example/main.py | Out-Null
python languages/python/02-core/error-handling-and-defensive-programming/example/main.py | Out-Null
python languages/python/03-advanced/structs-and-classes/example/main.py | Out-Null
python languages/python/03-advanced/constructors-and-invariants/example/main.py | Out-Null
python languages/python/03-advanced/copy-and-move-semantics/example/main.py | Out-Null
python languages/python/03-advanced/inheritance-and-polymorphism/example/main.py | Out-Null
python languages/python/03-advanced/templates-basics/example/main.py | Out-Null

Write-Host "[3/6] Go compile check..."
$tmpDir = Join-Path $env:TEMP ("go-smoke-" + [Guid]::NewGuid().ToString("N"))
New-Item -Path $tmpDir -ItemType Directory | Out-Null

try {
    $index = 0
    $goFiles = Get-ChildItem -Path languages/go -Recurse -Filter *.go | Sort-Object FullName
    foreach ($file in $goFiles) {
        $outputPath = Join-Path $tmpDir ("go_build_" + $index + ".exe")
        go build -o $outputPath $file.FullName
        $index++
    }
}
finally {
    if (Test-Path $tmpDir) {
        Remove-Item -Path $tmpDir -Recurse -Force
    }
}

Write-Host "[4/6] Go runtime smoke..."
go run languages/go/01-foundations/functions/example/main.go | Out-Null
go run languages/go/01-foundations/formatted-output-and-iomanip/example/main.go | Out-Null
go run languages/go/02-core/algorithms-basics/example/main.go | Out-Null
go run languages/go/02-core/sorting-and-searching/example/main.go | Out-Null
go run languages/go/02-core/maps-and-frequency-counting/example/main.go | Out-Null
go run languages/go/02-core/error-handling-and-defensive-programming/example/main.go | Out-Null
go run languages/go/03-advanced/structs-and-classes/example/main.go | Out-Null
go run languages/go/03-advanced/constructors-and-invariants/example/main.go | Out-Null
go run languages/go/03-advanced/copy-and-move-semantics/example/main.go | Out-Null
go run languages/go/03-advanced/inheritance-and-polymorphism/example/main.go | Out-Null
go run languages/go/03-advanced/templates-basics/example/main.go | Out-Null

Write-Host "[5/6] C# build check..."
$projects = Get-ChildItem -Path languages/csharp -Recurse -Filter *.csproj | Sort-Object FullName
foreach ($project in $projects) {
    dotnet build $project.FullName --nologo --verbosity quiet
}

Write-Host "[6/6] C# runtime smoke..."
dotnet run --project languages/csharp/01-foundations/functions/example/functions-example.csproj | Out-Null
dotnet run --project languages/csharp/01-foundations/formatted-output-and-iomanip/example/formatted-output-and-iomanip-example.csproj | Out-Null
dotnet run --project languages/csharp/02-core/algorithms-basics/example/algorithms-basics-example.csproj | Out-Null
dotnet run --project languages/csharp/02-core/sorting-and-searching/example/sorting-and-searching-example.csproj | Out-Null
dotnet run --project languages/csharp/02-core/maps-and-frequency-counting/example/maps-and-frequency-counting-example.csproj | Out-Null
dotnet run --project languages/csharp/02-core/error-handling-and-defensive-programming/example/error-handling-and-defensive-programming-example.csproj | Out-Null
dotnet run --project languages/csharp/03-advanced/structs-and-classes/example/structs-and-classes-example.csproj | Out-Null
dotnet run --project languages/csharp/03-advanced/constructors-and-invariants/example/constructors-and-invariants-example.csproj | Out-Null
dotnet run --project languages/csharp/03-advanced/copy-and-move-semantics/example/copy-and-move-semantics-example.csproj | Out-Null
dotnet run --project languages/csharp/03-advanced/inheritance-and-polymorphism/example/inheritance-and-polymorphism-example.csproj | Out-Null
dotnet run --project languages/csharp/03-advanced/templates-basics/example/templates-basics-example.csproj | Out-Null

Write-Host "Multi-language smoke checks passed."
