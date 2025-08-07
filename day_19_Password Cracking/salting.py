# import bcrypt

# # Hash a password
# password = b"secret123"
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password, salt)

# print("Hashed password:", hashed)

# # Check password
# def check_password(stored_hash, user_input):
#     return bcrypt.checkpw(user_input.encode(), stored_hash)

# print("Is correct:", check_password(hashed, "secret123"))  # True

# Salt = Random data added to a password before hashing
# Prevents identical passwords from having the same hash
# hash("password" + "randomsalt")

import hashlib
import os

password1 = "mypassword"
password2="mypassword"

# Generate a random salt
salt1 = os.urandom(16)  # 16 bytes of randomness
salt2=os.urandom(16)
salted_password1 = salt1 + password1.encode()
salted_password2=salt2+password2.encode()

hash_with_salt1 = hashlib.sha256(salted_password1).hexdigest()
hash_with_salt2=hashlib.sha256(salted_password2).hexdigest()


# print("Salt:", salt)
print("Salted Hash 1:", hash_with_salt1)
print("Salted Hash 2:", hash_with_salt2)



# import hashlib

# password = "mypassword"
# hash1 = hashlib.sha256(password.encode()).hexdigest()
# print(hash1)
# hash2 = hashlib.sha256(password.encode()).hexdigest()
# print(hash2)
# print(hash1 == hash2)  # True – same password = same hash



# password1= "mypassword"
# password2= "mypassword"

# # Generate a random salt
# salt = os.urandom(16)  # 16 bytes of randomness
# print(salt.hex())
# salted_password1 = salt + password1.encode()
# salt = os.urandom(16)  # 16 bytes of randomness
# salted_password2 = salt + password2.encode()

# hash_with_salt1 = hashlib.sha256(salted_password1).hexdigest()
# hash_with_salt2 = hashlib.sha256(salted_password2).hexdigest()
# print("Salt:", salt)
# print("Salted Hash:", hash_with_salt2)
# if hash_with_salt1==hash_with_salt2:
#     print("password matched")
# else:
#     print("Not matched")