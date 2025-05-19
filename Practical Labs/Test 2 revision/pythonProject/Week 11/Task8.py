def count_vowels_and_consonants(text):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    vowel_count = sum(1 for char in text
                      if char in vowels)
    consonant_count = sum(1 for char in text
                          if char in consonants)

    return vowel_count, consonant_count


text = input("Enter a string: ")
vowel_count, consonant_count = count_vowels_and_consonants(text)

print(f"The string you entered includes {vowel_count} vowels and {consonant_count} consonants.")