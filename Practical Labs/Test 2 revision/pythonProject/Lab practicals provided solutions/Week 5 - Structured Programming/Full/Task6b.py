def main():
    sentence = input("Enter the sentence: ")
    letter = input("Enter the capital letter: ")
    letter = letter.upper();

    numTimes = countLetter(sentence, letter)

    print("The numbers of times the capital letter "
    +letter+" is found in \""+sentence+"\" is "+str(numTimes))


def countLetter(userSentence, userLetter):
    counterVal = 0;

    for letter in userSentence:

        if letter == userLetter:
            counterVal+=1

    return counterVal;

main()
