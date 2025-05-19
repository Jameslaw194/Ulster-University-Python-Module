#Task5
#Create a text file that lists your expenses for the last month in the following #categories: rent, transport, food, clothing, socializing, misc. Write a program that #reads the data from a file and uses matplotlib to plot a pie chart showing how you #spend your money. The file format may look something like:

#Expenses
#rent 1000
#transport 300
#food 400
#clothing 150
#socializing 200
#misc 100

import matplotlib.pyplot as plt

# Create empty dictionaries to store expense data
categories = {}
total_expense = 0

# Read expense data from the text file
with open("expenses.txt", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            category, cost = parts[0], float(parts[1])
            categories[category] = cost
            total_expense += cost

# Extract category names and expenses
category_names = list(categories.keys())
expenses = list(categories.values())

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(expenses, labels=category_names, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title("Monthly Expenses")

# Display the pie chart
plt.show()


#In this code:

#We read the expense data from the "expenses.txt" file and store it in a dictionary #where keys are categories (e.g., "rent", "transport") and values are the #corresponding expenses.
#We calculate the total expenses for the month.
#We then use Matplotlib to create a pie chart with the category names and expenses as #data.
#The autopct parameter is used to display the percentage on each slice of the pie #chart.
#We set the title of the pie chart as "Monthly Expenses" for clarity.
#Finally, we display the pie chart using plt.show().
