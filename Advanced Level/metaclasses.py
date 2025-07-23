"""
1. Definition:  
Classes that create other classes 
2. Why Use:  
Enforce coding standards automatically
"""

class CodingStyleMeta(type):
    def __new__(cls, name, bases, dct):
        if not name[0].isupper():
            raise ValueError("Class names must be PascalCase")
        return super().__new__(cls, name, bases, dct)

class PythonProject(metaclass=CodingStyleMeta):
    pass
  
# validation outputs givven below
# class badName(metaclass=CodingStyleMeta):  # Raises ValueError
#     pass
