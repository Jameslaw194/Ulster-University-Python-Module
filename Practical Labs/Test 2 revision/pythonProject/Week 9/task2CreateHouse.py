from task2 import House


def search_house_by_address(house_objects, address):
    for house in house_objects:
        if house.address == address:
            return house
    return None


def main():
    house_objects = []
    total_houses_created = 0

    while True:
        print("\nOptions:")
        print("1. Create a new House object")
        print("2. Print details of all House objects")
        print("3. Search for a house by address")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_house(house_objects, total_houses_created)
        elif choice == "2":
            print_details(house_objects)
            print(f"\nTotal houses created: {total_houses_created}")
        elif choice == "3":
            search_address = input("Enter address to search for: ")
            result = search_house_by_address(house_objects, search_address)
            if result:
                print("\nHouse found:")
                print(result)
            else:
                print("\nHouse not found.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")


def create_house(house_objects, total_houses_created):
    address = input("Enter house address: ")
    floors = int(input("Enter number of floors: "))
    rooms = int(input("Enter number of rooms: "))
    heating_type = input("Enter heating type: ")

    new_house = House(address, floors, rooms, heating_type)
    house_objects.append(new_house)
    total_houses_created += 1
    print(new_house)


def print_details(house_objects):
    for i, house in enumerate(house_objects, 1):
        print(f"\nHouse {i}:")
        print(house)


if __name__ == "__main__":
    main()
