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

$levelNames = @("01-foundations", "02-core", "03-advanced", "04-expert")
$languageExtensions = @{
    cpp = "cpp"
    csharp = "cs"
    go = "go"
    python = "py"
}

function Get-HeadingLineNumber([string[]]$lines, [string]$heading) {
    $escapedHeading = [regex]::Escape($heading)
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match "^[ ]{0,3}$escapedHeading[ ]*$") {
            return $i + 1
        }
    }

    return -1
}

$failures = @()
$moduleCount = 0

foreach ($language in $languageExtensions.Keys) {
    $langRoot = Join-Path $root "languages/$language"
    if (-not (Test-Path $langRoot)) {
        continue
    }

    foreach ($level in $levelNames) {
        $levelPath = Join-Path $langRoot $level
        if (-not (Test-Path $levelPath)) {
            continue
        }

        $moduleDirs = Get-ChildItem -Path $levelPath -Directory
        foreach ($module in $moduleDirs) {
            $moduleCount++
            $ext = $languageExtensions[$language]
            $readmePath = Join-Path $module.FullName "README.md"
            $exampleDir = Join-Path $module.FullName "example"
            $exerciseDir = Join-Path $module.FullName "exercises"
            $mainPath = Join-Path $exampleDir "main.$ext"
            $exercise01 = Join-Path $exerciseDir "01.$ext"
            $exercise02 = Join-Path $exerciseDir "02.$ext"

            if (-not (Test-Path $readmePath)) {
                $failures += "$($module.FullName): missing README.md"
                continue
            }

            if (-not (Test-Path $exampleDir)) {
                $failures += "$($module.FullName): missing example/ directory"
            }

            if (-not (Test-Path $exerciseDir)) {
                $failures += "$($module.FullName): missing exercises/ directory"
            }

            if (-not (Test-Path $mainPath)) {
                $failures += "$($module.FullName): missing example/main.$ext"
            }

            if (-not (Test-Path $exercise01)) {
                $failures += "$($module.FullName): missing exercises/01.$ext"
            }

            if (-not (Test-Path $exercise02)) {
                $failures += "$($module.FullName): missing exercises/02.$ext"
            }

            $lines = Get-Content -Path $readmePath
            $positions = @{}
            $missingHeadings = @()
            foreach ($heading in $requiredHeadings) {
                $lineNumber = Get-HeadingLineNumber -lines $lines -heading $heading
                if ($lineNumber -lt 0) {
                    $missingHeadings += $heading
                } else {
                    $positions[$heading] = $lineNumber
                }
            }

            if ($missingHeadings.Count -gt 0) {
                $failures += "$($module.FullName): README missing headings -> $($missingHeadings -join ', ')"
                continue
            }

            $lastIndex = -1
            foreach ($heading in $requiredHeadings) {
                $currentIndex = $positions[$heading]
                if ($currentIndex -lt $lastIndex) {
                    $failures += "$($module.FullName): README headings out of order."
                    break
                }
                $lastIndex = $currentIndex
            }
        }
    }
}

if ($moduleCount -eq 0) {
    Write-Host "No module directories found for completeness validation."
    exit 1
}

if ($failures.Count -gt 0) {
    Write-Host "Module completeness validation failed:"
    $failures | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host "Module completeness validation passed for $moduleCount module directories."
