"""
1. Definition:  
Functions that yield values one at a time
2. Why Use:  
Memory-efficient iteration over large datasets  
"""

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)

"""
Output:
3
2
1
"""
