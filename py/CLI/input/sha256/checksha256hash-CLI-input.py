import os
import sys
import hashlib

print("CheckHash Program by joejoe135791")
print("Make sure that this program is executed in the same folder as the file you're checking the hash of")
print("if you download this from the same repository and do not fully trust it. download this program from https://github.com/joejoe135791/checkhash")
print("====================")
while True:
    userFilenameInput = input("Enter the file name: ")
    filePathInput = f"{os.getcwd()}/{userFilenameInput}"
    if os.path.isfile(filePathInput):
        break
    else:
        print(f"\n{filePathInput} Not found! please try again")
userHashInput = input("Please enter the SHA256 hash given by the repository: ")
print(f"generating SHA256 hash of '{userFilenameInput}'")
print(f"Your SHA256 hash:\n{userHashInput}\n")
generatedFileHash = hashlib.sha256(open(userFilenameInput,'rb').read()).hexdigest()
print(f"Generated SHA256 hash of {filePathInput}:\n{generatedFileHash}\n")
if userHashInput == generatedFileHash:
    print(f"SHA256 hash verified, this program has likely not been tampered with")
else:
    print("THE SHA256 HASHES DO NOT MATCH UP! This program may have been modified or tampered with")