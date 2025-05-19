# Initialize an empty dictionary to store inventory items
inventory = {}

# Function to add an item to the inventory
def add_item(item_name, quantity):
    global inventory
    # Check if the item already exists in the inventory
    if item_name in inventory:
        # If it exists, increase the quantity
        inventory[item_name] += quantity
    else:
        # If it doesn't exist, add it with the given quantity
        inventory[item_name] = quantity

# Function to sell an item from the inventory
def sell_item(item_name, quantity):
    global inventory
    # Check if the item exists in the inventory
    if item_name in inventory:
        # Check if there's enough stock
        if inventory[item_name] >= quantity:
            # If available, reduce the quantity in stock
            inventory[item_name] -= quantity
        else:
            # If not enough stock, print an error message
            print(f"Error: Not enough {item_name} in stock.")
    else:
        # If item not found, print an error message
        print(f"Error: {item_name} not found in inventory.")

# Function to display the current inventory
def display_inventory():
    # Check if the inventory is empty
    if not inventory:
        print("Inventory is empty.")
    else:
        # If not empty, print the current inventory
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

# Main function for the inventory management system
def task5():
    # Infinite loop to keep the program running
    while True:
        # Display menu options
        print("\nInventory Management System")
        print("1. Add Item to Inventory")
        print("2. Sell Item from Inventory")
        print("3. Display Current Inventory")
        print("4. Exit")

        # Get user choice
        choice = input("Choose an option (1-4): ")

        # Handle different choices
        if choice == '1':
            # Add item to inventory
            item_name = input("\nEnter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item_name, quantity)
        elif choice == '2':
            # Sell item from inventory
            item_name = input("\nEnter item name: ")
            quantity = int(input("Enter quantity to sell: "))
            sell_item(item_name, quantity)
        elif choice == '3':
            # Display current inventory
            display_inventory()
        elif choice == '4':
            # Exit the program
            print("\nExiting the program. Goodbye!")
            break
        else:
            # Handle invalid input
            print("Invalid option. Please choose again.")

# Call the main function to start the inventory management system
task5()
