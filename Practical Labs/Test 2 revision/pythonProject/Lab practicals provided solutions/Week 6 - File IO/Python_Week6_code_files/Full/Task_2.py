def analyze_stock_file(filename):
    num_records = 0
    max_value = None
    min_value = None
    total_sum = 0

    try:
        file = open(filename, 'r')

        for line in file:
            # Convert the current line to a float
            value = float(line.strip())
            num_records += 1

            # Update max and min values
            if max_value is None or value > max_value:
                max_value = value
            if min_value is None or value < min_value:
                min_value = value

            # Update total sum
            total_sum += value

        # Calculate average
        avg_value = total_sum / num_records

        return num_records, max_value, min_value, avg_value

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except ValueError:
        print("Error: Ensure that the file contains valid stock values.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file.close()


def main():
    filename = 'stock.txt'
    results = analyze_stock_file(filename)
    if results:
        num_records, max_value, min_value, avg_value = results
        print(f"Number of daily records: {num_records}")
        print(f"Maximum stock value: £{max_value:.2f}")
        print(f"Minimum stock value: £{min_value:.2f}")
        print(f"Average stock value: £{avg_value:.2f}")


main()
