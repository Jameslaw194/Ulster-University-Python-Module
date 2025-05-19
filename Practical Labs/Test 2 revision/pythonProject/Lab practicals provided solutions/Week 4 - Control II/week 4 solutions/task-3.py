#com101 labs week 4 task 3
#modifications to the code are noted with triple #
# This program calculates the sum of a series
# of numbers entered by the user.

big = int(input('How many numbers are you going to enter?'))   ### input number of numbers to be entered

# Initialize an accumulator variable.
total = 0.0
   
# Explain what we are doing.
print('This program calculates the sum and average of the')   ###amend print to note average
print(big, 'numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(big):
    number = int(input('Enter a number: '))
    total = total + number

# Display the total of the numbers.
print('The total is', total)
print('The average is',format(total/big,'.2f'))      ###note format to prevent long decimal output
        


