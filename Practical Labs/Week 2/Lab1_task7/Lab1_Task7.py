# numShares = 1000
# purchasePrice = 32.87
# commissionRate = 0.02
# sellingPrice = 33.92

numShares = int(input("Enter the number of shares: "))
purchasePrice = float(input("Enter the purchase price: "))
commissionRate = float(input("Enter the commission rate as a %: "))
commissionRate = commissionRate/100
sellingPrice = float(input("Enter the selling price: "))

amountPaidForStock = numShares * purchasePrice
purchaseCommission = commissionRate * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = numShares * sellingPrice
sellingCommission = commissionRate * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print(f"Joe paid £{amountPaidForStock:.2f} for his stock")
print(f"Joe paid £{purchaseCommission:.2f} in commission purchase")
print(f"Joe sold his stock for £{stockSoldFor:.2f}")
print(f"Joe paid £{sellingCommission:.2f} in commission sale")
print(f"Joe had £{profitOrLoss:.2f} left")

if profitOrLoss > 0:
    print("Joe made a profit")
    print("Joe is happy :)")
else:
    print("Joe made a loss")
    print("Joe is sad :(")
