import secrets
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = secrets.token_bytes(8)  
cipher = DES.new(key, DES.MODE_ECB)

# Encryption
message = b'Hello World'
encrypted = cipher.encrypt(pad(message, 8))

print("DES Key (hex):", key.hex())
print("DES Encrypted:", encrypted.hex())

# Decryption
decrypted = unpad(cipher.decrypt(encrypted), 8)

print("DES Decrypted:", decrypted.decode())

# pip install pycryptodome