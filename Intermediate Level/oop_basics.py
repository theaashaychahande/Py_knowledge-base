"""
1. Definition:  
Object-Oriented Programming models real-world entities  
2. Why Use:  
To organize complex code with clear relationships 
"""

class Sensor:
    def __init__(self, location):
        self.location = location
        self.readings = []
    
    def add_reading(self, value):
        self.readings.append(value)
    
    def get_average(self):
        return sum(self.readings) / len(self.readings) if self.readings else 0

# Usage
temp_sensor = Sensor("server_room")
temp_sensor.add_reading(25.6)
temp_sensor.add_reading(27.1)
print(f"{temp_sensor.location} avg: {temp_sensor.get_average():.1f}°C")

"""
Output:
server_room avg: 26.3°C
"""
