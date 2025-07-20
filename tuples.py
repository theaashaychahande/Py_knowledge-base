"""
1. Definition:  
Tuples are like lists but unchangeable (perfect for fixed data 
2. Why Use:  
When you need data that shouldn't be modified accidentally  
"""

# Aashay's location coordinates (latitude, longitude)  
aashays_spot = (28.6139, 77.2090) 
print("GPS:", aashays_spot)  

# Unpacking tuple  
lat, lon = aashays_spot  
print(f"Latitude: {lat}, Longitude: {lon}")  

# Tuple vs list  
aashays_mutable_list = ["read", "code", "sleep"]  
aashays_immutable_tuple = ("read", "code", "sleep")  


"""
Output:  
GPS: (28.6139, 77.2090)  
Latitude: 28.6139, Longitude: 77.209  
"""
