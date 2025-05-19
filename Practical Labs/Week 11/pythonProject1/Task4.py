def search_in_file(filename, keyword):
    with open(filename, 'r') as file:
        content = file.read()

    if keyword in content:
        print(f"The substring, '{keyword}', is in the string.")
    else:
        print(f"The substring, '{keyword}', was not found in the string.")


filename = 'text_file.txt'
keyword = input("Enter the keyword to search for: ")

search_in_file(filename, keyword)