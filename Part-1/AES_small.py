import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = secrets.token_bytes(16)  
cipher = AES.new(key, AES.MODE_ECB)

# Encryption
message = b'Hello World'
encrypted = cipher.encrypt(pad(message, 16))

print("AES Key (hex):", key.hex())
print("AES Encrypted:", encrypted.hex())

# Decryption
decrypted = unpad(cipher.decrypt(encrypted), 16)

print("AES Decrypted:", decrypted.decode())

# pip install pycryptodome