"""
1. Definition:  
Handling dates and times
2. Why Use:  
Schedule events and track time
"""


from datetime import datetime, timedelta


birthday = datetime(2023, 11, 15)
today = datetime.now()
days_left = (birthday - today).days

print(f"Days until Priyanka's birthday: {days_left}")


meeting = datetime.now() + timedelta(days=2)
print(f"Vansh's meeting: {meeting.strftime('%a, %d %b')}")


"""
Sample Output:
Days until Priyanka's birthday: 87
Vansh's meeting: Tue, 15 Aug
"""
