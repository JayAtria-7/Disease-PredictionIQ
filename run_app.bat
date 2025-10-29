@echo off
echo ========================================
echo Disease PredictionIQ Web App
echo Quick Start Script
echo Author: Jay Prakash
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version
echo.

echo [2/4] Installing Flask dependencies...
pip install -r requirements-flask.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo [3/4] Checking for trained models...
if not exist "models\scaler.pkl" (
    echo.
    echo ========================================
    echo WARNING: Model files not found!
    echo ========================================
    echo Please run the Jupyter notebook first to train and save models:
    echo   1. Open: notebooks/01_data_exploration_and_preprocessing.ipynb
    echo   2. Run all cells to train models
    echo   3. Models will be saved in models/ directory
    echo ========================================
    echo.
    pause
    exit /b 1
)
echo Models found!
echo.

echo [4/4] Starting Flask web application...
echo.
echo ========================================
echo Application will start on:
echo http://localhost:5000
echo ========================================
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py
