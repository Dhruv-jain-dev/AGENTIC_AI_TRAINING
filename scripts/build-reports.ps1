$ErrorActionPreference = 'Stop'

$repoOwner = 'Dhruv-jain-dev'
$repoName = 'AGENTIC_AI_TRAINING'
$branch = 'main'
$root = Split-Path -Parent $PSScriptRoot

function Get-Overview {
  param([string]$Markdown)
  $overviewMatch = [regex]::Match($Markdown, '## Overview\s+([\s\S]*?)(?=\n##|\n---|$)', 'IgnoreCase')
  if ($overviewMatch.Success -and $overviewMatch.Groups[1].Value.Trim()) {
    return ($overviewMatch.Groups[1].Value.Trim() -replace '\*\*', '' -replace '`', '')
  }

  $paragraph = ($Markdown -split "`r?`n" | Where-Object {
    $_.Trim() -and -not ($_.Trim() -match '^#') -and -not ($_.Trim() -match '^Date:')
  } | Select-Object -First 1)

  if ($paragraph) {
    return ($paragraph.Trim() -replace '\*\*', '' -replace '`', '')
  }

  return ''
}

function Get-Tags {
  param([string]$Markdown)
  [regex]::Matches($Markdown, '^### \d+\.\s+(.+)$', 'Multiline') |
    ForEach-Object { ($_.Groups[1].Value -replace '\*\*|`', '') -replace "`r", '' } |
    ForEach-Object { $_.Trim() } |
    Select-Object -First 4
}

function Get-DateValue {
  param([string]$Markdown)
  $dateMatch = [regex]::Match($Markdown, '\*\*Date:\*\*\s*(.+)$', 'Multiline')
  if ($dateMatch.Success) {
    return $dateMatch.Groups[1].Value.Trim()
  }
  return ''
}

function Get-Title {
  param([string]$Markdown, [string]$Fallback)
  $titleMatch = [regex]::Match($Markdown, '^#\s+(.+)$', 'Multiline')
  $rawTitle = if ($titleMatch.Success) { $titleMatch.Groups[1].Value } else { $Fallback }
  return ($rawTitle -replace '^Day\s*\d+\s*[-–—]\s*', '').Trim()
}

function Get-Files {
  param([System.IO.DirectoryInfo]$Folder)
  Get-ChildItem -Path $Folder.FullName -File -Recurse | ForEach-Object {
    $relative = $_.FullName.Substring($root.Length + 1) -replace '\\', '/'
    [pscustomobject][ordered]@{
      name = $_.Name
      path = $relative
      url = "https://github.com/$repoOwner/$repoName/blob/$branch/$relative"
      rawUrl = "https://raw.githubusercontent.com/$repoOwner/$repoName/$branch/$relative"
      isMarkdown = [bool]($_.Extension -match '\.md$')
    }
  }
}

function Get-MarkdownFile {
  param([array]$Files)
  $preferredNames = @('README.md', 'Readme.md', 'readme.md', 'index.md', 'report.md')
  foreach ($name in $preferredNames) {
    $hit = $Files | Where-Object { $_.name -ieq $name } | Select-Object -First 1
    if ($hit) { return $hit }
  }
  return $Files | Where-Object { $_.isMarkdown } | Select-Object -First 1
}

$reports = Get-ChildItem -Path $root -Directory -Filter 'DAY-*' | ForEach-Object {
  $day = [int]($_.Name -replace '\D', '')
  $files = Get-Files -Folder $_
  $markdownFile = Get-MarkdownFile -Files $files
  $markdown = ''

  if ($markdownFile) {
    $markdown = [System.IO.File]::ReadAllText((Join-Path $root $markdownFile.path), [System.Text.Encoding]::UTF8)
  }

  [pscustomobject][ordered]@{
    day = $day
    folderName = $_.Name
    folderUrl = "https://github.com/$repoOwner/$repoName/tree/$branch/$($_.Name)"
    files = @($files)
    markdownFile = $markdownFile
    title = if ($markdown) { Get-Title -Markdown $markdown -Fallback $_.Name } else { $_.Name }
    date = if ($markdown) { Get-DateValue -Markdown $markdown } else { '' }
    overview = if ($markdown) { Get-Overview -Markdown $markdown } else { "Uploaded files inside $($_.Name)." }
    tags = if ($markdown) { @((Get-Tags -Markdown $markdown)) } else { @() }
    markdown = $markdown
  }
} | Sort-Object day -Descending

$json = $reports | ConvertTo-Json -Depth 8 -Compress
Set-Content -Path (Join-Path $root 'reports.js') -Value "window.REPORTS = $json;" -Encoding UTF8
