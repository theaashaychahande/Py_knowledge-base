"""
1. Definition:  
`input()` gets text from the user, `print()` shows text on screen
2. Why Use:  
To make programs interactive (talk to users) and display results
"""

# 3. Format:
# user_input = input("Prompt: ")  # Gets input
# print("Message")                # Shows output

# 4. Code Examples:
# Simple input/output
name = input("Enter your name: ")
print("Hello,", name)

# Number input (needs conversion)
age = int(input("Enter your age: "))  # Convert text to number
print("Next year you'll be", age + 1)

# Fancy output (f-strings)
print(f"{name} is {age} years old.")

# 5. Output (example run):
# Enter your name: Alex
# Hello, Alex
# Enter your age: 19
# Next year you'll be 20
# Alex is 19 years old.
