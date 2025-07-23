"""
1. Definition:  
Functions that modify other functions without changing their code  
2. Why Use:  
To add reusable functionality like logging or timing 
"""

def log_calls(func):
    def wrapper(*args):
        print(f"Calling {func.__name__}")
        return func(*args)
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(2, 3))

"""
Output:
Calling add
5
"""
