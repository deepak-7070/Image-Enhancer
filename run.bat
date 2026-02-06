@echo off
echo ========================================
echo   AI Image Enhancer - Web Interface
echo ========================================
echo.
echo Starting server...
echo.
timeout /t 2 >nul
start http://127.0.0.1:5000
python app.py
pause
