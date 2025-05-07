import unittest
from Account import Account

class TestAccount(unittest.TestCase):
    def test_deposit(self):
        acc = Account(1, "Robin")
        acc.deposit(1000)
        self.assertEqual(acc.getBalance(), 1000)

    def test_withdraw(self):
        acc = Account(2, "Pratap")
        acc.deposit(1000)
        acc.withdraw(300)
        self.assertEqual(acc.getBalance(), 700)
        with self.assertRaises(Exception):
            acc.withdraw(800)

    def test_getBalance(self):
        acc = Account(3, "Singh")
        self.assertEqual(acc.getBalance(), 0)


if __name__ == "__main__":
    unittest.main()