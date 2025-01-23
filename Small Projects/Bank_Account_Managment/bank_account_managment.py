class BankAccount:
    """
    Represents a bank account with basic functionalities such as deposit,
    withdrawal, and balance inquiry.
    """

    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Must be greater than zero.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}, Holder: {self.account_holder}, Balance: ${self.balance:.2f})"


class Bank:
    """
    Represents a bank that manages multiple accounts.
    """

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_deposit=0.0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            new_account = BankAccount(account_number, account_holder, initial_deposit)
            self.accounts[account_number] = new_account
            print(f"Account created: {new_account}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} has been deleted.")
        else:
            print("Account not found.")

    def list_accounts(self):
        if self.accounts:
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts found.")


# Sample user interface for interacting with the Bank System
def main():
    bank = Bank()

    while True:
        print("\n=== Bank Account Management System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Delete Account")
        print("6. List All Accounts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            acc_number = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            initial_deposit = float(input("Enter initial deposit (default 0): "))
            bank.create_account(acc_number, acc_holder, initial_deposit)

        elif choice == "2":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                print(f"Balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")

        elif choice == "5":
            acc_number = input("Enter account number: ")
            bank.delete_account(acc_number)

        elif choice == "6":
            bank.list_accounts()

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
