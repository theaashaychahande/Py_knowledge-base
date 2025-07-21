"""
1. Definition:  
Techniques to find/fix errors and verify correctness
2. Why Use:  
Ensure code works as intended and simplify troubleshooting 
"""

# Debugging with breakpoint()
def faulty_calculation(a, b):
    result = a * b  # Intentional error - should be +
    return result

# Testing with asserts
assert faulty_calculation(2, 3) == 5, "Multiplication error found"

"""
Output (when error exists):
Traceback (most recent call last):
  File "debugging_testing.py", line 9, in <module>
    assert faulty_calculation(2, 3) == 5, "Multiplication error found"
AssertionError: Multiplication error found
"""
