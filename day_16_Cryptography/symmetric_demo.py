from cryptography.fernet import Fernet

# pip install cryptography==3.4.8
# Generate a key
# key = Fernet.generate_key()
# print(key)
# cipher = Fernet(key)

# # Encrypt a message
# message = b"We are learning Cryptography in Python"
# encrypted = cipher.encrypt(message)

# # Decrypt the message
# decrypted = cipher.decrypt(encrypted)

# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted.decode())


# # Step 1: Generate and print a key
# key = Fernet.generate_key()
# ashish = Fernet(key)
# print("Key:", key.decode())

# # # # Step 2: Encrypt a message
# message = b"My secret message"
# encrypted = ashish.encrypt(message)
# print("Encrypted:", encrypted.decode())

# # # # Step 3: Decrypt the message
# decrypted = ashish.decrypt(encrypted)
# print("Decrypted:", decrypted.decode())

# Generate key and save it
key = Fernet.generate_key()
cipher = Fernet(key)

# Save key to file (optional)
with open("filekey.key", "wb") as f:
    f.write(key)

# Encrypt the contents of a file
with open("sample.txt", "rb") as file:
    original = file.read()

encrypted = cipher.encrypt(original)

with open("sample_encrypted", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

# Decrypt the file
with open("sample_encrypted", "rb") as enc_file:
    encrypted_data = enc_file.read()

decrypted = cipher.decrypt(encrypted_data)
print(decrypted)

with open("sample_decrypted.txt", "wb") as dec_file:
    data=dec_file.write(decrypted)
