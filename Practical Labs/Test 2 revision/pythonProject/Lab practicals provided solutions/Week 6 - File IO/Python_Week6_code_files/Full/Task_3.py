def count_names(file_name):
    file = open(file_name, 'r')
    count = 0
    for line in file:
        # Strip whitespace and ignore empty lines
        if line.strip():
            count += 1
    file.close()
    return count


def count_occurrences(file_name, target_name):
    file = open(file_name, 'r')
    count = 0
    for line in file:

        name = line.strip()
        if name == target_name:
            count+=1

        #for loop efficient (assume that there is one name per line)
        #count += line.strip().count(target_name)

    file.close()
    return count


def main():
    file_name = 'names.txt'

    # Count total number of names
    total_names = count_names(file_name)
    print(f"Total number of names in the file: {total_names}")

    # User-supplied name for occurrence count
    target_name = input("Enter the name to search for: ")
    occurrences = count_occurrences(file_name, target_name)
    print(f"The name '{target_name}' occurs {occurrences} times in the file.")


main()

