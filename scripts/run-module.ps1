param(
    [Parameter(Mandatory = $true)]
    [string]$ModulePath
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
}

if (-not $pythonCmd) {
    Write-Host "Python was not found in PATH."
    exit 1
}

& $pythonCmd.Path "$PSScriptRoot\automation.py" run-module --module-path $ModulePath
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
