"""
1. Definition:  
Small anonymous functions  
2. Why Use:  
For quick one-time operations 
"""

# Basic math
square = lambda x: x ** 2
print("Square of 5:", square(5))  # 25

# Sorting
data = [{"id": 2}, {"id": 1}, {"id": 3}]
sorted_data = sorted(data, key=lambda x: x["id"])
print("Sorted:", sorted_data)  # [{'id': 1}, {'id': 2}, {'id': 3}]

"""
Output:
Square of 5: 25
Sorted: [{'id': 1}, {'id': 2}, {'id': 3}]
"""
