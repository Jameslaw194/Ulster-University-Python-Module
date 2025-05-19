import math

def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

number = input("Enter a number: ")

num = int(number)
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")