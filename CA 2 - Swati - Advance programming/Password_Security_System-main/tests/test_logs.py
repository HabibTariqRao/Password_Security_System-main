import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logger import log_activity, get_logs

log_activity("admin", "Strong", False)

print(get_logs())