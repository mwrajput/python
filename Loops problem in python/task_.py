n = 5

sum = 0
fact = 1
for i in range(1, n+1):
    fact = (fact * i)
    sum = sum + i/fact

print(sum)