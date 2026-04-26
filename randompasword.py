"""
Random Password Generator - DecodeLabs Project 3 (Single File Version)
Input: User-specified length. Process: Secure random string. Output: Generated password.
Follows PDF specs: import string/secrets, validate int >=8, use ''.join() for O(n).
"""
import argparse
import string
import secrets
import sys

def get_password_length() -> int:
"""Phase 1: Input validation (PDF requirement)."""
while True:
try:
length = int(input("Enter password length (min 8): "))
if length < 8:
print("Length must be at least 8.")
continue
return length
except ValueError:
print("Enter a valid integer.")

def generate_password(length: int) -> str:
"""Phase 2: Secure generation (secrets + string + ''.join())."""
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(chars) for _ in range(length))
return password

def main_cli():
"""CLI mode with argparse (modern merge)."""
parser = argparse.ArgumentParser(description="DecodeLabs Project 3: Password Generator")
parser.add_argument('-l', '--length', type=int, default=None, metavar='N', help='Length (min 8)')
args = parser.parse_args()

length = args.length or get_password_length()
password = generate_password(length)
print(f"Generated password: {password}")
def main_interactive():
"""Interactive mode (pure PDF style)."""
length = get_password_length()
password = generate_password(length)
print(f"Your secure password ({length} chars): {password}")

if name == "main":
# Use CLI if args provided, else interactive
import sys
if len(sys.argv) > 1:
main_cli()
else:
main_interactive()
