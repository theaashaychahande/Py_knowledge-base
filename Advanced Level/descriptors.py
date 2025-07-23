"""
1. Definition:  
Objects that manage attribute access 
2. Why Use:  
Validate data before assignment
"""

class AgeValidator:
    def __set__(self, obj, value):
        if not 16 <= value <= 25:
            raise ValueError("Age must be 16-25")
        obj.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name

class Student:
    age = AgeValidator()

disha = Student()
disha.age = 19  
# Valid
