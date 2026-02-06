@echo off
echo Starting AI Image Enhancer...
echo.
cd html
echo Flask is starting on http://127.0.0.1:8000
echo.
echo Opening in browser in 3 seconds...
timeout /t 3
start http://127.0.0.1:8000
python app.py
pause
