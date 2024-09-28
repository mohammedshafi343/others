import random
import string

def generate_password(length, include_symbols):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    length = int(input("Enter the desired password length: "))
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    password = generate_password(length, include_symbols)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    password_generator()
