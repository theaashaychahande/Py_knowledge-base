"""
1. Definition:  
Automated code verification
2. Why Use:  
Ensure code works as expected 
"""

def add(a, b):
    return a + b
  
assert add(2, 3) == 5, "2+3 should be 5"
assert add(-1, 1) == 0, "-1+1 should be 0"

print("All tests passed!")


"""
Output:
All tests passed!
"""
