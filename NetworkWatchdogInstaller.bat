@echo off
title Network Watchdog Control Panel
cls

REM Always work from script directory
cd /d "%~dp0"

:menu
cls
python tools\banner.py

echo =========================================================
echo                     MAIN MENU
echo =========================================================
echo ^[01^] Install Dependencies
echo ^[02^] Run Watchdog (Normal Mode)
echo ^[03^] Run Watchdog (Background Mode)
echo ^[04^] Stop Watchdog
echo ^[05^] View Logs
echo ^[06^] Background Status
echo ^[07^] Extra Tools ^>^>
echo ^[08^] About
echo ^[09^] Exit
echo =========================================================
echo.

set /p choice="Choose an option: "

if "%choice%"=="1" goto deps
if "%choice%"=="2" goto normal
if "%choice%"=="3" goto background
if "%choice%"=="4" goto stop
if "%choice%"=="5" goto logs
if "%choice%"=="6" goto status
if "%choice%"=="7" goto extra
if "%choice%"=="8" goto about
if "%choice%"=="9" exit

echo Invalid selection.
pause
goto menu

:deps
cls
python tools\banner.py
echo Installing dependencies...
pip install psutil colorama pyfiglet win10toast requests
pause
goto menu

:normal
cls
python tools\banner.py
python -m service.network_watchdog_service
pause
goto menu

:background
cls
python tools\banner.py
start "" /B pythonw -m service.network_watchdog_service
echo Watchdog is now running in background mode.
pause
goto menu

:stop
cls
python tools\banner.py
echo Stopping all watchdog processes...
taskkill /IM python.exe /F >nul 2>&1
taskkill /IM pythonw.exe /F >nul 2>&1
echo All watchdog processes stopped.
pause
goto menu

:logs
cls
python tools\banner.py
echo Showing activity log...
echo.
type logs\activity.log 2>nul
echo.
pause
goto menu

:status
cls
python tools\banner.py
echo Checking for background watchdog...

tasklist /FI "IMAGENAME eq pythonw.exe" | find /I "pythonw.exe" >nul
if %ERRORLEVEL%==0 (
    echo --------------------------------------------
    echo  Background Mode: RUNNING
    echo  Process: pythonw.exe is active
    echo --------------------------------------------
) else (
    echo --------------------------------------------
    echo  Background Mode: NOT RUNNING
    echo --------------------------------------------
)
echo.
pause
goto menu

:extra
cls
python tools\banner.py
echo =========================================================
echo                    EXTRA TOOLS
echo =========================================================
echo ^[A^] Clear Logs
echo ^[B^] Open Logs Folder
echo ^[C^] Show Python Version
echo ^[D^] Open Project Folder
echo ^[E^] Launch Watchdog (LOG Mode)
echo ^[F^] Launch Watchdog (Domain Mode)
echo ^[G^] Restart Background Mode
echo ^[H^] Run Diagnostic Mode
echo ^[I^] Return to Main Menu
echo =========================================================
echo.

set /p sub="Choose an option: "

if /I "%sub%"=="A" goto clearlogs
if /I "%sub%"=="B" goto openlogs
if /I "%sub%"=="C" goto pyver
if /I "%sub%"=="D" goto openfolder
if /I "%sub%"=="E" goto logmode
if /I "%sub%"=="F" goto domainmode
if /I "%sub%"=="G" goto restartbackground
if /I "%sub%"=="H" goto diagnostic
if /I "%sub%"=="I" goto menu

echo Invalid option.
pause
goto extra

:clearlogs
cls
python tools\banner.py
del logs\*.log >nul 2>&1
echo Logs have been cleared.
pause
goto extra

:openlogs
cls
python tools\banner.py
explorer logs\
goto extra

:pyver
cls
python tools\banner.py
python --version
echo.
pause
goto extra

:openfolder
cls
python tools\banner.py
explorer .
goto extra

:logmode
cls
python tools\banner.py
python -m service.watchdog_log_mode
pause
goto extra

:domainmode
cls
python tools\banner.py
python -m service.watchdog_domain_mode
pause
goto extra

:restartbackground
cls
python tools\banner.py
taskkill /IM pythonw.exe /F >nul 2>&1
start "" /B pythonw -m service.network_watchdog_service
echo Background watchdog restarted.
pause
goto extra

:diagnostic
cls
python tools\banner.py
python -m service.diagnostic_mode
pause
goto extra

:about
cls
python tools\banner.py
echo =========================================================
echo             NETWORK WATCHDOG CONTROL PANEL
echo ---------------------------------------------------------
echo  Version : 4.5 (Advanced)
echo  Author  : rayhanrwa
echo  System  : Windows-based Network Activity Monitoring
echo ---------------------------------------------------------
echo  Features:
echo    • Real-time connection logging
echo    • Background monitoring mode
echo    • Auto threat classification
echo    • DNS-aware domain resolution (optional)
echo    • Log viewer, cleaner, and tools
echo    • Modular service launcher
echo =========================================================
echo.
pause
goto menu
