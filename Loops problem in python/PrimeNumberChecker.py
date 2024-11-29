"""
Prime Number Checker

prime number whose is

divisble by 1 and only itself

"""

n = int(input('Enter number : '))
its_prime = True
if n > 1:
    for i in range(2,n+1):
        if (n % i) == 0:
            its_prime = False
            break

if its_prime == True:
    print(f"Number is not prime")
elif its_prime == False:
    print(f"Number is prime")
    