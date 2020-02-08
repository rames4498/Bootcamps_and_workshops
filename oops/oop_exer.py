class BankAccount:
    def __init__(self,balance):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
'''    
'''    
a = BankAccount(500)
b = BankAccount(50)
k = BankAccount(500)
print(a.deposit(75))
print(a.withdraw(10))
print(k.withdraw(50))
