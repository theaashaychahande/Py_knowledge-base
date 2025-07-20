"""
1. Definition:  
String methods are tools to modify or analyze text
2. Why Use:  
To clean, format, and manipulate text easily
"""  

# Basic methods  
name = "aashay"  
print("Shout:", name.upper())          # AASHAY  
print("Whisper:", name.capitalize())   # Aashay  

# Formatting  
age = 19  
print(f"{name.title()} is {age} years old")  # Aashay is 19 years old  

# Splitting text  
hobbies = "coding,gaming,music"  
print("Aashay's hobbies:", hobbies.split(","))  # ['coding', 'gaming', 'music']  

# Replacing text  
text = "Aashay loves Java"  
print(text.replace("Java", "Python"))  # Aashay loves Python  

"""
Output:  
Shout: AASHAY  
Whisper: Aashay  
Aashay is 19 years old  
Aashay's hobbies: ['coding', 'gaming', 'music']  
Aashay loves Python  
"""  
