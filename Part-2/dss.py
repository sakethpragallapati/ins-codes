from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = input("Enter a message: ").encode('utf-8')

signature = private_key.sign(message,hashes.SHA256())
print(f"Signature Generated: {signature.hex()}")

try:
    public_key.verify(signature,message,hashes.SHA256())
    print("VERIFICATION SUCCESSFUL!")
except:
    print("VERIFICATION FAILED!")

try:
    public_key.verify(signature,message+b'modified',hashes.SHA256())
    print("VERIFICATION SUCCESSFUL!")
except:
    print("VERIFICATION FAILED!")