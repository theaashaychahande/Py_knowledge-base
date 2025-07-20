"""
1. Definition:  
Modules are Python files you can reuse in other programs 
2. Why Use:  
To organize code and use others' work (like math tools)  
"""

# Example 1: Built-in module (math)
import math
print(f"Aashay's circle area:", math.pi * 5**2) 

# Example 2: Custom module (imaginary file)
# File: vansh_utils.py
"""
def greet(name):
    print(f"Vansh says hello to {name}!")
"""
# Usage:
# from vansh_utils
# import greet
# greet("Aashay") → "Vansh says hello to Aashay!"

# Example 3: Renaming imports
import random as r
print(f"Aashay's random number:", r.randint(1, 10))  # (rand+int)

# Example 4: Partial import
from datetime import date
vanshs_birthday = date(2004, 7, 15)  # Hypothetical date
print("Vansh's age in days:", (date.today() - vanshs_birthday).days)

"""
Output (example):
Aashay's circle area: 78.53981633974483
Aashay's random number: 7
Vansh's age in days: 7300  # ~20 years
"""
