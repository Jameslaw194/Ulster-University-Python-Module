def capitalize(sentence):
    for i in range(0, len(sentence)):
        if i == 0:
            sentence = sentence[i].upper() + sentence[1:]
        elif sentence[i] == '.' and i != len(sentence)-1:
            sentence = sentence[:i+2] + sentence[i+2].upper() + sentence[i+3:]
    return sentence

def main():
    sentence = input('Enter sentence to be capitalized:')
    print(capitalize(sentence))

# Call the main function.
if __name__ == '__main__':
    main()
