"""
1. Definition:  
Building web applications.  
2. Why Use:  
Create interactive websites.  
"""


from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Aashay's Blog"

# type "app.run()"
"""
(Starts server at http://localhost:5000)
"""
