@echo off
echo ========================================
echo AI Image Enhancer - Simple Mode
echo ========================================
echo.

if "%~1"=="" (
    echo Drag and drop an image onto this file
    echo Or run: enhance.bat "path\to\image.jpg"
    echo.
    pause
    exit /b
)

python enhance.py "%~1"
