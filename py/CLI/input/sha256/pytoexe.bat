@echo off
pyinstaller --onefile checksha256hash-CLI-input.py -n checksha256hash-CLI-input -c --distpath ./compiledexe
python copyjsons.py
echo exe (should) be created, press enter to close
pause
exit