# com101 lab 3 task 11
#this code returns whether a year is a leap year or not
# con1, con2, con3 are boolean variables

year = int(input('What year is it?'))

#check if year is divisible by 100

if year%100 == 0:
    con1= True
else:
    con1= False

#check of year is divisible by 400
    
if year%400 == 0:
    con2= True
else:
    con2= False

# check if divisible by 4

if year%4 == 0:
    con3= True
else:
    con3= False

if (con1 and con2) or (not(con1) and con3):
    print(year, ' is a leap year')
else:
    print(year, ' is not a leap year')
