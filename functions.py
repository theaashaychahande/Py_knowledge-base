"""
1. Definition:  
Functions are reusable code blocks that perform specific tasks  
2. Why Use:  
To avoid repeating code and organize your program better  
"""

# Basic function
def greet(name): # this is for greeting msg
    return f"Hey {name}, Aashay here!"

print(greet("Vansh"))  # Hey Vansh, Aashay here!

# Function with default argument
def order_food(item, quantity=1):
    print(f"Ordering {quantity} {item}(s)")

order_food("Burger")      # Ordering 1 Burger(s)
order_food("Pizza", 2)   # Ordering 2 Pizza(s)

# Return multiple values
def get_aashays_stats():
    return "Aashay", 19, "Python"

name, age, lang = get_aashays_stats()
print(f"{name} is {age} and loves {lang}")

"""
Output:
Hey Vansh, Aashay here!
Ordering 1 Burger(s)
Ordering 2 Pizza(s)
Aashay is 19 and loves Python
"""
