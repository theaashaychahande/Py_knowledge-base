"""
1. Definition:  
One-liners to create/modify lists
2. Why Use:  
Cleaner and faster than manual loops
"""

# Aashay's MMA 
moves = ["jab", "hook", "uppercut"]  
power_moves = [f"BOOM {move.upper()}" for move in moves]  
# ['BOOM JAB', 'BOOM HOOK', 'BOOM UPPERCUT']  

# Nagpur temperatures 
fahrenheit = [92, 88, 95]  
celsius = [round((f-32)*5/9, 1) for f in fahrenheit]  # [33.3, 31.1, 35.0]  

# Piyush's coding languages  
languages = ["Python", "Java", "Kotlin"]  
short_names = [lang[:3] for lang in languages]  # ['Pyt', 'Jav', 'Kot']  

# Vansh's cooking ingredients
items = ["flour", "sugar", "eggs"]  
shopping_list = [f"BUY {item}" for item in items]  
# ['BUY flour', 'BUY sugar', 'BUY eggs']  

"""
Output samples:  
['BOOM JAB', 'BOOM HOOK', 'BOOM UPPERCUT']  
[33.3, 31.1, 35.0]  
['Pyt', 'Jav', 'Kot']  
['BUY flour', 'BUY sugar', 'BUY eggs']  
"""
