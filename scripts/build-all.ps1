$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$cppFiles = Get-ChildItem -Recurse -Path "languages/cpp" -Filter "*.cpp"
if ($cppFiles.Count -eq 0) {
    Write-Host "No C++ files found under languages/cpp"
    exit 0
}

$buildDir = Join-Path $root "build"
New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

$extraFlags = @()
if ($IsLinux -or $IsMacOS) {
    $extraFlags += "-pthread"
}

$index = 0
foreach ($file in $cppFiles) {
    $output = Join-Path $buildDir ("check_" + $index)
    Write-Host "Compiling: $($file.FullName)"
    g++ -std=c++17 -Wall -Wextra -pedantic @extraFlags $file.FullName -o $output
    $index++
}

Write-Host "Compiled $index file(s) successfully."
