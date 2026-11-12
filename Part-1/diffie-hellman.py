import secrets

# 1. Publicly shared prime number (P) and generator (G)
P = 997  # In real applications, P is a massive 2048-bit or 4096-bit prime number
G = 2

# 2. Alice and Bob generate their private keys
alice_private = secrets.randbelow(P)
bob_private = secrets.randbelow(P)

# 3. They generate public keys
alice_public = pow(G, alice_private, P)
bob_public = pow(G, bob_private, P)

# 4. They exchange public keys and compute the shared secret
alice_shared_key = pow(bob_public, alice_private, P)
bob_shared_key = pow(alice_public, bob_private, P)

print(f"Alice's Private Key: {alice_private}")
print(f"Bob's Private Key: {bob_private}\n")

print(f"Alice's Shared Key: {alice_shared_key}")
print(f"Bob's Shared Key: {bob_shared_key}")
print(f"Keys match: {alice_shared_key == bob_shared_key}")