# this program does a temperature conversion

def main():
    print("Enter 1 to convert Centrigade to Fahrenheit")
    print("Enter 2 to convert Fahrenheit to Centrigade")
    userChoice = int(input("Enter Choice: "))

    if userChoice == 1:
        #get temperature in centigrade
        temp=float(input('Enter the temperature in Centigrade: '))

        #get temp. in Farenheit
        temp_far=fahrenheit(temp)

        #display result
        print('The temperature in Fahrenheit is', round(temp_far,2),'degrees')

    else:
        temp=float(input('Enter the temperature in Fahrenheit: '))
        temp_cent = centigrade(temp)
        print('The temperature in Centrigrade is',round(temp_cent,2 ),'degrees')
        
# end of main function

def fahrenheit(temp):
    #convert centigrade to fahrenheit
    #using standard formula
    result = temp*1.8 +32
    return result
# end of fahrenheit function

def centigrade(temp):
    result = (temp - 32) * 5/9
    return result

# call main function
main()


