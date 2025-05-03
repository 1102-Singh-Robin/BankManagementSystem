# 5. **Loan** (New class)
#    - Attributes: `loan_id`, `customer`, `amount`, `interest_rate`, `duration`
#    - Methods: `calculate_repayment_amount()`, `__str__()`

class Loan:
    def __init__(self, loanId, customer, amount, interestRate, duration):
        self.loanId = loanId
        self.customer = customer
        self.amount = amount
        self.interestRate = interestRate
        self.duration = duration

    def calculateRepaymentAmount(self):
        pass

    def monthlyPayment(self):
        pass

    def principalBalance(self):
        pass

    def __str__(self):
        return f"""
                Loan Id: {self.loanId}
                Customer: {self.customer}
                Amount: {self.amount}
                Interest: {self.interestRate} %
                Duration: {self.duration} Months
                """
    
