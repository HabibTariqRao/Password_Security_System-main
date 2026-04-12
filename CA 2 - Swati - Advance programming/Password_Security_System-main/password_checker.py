import re

# Evaluate password strength based on multiple criteria
def check_password_strength(password):
    score = 0
    feedback = []

    # Check minimum length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Check for numeric digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Determine strength level based on score
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback