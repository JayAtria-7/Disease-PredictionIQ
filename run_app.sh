#!/bin/bash

echo "========================================"
echo "Disease PredictionIQ Web App"
echo "Quick Start Script"
echo "Author: Jay Prakash"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/4] Checking Python installation..."
python3 --version
echo ""

echo "[2/4] Installing Flask dependencies..."
pip3 install -r requirements-flask.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo ""

echo "[3/4] Checking for trained models..."
if [ ! -f "models/scaler.pkl" ]; then
    echo ""
    echo "========================================"
    echo "WARNING: Model files not found!"
    echo "========================================"
    echo "Please run the Jupyter notebook first to train and save models:"
    echo "  1. Open: notebooks/01_data_exploration_and_preprocessing.ipynb"
    echo "  2. Run all cells to train models"
    echo "  3. Models will be saved in models/ directory"
    echo "========================================"
    echo ""
    exit 1
fi
echo "Models found!"
echo ""

echo "[4/4] Starting Flask web application..."
echo ""
echo "========================================"
echo "Application will start on:"
echo "http://localhost:5000"
echo "========================================"
echo "Press Ctrl+C to stop the server"
echo "========================================"
echo ""

python3 app.py
