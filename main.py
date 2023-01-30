 


# Creating classes
class BankAccount(object):
    def __init__(self, name):
        self.name = name 
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            new_balance = self.balance + amount
            self.balance = new_balance
        
    def withdraw(self, amount):
        if amount > 0:
            new_balance = self.balance - amount
            self.balance = new_balance
    
    def __str__(self) -> str:
        return 'Account "' + self.name + '" has a balance of ' + str(self.balance)

