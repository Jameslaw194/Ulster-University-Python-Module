#week 4 lab q7
#This code uses the sieve of Eratosthenes to test for a prime


n= int(input('What is your number?'))

prime = True
i=1
while prime and i<=n**(1/2):
    i=i+1
    if n%i==0:
        prime=False
        low = i

if prime:
    print (n,' is prime')
else:
    print (n,' is not prime its lowest divisor is', low)
    
