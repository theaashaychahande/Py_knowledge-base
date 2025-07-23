"""
1. Definition:  
Functions that remember their creation environment  
2. Why Use:  
Create function factories with preset values
"""


def counter_factory(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
  

aashays_counter = counter_factory(10)
print(f"Aashay's count: {aashays_counter()}")  
print(f"Aashay's count: {aashays_counter()}") 

"""
Output:
Aashay's count: 11
Aashay's count: 12
"""
