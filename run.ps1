# PowerShell Launcher for DhakreyStock AI
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Starting DhakreyStock AI - NSE & BSE Valuation Engine" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

$rootDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# 1. Start Backend in new process
Write-Host "[1/2] Starting Backend API Server (FastAPI on http://127.0.0.1:8000)..." -ForegroundColor Green
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "cd '$rootDir\backend'; `$env:PYTHONPATH='.'; .\venv\Scripts\python.exe main.py"

Start-Sleep -Seconds 2

# 2. Start Frontend in new process
Write-Host "[2/2] Starting Frontend App (Vite on http://localhost:5173)..." -ForegroundColor Green
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "cd '$rootDir\frontend'; npm run dev"

Write-Host ""
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  DhakreyStock AI is launching!" -ForegroundColor Cyan
Write-Host "  Frontend: http://localhost:5173" -ForegroundColor Yellow
Write-Host "  API Docs: http://127.0.0.1:8000/docs" -ForegroundColor Yellow
Write-Host "========================================================" -ForegroundColor Cyan
