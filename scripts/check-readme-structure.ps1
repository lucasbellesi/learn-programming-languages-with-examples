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

function Get-HeadingLineNumber([string[]]$lines, [string]$heading) {
    $escapedHeading = [regex]::Escape($heading)
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match "^[ ]{0,3}$escapedHeading[ ]*$") {
            return $i + 1
        }
    }

    return -1
}

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
    $lines = Get-Content -Path $file
    $missing = @()
    $positions = @{}

    foreach ($heading in $requiredHeadings) {
        $lineNumber = Get-HeadingLineNumber -lines $lines -heading $heading
        if ($lineNumber -lt 0) {
            $missing += $heading
        } else {
            $positions[$heading] = $lineNumber
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
