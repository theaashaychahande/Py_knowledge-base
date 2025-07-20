"""
1. Definition:  
Sets store unique, unordered items (like a math set) 
2. Why Use:  
To remove duplicates or check membership super fast  
"""

# Aashay's programming languages (automatically removes duplicates)
languages = {"Python", "Java", "C++", "Python"} 
print("Unique languages:", languages)  

# Adding/removing
languages.add("JavaScript")
languages.discard("Java")
print("Updated set:", languages)

# Set operations
backend = {"Python", "Java", "C++"}  
frontend = {"JavaScript", "HTML", "CSS"}  

# What Aashay knows in both
print("Intersection:", backend & frontend)  # set()

# All languages combined
print("Union:", backend | frontend) 

"""
Output:
Unique languages: {'Python', 'Java', 'C++'}
Updated set: {'Python', 'C++', 'JavaScript'}
Intersection: set()
Union: {'Python', 'Java', 'C++', 'JavaScript', 'HTML', 'CSS'}
"""
