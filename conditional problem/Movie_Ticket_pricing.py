"""
Movie Ticket pricing

WorkFlow Details:

    Movie Tickets are priced Based on age :
        $12 for adults (18 and over)
        $8  for children
    Special Discount to Everyone:
        Everyone gets a $2 discount on wednesday

"""

age = int(input('Enter your Age : '))
day = str(input('Enter What day is today : '))

if day == "wednesday":
        print('Ticket Price is $2')
else:
    if age < 18 :
        print('Ticket Price is 8$')
    elif age >= 18 :
        print('Ticket Price is 12$')
    else:
        print('Invalid')    
        