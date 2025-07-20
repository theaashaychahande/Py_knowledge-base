"""
1. Definition:  
Dictionaries store key-value pairs (like a real dictionary).  
2. Why Use:  
To quickly lookup values using descriptive keys instead of positions.  
"""

# Aashay's profile
profile = {
    "name": "Aashay",
    "age": 19,
    "skills": ["Python", "C++"],
    "active": True
}

# Accessing values
print(profile["name"], "knows", profile["skills"][0])  # Aashay knows Python

# Adding new data
profile["hobby"] = "gaming"
print("After update:", profile)

# Dictionary methods
print("Keys:", profile.keys())     # All keys
print("Age value:", profile.get("age", "N/A"))  # Safe lookup

"""
Output:
Aashay knows Python
After update: {'name': 'Aashay', 'age': 19, 'skills': ['Python', 'C++'], 'active': True, 'hobby': 'gaming'}
Keys: dict_keys(['name', 'age', 'skills', 'active', 'hobby'])
Age value: 19
"""
