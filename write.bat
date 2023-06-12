@echo off
cd src
call "../.venv/Scripts/mpremote.exe" rm :*
FOR %%f IN (*.py) do (
    echo %%f
    call "../.venv/Scripts/mpremote.exe" cp %%f :
)
call "../.venv/Scripts/mpremote.exe" rm :main.py
call "../.venv/Scripts/mpremote.exe" run main.py