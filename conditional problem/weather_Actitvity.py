"""

Suggest an Activity based on Weather Situation


like:
Sunny - go for Walk
Rainy - read a book
Snowy - Build a snowMan

"""

weather_Situation = input("Enter Weather Situation : ").lower()

if weather_Situation == "sunny":
    print("Go for walk")
elif weather_Situation == "rainy":
    print("Read a book")
elif weather_Situation == "snowy":
    print("Build a snowman")
else:
    print("Jo marzi kro")
