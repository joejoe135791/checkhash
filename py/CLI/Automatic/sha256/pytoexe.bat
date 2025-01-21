@echo off
pyinstaller --onefile checksha256hash-CLI-automatic.py -n checksha256hash-CLI-automatic -c --distpath ./compiledexe
python copyjsons.py
echo exe (should) be created, press enter to close
pause
exit