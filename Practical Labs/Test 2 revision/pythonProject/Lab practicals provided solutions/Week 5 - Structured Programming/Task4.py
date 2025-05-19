def is_even(number):
    # determine whether number is even
    #if so return True, otherwise return False

    if (number % 2) == 0:
        status = True
    else:
        status = False
    # end of if statement
    
    return status
#end of function is_even

def main():
    userNumber = int(input("Enter number to be tested: "))

    if is_even(userNumber):
        print("This is an even number")
    else:
        print("This is an odd number")

main()
    
