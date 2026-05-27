@echo off
REM Workstation launcher — Windows (double-click friendly)
REM Forwards to start.ps1 with execution policy bypass.
powershell -ExecutionPolicy Bypass -NoProfile -File "%~dp0start.ps1" %*
