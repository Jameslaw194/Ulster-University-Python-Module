#task 3 week3 labs
#this is a modified version of the code grader.py

# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
#modify to take 3 scores in float format
score1 = float(input('Enter your first test score: '))
score2 = float(input('Enter your second test score: '))
score3 = float(input('Enter your third test score: '))

#take average and print it
score = (score1+score2+score3)/3

print('Your average score is ',format(score,'.2f'))

# Determine the grade.
if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
# End of if-elif structure



    

