# The circle module has functions that perform
# calculations related to circles.

#define pi
PI = 3.1415

# The area function accepts a circle's radius as an
# argument and returns the area of the circle.
def area(radius):
	return PI * radius**2

# The circumference function accepts a circle's
# radius and returns the circle's circumference.
def circumference(radius):
	return 2 * PI * radius


def main():
        goAgain = 'y'
        
        print("Enter 'a' to calculate the area of a circle")
        print("Enter 'b' to calculate the circumference of a circle")
        print("Enter 'c' to end the program")       
        
        
        userChoice = input("Enter choice: ")
                
        if userChoice == 'a':
                radius = float(input("Enter radius: "))
                print("The area is", round(area(radius),2))

                goAgain = input("Do you want to go again? ('y' for yes): ")
                if goAgain == 'y':
                         main()
                        
                        
        elif userChoice == 'b':
                radius = float(input("Enter radius: "))
                print("The circumference is", round(circumference(radius),2 ))

                goAgain = input("Do you want to go again? ('y' for yes): ")
                if goAgain == 'y':
                         main()
                
                         
        else:
                print("End of program")

main()
                               
              
