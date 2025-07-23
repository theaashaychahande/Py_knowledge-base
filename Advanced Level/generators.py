"""
1. Definition:  
Functions that modify other functions 
2. Why Use:  
Add reusable behavior like logging or access control 
"""

def require_login(func):
    def wrapper(user):
        if user not in ["Aashay", "Priyanka", "Vansh"]:
            raise ValueError(f"{user} not authorized")
        return func(user)
    return wrapper

@require_login
def view_profile(user):
    return f"{user}'s profile"

print(view_profile("Aashay")) 

"""
Output:
Aashay's profile
"""
