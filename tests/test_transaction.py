import unittest
from Account import Account
from Transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_transfer(self):
        acc1 = Account(1, "Robin")
        acc2 = Account(2, "Singh")
        acc1.deposit(500)
        Transaction.transfer(acc1, acc2, 300)

        self.assertEqual(acc1.getBalance(), 200)
        self.assertEqual(acc2.getBalance(), 300)

        with self.assertRaises(Exception):
            Transaction.transfer(acc1, acc2, 500)

if __name__ == "__main__":
    unittest.main()