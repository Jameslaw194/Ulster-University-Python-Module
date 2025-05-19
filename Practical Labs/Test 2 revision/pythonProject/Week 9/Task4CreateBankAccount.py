import json
from task4 import BankAccount

def save_accounts(accounts):
    with open('accounts.json', 'w') as file:
        json.dump([account.__dict__ for account in accounts], file)

def load_accounts():
    try:
        with open('accounts.json', 'r') as file:
            data = json.load(file)
            return [BankAccount(**{k: v for k, v in account.items() if k != 'balance'}) for account in data]
    except FileNotFoundError:
        return []

def main():
    accounts = load_accounts()

    while True:
        print("\nOptions:")
        print("1. Create a new account")
        print("2. Print details of all accounts")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            accNo = input("Enter account number: ")
            openBal = float(input("Enter opening balance: "))
            overLimit = float(input("Enter overdraft limit: "))

            new_account = BankAccount(name, accNo, openBal, overLimit)
            accounts.append(new_account)
            save_accounts(accounts)

            print("\nNew account created successfully.")
        elif choice == "2":
            if not accounts:
                print("\nNo accounts have been created yet.")
            else:
                print("\nAccount Details:")
                for i, account in enumerate(accounts, 1):
                    print(f"\nAccount {i}:")
                    print(account)
        elif choice == "3":
            if not accounts:
                print("\nNo accounts have been created yet.")
            else:
                accNo = input("Enter account number to deposit money: ")
                amount = float(input("Enter deposit amount: "))
                account = next((account for account in accounts if account.accNo == accNo), None)
                if account:
                    account.deposit(amount)
                    save_accounts(accounts)
                else:
                    print("\nAccount not found.")
        elif choice == "4":
            if not accounts:
                print("\nNo accounts have been created yet.")
            else:
                accNo = input("Enter account number to withdraw money: ")
                amount = float(input("Enter withdrawal amount: "))
                account = next((account for account in accounts if account.accNo == accNo), None)
                if account:
                    account.withdraw(amount)
                    save_accounts(accounts)
                else:
                    print("\nAccount not found.")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()