"""
1. Definition:  
Ways to pass flexible arguments to functions 
2. Why Use:  
Handle variable inputs without overloading functions  
"""

# MMA move combo generator (*args)
def create_combo(*moves):
    combo = " → ".join(moves)
    return f"Fight Combo: {combo}!"
print(create_combo("jab", "cross", "kick")) 


# Boxing equipment checklist (**kwargs) 
def pack_bag(**gear):
    return "\n".join(f"✓ {item}: {qty}" for item, qty in gear.items())
print(pack_bag(gloves=2, wraps=4, mouthguard=1))


# Default arguments 
def debug_code(message, level="INFO", project="Python"):
    print(f"[{level}] {project}: {message}")
debug_code("Variable not found", "WARNING")


"""
Output:
Fight Combo: jab → cross → kick!
✓ gloves: 2
✓ wraps: 4
✓ mouthguard: 1
[WARNING] Python: Variable not found
"""
