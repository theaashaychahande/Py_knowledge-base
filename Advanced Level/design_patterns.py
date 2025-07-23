"""
1. Definition:  
Reusable solutions to common problems
2. Why Use:  
Write maintainable code
"""

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Singleton()
db2 = Singleton()
print(db1 is db2)  


"""
Output:
True
"""
