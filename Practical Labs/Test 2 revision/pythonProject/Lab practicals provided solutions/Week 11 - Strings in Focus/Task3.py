def wordSwap(str1):
    # Replace 'left' with 'right' and 'up' with 'down' using the replace method
    output_string = str1.replace('left', 'right').replace('up', 'down')
    # Return the modified string
    return output_string


# Test the function with some examples


def main():
    print(wordSwap('I left my keys upstairs'))
    print(wordSwap('Turn left and go up the hill'))
    print(wordSwap('No change'))


main()
