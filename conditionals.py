"""
1. Definition: 
Code that runs only when certain conditions are met
2. Why Use:
To control program flow based on different situations
"""

# Burger decision
money = 20
hungry = True

# Basic if/else
age = int(input("How old are you? "))
if age >= 18:
    print("You can vote!")
else:
    print("Wait", 18 - age, "more years to vote")


# elif example
if hungry and money > 15:
    print("Getting good burger")
elif hungry and money > 10:
    print("Fast food burger")
else:
    print("Making sandwich")

# Grade check
grade = 'B'

if grade == 'A':
    print("Perfect")
elif grade == 'B':
    print("Not bad")
elif grade == 'C':
    print("Could be better")
else:
    print("Oh no")

"""
Output:
Getting good burger
Not bad
"""
