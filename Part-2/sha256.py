import hashlib

def sha256_function(message):
    encoded_message = message.encode('utf-8')
    hash_object = hashlib.sha256(encoded_message)
    return hash_object.hexdigest()

original_message = input("Enter a message: ")
hashed_message = sha256_function(original_message)

print(f"\nOriginal Message: {original_message}")
print(f"SHA-256 Hash: {hashed_message}")