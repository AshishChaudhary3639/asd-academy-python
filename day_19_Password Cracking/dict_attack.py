import hashlib

def dictionary_attack_sha256(target_hash, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()
            hashed = hashlib.sha256(password.encode()).hexdigest()  # Secure Hash Algorithm 256-bit
            if hashed == target_hash:
                return password
    return None

# Save a wordlist.txt file with some passwords
target_hash = hashlib.sha256('password1234'.encode()).hexdigest()
result = dictionary_attack_sha256(target_hash, 'wordlist.txt')
print("Password found:", result)


import hashlib

# Target password and its hash (e.g., 'hello123')
target_password = input("Enter the Password:")
target_hash = hashlib.sha256(target_password.encode()).hexdigest()
print("Target SHA-256 Hash:", target_hash)

# Simulated wordlist
wordlist = ["123456", "password", "hello", "hello123", "admin","ayush"]

def crack_sha256(hash_to_crack, wordlist):
    for word in wordlist:
        hashed_word = hashlib.sha256(word.encode()).hexdigest()
        if hashed_word == hash_to_crack:
            return word
    return None

cracked_password = crack_sha256(target_hash, wordlist)
print("Cracked Password:", cracked_password if cracked_password else "Not found.")
