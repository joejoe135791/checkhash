import os
import sys
import hashlib
import json

if os.name == 'nt':
    os.system('color')

print("CheckHash Program by joejoe135791")
print("Make sure that this program is executed in the same folder as the file you're checking the hash of")
print("if you download this from the same repository and do not fully trust it. download this program from https://github.com/joejoe135791/checkhash")
print("====================")
print(f'\033[91mWARNING! This program is automatically checking the hash of the file in autoHash.json! Make sure the json file is legitimate as it can be easily tampered with!\033[0m')
input("Press any button to acknoledge this warning")
if os.path.isfile(f"{os.getcwd()}/autoHash.json"):
    jsonHashData = json.load(open(f"{os.getcwd()}/autoHash.json"))
else:
    sys.exit("autoHash.json NOT FOUND!")

userFilenameInput = jsonHashData['programName']
filePathInput = f"{os.getcwd()}/{userFilenameInput}"
if os.path.isfile(filePathInput):
    pass
else:
    sys.exit(f"\n{filePathInput} Not found! please try again")
userHashInput = jsonHashData['programHash']
print(f"generating SHA256 hash of '{userFilenameInput}'")
print(f"Your SHA256 hash:\n{userHashInput}\n")
generatedFileHash = hashlib.sha256(open(userFilenameInput,'rb').read()).hexdigest()
print(f"Generated SHA256 hash of {filePathInput}:\n{generatedFileHash}\n")
if userHashInput == generatedFileHash:
    print(f"SHA256 hash verified, this program has likely not been tampered with")
else:
    print("THE SHA256 HASHES DO NOT MATCH UP! This program may have been modified or tampered with")