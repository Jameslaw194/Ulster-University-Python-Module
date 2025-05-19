def yearly_rainfall():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    rainfall = []
    total_rainfall = 0

    for each_month in months:
        month = int(input(f"Enter the rainfall for {each_month}: "))
        total_rainfall += int(month)
        rainfall.append(month)

    avg = sum(rainfall) / len(rainfall)

    print(f"Total rainfall: {total_rainfall}")
    print(f"Average rainfall: {avg}")
