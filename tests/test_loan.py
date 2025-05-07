import unittest
from Customer import Customer
from loan import Loan
from Account import Account

class TestLoan(unittest.TestCase):
    def test_loanPayment(self):
        cust = Customer("Robin", 3)
        loan = Loan(loanId = 1, customer = cust, amount = 1000, interestRate = 5, duration = 5)
        
        balance = loan.principalBalance()
        self.assertEqual(balance, 1000)
        with self.assertRaises(Exception):
            loan.makePayment()
        
        acc = Account(106, "Robin")
        acc.deposit(10000)
        cust.addAccount(acc)
        
        loan.makePayment()
        
        self.assertEqual(loan.paymentsDone, 1)
        self.assertLess(loan.principalBalance(), balance)

if __name__ == "__main__":
    unittest.main()