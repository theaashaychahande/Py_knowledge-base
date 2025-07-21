"""
1. Definition:  
JSON is a lightweight data format for APIs/configs  
2. Why Use:  
To exchange data between systems and store settings  
"""

import json

# Sample API response (simulated)
api_response = """
{
    "system": "production",
    "users": [
        {"id": 101, "active": true},
        {"id": 102, "active": false}
    ]
}
"""

# Parse JSON
data = json.loads(api_response)
print("System status:", data["system"])  # production
print("Active users:", sum(user["active"] for user in data["users"]))  # 1

# Generate JSON
config = {
    "timeout": 30,
    "retry": False,
    "services": ["auth", "db"]
}
print("Config JSON:", json.dumps(config, indent=2))

"""
Output:
System status: production
Active users: 1
Config JSON: {
  "timeout": 30,
  "retry": false,
  "services": ["auth", "db"]
}
"""
