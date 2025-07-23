"""
1. Definition:  
Caching function results for repeated inputs 
2. Why Use:  
Avoid redundant calculations
"""

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

print(f"Priyanka's calculation: {factorial(5)}")  
print(f"Vansh's calculation: {factorial(7)}")

'''
Output:
Priyanka's calculation: 120
Vansh's calculation: 5040
"""
