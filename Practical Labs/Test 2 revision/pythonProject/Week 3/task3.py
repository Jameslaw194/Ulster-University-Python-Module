# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score1 = int(input('Enter your coursework score (out of 100): '))
score2 = int(input('Enter your coursework score (out of 100): '))
score3 = int(input('Enter your coursework score (out of 100): '))

average = (score1 + score2 + score3) / 3

# Determine the grade.
if average >= A_score:
    print('Your grade is A.')
elif average >= B_score:
    print('Your grade is B.')
elif average >= C_score:
    print('Your grade is C.')
elif average >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
# End of if-elif structure
