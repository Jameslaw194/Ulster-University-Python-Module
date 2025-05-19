def get_chinese_animal(year):
    animals = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare']
    start_year = 2000
    index = (year - start_year) % 12
    return animals[index]

user_year = int(input("Enter a year: "))

result = get_chinese_animal(user_year)
print(f"The Chinese New Year animal for {user_year} is: {result}")
