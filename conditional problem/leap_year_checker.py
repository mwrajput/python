"""
 Leap year Checker
 
 leap year are divisible by 4 and 400
 but not divisible by 100

"""

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
     print (f"{year} is Leap year ")
else:
    print (f"{year} is not Leap year ")