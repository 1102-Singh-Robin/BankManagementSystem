#Integration testing

import unittest
from Account import Account
from Bank import Bank
from Transaction import Transaction
from Customer import Customer
from loan import Loan

class TestBankManagementSystem(unittest.TestCase):
    def test_add_customer_with_account_and_loan(self):
        bank = Bank("US Bank")
        customerId = bank.addCustomer("Robin")

        cust = bank.getCustomer(customerId)

        acc = Account(101, "Robin")
        loan = Loan(loanId = 1, customer = cust, amount = 1000, interestRate = 5, duration = 2)

        self.assertEqual(len(cust.accounts), 0)
        self.assertEqual(len(cust.loans), 0)

        cust.addAccount(acc)
        cust.addLoan(loan)

        self.assertEqual(len(cust.accounts), 1)
        self.assertEqual(len(cust.loans), 1)

    def test_money_transfer_between_customers(self):
        bank = Bank("US Bank")
        bank.addCustomer("Robin")
        bank.addCustomer("Rohit")

        robin = bank.getCustomer(1)
        rohit = bank.getCustomer(2)

        accRobin = Account(101, "Robin")
        accRohit = Account(102, "Rohit")

        robin.addAccount(accRobin)
        rohit.addAccount(accRohit)

        accRobin.deposit(1000)

        Transaction.transfer(accRobin, accRohit, 200)

        self.assertEqual(accRobin.getBalance(), 800)
        self.assertEqual(accRohit.getBalance(), 200)

    def test_loan_payment_and_balance_change(self):
        bank = Bank("US Bank")
        bank.addCustomer("Robin")

        robin = bank.getCustomer(1)
        acc = Account(1004, "Robin")
        acc.deposit(10000)

        robin.addAccount(acc)

        loan = Loan(loanId = 1, customer = robin, amount = 1000, interestRate = 5, duration = 5)
        robin.addLoan(loan)

        initialPrincipal = loan.principalBalance()

        for _ in range(5):
            loan.makePayment()

        self.assertEqual(loan.paymentsDone, 5)
        self.assertLess(loan.principalBalance(), initialPrincipal)
        self.assertLess(acc.getBalance(), 10000)

    def test_account_and_loan_str(self):
        bank = Bank("US Bank")
        customerId = bank.addCustomer("Robin")
        robin = bank.getCustomer(customerId)

        acc = Account(1001, "Robin")
        loan = Loan(1010, robin, 3000, 8, 3)

        robin.addAccount(acc)
        robin.addLoan(loan)

        summary = str(robin)
        self.assertIn("Number of Accounts: 1", summary)
        self.assertIn("Number of Loans: 1", summary)

    def test_insufficient_funds_transfer_exception(self):
        acc1 = Account(10010, "Robin")
        acc2 = Account(10011, "Singh")

        acc1.deposit(100)

        with self.assertRaises(Exception) as ex:
            Transaction.transfer(acc1, acc2, 150)

        self.assertIn("Not Enough Funds", str(ex.exception))

if __name__ == "__main__":
    unittest.main()