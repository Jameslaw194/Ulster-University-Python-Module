
# This program simulates 25 tosses of a coin.
import random

def main():
    tosses = 25
    coin(tosses)
#end of main function    

def coin(tosses):
    for toss in range(tosses):
        # Simulate the coin toss.
        if random.randint(1, 2) == 1:
            print('Heads')
        else:
            print('Tails')
        # end of if statement
     #end of for loop   
#end of coin function

            
# Call the main function.
main()


