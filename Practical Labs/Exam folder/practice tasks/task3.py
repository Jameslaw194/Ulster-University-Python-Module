# Define function T1
def T1(n):
    # Calculate T1 according to the formula: 0.0045 * n^3
    return 0.0045 * n ** 3


# Define function T2
def T2(n):
    # Calculate T2 according to the formula: 0.36 * n^2 + 0.15 * n
    return 0.36 * n ** 2 + 0.15 * n


# Function for Task 3: Compare efficiency of two algorithms
def task3():
    # Start with n = 0
    n = 0

    # Infinite loop to iterate through increasing values of n
    while True:
        # Calculate T1 and T2 for current value of n
        t1 = T1(n)
        t2 = T2(n)

        # Check if T1 becomes less than or equal to T2
        if t1 <= t2:
            # If true, print the result and break the loop
            print(f"At n = {n}, A2 becomes more efficient")
            break

        # If not true, print the result and increment n
        print(f"For n = {n}, A1 is still faster")
        n += 1


# Call the task3 function to execute the program
task3()
