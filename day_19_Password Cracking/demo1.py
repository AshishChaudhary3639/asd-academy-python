# import hashlib
# import itertools
# import string
# def brute_force_md5(target_hash,max_length=4):
#     characters=string.ascii_lowercase+string.digits
#     for length in range(1,max_length+1):
#         for guess in itertools.product(characters,repeat=length):
#             # print("Guesses=",guess)
#             guess_word=''.join(guess)
#             print("Guess Word",guess_word)
#             hashed=hashlib.md5(guess_word.encode()).hexdigest()
#             if target_hash==hashed:
#                 return guess_word

# text=input("Enter your password:")
# target_hash=hashlib.md5(text.encode()).hexdigest()
# print("Target Hash:",target_hash)
# result=brute_force_md5(target_hash)
# print("Password found:",result)

import random
chars="abcdefghijklmnopqrstuvwxyz1234567890"
allchar=list(chars)
pwd=input("Enter the password")
sample_pwd=""
while(sample_pwd!=pwd):
    sample_pwd=random.choices(allchar,k=len(pwd))
    print("<====="+str(sample_pwd)+"======>")
    if (sample_pwd==list(pwd)):
        print("Sample=",sample_pwd)
        print("The password is:"+ "".join(sample_pwd))
        break