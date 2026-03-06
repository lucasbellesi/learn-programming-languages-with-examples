$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

Write-Host "[1/2] Checking markdown links..."
& "$PSScriptRoot\check-links.ps1"

Write-Host "[2/2] Compiling C++ files..."
& "$PSScriptRoot\build-all.ps1"

Write-Host "Repository verification completed successfully."
