"""
1. Definition:  
Modules are single files, packages are directories of modules 
2. Why Use:  
To organize large projects and reuse code across files  
"""

# Sample file structure:
"""
my_package/
├── __init__.py
├── utils.py       # Contains: def log(msg): print("LOG:", msg)
└── calculations.py # Contains: def square(x): return x ** 2
"""

# Import examples (uncomment to test after creating files)
# from my_package.utils import log
# from my_package.calculations import square

# log(square(5))  # Would output: LOG: 25

print("Run after creating package files as shown above")

"""
Output:
Run after creating package files as shown above
"""
