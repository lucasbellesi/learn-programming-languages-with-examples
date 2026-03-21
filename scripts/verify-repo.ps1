$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

function Assert-LastExitCode([string]$action) {
    if (($null -ne $LASTEXITCODE) -and ($LASTEXITCODE -ne 0)) {
        Write-Host "$action failed with exit code $LASTEXITCODE."
        exit $LASTEXITCODE
    }
}

Write-Host "[1/2] Checking markdown links..."
& "$PSScriptRoot\check-links.ps1"
Assert-LastExitCode "Markdown link check"

Write-Host "[2/2] Compiling C++ files..."
& "$PSScriptRoot\build-all.ps1"
Assert-LastExitCode "C++ build"

Write-Host "Repository verification completed successfully."
