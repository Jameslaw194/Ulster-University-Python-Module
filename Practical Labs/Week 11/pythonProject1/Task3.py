def swap_substrings(text):
    return text.replace('left', 'right').replace('up', 'down')

text = input("Enter a sentence: ")
result = swap_substrings(text)
print(result)