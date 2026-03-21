$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$requiredHeadings = @(
    "## Quick Run",
    "## Topics Covered",
    "## Common Pitfalls",
    "## Exercise Focus",
    "### Exercise Specs",
    "## Checkpoint"
)

$languageNames = @("cpp", "csharp", "go", "python")
$levelNames = @("01-foundations", "02-core", "03-advanced", "04-expert")

$moduleReadmes = foreach ($language in $languageNames) {
    foreach ($level in $levelNames) {
        $levelPath = Join-Path $root "languages/$language/$level"
        if (-not (Test-Path $levelPath)) {
            continue
        }

        Get-ChildItem -Path $levelPath -Directory |
            ForEach-Object { Join-Path $_.FullName "README.md" } |
            Where-Object { Test-Path $_ }
    }
}

$moduleReadmes = $moduleReadmes | Sort-Object -Unique

if ($moduleReadmes.Count -eq 0) {
    Write-Host "No module README files found for validation."
    exit 1
}

$failures = @()

foreach ($file in $moduleReadmes) {
    $content = Get-Content -Path $file -Raw
    $missing = @()
    $positions = @{}

    foreach ($heading in $requiredHeadings) {
        $index = $content.IndexOf($heading)
        if ($index -lt 0) {
            $missing += $heading
        } else {
            $positions[$heading] = $index
        }
    }

    if ($missing.Count -gt 0) {
        $failures += "${file}: missing -> $($missing -join ', ')"
        continue
    }

    $lastIndex = -1
    foreach ($heading in $requiredHeadings) {
        $currentIndex = $positions[$heading]
        if ($currentIndex -lt $lastIndex) {
            $failures += "${file}: required headings are out of order."
            break
        }
        $lastIndex = $currentIndex
    }
}

if ($failures.Count -gt 0) {
    Write-Host "README structure validation failed:"
    $failures | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host "README structure validation passed for $($moduleReadmes.Count) module files."
