import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from entropy_calculator import calculate_entropy

print(calculate_entropy("Khan@2122"))