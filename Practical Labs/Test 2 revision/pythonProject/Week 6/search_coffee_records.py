def main():
    choice = None
    print("Enter 'a' to search for a type of coffee")
    print("Enter 'b' to search for a roast of coffee")
    print("Enter 'c' to end the program")
    choice = input("Enter choice: ")

    if choice == 'a':
        found = False
        count = 0
        qtyamount = 0
        search = input("Enter a description to search for: ")
        coffeeFile = open("coffee.txt", "r")
        for line in coffeeFile:
            strippedLine = line.strip()
            descr, roast, type, qty = strippedLine.split(", ")
            if descr == search:
                count += 1
                qtyamount += int(qty)
                print("Description:", descr)
                print("Roast:", roast)
                print("Type:", type)
                print("Quantity:", qty)
                print()
                found = True
        print(f"There are {count} records for {search}")
        print(f"The total quantity is {qtyamount} kilos")
        coffeeFile.close()
        if not found:
            print("That item was not found in the file.")
        again = input("Do you want to go again? ('y' for yes): ")
        if again == 'y':
            main()


    if choice == 'b':
        count = 0
        found = False
        search = input("Enter a roast to search for: ")
        coffeeFile = open("coffee.txt", "r")
        for line in coffeeFile:
            strippedLine = line.strip()
            descr, roast, type, qty = strippedLine.split(", ")
            if roast == search:
                count += 1
                found = True
        print(f"You searched for {search} roast. That was found {count} times in the file.")
        coffeeFile.close()
        if not found:
            print("That item was not found in the file.")
        again = input("Do you want to go again? ('y' for yes): ")
        if again == 'y':
            main()




main()

