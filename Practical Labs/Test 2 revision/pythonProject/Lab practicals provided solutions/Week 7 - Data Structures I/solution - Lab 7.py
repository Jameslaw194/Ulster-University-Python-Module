#Practical Lab 7 - Lists and Tuples

# Task 1
# Design a program that lets a user enter rainfall for 12 months which is then entered into a list.
# The program should process the list to calculate and display the total rainfall for the year, the
# average monthly rainfall, and print out the month number with the highest and lowest amounts of rainfall.

def task1():

    # Local variables
    total = 0.0
    average = 0.0
    highest = 0.0
    lowest = 0.0
    month_lowest = ''
    month_highest = ''

    # List to receive rainfall amounts
    month_rain = [0.0] * 12

    # Initalize a list with names of the months.
    month_list = ['January', 'February', 'March',
                  'April', 'May', 'June', 'July',
                  'August', 'September', 'October',
                  'November', 'December']

    # Get the amount of rainfall for each month.
    for i in range(12):
        month_rain[i] = float(input('Enter the rainfall for ' + month_list[i] + ": "))

    total = sum(month_rain)

    # Calculate the average.
    average = total / 12.0

    # Calculate the maximum.
    highest = max(month_rain)

    # Get the index of the month with the highest rainfall.
    month_highest = month_rain.index(highest)

    # Calculate the minimum.
    lowest = min(month_rain)

    # Get the index of the month with the lowest rainfall.
    month_lowest = month_rain.index(lowest)

    # Display results
    print('Total rainfall:', format(total, '.2f'))
    print('Average rainfall:', format(average, '.2f'))
    print('Highest rainfall:', month_list[month_highest])
    print('Lowest rainfall:', month_list[month_lowest])

#Task 2
# You will find a file named charge_accounts.txt within the Practical Lab 9 folder on BBL.
# This file contains a list of a company’s valid bank account numbers. Each account number is a seven-digit number,
# e.g. 5658845. Write a program that reads the contents of the file into a list. The program should then ask the
# user to enter a charge account number and determine whether the number is valid by searching for it in the list.
# If the number is in the list, the program should display a message indicating the number is valid. If the number
# is not in the list, the program should display a message indicating the number is invalid.

def task2():
    # Local variables
    test_account = ''

    try:
        # Open the file for reading
        input_file = open('charge_accounts.txt', 'r')

        accounts = []

        # Strip trailing '\n' from all elements of the list
        for each_row in input_file:
            accounts.append(each_row.rstrip('\n'))

        # Get user input
        test_account = input('Enter the account number to be validated: ')

        # Use in operator to search for the account specified by user
        if test_account in accounts:
            print('Account number', test_account, 'is valid.')
        else:
            print('Account number', test_account, 'is not valid.')

    except IOError:
        print('The file could not be found')
    except:
        print('An error occurred')


#Task 3
#When analysing data it may be desirable to remove the most extreme values before performing other calculations.
# Write a function that takes a list of values and a non-negative integer, n, as its parameters. The function should
# create a new copy of the list with the n largest elements and n smallest elements removed. Then it should return the
# new copy of the list as the function result. Test your program by declaring a list and a value for n, which you
# pass to the function. NOTE: The order of the elements in the returned list does not need to match the order of the
# original list.

def task3():
    list = [1,2,3,45,45,57,67,78,56,45,6,23,1,3345,23,13,423,5,56688]
    n = 3

    list.sort()
    print(list)
    new_list = []

    for i in range(len(list)):
        if not (i <= n-1 or i >= len(list)-n):
            new_list.append(list[i])

    print(new_list)


#Task 4
# When writing out a list of items in English, one normally separates the items with commas. In addition,
# the word ‘and’ is normally included before the last item, unless the list only contains one item.
# Consider the following examples: Car / Car and boat / Car, boat and bikes / Car, boat, bike and plane
# Write a function that takes a list of strings as its only parameter. Your function should return a string that
# contains all of the items in the list formatted in the manner described previously as its only result. Include
# a main program that reads several items from the user, formats them by calling your function, and then displays
# the result returned by the function.

def task4(string_list):

    # format the list
    list_len = len(string_list)
    string_builder = ''
    if list_len <=1:
        string_builder = string_list[0]
    else:
        for i in range(list_len):
            if i == list_len-1:
                string_builder = string_builder + str(string_list[i])
            elif i == list_len - 2:
                string_builder = string_builder + string_list[i] + ' and '
            else:
                string_builder = string_builder + string_list[i] + ', '

    print(string_builder)


# Task 7
# Download the file landmarks.txt from Blackboard. Your challenge in this task is to 
# write simple Python code to locate, open, and read the contents of the file into a 
# List. Process the list using appropriate methods to return all those countries with 
# a character count (including spaces) of more than 15 characters. Write the identified 
# landmarks to a new file called landmarks_extracted.txt.

def task5(): #called by task 5 and not 7 for simplicity.
    # Step 1: Locate and open 'landmarks.txt' file
    try:
        with open("landmarks.txt", "r") as file:
            # Initialize an empty list for landmarks with more than 15 characters
            long_landmarks = []
            
            # Step 2: Process each line individually
            for line in file:
                # Remove leading and trailing whitespace
                landmark = line.strip()
                
                # Check if the character count is more than 15
                if len(landmark) > 15:
                    # Add to the list if condition is met
                    long_landmarks.append(landmark)
        
        # Step 3: Write the filtered landmarks to 'landmarks_extracted.txt'
        with open("landmarks_extracted.txt", "w") as output_file:
            for landmark in long_landmarks:
                output_file.write(landmark + "\n")

        print("Filtered landmarks written to landmarks_extracted.txt successfully.")

    except FileNotFoundError:
        print("The file landmarks.txt was not found. Please check the file location and try again.")


# MAIN PROGRAM

selection = ''

while(selection != '0'):
    selection = input('\nWhich task do you want to execute? ')
    if(selection == '1'):
        task1()
    elif(selection == '2'):
        task2()
    elif(selection == '3'):
        task3()
    elif(selection == '4'):
        string_list = []
        words = ''
        while words != 'end':
            words = input('Add a word to the list: ')
            if words != 'end':
                string_list.append(words)
        task4(string_list)
    elif (selection == '5'):
        task5()
