leapYear = int(input("Enter the year you want to check: "))


if leapYear % 100 == 0 and leapYear % 400 == 0:
    print("Its a leap year!")
elif leapYear % 4 == 0 and leapYear % 100 != 0:
    print("Its a leap year!")
else:
    print("Its not leap year")