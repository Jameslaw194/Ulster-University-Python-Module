def fahrenheit(temp):
    #convert centigrade to fahrenheit
    #using standard formula
    result = temp*1.8 +32
    print(result)
# end of fahrenheit function


def centigrade(temp):
    result = temp - 32 * 5/9
    print(result)

def main():
    print("Enter 1 to convert Centigrade to Fahrenheit")
    print("Enter 2 to convert Fahrenheit to Centigrade")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        temp = int(input("Enter the temperature in Centigrade: "))
        fahrenheit(temp)
    elif choice == 2:
        temp = int(input("Enter the temperature in Fahrenheit: "))
        centigrade(temp)
    else:
        print("Invalid choice")

main()