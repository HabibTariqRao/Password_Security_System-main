import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from password_checker import check_password_strength

password = "Test123"

strength, feedback = check_password_strength(password)

print("Password:", password)
print("Strength:", strength)
print("Feedback:", feedback)