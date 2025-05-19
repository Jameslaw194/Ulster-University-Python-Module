def capitalise_sentences(text):
    sentences = text.split('. ')
    capitalised_sentences = [sentence.capitalize() for sentence in sentences]
    return '. '.join(capitalised_sentences)

text = input("Enter sentence to be capitalised: ")
result = capitalise_sentences(text)
print(result)