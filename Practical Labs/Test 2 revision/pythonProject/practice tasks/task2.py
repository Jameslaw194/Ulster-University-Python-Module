# Function to read data from the file
def read_data(file_path):
    # Initialize empty lists to store eye colors and ages
    eye_colors = []
    ages = []

    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Skip the header row (assuming it starts with '#')
        next(f)

        # Iterate through each line in the file
        for line in f:
            # Split the line into parts based on comma separator
            parts = line.strip().split(',')

            # Append eye color to the list
            eye_colors.append(parts[0])

            # Convert age string to float and append to ages list
            ages.append(float(parts[1]))

    # Return both lists
    return eye_colors, ages


# Function to calculate the average age
def calculate_average_age(ages):
    # Sum up all ages and divide by the number of ages
    return sum(ages) / len(ages)


# Function to calculate color percentages
def calculate_color_percentages(eye_colors):
    # Get total number of eye colors
    total = len(eye_colors)

    # Initialize a dictionary to store color percentages
    color_percentages = {}

    # Iterate through unique eye colors
    for color in set(eye_colors):
        # Count occurrences of each color
        count = eye_colors.count(color)

        # Calculate percentage and round to one decimal place
        percentage = round((count / total) * 100, 1)

        # Store color and its percentage in the dictionary
        color_percentages[color] = percentage

    # Return the dictionary of color percentages
    return color_percentages


# Main function for task 2
def task2():
    # Specify the file path
    file_path = 'optometry.txt'

    # Read data from the file
    eye_colors, ages = read_data(file_path)

    # Calculate average age
    average_age = calculate_average_age(ages)

    # Calculate color percentages
    color_percentages = calculate_color_percentages(eye_colors)

    # Print the average age rounded to one decimal place
    print(f"Average age: {round(average_age, 1)} years")

    # Print eye color percentages
    print("\nEye Color Percentages:")
    for color, percentage in color_percentages.items():
        print(f"{color}: {percentage}%")


# Run the main function when the script is executed directly
if __name__ == "__main__":
    task2()
