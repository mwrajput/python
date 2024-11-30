"""
Problem: Create a function that returns both the area and circumference of a circle given its radius.
"""

import math
def calc(radius):
    area = math.pi * (radius **radius)
    c = 2*math.pi*radius
    
    return round(area, 2), round(c, 2)

areaOut ,c =  calc (5)
print(f"Area : {areaOut} \nCircumference : {c}")