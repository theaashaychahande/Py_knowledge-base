"""
1. Definition:  
Specialized container datatypes  
2. Why Use:  
More efficient data handling 
"""

from collections import Counter

coding_skills = {
    "Aashay": ["Python", "Java"],
    "Priyanka": ["Python", "C++"],
    "Vansh": ["Java", "Kotlin"]
}

all_skills = sum(coding_skills.values(), [])
print(Counter(all_skills))

"""
Output:
Counter({'Python': 2, 'Java': 2, 'C++': 1, 'Kotlin': 1})
"""
