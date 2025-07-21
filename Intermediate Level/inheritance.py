"""
1. Definition:  
Child classes inherit attributes/methods from parents 
2. Why Use:  
To reuse code and model hierarchical relationships  
"""

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def describe(self):
        return f"{self.name} - {self.role}"

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name, "Developer")
        self.language = language
    
    def describe(self):
        base = super().describe()
        return f"{base} ({self.language})"

# Usage
dev = Developer("Alex", "Python")
print(dev.describe())  # Alex - Developer (Python)

"""
Output:
Alex - Developer (Python)
"""
