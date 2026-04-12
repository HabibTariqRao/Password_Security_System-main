import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from auth import register_user, login_user

print(register_user("admin", "Admin@123"))
print(login_user("admin", "Admin@123"))