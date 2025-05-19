def searchText():
    # Ask the user to enter a substring
    user_substring = input("Please enter a substring: ")

    with open("text_file.txt", 'r') as file:
        # file content read in as a string, string split
        # into a list of words
        words = file.read()

        # Use the in operator to check if the substring is in the string
        if user_substring in words:
            # Print a message if True
            print(f"The substring {user_substring} is in the string")
        else:
            # Print a message if False
            print(f"The substring {user_substring} is not in the string.")


def main():
    searchText()


main()
