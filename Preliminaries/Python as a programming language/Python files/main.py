# this is a sample Python program file

import re
import sys
import platform


print("Hello, world!", end='\n\n')

while True:
    name = input("Please enter your name: ")
    if re.match(r'^[A-Za-z ]+$', name):
        break
    print("That doesn't look like a name!")

print(f"\nHello, {name.strip().split()[0].title()}!", end='\n\n')

print(f"This program has been interpreted by Python {sys.version.split()[0]} "
      f"running on {platform.platform(aliased=True, terse=True)}")
