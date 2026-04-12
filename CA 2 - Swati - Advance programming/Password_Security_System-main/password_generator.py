import random
import string

# Generate a random secure password
def generate_password(length=12, upper=True, numbers=True, symbols=True):

    # Start with lowercase characters
    characters = string.ascii_lowercase

    # Add uppercase characters if enabled
    if upper:
        characters += string.ascii_uppercase

    # Add numeric digits if enabled
    if numbers:
        characters += string.digits

    # Add special symbols if enabled
    if symbols:
        characters += "!@#$%^&*()"

    # Randomly select characters to form password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password