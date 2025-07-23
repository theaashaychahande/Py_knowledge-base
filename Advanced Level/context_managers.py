"""
1. Definition:  
Objects that handle resource setup/cleanup 
2. Why Use:  
Ensure files/connections are properly closed  
"""

class GymSession:
    def __enter__(self):
        print("Aashay: Started workout")
    
    def __exit__(self, *args):
        print("Aashay: Shower time")

with GymSession():
    print("--> Lifting weights")
  
"""
Output:
Aashay: Started workout  
--> Lifting weights  
Aashay: Shower time  
"""
