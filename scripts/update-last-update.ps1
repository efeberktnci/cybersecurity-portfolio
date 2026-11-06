param(
  [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
  [string]$Date = (Get-Date -Format "yyyy--MM--dd"),
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"

function Update-File([string]$path, [string]$date, [bool]$dryRun) {
  $content = Get-Content -Raw -LiteralPath $path

  # Shields.io badge format we use across the repo:
  # ![Last update](https://img.shields.io/badge/Last%20update-YYYY--MM--DD-2F9E44?style=for-the-badge)
  # Also fixes a previously-broken form where the URL accidentally contained "$1" instead of "Last%20update-".
  $pattern = '(https://img\.shields\.io/badge/)(?:Last%20update-|\$1)\d{4}--\d{2}--\d{2}-(?:495057|2F9E44)(\?style=for-the-badge)'
  $replacement = '${1}Last%20update-' + $date + '-2F9E44${2}'

  $updated = [regex]::Replace($content, $pattern, $replacement)

  if ($updated -ne $content) {
    if ($dryRun) {
      Write-Output ("[DRY RUN] Would update: {0}" -f $path)
      return $true
    }

    Set-Content -LiteralPath $path -Value $updated -NoNewline
    Write-Output ("Updated: {0}" -f $path)
    return $true
  }

  return $false
}

$targets = Get-ChildItem -LiteralPath $Root -Recurse -File -Filter "README.md" |
  Where-Object { $_.FullName -notmatch '\\.git\\' } |
  Select-Object -ExpandProperty FullName

$changed = 0
foreach ($file in $targets) {
  if (Update-File -path $file -date $Date -dryRun:$DryRun) {
    $changed++
  }
}

Write-Output ("Done. Files updated: {0}. Date: {1}" -f $changed, $Date)
