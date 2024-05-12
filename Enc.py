# Encryption and Decryption of files and folders
from cryptography.fernet import Fernet
import os

# # key generation
# key = Fernet.generate_key()

# # string the key in a file
# with open("filekey.key", "wb") as filekey:
#     filekey.write(key)

# opening the key
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

# using the generated key
fernet = Fernet(key)
for dirname, subdirlist, filelist in os.walk("C:\D-sim\pyprojs\AI Images"):
    print(dirname)
    for filename in filelist:
        print(f"Encrypting {filename}...")
        # opening the original file to encrypt
        with open(dirname + "\\" + filename, "rb") as file:
            original = file.read()
        # delete originarl file
        os.remove(dirname + "\\" + filename)

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(dirname + "\\" + filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
