"""
1. Definition:  
Same interface, different implementations 
2. Why Use:  
To write flexible code that works with multiple types 
"""

class Database:
    def connect(self):
        return "Connected to generic database"

class MySQL(Database):
    def connect(self):
        return "Connected to MySQL server"

class MongoDB(Database):
    def connect(self):
        return "Connected to MongoDB cluster"

# Single interface
def test_connection(db):
    print(db.connect())

test_connection(Database())  # Connected to generic database  
test_connection(MySQL())     # Connected to MySQL server  
test_connection(MongoDB())   # Connected to MongoDB cluster  

"""
Output:
Connected to generic database
Connected to MySQL server  
Connected to MongoDB cluster
"""
