def read_grocery_list(filename):
    # Open the file in read mode
    file = open(filename, 'r')
    # Read the contents of the file
    contents = file.read()
    # Close the file
    file.close()
    return contents


def add_items(filename):
    # Allow the user to add 5 items to the grocery list
    print("Please enter 5 grocery items:")
    file = open(filename, 'a')  # Open the file in append mode
    for i in range(5):
        item = input(f"Item {i + 1}: ")
        file.write(item + '\n')  # Write each item on a new line
    file.close()  # Close the file


def main():
    # Specify the filename
    filename = 'grocery_lit.txt'
    add_items(filename)
    # Call the function to read the grocery list and store the result
    grocery_contents = read_grocery_list(filename)
    # Print the contents to the console
    print(grocery_contents)


main()
