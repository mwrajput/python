"""
Transportaion Mode Selection

it is based on distance 

like 
 < 3km -- walk
 >3km- <15km < --- bike
 
 >15km -- car


    """

distance = int(input("Enter Distance : "))

if distance <= 3:
    print ("walk")
elif distance > 3 and distance < 15:
    print ("Use Bike")
elif distance >= 15:
    print ("use car")
else:
    print("Go on bus")