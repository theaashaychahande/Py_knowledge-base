"""
1. Definition:  
Making code run faster
2. Why Use:  
Handle larger datasets efficiently
"""


import sys

nums_list = [x for x in range(10000)]
nums_gen = (x for x in range(10000))

print(f"List: {sys.getsizeof(nums_list)} bytes")
print(f"Generator: {sys.getsizeof(nums_gen)} bytes")


"""
Output:
List: 85176 bytes
Generator: 112 bytes
"""
