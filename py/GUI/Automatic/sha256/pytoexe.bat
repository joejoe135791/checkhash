@echo off
pyinstaller --onefile checksha256hash-GUI-automatic.py -n checksha256hash-GUI-automatic -c --distpath ./compiledexe
python copyjsons.py
echo exe (should) be created, press enter to close
pause
exit