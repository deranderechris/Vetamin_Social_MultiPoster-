@echo off
title Vetamin Social MultiPoster CLI

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
echo Starte CLI...
python -m src.main
pause
