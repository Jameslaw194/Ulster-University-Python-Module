# Prompt the user to enter the original price
original_price = float(input("Enter original price: "))

# Calculate the discount
discount = original_price * 0.20

# Calculate the sale price
sale_price = original_price - discount

# Output the sale price
print(f"The sale price is {sale_price:.2f}")
