print('number\tSquare\tCube')
print('--------------------')

max = int(input("Enter the largest number you want to calculate: "))

for number in range(max, 0, -1):
    square = number ** 2
    cube = number ** 3
    print(number, '\t', square, '\t', cube)

