# This program gets three test scores and displays
# their average.  It congratulates the user if the
# average is a high score.

# The high score variable holds the value that is
# considered a high score.

#task1(a) change high_score to 70
high_score = 70
 
# Get the three test scores.
#task 1(a) add in an extra score and task 1(b) change int to float
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))
test4 = float(input('Enter the score for test 4: '))

# Calculate the average test score.
average = (test1 + test2 + test3 + test4) / 4

# Print the average.
#task 1(b) print out to 2dps
print('The average score is', format(average,'.2f' ))

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')

