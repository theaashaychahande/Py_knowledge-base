"""
1. Definition:  
Recording application events.  
2. Why Use:  
Debug errors and track usage.  
"""


import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def login(username):
    logging.info(f"{username} logged in")
    print(f"Welcome {username}")

login("Aashay")


"""
app.log contents:
INFO:root:Aashay logged in
"""
