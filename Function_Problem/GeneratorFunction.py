"""

Problem: Write a generator function that yields even numbers up to a specified limit.

yield creates a generator in Python, producing values one at a time on demand
without storing them in memory.
"""

def even_generator(limit):
    sum = 0
    for i in range(0,limit+1,2):
        # sum= sum + i
        # print (i)
        # return sum
        yield i
        
    
# output = even_generator(100)
# print(output)

for num in even_generator(20):
    print(num)