"""
Function with *args

Problem: Write a function that takes variable number of arguments and returns their sum.

learning

1) Built in funtion sum()
2) what is *args
3) apply loop
"""

def add(*args):
    # return sum(args)
    sum=0
    for i in range(len(args)):
        sum += args[i]
    return sum

output = add(1,2,3,4)
print(output)