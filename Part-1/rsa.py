from math import gcd

# 1. Key Generation
p, q = 3, 11
n = p * q                
phi = (p - 1) * (q - 1) 

e = 3
while gcd(e, phi) != 1:
    e += 2
d = pow(e, -1, phi)      # Private key exponent (d = 7)

message = 4
ciphertext = pow(message, e, n)    
decrypted  = pow(ciphertext, d, n)

print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")
print(f"Message: {message} | Cipher: {ciphertext} | Decrypted: {decrypted}")

