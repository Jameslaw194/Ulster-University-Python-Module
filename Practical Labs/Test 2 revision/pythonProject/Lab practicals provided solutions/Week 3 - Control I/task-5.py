#task 5 week 3

#set cost pernail at £0.1 and postage at £2
cost_per_nail = 0.1
postage = 2

#input number of nails
nails = int(input('How many nails do you wish to purchase?'))

#calculate discount using if-elif-else statement
#discount is the factor we will multiply the original cost by
#Thus of we are getting 20% off we pay 0.8 of te price etc
if (nails>200):
    discount = 0.75
elif (nails>99):
    discount = 0.8
elif (nails>51):
    discount = 0.9
else:
    discount = 1.0

#end of decision structure

cost = nails*cost_per_nail*discount
total = cost + postage

#output bill

print('Your', nails, ' nails will cost £', format(cost,'.2f'))
print('The total bill, including postage is £', format(total,'.2f'))

