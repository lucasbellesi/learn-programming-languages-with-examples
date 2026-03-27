$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

function Convert-ToXmlAttributeValue([string]$value) {
    return $value.Replace("&", "&amp;").Replace('"', "&quot;").Replace("<", "&lt;").Replace(">", "&gt;")
}

function Test-CSharpExerciseFile([string]$exercisePath, [string]$tempRoot, [int]$index) {
    $projectDir = Join-Path $tempRoot ("exercise-" + $index)
    New-Item -Path $projectDir -ItemType Directory | Out-Null

    $escapedExercisePath = Convert-ToXmlAttributeValue ([System.IO.Path]::GetFullPath($exercisePath))
    $projectPath = Join-Path $projectDir "exercise-check.csproj"
    @"
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>disable</ImplicitUsings>
    <Nullable>disable</Nullable>
    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="$escapedExercisePath" Link="Program.cs" />
  </ItemGroup>
</Project>
"@ | Set-Content -Path $projectPath

    dotnet build $projectPath --nologo --verbosity quiet | Out-Null
}

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
$pythonProject01Input = Join-Path $env:TEMP ("python-project-01-" + [Guid]::NewGuid().ToString("N") + ".txt")
$pythonAssessment01Input = Join-Path $env:TEMP ("python-assessment-01-" + [Guid]::NewGuid().ToString("N") + ".txt")
@("0", "2", "Ana Smith", "101", "91", "Bob Lee", "77") | Set-Content -Path $pythonProject01Input
@("3", "Ana Smith", "91", "Bob Lee", "55", "Carla Mendez", "88") | Set-Content -Path $pythonAssessment01Input
Get-Content $pythonProject01Input | python languages/python/projects/01-foundations/main.py | Out-Null
Get-Content $pythonAssessment01Input | python languages/python/assessments/01-foundations/main.py | Out-Null
Push-Location languages/python/projects/02-core
try {
    $pythonProjectInput = Join-Path (Get-Location) "smoke-input.txt"
    @(
        "Ana Smith 91"
        "Bob Lee 77"
        "InvalidRow"
        "Carla Mendez 88"
    ) | Set-Content -Path $pythonProjectInput
    $pythonProject02Input = Join-Path $env:TEMP ("python-project-02-" + [Guid]::NewGuid().ToString("N") + ".txt")
    $pythonProjectInput | Set-Content -Path $pythonProject02Input
    Get-Content $pythonProject02Input | python main.py | Out-Null
    if (-not (Test-Path "report.txt")) {
        throw "Python 02-core project did not create report.txt"
    }
}
finally {
    Remove-Item -ErrorAction SilentlyContinue "smoke-input.txt", "report.txt"
    if ($pythonProject02Input) {
        Remove-Item -ErrorAction SilentlyContinue $pythonProject02Input
    }
    Pop-Location
}
Push-Location languages/python/assessments/02-core
try {
    $pythonAssessment02Input = Join-Path $env:TEMP ("python-assessment-02-" + [Guid]::NewGuid().ToString("N") + ".txt")
    @("91", "88", "72", "105", "60", "-1") | Set-Content -Path $pythonAssessment02Input
    Get-Content $pythonAssessment02Input | python main.py | Out-Null
    if (-not (Test-Path "core_assessment_report.txt")) {
        throw "Python 02-core assessment did not create core_assessment_report.txt"
    }
}
finally {
    Remove-Item -ErrorAction SilentlyContinue "core_assessment_report.txt"
    if ($pythonAssessment02Input) {
        Remove-Item -ErrorAction SilentlyContinue $pythonAssessment02Input
    }
    Pop-Location
}
Remove-Item -ErrorAction SilentlyContinue $pythonProject01Input, $pythonAssessment01Input

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
$goProject01Input = Join-Path $env:TEMP ("go-project-01-" + [Guid]::NewGuid().ToString("N") + ".txt")
$goAssessment01Input = Join-Path $env:TEMP ("go-assessment-01-" + [Guid]::NewGuid().ToString("N") + ".txt")
@("0", "2", "Ana Smith", "101", "91", "Bob Lee", "77") | Set-Content -Path $goProject01Input
@("3", "Ana Smith", "91", "Bob Lee", "55", "Carla Mendez", "88") | Set-Content -Path $goAssessment01Input
Get-Content $goProject01Input | go run languages/go/projects/01-foundations/main.go | Out-Null
Get-Content $goAssessment01Input | go run languages/go/assessments/01-foundations/main.go | Out-Null
Push-Location languages/go/projects/02-core
try {
    $goProjectInput = Join-Path (Get-Location) "smoke-input.txt"
    @(
        "Ana Smith 91"
        "Bob Lee 77"
        "InvalidRow"
        "Carla Mendez 88"
    ) | Set-Content -Path $goProjectInput
    $goProject02Input = Join-Path $env:TEMP ("go-project-02-" + [Guid]::NewGuid().ToString("N") + ".txt")
    $goProjectInput | Set-Content -Path $goProject02Input
    Get-Content $goProject02Input | go run main.go | Out-Null
    if (-not (Test-Path "report.txt")) {
        throw "Go 02-core project did not create report.txt"
    }
}
finally {
    Remove-Item -ErrorAction SilentlyContinue "smoke-input.txt", "report.txt"
    if ($goProject02Input) {
        Remove-Item -ErrorAction SilentlyContinue $goProject02Input
    }
    Pop-Location
}
Push-Location languages/go/assessments/02-core
try {
    $goAssessment02Input = Join-Path $env:TEMP ("go-assessment-02-" + [Guid]::NewGuid().ToString("N") + ".txt")
    @("12 17 31 77 91 105 64 -3 88 -1") | Set-Content -Path $goAssessment02Input
    Get-Content $goAssessment02Input | go run main.go | Out-Null
    if (-not (Test-Path "core_assessment_report.txt")) {
        throw "Go 02-core assessment did not create core_assessment_report.txt"
    }
}
finally {
    Remove-Item -ErrorAction SilentlyContinue "core_assessment_report.txt"
    if ($goAssessment02Input) {
        Remove-Item -ErrorAction SilentlyContinue $goAssessment02Input
    }
    Pop-Location
}
Remove-Item -ErrorAction SilentlyContinue $goProject01Input, $goAssessment01Input

