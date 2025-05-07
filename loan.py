class Loan:
    def __init__(self, loanId, customer, amount, interestRate, duration):
        self.loanId = loanId
        self.customer = customer
        self.amount = amount
        self.interestRate = interestRate
        self.duration = duration
        self.paymentsDone = 0
        self.payment = self.monthlyPaymentInit(interestRate, duration, amount)

    def monthlyPaymentInit(self, interest, years, principal):
        monthlyInterest = (interest/100) / 12
        totalMonths = years * 12

        payment = (principal * monthlyInterest * (1 + monthlyInterest) ** totalMonths) / (((1 + monthlyInterest) ** totalMonths) - 1)
        return payment

    def monthlyPayment(self):
        return self.payment
    
    def makePayment(self):
        monthlyInterest = (self.interestRate / 100) / 12
        interestAmount = self.amount * monthlyInterest
        principalPart = self.payment - interestAmount

        for account in self.customer.accounts:
            if account.getBalance() >= self.payment:
                account.withdraw(self.payment)
                self.amount -= principalPart
                self.paymentsDone += 1
                return
        
        raise Exception("Insufficient funds in all accounts to make loan payment.")

    def principalBalance(self):
        return self.amount

    def __str__(self):
        return f"""
                Loan Id: {self.loanId}
                Customer: {self.customer}
                Amount: {self.amount: .2f}
                Interest: {self.interestRate} %
                Duration: {self.duration * 12} Months
                Monthly Payment: {self.payment: .2f}
                Payments Done: ({self.paymentsDone} / {self.duration * 12})
                """
    