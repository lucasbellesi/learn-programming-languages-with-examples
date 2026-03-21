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

function Assert-LastExitCode([string]$action) {
    if ($LASTEXITCODE -ne 0) {
        Write-Host "$action failed with exit code $LASTEXITCODE."
        exit $LASTEXITCODE
    }
}

function Assert-WslToolchainReady() {
    wsl bash -lc "command -v g++ >/dev/null 2>&1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "WSL fallback is not ready: unable to run g++ inside WSL."
        Write-Host "Install g++ in WSL, fix WSL access, or install native g++ on Windows."
        exit 1
    }
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
        Write-Host "Native g++ not found. Using WSL g++ fallback."
        Assert-WslToolchainReady
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
        Assert-LastExitCode "Compilation via WSL for $normalized/example/main.cpp"
    } else {
        $extraFlags = @()
        if (-not $runningOnWindows) {
            $extraFlags += "-pthread"
        }
        g++ -std=c++17 -Wall -Wextra -pedantic @extraFlags $exampleFile -o $outputPath
        Assert-LastExitCode "Compilation for $normalized/example/main.cpp"
    }

    Write-Host "Running example..."
    if ($useWsl) {
        $outputWslPath = Convert-ToWslPath $outputPath
        wsl bash -lc "'$outputWslPath'"
        Assert-LastExitCode "Execution via WSL for $normalized/example/main.cpp"
    } elseif ($runningOnWindows) {
        if (Test-Path "$outputPath.exe") {
            & "$outputPath.exe"
        } else {
            & $outputPath
        }
        Assert-LastExitCode "Execution for $normalized/example/main.cpp"
    } else {
        & $outputPath
        Assert-LastExitCode "Execution for $normalized/example/main.cpp"
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
