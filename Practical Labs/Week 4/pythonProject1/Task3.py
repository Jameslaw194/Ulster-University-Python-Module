# This program calculates the sum of a series
# of numbers entered by the user.

# Initialize an accumulator variable.
total = 0.0

big = int(input("How many numbers do you want to calculate?: "))

# Explain what we are doing.
print('This program calculates the sum of')
print(big, 'numbers you will enter.')

# Get the numbers and accumulate them.
for counter in range(big):
    number = int(input('Enter a number: '))
    total = total + number

#calculate average
average = total / big

# Display the total and average of the numbers.
print('The total is', total)
print('The average is', average)


