param(
  [switch]$Global
)

$hookPath = Join-Path (Get-Location) ".githooks"
if (-not (Test-Path $hookPath)) {
  Write-Error "Hook path not found: $hookPath"
  exit 1
}

if ($Global) {
  git config --global core.hooksPath ".githooks"
} else {
  git config core.hooksPath ".githooks"
}

Write-Host "Configured git hooksPath -> .githooks"

