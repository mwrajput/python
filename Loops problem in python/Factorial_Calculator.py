"""
Factorial Calculator
using while loop

5! = 5*4*3*2*1

"""

n = 5
factorial = 1
while n >= 1:
    factorial = factorial * n
    n -= 1
    
print (f"factorial of {n} is : ", factorial)



# How it works ?

# factorial = factorial * n

# 1 * 5  =5 
# 5 * 4 = 20
# 20 * 3 = 60
# 60 * 2 = 120 
# 120 * 1 = 120

