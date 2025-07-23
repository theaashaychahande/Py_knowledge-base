"""
1. Definition:  
Threading (I/O-bound) vs Multiprocessing (CPU-bound) 
2. Why Use:  
Scale different types of workloads 
"""

import threading
import multiprocessing

def task(name):
    print(f"{name} executing")

t1 = threading.Thread(target=task, args=("Piyush",))
t1.start()

p1 = multiprocessing.Process(target=task, args=("Ritesh",))
p1.start()


"""
Possible Output:
Piyush executing
Ritesh executing
"""
