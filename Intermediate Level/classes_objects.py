"""
1. Definition:  
Classes are blueprints, objects are their instances  
2. Why Use:  
To model real entities with data + behavior together  
"""

class NetworkDevice:
    def __init__(self, name, ip):
        self.name = name  
        self.ip = ip
        self.is_online = False
    
    def connect(self):
        self.is_online = True
        return f"{self.name} ({self.ip}) connected"
    
    def __str__(self):
        return f"Device: {self.name} | IP: {self.ip}"

# Creating objects
router = NetworkDevice("Main Router", "192.168.1.1")
switch = NetworkDevice("Core Switch", "10.0.0.1")

# Using methods
print(router.connect())  # Main Router (192.168.1.1) connected
print(switch)           # Device: Core Switch | IP: 10.0.0.1

"""
Output:
Main Router (192.168.1.1) connected  
Device: Core Switch | IP: 10.0.0.1
"""
