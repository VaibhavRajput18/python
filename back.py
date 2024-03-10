class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= 1000:
                self.balance -= amount
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount.")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= 1000:
                self.balance -= amount
                print("Amount withdrawn successfully.")
            else:
                print("Withdrawal not allowed")
        else:
            print("Invalid amount.")

# Menu driven program
account = SavingsAccount()

while True:
    print("------------------------------------------------------------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        print("Account balance:", account.balance)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")