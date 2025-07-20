"""
1. Definition:  
Lists store multiple items in order (like a shopping list)  
2. Why Use:  
To group related data together that you can modify  
"""

# Aashay's grocery list
groceries = ["milk", "eggs", "bread", "apples"]
print("Full list:", groceries)

# Adding items
groceries.append("coffee")  
print("Updated list:", groceries)

# Accessing items
print("First item:", groceries[0])  # milk
print("Last item:", groceries[-1])   # coffee

# Slicing
print("First 2 items:", groceries[:2])  # ['milk', 'eggs']

# Changing items
groceries[1] = "organic eggs"  
print("Modified list:", groceries)

"""
Output:
Full list: ['milk', 'eggs', 'bread', 'apples']
Updated list: ['milk', 'eggs', 'bread', 'apples', 'coffee']
First item: milk
Last item: coffee
First 2 items: ['milk', 'eggs']
Modified list: ['milk', 'organic eggs', 'bread', 'apples', 'coffee']
"""
