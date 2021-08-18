"""
Day 1's work
"""

import random

num = random.randint(0, 6)

print(f"Your dice roll : {num}")


# modification from day 2

if num >= 4:
    print("You won!")
else:
    print("Sad, try again next time.")
