def main():
    sentence = input("Please enter in a sentence ")
    newSentence = ""

    for char in sentence:

        if char.isdigit():
            newSentence += "X"
        else:
            newSentence += char

    print(newSentence)


main()
