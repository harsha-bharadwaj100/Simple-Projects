# Encryption and Decryption of files and folders
from cryptography.fernet import Fernet

# # key generation
# key = Fernet.generate_key()

# # string the key in a file
# with open("filekey.key", "wb") as filekey:
#     filekey.write(key)

# opening the key
with open("filekey.key", "rb") as filekey:
    key = filekey.read()

# using the key
fernet = Fernet(key)

# opening the encrypted file
with open("image (1).png", "rb") as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open("image (1).png", "wb") as dec_file:
    dec_file.write(decrypted)
