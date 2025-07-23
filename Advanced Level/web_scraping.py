"""
1. Definition:  
Extracting data from websites 
2. Why Use:  
Collect information when APIs aren't available
"""


from bs4 import BeautifulSoup
import requests

page = requests.get("http://example.com")
soup = BeautifulSoup(page.text, "html.parser")
print(f"Page title: {soup.title.string}")


"""
Output:
Page title: Example Domain
"""
