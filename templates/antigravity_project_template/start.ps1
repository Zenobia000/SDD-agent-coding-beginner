# Workstation launcher — Windows native
# Auto: Windows Terminal -> WSL -> cd project -> zellij
#
# Usage:
#   .\start.ps1          # 3-pane
#   .\start.ps1 4        # 4-pane

param([string]$Layout = "default")

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

# Check WSL
if (-not (Get-Command wsl.exe -ErrorAction SilentlyContinue)) {
    Write-Error "WSL not installed. Run as Admin: wsl --install"
    exit 1
}

# Check Windows Terminal
if (-not (Get-Command wt.exe -ErrorAction SilentlyContinue)) {
    Write-Error "Windows Terminal not found. Install from Microsoft Store: Windows Terminal"
    exit 1
}

# Convert Windows path -> WSL path (D:\foo -> /mnt/d/foo)
$wslPath = (& wsl.exe wslpath -a "$ProjectRoot").Trim()
if (-not $wslPath) {
    Write-Error "Failed to resolve WSL path for: $ProjectRoot"
    exit 1
}

# Launch Windows Terminal -> WSL -> ./start in the project dir
& wt.exe wsl.exe --cd "$wslPath" -- bash ./start $Layout
