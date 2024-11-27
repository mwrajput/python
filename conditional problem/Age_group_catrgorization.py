"""
Age Group Categorization

Workflow Details:
    
    classify a person's age group:
        child < 13
        Teenagers (13-19)
        Adult (20-59)
        Senior (60+)

what we learn:

i)how to handle conditions
 
    
"""

age = int(input('Enter Your Age : '))

if age < 13:
    print("Hello My dear 'child'")
elif age >=13 and age <= 19 :
    print("You are a 'Teenager'")
elif age >=20 and age <=59:
    print("You are a 'Adult'")
elif age > 60:
    print("You are a 'Senior'")
else:
    print("Sorry You are Not in list")
    
