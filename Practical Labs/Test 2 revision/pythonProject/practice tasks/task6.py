'''def load_accounts(filename):
    accounts = []
    with open(filename, 'r') as f:
        for line in f:
            ac_no, balance = line.strip().split(',')
            accounts.append([ac_no, float(balance)])
    return accounts

def validate_account(account_number, accounts):
    for ac_no, _ in accounts:
        if ac_no == account_number:
            return True
    return False

def task6():
    filename = 'accounts.txt'
    accounts = load_accounts(filename)

    while True:
        account_number = input("Enter an account number: ")

        if validate_account(account_number, accounts):
            for ac_no, balance in accounts:
                if ac_no == account_number:
                    print(f"Account {account_number} found. Balance: £{balance:.2f}")
                    break
        else:
            print("Error, invalid account number. Try again.")

#task6()
'''

import sys
import pickle


# Function to read the accounts file and convert its contents into a 2D list
def read_accounts(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Split each line into account number and balance
            accounts = [line.strip().split(',') for line in file]

        # Convert string values to appropriate types (int for account number, float for balance)
        return [[int(account[0]), float(account[1].strip('£'))] for account in accounts[1:]]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


# Function to validate an account number entered by the user
def validate_account(accounts):
    while True:
        try:
            # Prompt user for account number input
            account_number = int(input("Enter an account number: "))

            # Check if the number is negative (invalid)
            if account_number < 0:
                print("Account number cannot be negative.")
                continue

            # Search for the account in the list
            account = next((account for account in accounts if account[0] == account_number), None)

            # If found, return the account details
            if account:
                print(f"Account {account_number} found.")
                return account
            else:
                # If not found, prompt user to try again
                print("Invalid account number. Please try again.")
        except ValueError:
            # Handle invalid input (not an integer)
            print("Invalid input. Please enter a valid account number.")


# Function to save accounts data to a binary file using pickle
def save_accounts(accounts, file_path):
    # Open the file in write-binary mode
    with open(file_path, 'wb') as file:
        # Use pickle.dump() to serialize the data and write it to the file
        pickle.dump(accounts, file)


# Function to load accounts data from a binary file using pickle
def load_accounts(file_path):
    try:
        # Open the file in read-binary mode
        with open(file_path, 'rb') as file:
            # Use pickle.load() to deserialize the data from the file
            return pickle.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []


# Main function that ties everything together
def main():
    # Specify the path to the accounts file
    file_path = 'accounts.txt'

    # Read the accounts data from the file
    accounts = read_accounts(file_path)

    # Loop until a valid account is entered
    while True:
        # Validate the account number entered by the user
        account = validate_account(accounts)

        # If a valid account was found, break out of the loop
        if account:
            break

    # Display the account balance
    print(f"Account balance: £{account[1]:.2f}")

    # Save the accounts data to a binary file named 'bank.dat'
    save_accounts(accounts, 'bank.dat')

    # Load the saved data back into memory for demonstration
    loaded_accounts = load_accounts('bank.dat')

    # Print the number of accounts loaded from the file
    print(f"Loaded {len(loaded_accounts)} accounts from bank.dat")


if __name__ == "__main__":
    # This ensures the main() function only runs when the script is executed directly
    main()

