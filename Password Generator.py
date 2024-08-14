import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."
    
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_characters = lower + upper + digits + special
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Prompt user for the desired password length
try:
    length = int(input("Enter the desired length of the password: "))
    if length < 1:
        print("Password length must be at least 1.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")

except ValueError:
    print("Error: Please enter a valid integer for the password length.")
