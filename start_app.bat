@echo off
echo ========================================================
echo   Starting DhakreyStock AI - NSE & BSE Valuation Engine
echo ========================================================
echo.

:: Start FastAPI Backend in background
echo [1/2] Starting Backend API Server (FastAPI on http://127.0.0.1:8000)...
start "DhakreyStock Backend API" cmd /k "cd /d %~dp0backend && set PYTHONPATH=.&& venv\Scripts\python.exe main.py"

:: Wait 2 seconds
timeout /t 2 /nobreak >nul

:: Start Vite Frontend
echo [2/2] Starting Frontend App (Vite on http://localhost:5173)...
start "DhakreyStock Web UI" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo ========================================================
echo   DhakreyStock AI is launching!
echo   Frontend: http://localhost:5173
echo   API Docs: http://127.0.0.1:8000/docs
echo ========================================================
echo.
pause
