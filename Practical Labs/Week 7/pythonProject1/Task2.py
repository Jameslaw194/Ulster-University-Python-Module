def validate_account(account_number):
    with open('charge_accounts.txt', 'r') as f:
        valid_accounts = [int(line.strip()) for line in f]

    return account_number in valid_accounts


def query():
    while True:
        account_number = input("Enter a charge account number (or 'q' to quit): ")

        if account_number.lower() == 'q':
            break

        if validate_account(int(account_number)):
            print("Account number is valid.")
        else:
            print("Account number is invalid. Please try again.")
