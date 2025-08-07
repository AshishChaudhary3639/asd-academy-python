import hashlib
def dictionary_attack(target_hash,wordlist):
    with open("wordlist.txt","r") as file:
        for line in file:
            password=line.strip()
            hashed=hashlib.sha256(password.encode()).hexdigest()
            if hashed==target_hash:
                return password

password=input("Enter the password")
target_hash=hashlib.sha256(password.encode()).hexdigest()
result=dictionary_attack(target_hash,"wordlist.txt")
print("Password found",result)