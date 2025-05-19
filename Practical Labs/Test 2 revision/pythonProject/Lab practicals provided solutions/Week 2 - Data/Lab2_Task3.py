# Prompt the user to enter the dimensions of the box
height = int(input("Enter in height: "))
width = int(input("Enter in width: "))
depth = int(input("Enter in depth: "))

# Calculate the perimeter
perimeter = 4 * (height + width + depth)

# Calculate the volume
volume = height * width * depth

# Output the results
print(f"The perimeter is {perimeter}")
print(f"The volume is {volume}")
