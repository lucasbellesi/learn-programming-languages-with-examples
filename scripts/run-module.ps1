param(
    [Parameter(Mandatory = $true)]
    [string]$ModulePath
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

function Convert-ToWslPath([string]$path) {
    $fullPath = [System.IO.Path]::GetFullPath($path)
    $drive = $fullPath.Substring(0, 1).ToLower()
    $rest = $fullPath.Substring(2).Replace("\", "/")
    return "/mnt/$drive$rest"
}

$normalized = $ModulePath -replace "\\", "/"
$fullModulePath = Join-Path $root $normalized
$runningOnWindows = $env:OS -eq "Windows_NT"

if (-not (Test-Path $fullModulePath -PathType Container)) {
    Write-Host "Module folder not found: $normalized"
    exit 1
}

$exampleFile = Join-Path $fullModulePath "example/main.cpp"
if (-not (Test-Path $exampleFile -PathType Leaf)) {
    Write-Host "Missing example file: $normalized/example/main.cpp"
    exit 1
}

$outputPath = Join-Path ([System.IO.Path]::GetTempPath()) ("run_module_" + [Guid]::NewGuid().ToString("N"))

$nativeGpp = Get-Command g++ -ErrorAction SilentlyContinue
$wslCommand = Get-Command wsl -ErrorAction SilentlyContinue
$useWsl = $false

if (-not $nativeGpp) {
    if ($runningOnWindows -and $wslCommand) {
        $useWsl = $true
    } else {
        Write-Host "g++ was not found in PATH."
        Write-Host "Install g++ (or use WSL on Windows) and try again."
        exit 1
    }
}

Write-Host "Compiling example: $normalized/example/main.cpp"
try {
    if ($useWsl) {
        $exampleWslPath = Convert-ToWslPath $exampleFile
        $outputWslPath = Convert-ToWslPath $outputPath
        wsl bash -lc "g++ -std=c++17 -Wall -Wextra -pedantic -pthread '$exampleWslPath' -o '$outputWslPath'"
    } else {
        $extraFlags = @()
        if (-not $runningOnWindows) {
            $extraFlags += "-pthread"
        }
        g++ -std=c++17 -Wall -Wextra -pedantic @extraFlags $exampleFile -o $outputPath
    }

    Write-Host "Running example..."
    if ($useWsl) {
        $outputWslPath = Convert-ToWslPath $outputPath
        wsl bash -lc "'$outputWslPath'"
    } elseif ($runningOnWindows) {
        if (Test-Path "$outputPath.exe") {
            & "$outputPath.exe"
        } else {
            & $outputPath
        }
    } else {
        & $outputPath
    }

    $exerciseDir = Join-Path $fullModulePath "exercises"
    if (Test-Path $exerciseDir -PathType Container) {
        $exerciseFiles = Get-ChildItem $exerciseDir -Filter "*.cpp" | Sort-Object Name
        if ($exerciseFiles.Count -gt 0) {
            Write-Host ""
            Write-Host "Exercises in $normalized/exercises:"
            foreach ($exercise in $exerciseFiles) {
                Write-Host "- $normalized/exercises/$($exercise.Name)"
            }
        }
    }
} finally {
    Remove-Item "$outputPath" -ErrorAction SilentlyContinue
    Remove-Item "$outputPath.exe" -ErrorAction SilentlyContinue
}
