def process_countries():

    with open('landmarks.txt', 'r') as f:
        countries = f.readlines()

    country_names = []
    for line in countries:
        if line.startswith("Country:"):
            country_names.append(line.strip())

    valid_countries = [country for country in country_names if len(country) > 15]

    with open('landmarks_extracted.txt', 'w') as f:
        for country in valid_countries:
            f.write(f"{country}\n")

process_countries()
