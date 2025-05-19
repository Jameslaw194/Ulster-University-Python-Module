#lab 4 com101 task 2
# comments to modified code indicated by triple #

####input largest number
big = int(input('What is the largest integer you want the table to go to?'))

print('number\tSquare\tCube') ### add cube to header
print('----------------------') ### extend underlining

###note we must go to one more in the range statement
for number in range (1,big+1):
    square = number**2
    cube = number**3  ###add cube calculation
    print(number, '\t', square, '\t',cube) ###add cube to print
    
