# 3. **Transaction**
#    - Static Method: `transfer(from_account, to_account, amount)`
import Account
class Transaction:
    def transfer(fromAccount: Account, toAccount: Account, amount):
        
        if fromAccount.getBalance >= amount:
            fromAccount.withdraw(amount)
            toAccount.deposit(amount)

        else:
            raise Exception("Not Enough Funds")

