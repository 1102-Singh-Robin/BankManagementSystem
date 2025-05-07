class Account:
    def __init__(self, accountNum, ownerName):
        self.accountNumber = accountNum
        self.ownerName = ownerName
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount

        else:
            raise Exception("Not enough money to withdraw, Try a smaller amount")

    def getBalance(self):
        return self.balance
    
    def __str__(self):
        return f"""
                Name: {self.ownerName}
                Account Number: {self.accountNumber}
                Balance: {self.balance}"""
    