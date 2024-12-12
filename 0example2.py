# Demonstrates alignment of numbers in columns

import random

print("To get the sum of 2 dice:")
for i in range(100):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    roll = d1 + d2
    print(f"  {d1} {d2} sum is " + f"{roll}".rjust(2))