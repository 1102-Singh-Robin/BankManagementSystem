import unittest
from Customer import Customer
from Account import Account
from loan import Loan

class TestCustomer(unittest.TestCase):
    def test_addAccount(self):
        cust = Customer("Robin", 1)
        acc = Account(1, "Robin")
        cust.addAccount(acc)
        self.assertEqual(len(cust.getAccount()), 1)
    
    def test_addLoan(self):
        cust = Customer("Robin", 2)
        loan = Loan(loanId = 1, customer = cust, amount = 1000, interestRate = 5, duration = 1)
        cust.addLoan(loan)
        self.assertEqual(len(cust.getLoans()), 1)


if __name__ == "__main__":
    unittest.main()