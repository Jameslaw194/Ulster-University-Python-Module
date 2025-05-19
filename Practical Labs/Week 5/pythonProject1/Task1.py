
# This program demonstrates a function that accepts
# two arguments.

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    show_division(num1, num2)

# The show_division function accepts two arguments
# and displays their ratio .
def show_division(num1, num2):
    result = num1 / num2
    print(result)

# Call the main function.
main()

