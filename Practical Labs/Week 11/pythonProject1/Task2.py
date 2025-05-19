def main():
    sentence = input("Enter a sentence: ")
    count = 0
    for i in range(len(sentence)):
        modified_sentence = sentence.replace(count, 'X')
        count = count + 1

    print(modified_sentence)
main()