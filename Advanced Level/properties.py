"""
1. Definition:  
Managed attributes with getter/setter logic
2. Why Use:  
Maintain data integrity 
"""

class GymMember:
    def __init__(self, name):
        self.name = name
        self._weight = 70
    
    @property
    def weight(self):
        return f"{self._weight}kg"
    
    @weight.setter
    def weight(self, value):
        if not 50 <= value <= 120:
            raise ValueError("Invalid weight")
        self._weight = value

aashay = GymMember("Aashay")
aashay.weight = 75
print(f"{aashay.name}: {aashay.weight}")


"""
Output:
Aashay: 75kg
"""
