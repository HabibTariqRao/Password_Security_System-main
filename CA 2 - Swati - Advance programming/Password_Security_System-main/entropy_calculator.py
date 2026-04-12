import math

# Calculate password entropy
def calculate_entropy(password):

    charset = 0

    # Determine character set size
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in "!@#$%^&*()" for c in password):
        charset += 10

    # Entropy formula: length * log2(charset)
    entropy = len(password) * math.log2(charset) if charset else 0

    return round(entropy, 2)