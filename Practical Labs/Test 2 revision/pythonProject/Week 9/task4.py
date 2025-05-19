class BankAccount:
    def __init__(self, name, accNo, openBal, overLimit):
        self.name = name
        self.accNo = accNo
        self.openBal = openBal
        self.overLimit = overLimit
        self.balance = openBal

    def __str__(self):
        return f"Customer Name: {self.name}\nAccount Number: {self.accNo}\nCurrent balance: {self.balance}\nOpening balance: {self.openBal}\nOverdraft limit: {self.overLimit}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n${amount} deposited. New balance: ${self.balance}")
        else:
            print("\nDeposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.check_overdraft(amount):
                self.balance -= amount
                print(f"\n${amount} withdrawn. New balance: ${self.balance}")
            else:
                print("\nWithdrawal denied. Overdraft limit reached.")
        else:
            print("\nWithdrawal amount must be positive.")

    def check_overdraft(self, amount):
        return (self.balance - amount) <= self.overLimit