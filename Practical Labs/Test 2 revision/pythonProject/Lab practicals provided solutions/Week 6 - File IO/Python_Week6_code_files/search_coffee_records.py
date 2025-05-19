def main():

    found = False

    search = input("Enter a description to search for: ")

    coffeeFile = open("coffee.txt", "r")

    for line in coffeeFile:
    
        strippedLine = line.strip()
        descr, qty = strippedLine.split(", ") 

        if descr == search:
            print("Description:", descr)
            print("Quantity:", qty)
            print()

            found = True

    coffeeFile.close()

    if not found:
        print("That item was not found in the file.")

main()

