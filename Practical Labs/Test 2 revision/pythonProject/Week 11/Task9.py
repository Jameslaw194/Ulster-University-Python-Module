def pig_latin(text):
    words = text.split()
    pig_latin_words = []

    for word in words:
        if len(word) > 1:
            pig_latin_word = word[1:] + word[0] + 'AY'
            pig_latin_words.append(pig_latin_word)
        else:
            pig_latin_words.append(word)

    return ' '.join(pig_latin_words)


text = input("Enter a sentence: ")
print(pig_latin(text.upper()))