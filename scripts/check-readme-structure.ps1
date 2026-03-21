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

$moduleReadmes = Get-ChildItem -Path (Join-Path $root "languages") -Recurse -Filter README.md |
    Where-Object {
        $_.FullName -match '[\\/](cpp|csharp|go|python)[\\/]01-foundations[\\/][^\\/]+[\\/]README\.md$'
    }

if ($moduleReadmes.Count -eq 0) {
    Write-Host "No module README files found for validation."
    exit 1
}

$failures = @()

foreach ($file in $moduleReadmes) {
    $content = Get-Content -Path $file.FullName -Raw
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
        $failures += "$($file.FullName): missing -> $($missing -join ', ')"
        continue
    }

    $lastIndex = -1
    foreach ($heading in $requiredHeadings) {
        $currentIndex = $positions[$heading]
        if ($currentIndex -lt $lastIndex) {
            $failures += "$($file.FullName): required headings are out of order."
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
