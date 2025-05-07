from Bank import Bank
from Customer import Customer
from Account import Account
from loan import Loan

def main():
    bank = Bank("US Bank")
    print("Welcome to US Bank")

    while True:
        print("\n===== MENU =====")
        print("1. Add Customer")
        print("2. Open Account for Customer")
        print("3. Deposit into Account")
        print("4. Issue Loan")
        print("5. Make Loan Payment")
        print("6. View Customer Details")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            cust_id = bank.addCustomer(name)
            print(f"Customer '{name}' added with ID: {cust_id}")

        elif choice == "2":
            cust_id = int(input("Enter customer ID: "))
            customer = bank.getCustomer(cust_id)
            if not customer:
                print("Invalid customer ID.")
                continue
            acc_num = int(input("Enter new account number: "))
            account = Account(acc_num, customer.name)
            customer.addAccount(account)
            print("Account created.")

        elif choice == "3":
            cust_id = int(input("Enter customer ID: "))
            customer = bank.getCustomer(cust_id)
            if not customer:
                print("Invalid customer ID.")
                continue
            accounts = customer.getAccount()
            if not accounts:
                print("No accounts found for this customer.")
                continue
            print("Accounts:")
            for i, acc in enumerate(accounts):
                print(f"{i + 1}. {acc.accountNumber}")
            acc_index = int(input("Select account (number): ")) - 1
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_index].deposit(amount)
            print("Deposit successful.")

        elif choice == "4":
            cust_id = int(input("Enter customer ID: "))
            customer = bank.getCustomer(cust_id)
            if not customer:
                print("Invalid customer ID.")
                continue
            loan_id = int(input("Enter Loan ID: "))
            amount = float(input("Enter loan amount: "))
            rate = float(input("Enter interest rate (%): "))
            years = int(input("Enter duration (in years): "))
            loan = Loan(loan_id, customer, amount, rate, years)
            customer.addLoan(loan)
            print("Loan issued.")
            print(loan)

        elif choice == "5":
            cust_id = int(input("Enter customer ID: "))
            customer = bank.getCustomer(cust_id)
            if not customer:
                print("Invalid customer ID.")
                continue
            loans = customer.getLoans()
            if not loans:
                print("No loans found for this customer.")
                continue
            print("Loans:")
            for i, ln in enumerate(loans):
                print(f"{i + 1}. Loan ID: {ln.loanId}")
            loan_index = int(input("Select loan (number): ")) - 1
            try:
                loans[loan_index].makePayment()
                print("Payment successful.")
            except Exception as e:
                print(f"Payment failed: {e}")

        elif choice == "6":
            cust_id = int(input("Enter customer ID: "))
            customer = bank.getCustomer(cust_id)
            if customer:
                print(customer)
                for acc in customer.getAccount():
                    print(acc)
                for loan in customer.getLoans():
                    print(loan)
            else:
                print("Invalid customer ID.")

        elif choice == "0":
            print("Thank you for using US Bank!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
