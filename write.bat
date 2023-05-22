@echo off
cd src
FOR %%f IN (*.py) do (
    echo %%f
    call "../.venv/Scripts/mpremote.exe" cp %%f :
)
call "../.venv/Scripts/mpremote.exe" rm :main.py
call "../.venv/Scripts/mpremote.exe" run main.py