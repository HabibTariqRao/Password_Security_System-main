import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from breach_checker import check_password_breach

password = "Khan@2122"

breached, count = check_password_breach(password)

print("Breached:", breached)
print("Times found:", count)