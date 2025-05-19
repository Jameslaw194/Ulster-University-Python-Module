from Task1 import *
from Task2 import *
from Task3 import *
from Task4 import *

def main():
    option = int(input("Enter a choice (1 - 4) or 5 to quit:\n1, Calculate rainfall.\n2, Query account numbers.\n3, Format a number list.\n4, Format a word list.\n"))
    if option == 1:
        yearly_rainfall()
    elif option == 2:
        query()
    elif option == 3:
        sorting(original_list)
    elif option == 4:
        how_many()
    elif option == 5:
        print("Stopping")
    else:
        main()

main()