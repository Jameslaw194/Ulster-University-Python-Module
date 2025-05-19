# Prompt the user for the number of miles driven
miles_driven = float(input("Enter miles: "))

# Prompt the user for the gallons of fuel used
gallons_used = float(input("Enter gallons: "))

# Calculate the MPG

mpg = miles_driven / gallons_used

# Display the result
print(f"The MPG is {mpg:.2f}")
