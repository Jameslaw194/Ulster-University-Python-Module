def main():
    sentence = "A Python Book is Brilliant"
    print("The Number of Bs in \""+sentence+"\" is", countBs(sentence))


def countBs(sentence):
    counterVal = 0;

    for letter in sentence:

        if letter == 'B':
            counterVal+=1

    return counterVal;

main()
