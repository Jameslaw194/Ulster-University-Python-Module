# This program simulates 25 tosses of a coin.
import random


def main():
    tosses = int(input("How many tosses? "))
    coin(tosses)


# end of main function

def coin(tosses):
    head = 0
    tail = 0
    for toss in range(tosses):
        # Simulate the coin toss.
        if random.randint(1, 2) == 1:
            print('Heads')
            head += 1
        else:
            print('Tails')
            tail += 1
    print("Number of heads: ", head)
    print("Number of tails: ", tail)
        # end of if statement
    # end of for loop


# end of coin function


# Call the main function.
main()


