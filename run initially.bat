@echo off

set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %system

:start
cls

set python_ver=311

python %~dp0\get-pip.py

pip install -r "%~dp0requirements.txt"

pause
exit