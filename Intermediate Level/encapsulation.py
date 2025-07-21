"""
1. Definition:  
Restricting direct access to an object's internals 
2. Why Use:  
To prevent invalid modifications and hide complexity 
"""

class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print("Balance:", account.get_balance())  # 100

# This would fail:  
# print(account.__balance)  

"""
Output:
Balance: 100
"""
