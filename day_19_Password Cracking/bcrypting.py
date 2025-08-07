#Using Brute force
# import bcrypt
# import itertools
# import string
# import time

# # The real password (hashed with bcrypt)
# real_password = b"abc"
# hashed = bcrypt.hashpw(real_password, bcrypt.gensalt())

# # Character set for brute-force (lowercase only for speed)
# charset = string.ascii_lowercase
# max_length = 3  # Keep small, bcrypt is slow!

# start_time = time.time()

# found = False
# for length in range(1, max_length + 1):
#     for guess_tuple in itertools.product(charset, repeat=length):
#         guess = ''.join(guess_tuple).encode()

#         if bcrypt.checkpw(guess, hashed):
#             print(f"Password found: {guess.decode()}")
#             found = True
#             break
#     if found:
#         break

# print("Time taken:", round(time.time() - start_time, 2), "seconds")

#Using Dictionary Attack
import bcrypt

# Hash a known password
password = b"secure123"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Simulated dictionary
dictionary = [
    "123456", "password", "admin", "letmein", "secure123", "qwerty", "welcome"
]

# Try each word from dictionary
for word in dictionary:
    if bcrypt.checkpw(word.encode(), hashed):
        print(f"Password found: {word}")
        break
else:
    print("Password not found in dictionary")
