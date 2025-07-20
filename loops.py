"""
1. Definition:
Loops repeat code until a condition is met.
2. Why Use:
To avoid writing the same code multiple times.
"""

# Countdown with while
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")

# Shopping list with for
items = ["milk", "eggs", "bread"]
for item in items:
    print("Buy", item)

# Number range example
print("Counting to 5:")
for num in range(1, 6):
    print(num)

"""
Output:
3
2
1
Go!
Buy milk
Buy eggs
Buy bread
Counting to 5:
1
2
3
4
5
"""
