$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$reports = Get-ChildItem -Path $root -Directory -Filter 'DAY-*' | ForEach-Object {
  $day = [int]($_.Name -replace '\D','')
  $path = Join-Path $_.FullName 'Readme.md'
  if (Test-Path $path) {
    $md = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
    $title = ([regex]::Match($md, '^#\s+(.+)', 'Multiline')).Groups[1].Value
    $date = ([regex]::Match($md, '\*\*Date:\*\*\s*(.+)')).Groups[1].Value.Trim()
    [pscustomobject][ordered]@{ day = $day; title = $title; date = $date; markdown = $md }
  }
} | Sort-Object day -Descending
$json = $reports | ConvertTo-Json -Depth 5 -Compress
Set-Content -Path (Join-Path $root 'reports.js') -Value "window.REPORTS = $json;" -Encoding UTF8
