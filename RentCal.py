# amount = input("Enter the amount : ")

# Rent Calculator

rent = int(input("Enter House/FLat rent : "))
food = int(input("Enter Food Cost : "))
electricity = int(input("Enter Electricity Cost : "))
charge_Per_unit = int(input("Enter Charge Per Unit : "))
no_of_personals = int(input("Enter number of personal living : "))


total_bill = electricity* charge_Per_unit

output = (food +total_bill+ rent) // no_of_personals

print("The total amount per person  pay is : " , output) 