"""
1. Definition:  
Tools for higher-order functions and caching
2. Why Use:  
Optimize function performance and reduce redundancy  
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def calculate_ranking(student):
    """Simulate complex ranking calculation"""
    print(f"Processing {student}'s data...")
    return len(student) * 10  
  
print(calculate_ranking("Aashay")) 
print(calculate_ranking("Priyanka"))  
print(calculate_ranking("Aashay"))


"""
Output:
Processing Aashay's data...
60
Processing Priyanka's data...
80
60
"""
