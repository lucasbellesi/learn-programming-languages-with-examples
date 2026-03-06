$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$mdFiles = Get-ChildItem -Recurse -Filter *.md
$brokenLinks = @()

foreach ($file in $mdFiles) {
    $content = Get-Content -Raw $file.FullName
    $matches = [regex]::Matches($content, '\[[^\]]+\]\(([^)]+)\)')

    foreach ($match in $matches) {
        $target = $match.Groups[1].Value.Trim()

        if ($target.StartsWith("http://") -or
            $target.StartsWith("https://") -or
            $target.StartsWith("mailto:") -or
            $target.StartsWith("#")) {
            continue
        }

        $hashIndex = $target.IndexOf('#')
        if ($hashIndex -ge 0) {
            $target = $target.Substring(0, $hashIndex)
        }

        if ([string]::IsNullOrWhiteSpace($target)) {
            continue
        }

        $candidate = Join-Path $file.DirectoryName $target
        if (-not (Test-Path $candidate)) {
            $brokenLinks += "$($file.FullName): $target"
        }
    }
}

if ($brokenLinks.Count -gt 0) {
    Write-Host "Broken markdown links found:"
    $brokenLinks | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host "No broken markdown links found."
