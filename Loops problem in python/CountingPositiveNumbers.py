"""
Counting Positive Numbers 

numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

Here is the list iterate and count positive number

"""

numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

positiveNum = 0
for n in numbers:
    if n > 0:
        positiveNum += 1;

print(f"Total postive Number id {positiveNum}") 