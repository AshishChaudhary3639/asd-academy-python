import rsa
# from rsa.key import PublicKey,PrivateKey
message="Hello Asif we are learning python"
publicKey,privateKey=rsa.newkeys(512)
encrypted_message=rsa.encrypt(message.encode(),publicKey)
print(encrypted_message)
decrypted_message=rsa.decrypt(encrypted_message,privateKey).decode()
print(decrypted_message)


from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Generate RSA keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Message to encrypt
message = b"Secure message with RSA"

# Encrypt with public key
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
# Public_key.encrypt(...) encrypts the message.
# padding.OAEP(...): uses Optimal Asymmetric Encryption Padding, which adds security.
# MGF1 (mask generation function) and SHA256 are used to ensure randomness.
# label=None: optional label (used for binding metadata).

# Decrypt with private key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

print("Encrypted:", ciphertext)
print("Decrypted:", plaintext.decode())
