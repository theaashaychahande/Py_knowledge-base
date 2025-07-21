"""
1. Definition:  
Where variables are accessible in code 
2. Why Use:  
To control variable visibility and avoid naming conflicts 
"""

# Global variable
config = {"mode": "production"}

def set_config():
    # Local variable
    debug_mode = True
    
    def inner():
        # Nonlocal modification
        nonlocal debug_mode
        debug_mode = False
        
    inner()
    return debug_mode

# Testing scope
print("Global:", config)  # Accessible everywhere
result = set_config()     # Returns modified local variable 
print("Local result:", result) 

"""
Output:
Global: {'mode': 'production'}
Local result: False
"""
