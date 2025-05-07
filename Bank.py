from Customer import Customer
class Bank:
    def __init__(self, name):
        self.name = name
        self.numCustomer = 0
        self.customers: list[Customer] = []

    def addCustomer(self, name):
        tempCustomer = Customer(name, self.numCustomer + 1)
        self.customers.append(tempCustomer)
        self.numCustomer += 1
        return self.numCustomer

    def getCustomer(self, customerId):
        if customerId > 0:
            return self.customers[customerId - 1]
        
        return None

    def __str__(self):
        return f"""
                Bank: {self.name}
                Total Customers: {self.numCustomer}
                """