Write-Host "[5/6] C# build check..."
$projects = Get-ChildItem -Path languages/csharp -Recurse -Filter *.csproj | Sort-Object FullName
foreach ($project in $projects) {
    dotnet build $project.FullName --nologo --verbosity quiet
}

$csharpExerciseTempRoot = Join-Path $env:TEMP ("csharp-exercise-smoke-" + [Guid]::NewGuid().ToString("N"))
New-Item -Path $csharpExerciseTempRoot -ItemType Directory | Out-Null
try {
    $exerciseIndex = 0
    $exerciseFiles = Get-ChildItem -Path languages/csharp -Recurse -Filter *.cs |
        Where-Object { $_.FullName -like "*\exercises\*" } |
        Sort-Object FullName

    foreach ($exercise in $exerciseFiles) {
        Test-CSharpExerciseFile -exercisePath $exercise.FullName -tempRoot $csharpExerciseTempRoot -index $exerciseIndex
        $exerciseIndex++
    }
}
finally {
    if (Test-Path $csharpExerciseTempRoot) {
        Remove-Item -Path $csharpExerciseTempRoot -Recurse -Force
    }
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
$csharpProject01Input = Join-Path $env:TEMP ("csharp-project-01-" + [Guid]::NewGuid().ToString("N") + ".txt")
$csharpAssessment01Input = Join-Path $env:TEMP ("csharp-assessment-01-" + [Guid]::NewGuid().ToString("N") + ".txt")
@("0", "2", "Ana Smith", "101", "91", "Bob Lee", "77") | Set-Content -Path $csharpProject01Input
@("3", "Ana Smith", "91", "Bob Lee", "55", "Carla Mendez", "88") | Set-Content -Path $csharpAssessment01Input
Get-Content $csharpProject01Input | dotnet run --project languages/csharp/projects/01-foundations/foundations-project.csproj | Out-Null
Get-Content $csharpAssessment01Input | dotnet run --project languages/csharp/assessments/01-foundations/assessment-01-foundations.csproj | Out-Null
Push-Location languages/csharp/projects/02-core
try {
    $csharpProjectInput = Join-Path (Get-Location) "smoke-input.txt"
    @(
        "Ana Smith 91"
        "Bob Lee 77"
        "InvalidRow"
        "Carla Mendez 88"
    ) | Set-Content -Path $csharpProjectInput
    $csharpProject02Input = Join-Path $env:TEMP ("csharp-project-02-" + [Guid]::NewGuid().ToString("N") + ".txt")
    $csharpProjectInput | Set-Content -Path $csharpProject02Input
    Get-Content $csharpProject02Input | dotnet run --project core-project.csproj | Out-Null
    if (-not (Test-Path "report.txt")) {
        throw "C# 02-core project did not create report.txt"
    }
}
finally {
    Remove-Item -ErrorAction SilentlyContinue "smoke-input.txt", "report.txt"
    if ($csharpProject02Input) {
        Remove-Item -ErrorAction SilentlyContinue $csharpProject02Input
    }
    Pop-Location
}
Push-Location languages/csharp/assessments/02-core
try {
    $csharpAssessment02Input = Join-Path $env:TEMP ("csharp-assessment-02-" + [Guid]::NewGuid().ToString("N") + ".txt")
    @("12 17 31 77 91 105 64 -3 88 -1") | Set-Content -Path $csharpAssessment02Input
    Get-Content $csharpAssessment02Input | dotnet run --project assessment-02-core.csproj | Out-Null
    if (-not (Test-Path "core_assessment_report.txt")) {
        throw "C# 02-core assessment did not create core_assessment_report.txt"
    }
}
finally {
    Remove-Item -ErrorAction SilentlyContinue "core_assessment_report.txt"
    if ($csharpAssessment02Input) {
        Remove-Item -ErrorAction SilentlyContinue $csharpAssessment02Input
    }
    Pop-Location
}
Remove-Item -ErrorAction SilentlyContinue $csharpProject01Input, $csharpAssessment01Input

Write-Host "Multi-language smoke checks passed."
