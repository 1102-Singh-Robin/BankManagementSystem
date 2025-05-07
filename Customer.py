from Account import Account
from loan import Loan

class Customer:
    def __init__(self, name, customerId):
        self.name = name
        self.customerId = customerId
        self.accounts: list[Account] = []
        self.loans: list[Loan] = []

    def addAccount(self, account: Account):
        self.accounts.append(account)

    def getAccount(self):
        return self.accounts

    def addLoan(self, loan: Loan):
        self.loans.append(loan)

    def getLoans(self):
        return self.loans

    def __str__(self):
        return f"""
                Customer Name: {self.name}
                Customer Id: {self.customerId}
                Number of Accounts: {len(self.accounts)}
                Number of Loans: {len(self.loans)}
                """
    

