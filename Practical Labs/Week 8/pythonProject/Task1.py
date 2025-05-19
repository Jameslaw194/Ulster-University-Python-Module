people = {'Mark':'22', 'James':'19'}
search = input("Enter a name: ")

while search.lower() != 'q':
    if search in people:
        print(search," number is: ", people[search])
    else:
        print("Not found")
    search = input("Enter another name, or 'q' to quit: ")