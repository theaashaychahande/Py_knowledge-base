"""
1. Definition:  
Special check to run code only when script is executed directly
2. Why Use:  
Allow files to be both imported and run standalone 
"""

def helper():
    return "Helper function called"

if __name__ == "__main__":
    print("Script executed directly")
    print(helper())
else:
    print("Script imported as module")

"""
Output when run directly:
Script executed directly  
Helper function called  
"""
