"""
1. Definition:  
One-liners to build dictionaries/sets from iterables
2. Why Use:  
Create mappings/filter unique values efficiently 
"""

# Atharv's boxing  
punches = ["jab", "cross", "hook", "uppercut"]  
boxing_stats = {punch: len(punch)*10 for punch in punches}  
# {'jab': 30, 'cross': 50, 'hook': 40, 'uppercut': 70}  

# Pallotti student grades   
students = ["Apurv", "Aishwarya", "Ritesh"]  
grades = {name: f"{len(name)*10}%" for name in students}  
# {'Apurv': '50%', 'Aishwarya': '90%', 'Ritesh': '60%'}  

# Ritesh's unique cooking ingredients 
duplicates = ["flour", "sugar", "flour", "eggs"]  
unique_items = {item for item in duplicates}  # {'flour', 'sugar', 'eggs'}  

# Priyanka's coding language rankings  
languages = ["Python", "Java", "Kotlin"]  
rankings = {lang: idx+1 for idx, lang in enumerate(languages)}  
# {'Python': 1, 'Java': 2, 'Kotlin': 3}  

"""
Output samples:  
{'jab': 30, 'cross': 50, 'hook': 40, 'uppercut': 70}  
{'Apurv': '50%', 'Aishwarya': '90%', 'Ritesh': '60%'}  
{'flour', 'sugar', 'eggs'}  
{'Python': 1, 'Java': 2, 'Kotlin': 3}  
"""
