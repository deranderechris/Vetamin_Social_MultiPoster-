@echo off
title Vetamin Social MultiPoster GUI

echo Prüfe Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo Fehler: Python ist nicht installiert!
    echo Bitte installiere Python von https://www.python.org/downloads/
    pause
    exit /b
)

echo.
echo Prüfe ttkbootstrap...
python -c "import ttkbootstrap" >nul 2>&1
if errorlevel 1 (
    echo ttkbootstrap wird installiert...
    python -m pip install ttkbootstrap
)

echo.
echo Starte GUI...
python -m src.gui.app
pause
