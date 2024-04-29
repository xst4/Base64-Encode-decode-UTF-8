@echo off
cd /d %~dp0

title Checking Python installation...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed! (Go to https://www.python.org/downloads and install the latest version.^)
    echo Make sure it is added to PATH.
    goto ERROR
)

title Checking libraries...
echo Checking 'colorama' (1/4)
python -c "import colorama" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing colorama...
    python -m pip install colorama > nul
)

echo Checking 'getopt' (2/4)
python -c "import PIL" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing getopt...
    python -m pip install getopt > nul
)

echo Checking 'fade' (3/4)
python -c "import fade" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing fade...
    python -m pip install fade > nul
)

echo Checking 're' (4/4)
python -c "import re" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing re...
    python -m pip install re > nul
)

cls
title Starting ...
python main.py
if %errorlevel% neq 0 goto ERROR
exit

:ERROR
color 4 && title [Error]
pause > nul