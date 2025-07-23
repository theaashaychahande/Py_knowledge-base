"""
1. Definition:  
Processing structured data
2. Why Use:  
Clean and analyze datasets
"""


import pandas as pd

data = {
    "Name": ["Disha", "Vansh"],
    "Score": [85, 92]
}
df = pd.DataFrame(data)
print(df.describe())


"""
Output:
          Score
count   2.000000
mean   88.500000
std     4.949747
min    85.000000
25%    86.750000
50%    88.500000
75%    90.250000
max    92.000000
"""
