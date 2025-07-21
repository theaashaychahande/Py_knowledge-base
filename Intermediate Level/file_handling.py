"""
1. Definition:  
Reading/writing files 
2. Why Use:  
Persist data beyond program runtime 
"""

# Write to file  
with open("data.txt", "w") as f:  
    f.write("Sample text\nSecond line")  

# Read file  
with open("data.txt") as f:  
    print("File content:", f.read())  

"""
Output:  
File content: Sample text  
Second line  
"""  
