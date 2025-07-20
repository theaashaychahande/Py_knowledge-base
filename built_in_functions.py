"""
1. Definition:  
Pre-made tools in Python that work out-of-the-box  
2. Why Use:  
To perform common tasks without writing extra code  
"""

# Vansh's data examples
name = "Vansh"
age = 19
scores = [85, 92, 78]

# Most useful built-ins:
print(len(name))          # 5 (letters in "Vansh")
print(type(age))          # <class 'int'>
print(sum(scores))        # 255 (total score)
print(max(scores))        # 92 (highest score)
print(sorted(scores))     # [78, 85, 92] (ordered list)
print(bool("Vansh"))      # True (truthy check)

# Advanced examples:
print(abs(-15))           # 15 (absolute value)
print(round(9.876, 2))    # 9.88 (rounded)

"""
Output:
5
<class 'int'>
255
92
[78, 85, 92]
True
15
9.88
"""
