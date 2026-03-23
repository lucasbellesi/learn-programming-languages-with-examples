$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$checkpointKinds = @("projects", "assessments")
$languages = @("cpp", "csharp", "go", "python")
$requiredMainByLanguage = @{
    csharp = "main.cs"
    go = "main.go"
    python = "main.py"
}

$failures = @()
$checkpointCount = 0

foreach ($language in $languages) {
    $langRoot = Join-Path $root "languages/$language"
    if (-not (Test-Path $langRoot)) {
        continue
    }

    foreach ($kind in $checkpointKinds) {
        $kindPath = Join-Path $langRoot $kind
        if (-not (Test-Path $kindPath)) {
            continue
        }

        $checkpointDirs = Get-ChildItem -Path $kindPath -Directory
        foreach ($checkpoint in $checkpointDirs) {
            $checkpointCount++

            $readmePath = Join-Path $checkpoint.FullName "README.md"
            if (-not (Test-Path $readmePath)) {
                $failures += "$($checkpoint.FullName): missing README.md"
            }

            if ($requiredMainByLanguage.ContainsKey($language)) {
                $mainPath = Join-Path $checkpoint.FullName $requiredMainByLanguage[$language]
                if (-not (Test-Path $mainPath)) {
                    $failures += "$($checkpoint.FullName): missing $($requiredMainByLanguage[$language])"
                }
            }

            if ($language -eq "csharp") {
                $csprojFiles = Get-ChildItem -Path $checkpoint.FullName -Filter *.csproj -File
                if ($csprojFiles.Count -eq 0) {
                    $failures += "$($checkpoint.FullName): missing .csproj file"
                }
            }
        }
    }
}

if ($checkpointCount -eq 0) {
    Write-Host "No checkpoint directories found for completeness validation."
    exit 1
}

if ($failures.Count -gt 0) {
    Write-Host "Checkpoint completeness validation failed:"
    $failures | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host "Checkpoint completeness validation passed for $checkpointCount checkpoint directories."
