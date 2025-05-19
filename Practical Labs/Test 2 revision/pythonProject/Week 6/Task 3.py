def count_names(filename):
    num_lines = sum(1 for _ in open('names.txt'))
    print(f"Total number of names in the file: {num_lines}")

def count_occurrences(filename, targetname):
    word = targetname
    count = 0
    with open("names.txt", 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if (i == word):
                    count = count + 1
    print("Occurrences of the word", word, ":", count)

def main():
    filename = open("names.txt", "r")
    count_names(filename)
    targetname = str(input("Enter the name to search for: "))
    count_occurrences(filename, targetname)

main()