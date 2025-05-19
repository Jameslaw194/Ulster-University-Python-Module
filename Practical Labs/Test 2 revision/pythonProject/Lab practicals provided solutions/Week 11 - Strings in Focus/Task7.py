def replace(num):
    if num == 'A' or num == 'B' or num == 'C':
        return '2'
    elif num == 'D' or num == 'E' or num == 'F':
        return '3'
    elif num == 'G' or num == 'H' or num == 'I':
        return '4'
    elif num == 'J' or num == 'K' or num == 'L':
        return '5'
    elif num == 'M' or num == 'N' or num == 'O':
        return '6'
    elif num == 'P' or num == 'Q' or num == 'R' or num == 'S':
        return '7'
    elif num == 'T' or num == 'U' or num == 'V':
        return '8'
    elif num == 'W' or num == 'X' or num == 'Y' or num == 'Z':
        return '9'
    else:
        return num

def main():
    phoneNumber = input('Enter a phone number to be translated:')

    for i in range(0, len(phoneNumber)):
        phoneNumber = phoneNumber[:i] + replace(phoneNumber[i]) + phoneNumber[i+1:]
        
    print(phoneNumber)

# Call the main function.
if __name__ == '__main__':
    main()
