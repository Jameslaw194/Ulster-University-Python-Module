# Task1
#Two words are anagrams if they contain all of the same letters, but in a different order.
# For example, ‘Python and ‘Typhon, and ‘Study’ and ‘Dusty’ are anagrams. One way to determine if
# something is an anagram is to tally the individual letters that make up each word, and then to
# compare those tallies. Write and program that reads two words in from the keyboard, determines
# whether or not these are anagrams and produces a report detailing the character make-up of each word.


#APPROACH 1 - just use a list to order two strings and then compare them
def task1a():
    str = 'Earth'
    str2 = 'HEART'

    print(ord('E'), 'vs', ord('e'))

    str = str.upper()
    str2 = str2.upper()

    ls1 = []
    ls2 = []

    for ch in str:
        ls1.append(ch)

    for ch in str2:
        ls2.append(ch)

    ls1.sort()
    ls2.sort()

    print(ls1)
    print(ls2)

    if ls1 == ls2:
        print("True, these strings are anagrams")
    else:
        print('False, these strings are NOT anagrams"')

# APPROACH 2 - use a dictionary to keep tabs on the keys (letters of each word) and the values will be the tally of
# each letter
def task1b():

    dict1 = dict_tally(input('Enter the first word: ').lower())
    dict2 = dict_tally(input('Enter the word that you would like to compare: ').lower())

    print(dict1 == dict2)

def dict_tally(str):
    dict = {}
    for each_ch in str:
        if each_ch in dict:
            dict[each_ch] =  int(dict[each_ch]) + 1
        else:
            dict[each_ch] = 1
    return dict