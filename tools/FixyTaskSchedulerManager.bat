@echo off
title Fixy Task Scheduler Manager
color 0A

:MENU
cls
echo ===============================================
echo             Fixy The Maintainer Tool
echo ===============================================
echo.
echo  1^)  Create or update auto-start task
echo  2^)  Delete auto-start task
echo  0^)  Exit
echo.
set /p choice=Select an option:

if "%choice%"=="1" goto CREATE
if "%choice%"=="2" goto DELETE
if "%choice%"=="0" goto EXIT

echo.
echo Invalid option. Please try again.
pause
goto MENU

:CREATE
echo.
echo   Creating or updating Fixy Auto-Start task...
powershell -ExecutionPolicy Bypass -File "%~dp0setup_fixy_task_scheduler.ps1"
echo Created successfully
echo.
pause
goto MENU

:DELETE
echo.
echo   Removing Fixy Auto-Start task...
powershell -ExecutionPolicy Bypass -File "%~dp0delete_fixy_task_scheduler.ps1"
echo Removed successfully
echo.
pause
goto MENU

:EXIT
echo.
echo   Exiting...
timeout /t 1 >nul
exit /b