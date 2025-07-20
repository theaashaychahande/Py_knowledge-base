"""
1. Definition:  
Strings are for storing text like names or messages
2. Why Use:  
To handle all text data in your programs
"""

# Using strings with your name
username = "Aashay"
welcome_message = "Hey " + username + ", welcome to Python!"

# Checking length
print(username, "has", len(username), "letters")  # Aashay has 6 letters

# String slicing
print("Your nickname could be:", username[:3])  # Aas

# Multiline string
aashays_bio = """Aashay's favorites:
- Food: Pizza
- Hobby: Coding
- Language: Python
"""
print(aashays_bio)

"""
Output:
Aashay has 6 letters
Your nickname could be: Aas
Aashay's favorites:
- Food: Pizza
- Hobby: Coding
- Language: Python
"""
