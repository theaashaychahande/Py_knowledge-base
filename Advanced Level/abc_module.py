"""
1. Definition:  
Classes that define required methods 
2. Why Use:  
Ensure consistent interfaces
"""

from abc import ABC, abstractmethod

class Assignment(ABC):
    @abstractmethod
    def submit(self):
        pass

class MathHomework(Assignment):
    def submit(self):
        return "Piyush: Submitted PDF"

class Essay(Assignment):
    def submit(self):
        return "Disha: Submitted DOCX"

print(MathHomework().submit())


"""
Output:
Piyush: Submitted PDF
"""
