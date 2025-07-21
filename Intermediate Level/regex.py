"""
1. Definition:  
Pattern-matching syntax for text processing  
2. Why Use:  
To validate or extract data from strings efficiently 
"""

import re

# Validate email format
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

print("Valid email?", is_valid_email("test@example.com"))  # True
print("Valid email?", is_valid_email("invalid@.com"))     # False

# Extract dates
text = "Event on 2023-12-25 and 2024-01-01"
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print("Found dates:", dates)  # ['2023-12-25', '2024-01-01']

"""
Output:
Valid email? True  
Valid email? False  
Found dates: ['2023-12-25', '2024-01-01']
"""
