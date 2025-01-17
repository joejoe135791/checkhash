@echo off
echo This script will check the hash of the provided file, be sure to input the hash correctly, NO SPACES
set /p choice= "Please enter the md5 hash :"
echo You input %choice%
set filelocation= ./README.md
echo generated hash: certutil -hashfile "./README.md" SHA256
if %choice% EQU certutil -hashfile "./README.md" SHA256 (
    echo The generated hashes are correct, this file has likely not been modified
    ) else (
        echo The hashes do not line up, the file may have been tampered with!
    )
pause
exit