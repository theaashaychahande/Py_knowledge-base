"""
1. Definition:  
Errors crash your program, exceptions let you handle them gracefully  
2. Why Use:  
To prevent crashes and give helpful error messages 
"""

# Example 1: Catching TypeError
try:
    age = 19
    print(age + " years") 
except TypeError:
    print("Hey Vansh, convert numbers to strings properly!")

# Example 2: Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Vansh, you can't divide by zero!")
else:
    print("Result:", result)
finally:
    print("This always runs")

# Custom exception
class VanshsCustomError(Exception):
    pass

try:
    raise VanshsCustomError("Something went wrong")
except VanshsCustomError as e:
    print("Custom error caught:", e)

"""
Output:
Hey Vansh, convert numbers to strings properly!
Vansh, you can't divide by zero!
This always runs
Custom error caught: Something went wrong
"""
