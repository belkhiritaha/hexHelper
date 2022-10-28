from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization

# generate Alice keys
alice_private_key = X25519PrivateKey.generate()
alice_public_key = alice_private_key.public_key()
print("Alice public key: ", alice_public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo))

# generate Bob keys
bob_private_key = X25519PrivateKey.generate()
bob_public_key = bob_private_key.public_key()


# Alice and Bob exchange public keys
alice_shared_key = alice_private_key.exchange(bob_public_key)
bob_shared_key = bob_private_key.exchange(alice_public_key)

# Alice and Bob derive the same shared key
print(alice_shared_key == bob_shared_key)
