# Task2
# Morse Code is an encoding scheme that uses dashes and dots to represent numbers and letters.
# In this exercise, you will write a program that uses a dictionary to store the mapping from
# letters and numbers to Morse code. Use a full stop to represent a dot, and a hyphen to represent a dash.
# You will find a copy of the international Morse code on Wikipedia.
#
# Your program should read and message from the user. Then it should translate each letter and number
# in the message to Morse code, leaving a space between each sequence of dashes and dots. Your program
# should ignore any characters that are not letters or numbers. The Morse code for ‘Hello World’ Is shown
# here, as an example: …. . .-.. .-.. --- .-- --- .-. .-. .-..

def task2():
    codes = {'A': '.-',     'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',

            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.', ' ': 'SPACE'
            }

    msg = input('MESSAGE: ')
    encrypt(msg, codes)
    msg = input('\nCODE: ')
    decrypt(msg,codes)
    print()


def encrypt(msg, codes):
    for char in msg:
        if char.isspace():
            print('SPACE/',end='')
        elif char.isalpha() or char.isnumeric():
            # code['E']
            print(codes[char.upper()], end='/')

def decrypt(msg, codes):
    tempLetter =''
    word_builder = ''
    for eachMorse in msg:
        if eachMorse !='/':
            tempLetter += eachMorse
        else:
            for each_code in codes:
                # if codes[.] == '.'
                if codes[each_code] == tempLetter:
                    word_builder+=each_code
                    tempLetter =''
    print(word_builder,end='')