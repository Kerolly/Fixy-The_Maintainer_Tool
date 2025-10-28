@echo off
REM =============================================
REM   Open the Windows hosts file as Administrator
REM =============================================

echo.
echo Opening hosts file...
echo (Make sure this window is run as Administrator!)
echo.

:: Path to the hosts file
set "HOSTS=%SystemRoot%\System32\drivers\etc\hosts"

:: Open hosts file with Notepad
notepad "%HOSTS%"