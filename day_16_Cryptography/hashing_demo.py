import hashlib

password = "ayushsahu"
hashed = hashlib.sha256(password.encode()).hexdigest()

print("SHA-256 Hash:", hashed)

# User tries to log in with input
input_password = "ayushsahus"  # Input from login form

# Hash the input
input_hashed = hashlib.sha256(input_password.encode()).hexdigest()
print("Input Password:",input_hashed)

# Load stored hashed password (from database)
stored_hashed = "0a20b03b835e0326784c147d9c161d3deef24d9c46d5f8bc0f514e4311993e4d"

# Compare
if input_hashed == stored_hashed:
    print(" Password matched. Access granted.")
else:
    print(" Incorrect password. Access denied.")
