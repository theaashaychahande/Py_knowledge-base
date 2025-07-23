"""
1. Definition:  
Predefined attribute storage to save memory
2. Why Use:  
Optimize objects with many instances 
"""

class StudentProfile:
    __slots__ = ['name', 'id']
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

ritesh = StudentProfile("Ritesh", "24011012")
print(f"{ritesh.name}: {ritesh.id}")


"""
Output:
Ritesh: 24011012
"""
