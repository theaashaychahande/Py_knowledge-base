"""
1. Definition:  
Storing and querying structured data
2. Why Use:  
Persistent data storage 
"""

import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, grade TEXT)")

cursor.execute("INSERT INTO students VALUES ('Piyush', 'A')")
conn.commit()
for row in cursor.execute("SELECT * FROM students"):
    print(row)
  

"""
Output:
('Piyush', 'A')
"""
