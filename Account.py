class Account:
    def __init__(self, accountNum, ownerName, balance):
        self.accountNumber = accountNum
        self.ownerName = ownerName
        self.balance = balance

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
    

ab = Account(12345, "Robin", 123.40)
print(ab.__str__())
        
# ### Implementation Steps:
# 1. Create the `Account` class with deposit and withdrawal methods.
# 2. Develop the `Customer` class to manage multiple accounts.
# 3. Implement the `Transaction` class for handling money transfers.
# 4. Build the `Bank` class to store customers and their accounts.
# 5. In the main execution block, create instances, perform transactions, and print results.