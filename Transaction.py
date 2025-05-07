from Account import Account
class Transaction:
    def transfer(fromAccount: Account, toAccount: Account, amount):
        
        if fromAccount.getBalance() >= amount:
            fromAccount.withdraw(amount)
            toAccount.deposit(amount)

        else:
            raise Exception("Not Enough Funds")

