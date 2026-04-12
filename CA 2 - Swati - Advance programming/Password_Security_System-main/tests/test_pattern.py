import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pattern_checker import detect_pattern

print(detect_pattern("abcd1234"))