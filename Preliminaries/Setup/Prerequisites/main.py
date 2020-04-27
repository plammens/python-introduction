import sys
import subprocess


print(f"Python {sys.version}")

try:
    cp = subprocess.run(["python", "--version"])
except FileNotFoundError:
    print("ERROR: python not found in PATH", file=sys.stderr)
