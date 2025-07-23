"""
1. Definition:  
Functions that yield values one-by-one 
2. Why Use:  
Process large datasets without loading everything in memory
"""

def student_attendance():
    students = ["Piyush", "Disha", "Apurv"]
    for student in students:
        yield f"{student} - Present"

for record in student_attendance():
   print(record)
    
"""
Output:
Piyush - Present  
Disha - Present  
Apurv - Present  
"""
