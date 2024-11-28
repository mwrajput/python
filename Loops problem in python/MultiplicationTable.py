"""
Multiplication Table
print table of n number

skip 5th iteration
"""
n = int(input("Enter Number : "))

for i in range(1,10+1):
    if i == 5:
        continue
    else:        
        print(f"{n} x {i} = {n*i}")
