"""
1. Definition:  
Syntax for declaring expected variable/function types 
2. Why Use:  
Improve code clarity and catch errors early with tools like mypy
"""

def calculate_total(items: list[float], discount: float = 0.0) -> float:
    """Calculate total with optional discount."""
    subtotal = sum(items)
    return subtotal * (1 - discount)

# Usage
prices = [19.99, 5.50, 25.75]
final_price = calculate_total(prices, 0.1)  # 10% discount
print(f"Total: ${final_price:.2f}")  

"""
Output:
Total: $46.12
"""
