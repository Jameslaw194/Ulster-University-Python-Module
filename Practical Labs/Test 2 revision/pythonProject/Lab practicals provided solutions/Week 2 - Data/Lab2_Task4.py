# Prompt the user to enter the projected total sales
total_sales = float(input("Enter estimated total sales for the year: "))

# Calculate the profit (23% of total sales)
profit = total_sales * 0.23

# Output the profit
print(f"Profit estimated to be: £{profit:.2f}")
