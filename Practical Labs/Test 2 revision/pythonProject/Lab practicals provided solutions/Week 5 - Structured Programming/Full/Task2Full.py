
# This program simulates 25 tosses of a coin.
import random

def main():
    tosses = int(input("Enter number of tosses: "))
    coin(tosses)
#end of main function    

def coin(tosses):
    headCount = 0
    tailCount = 0
    for toss in range(tosses):
        # Simulate the coin toss.
        if random.randint(1, 2) == 1:
            print('Heads')
            headCount +=1
        else:
            print('Tails')
            tailCount += 1
        # end of if statement
     #end of for loop

    print("Number of heads", headCount)
    print("Number of tails", tailCount)
#end of coin function

            
# Call the main function.
main()


