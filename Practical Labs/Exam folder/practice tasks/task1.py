# Function for Task 1: Sum of Even Numbers
def task1():
    # Infinite loop to allow multiple iterations
    while True:
        try:
            # Prompt user for input
            num = int(input("Enter an even number: "))

            # Check if the number is odd
            if num % 2 != 0:
                # If odd, print error message and continue to next iteration
                print("Please enter an even number.")
                continue

            # Calculate the sum of even numbers from 2 to the given number
            total_sum = sum(range(2, num + 1, 2))

            # Display the result
            print(f"The sum of even numbers up to {num} is: {total_sum}")

            # Ask user if they want to continue
            response = input("Do you want to continue? (y/n): ").lower()

            # If user doesn't want to continue, break out of the loop
            if response != 'y':
                break

        except ValueError:
            # Handle invalid input (not an integer)
            print("Invalid input. Please enter a valid integer.")

# Call the task1 function to execute the program
task1()
