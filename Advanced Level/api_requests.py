"""
1. Definition:  
Fetching data from web APIs 
2. Why Use:  
Get real-time external data 
"""


import requests

response = requests.get("https://api.github.com/users/aashay")
data = response.json()
print(f"GitHub ID: {data['id']}")


"""
Output:
GitHub ID: [user's actual ID]
"""
