$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
$runningOnWindows = $env:OS -eq "Windows_NT"

function Convert-ToWslPath([string]$path) {
    $fullPath = [System.IO.Path]::GetFullPath($path)
    $drive = $fullPath.Substring(0, 1).ToLower()
    $rest = $fullPath.Substring(2).Replace("\", "/")
    return "/mnt/$drive$rest"
}

$cppFiles = Get-ChildItem -Recurse -Path "languages/cpp" -Filter "*.cpp"
if ($cppFiles.Count -eq 0) {
    Write-Host "No C++ files found under languages/cpp"
    exit 0
}

$buildDir = Join-Path $root "build"
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

$nativeGpp = Get-Command g++ -ErrorAction SilentlyContinue
$wslCommand = Get-Command wsl -ErrorAction SilentlyContinue
$useWsl = $false

if (-not $nativeGpp) {
    if ($runningOnWindows -and $wslCommand) {
        $useWsl = $true
        Write-Host "Native g++ not found. Using WSL g++ fallback."
    } else {
        Write-Host "g++ was not found in PATH."
        Write-Host "Install g++ (or use WSL on Windows) and try again."
        exit 1
    }
}

$index = 0
foreach ($file in $cppFiles) {
    Write-Host "Compiling: $($file.FullName)"

    if ($useWsl) {
        $wslFile = Convert-ToWslPath $file.FullName
        $wslOutput = "/tmp/build_all_check_$index"
        wsl bash -lc "g++ -std=c++17 -Wall -Wextra -pedantic -pthread '$wslFile' -o '$wslOutput'"
    } else {
        $output = Join-Path $buildDir ("check_" + $index)
        $extraFlags = @()
        if (-not $runningOnWindows) {
            $extraFlags += "-pthread"
        }
        g++ -std=c++17 -Wall -Wextra -pedantic @extraFlags $file.FullName -o $output
    }

    $index++
}

Write-Host "Compiled $index file(s) successfully."
