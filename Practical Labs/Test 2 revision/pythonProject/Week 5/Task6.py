def main():
    sentence = str(input("Enter a sentence: "))
    user_letter = str(input("Enter a letter to search for: "))
    countBs(sentence, user_letter)

def countBs(sentence, user_letter):
    letter = user_letter
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == letter:
            count += 1
    print(f"The Number of '{user_letter}s' in '{sentence}' is {count}")



main()