def translate_phone_number(phone_number):
    letters = [
        [2, ['A', 'B', 'C']],
        [3, ['D', 'E', 'F']],
        [4, ['G', 'H', 'I']],
        [5, ['J', 'K', 'L']],
        [6, ['M', 'N', 'O']],
        [7, ['P', 'Q', 'R', 'S']],
        [8, ['T', 'U', 'V']],
        [9, ['W', 'X', 'Y', 'Z']]
    ]

    converted = ""
    for char in phone_number:
        if char.isalpha():
            for digit, alphabet in letters:
                if char.upper() in alphabet:
                    converted += str(digit)
                    break
            else:
                converted += char
        else:
            converted += char

    return converted

phone_number = input("Enter a phone number to be converted: ")
print(translate_phone_number(phone_number))