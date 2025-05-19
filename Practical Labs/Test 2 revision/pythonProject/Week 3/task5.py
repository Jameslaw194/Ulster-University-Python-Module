nails = int(input("How many nails do you want to buy?: "))

nailPrice = 0.10
postageCharge = 2
cost = nails * nailPrice
postage = cost + postageCharge

if nails < 51:
    print(f"Charge of £{cost} before packaging")
    print(f"Total charge of £{postage} including packaging")
elif nails < 101:
    print("You get a discount of 10%")
    print(f"Charge of £{cost / 0.90:.2f} before packaging")
    print(f"Total charge of £{postage / 0.90:.2f} including packaging")
elif nails < 201:
    print("You get a discount of 20%")
    print(f"Charge of £{cost / 0.80:.2f} before packaging")
    print(f"Total charge of £{postage / 0.80:.2f} including packaging")
elif nails > 201:
    print("You get a discount of 25%")
    print(f"Charge of £{cost / 0.75:.2f} before packaging")
    print(f"Total charge of £{postage / 0.75:.2f} including packaging")
