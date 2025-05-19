def read_grocery_list(filename):
    contents = filename.read()
    filename.close()
    print(contents)

def add_items(filename):
    filename = open("grocery_list.txt", "a")
    choice = 'y'
    while choice == 'y':
        items = input("Enter items: ")
        filename.write("\n" + items)
        choice = input("Do you want to add more items? (y/n): ")
    filename.close()

def main():
    filename = open("grocery_list.txt", "r")
    read_grocery_list(filename)
    add_items(filename)

main()