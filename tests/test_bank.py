import unittest
from Bank import Bank

class TestBank(unittest.TestCase):
    def tes_addAndGetCustomer(self):
        testBank = Bank("Wells Fargo")
        customerId = testBank.addCustomer("Robin")
        customer = testBank.getCustomer(customerId)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "Dana")

if __name__ == "__main__":
    unittest.main()