#week 4 task 1 com101
#modifications are indicated with comments with a triple #
# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y' or keep_going=='Y': ###sentinal is 'y' or 'Y'###
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the % commission rate: '))
    
    if comm_rate>=0 and comm_rate<=100:
            
        # Calculate the commission.
        commission = sales * comm_rate/100

        ### add £50 to commission if it is over £5k###
        if sales>5000:
            commission = commission +50
            print('Congratulations, you got a bonus because'+\
                  'your sale was over £5,000!')

        # Display the commission.
        print('The commission is £', \
              format(commission, '.2f'),sep='')

        # See if the user wants to do another one.
        keep_going = input('Do you want to calculate another ' + \
                           'commission (Enter y for yes): ')
    else:
        print('There is an input error')
# end of while loop

print('In that case I wave my underpants at your auntie.')



