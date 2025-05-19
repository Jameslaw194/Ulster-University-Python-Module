def main():


    print("Enter 'a' to search for a type of coffee")
    print("Enter 'b' to search for a roast of coffee")
    print("Enter 'c' to end the program")

    userChoice = input("Enter choice: ")

    if userChoice == 'a':
        searchDesc()

        goAgain = input("Do you want to go again? ('y' for yes): ")
        if goAgain == 'y':
            main()

    elif userChoice == 'b':
        searchRoast()

        goAgain = input("Do you want to go again? ('y' for yes): ")
        if goAgain == 'y':
            main()

    else:
        print("End of program")


def searchDesc():
    found = False

    search = input("Enter a description to search for: ")

    coffeeFile = open("coffee.txt", "r")
    count = 0
    total = 0
    for line in coffeeFile:

        strippedLine = line.strip()
        descr, roast, coffeeType, qty = strippedLine.split(", ")

        if descr == search:
            print("Description:", descr)
            print("Roast: ", roast)
            print("Coffee Type: ", coffeeType)
            print("Quantity:", qty)
            print()

            count += 1
            total += int(qty)

            found = True

    coffeeFile.close()
    if found:
        print("There are", count, "records for", search)
        print("The total quantity is", total, "kilos")


    else:
        print("That item was not found in the file.")


def writeResults(roast, count, quantity):
    try:
        userFile = open("Results.txt", "a")
        userFile.write(roast + " " + str(count) + " " + str(quantity) + "\n")
    except FileNotFoundError:
        print("This file can not be found")


def searchRoast():
    found = False

    search = input("Enter a roast to search for: ")

    coffeeFile = open("coffee.txt", "r")
    count = 0
    total = 0
    for line in coffeeFile:

        strippedLine = line.strip()
        descr, roast, coffeeType, qty = strippedLine.split(", ")

        if roast == search:
            count += 1
            total += int(qty)
            found = True

    coffeeFile.close()
    if found:
        print("You searched for", search, "roast. That was found", count, "times in the file.")
        print("The total quantity is ",total,"kilos")
        writeResults(search, count, total)


    else:
        print("That roast was not found in the file.")


main()
