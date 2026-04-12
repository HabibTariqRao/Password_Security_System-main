import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from history import save_password, check_password_reuse

save_password("admin", "Khan@5487")

print(check_password_reuse("admin", "Khan@5487"))