"""
1. Definition:  
Special methods with double underscores that Python calls automatically  
2. Why Use:  
To define how objects behave with operators and built-in functions
"""

class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    # Called by print()/str()
    def __str__(self):
        return f"{self.name} (x{self.quantity})"
    
    # Called by + operator
    def __add__(self, other):
        if self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError("Can't add different items")
    
    # Called by len()
    def __len__(self):
        return self.quantity

# Usage
item1 = InventoryItem("RAM Stick", 5)
item2 = InventoryItem("RAM Stick", 3)

print(item1)             # RAM Stick (x5)
combined = item1 + item2 # Uses __add__
print(combined)          # RAM Stick (x8)
print(len(item1))        # 5 (uses __len__)

"""
Output:
RAM Stick (x5)  
RAM Stick (x8)  
5
"""
