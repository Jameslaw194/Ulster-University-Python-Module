def analyze_stock_file(filename):
    contents = filename.read()
    num_lines = sum(1 for _ in open('stock.txt'))
    print(f"Number of daily records is {num_lines}")

    filename = open("stock.txt", "r")
    largest = None
    smallest = None
    average = 0
    for line in filename:
        for num_str in line.split():
            number = float(num_str)
            average += number

            if largest is None or number > largest:
                largest = number
            if smallest is None or number < smallest:
                smallest = number

    average = average / num_lines
    filename.close()
    print(f"The maximum recorded value of the stock is £{largest}")
    print(f"The smallest recorded value of the stock is £{smallest}")
    print(f"The average value of the stock is £{average:.4}")

def main():
    filename = open("stock.txt", "r")
    analyze_stock_file(filename)

main()