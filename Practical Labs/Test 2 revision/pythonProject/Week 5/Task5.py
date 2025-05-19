# The circle module has functions that perform
# calculations related to circles.

#define pi
pi = 3.1415

# The area function accepts a circle's radius as an
# argument and returns the area of the circle.
def area(radius):
    return round(pi * radius**2, 2)

# The circumference function accepts a circle's
# radius and returns the circle's circumference.
def circumference(radius):
    return round(2 * pi * radius, 2)

def main():
    choice = str(input("(a) Calculate the area of a circle \n(b) Calculate its circumference \n(c) End the program\n"))
    radius = int(input("Enter a radius: "))

    if choice == "a":
        print(area(radius))
    elif choice == "b":
        print(circumference(radius))
    elif choice == "c":
        return 0
    else:
        print("Invalid input")

    run_again = str(input("Do you want to run the program again? (y/n) "))
    if run_again == "y":
        main()
    elif run_again == "n":
        print("Thank you!")
    else:
        print("Invalid input")



main()