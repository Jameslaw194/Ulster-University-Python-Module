# Task 3
# In the game of Scrabble, each letter has points associated with it. The total score of a word is
# the sum of the score of its letters. More common letters are worth fewer points while less common letter
# are worth more points.
# Write a program that computes and displays the score for any word entered. Note: in order to simplify the logic,
# you should use the UPPER() function to convert all words entered into uppercase.

def task3():
    scrabble= {1:['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
              2: ['D', 'G'],
              3: ['B', 'C', 'M', 'P'],
              4: ['F', 'H', 'V', 'W', 'Y'],
              5: ['K'],
              8: ['J','X'],
              10:['Q','Z']
              }

    #students could choose not to use a list though and provide a score per character instead:
    #SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             # "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             # "x": 8, "z": 10} # Capitalized (constant)

    word = input('Enter a word: ').upper()
    word_score = 0

    for ch in word:
        for score, letters in scrabble.items():
            for item in letters:
                if ch == item:
                    word_score += int(score)

    print()
    print(word, 'scores', word_score, 'points')