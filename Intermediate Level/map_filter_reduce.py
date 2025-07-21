"""
1. Definition:  
Tools for processing collections without loops 
2. Why Use:  
Cleaner data transformations
"""

from functools import reduce

# Data samples  
temperatures = [32, 104, 212]  
transactions = [19.99, 5.50, 25.75]  
log_levels = ["ERROR", "DEBUG", "INFO", "ERROR"]

# map: Convert temps to Celsius  
to_celsius = lambda f: round((f - 32) * 5/9)  
print("Temps in °C:", list(map(to_celsius, temperatures)))  

# filter: Get only ERROR logs  
is_error = lambda log: log == "ERROR"  
print("Error logs:", list(filter(is_error, log_levels)))  

# reduce: Sum transactions  
sum_total = reduce(lambda x, y: x + y, transactions)  
print("Total sales: $", sum_total)  

"""
Output:  
Temps in °C: [0, 40, 100]  
Error logs: ['ERROR', 'ERROR']  
Total sales: $ 51.24  
"""  
