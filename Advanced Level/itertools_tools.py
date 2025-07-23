"""
1. Definition:  
Tools for working with iterators 
2. Why Use:  
Efficient looping and combinations  
"""


import itertools

teams = ["Piyush", "Disha", "Ritesh"]
for pair in itertools.combinations(teams, 2):
    print(f"Project pair: {pair}")
  
"""
Output:
Project pair: ('Piyush', 'Disha')  
Project pair: ('Piyush', 'Ritesh')  
Project pair: ('Disha', 'Ritesh')  
"""
