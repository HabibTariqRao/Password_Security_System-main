# List of commonly used weak passwords
COMMON_PASSWORDS = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "abc123",
    "letmein"
]

# Detect weak or predictable patterns in passwords
def detect_pattern(password):

    warnings = []

    # Check if password is a common password
    if password.lower() in COMMON_PASSWORDS:
        warnings.append("Common password detected")

    # Check for sequential numeric pattern
    if "123" in password:
        warnings.append("Sequential numbers detected")

    # Check for alphabetical sequence
    if "abc" in password.lower():
        warnings.append("Alphabet sequence detected")

    # Check for palindrome pattern
    if password == password[::-1]:
        warnings.append("Palindrome pattern detected")

    return warnings