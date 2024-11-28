"""
Fruit Ripeness checker

Determine if a fruit is ripe, overripe, 

check based on its color

(Banana : 
    Green -- UnRipe
    yellow --Ripe
    Brown -- OverRipe
)


"""

fruit = input("Enter Fruit name : ").lower()

if fruit == "banana":
    fruit_color = input("Enter a fruit color : ").lower()

    if fruit_color == "green" and fruit_color == "banana":
        print(f" {fruit} is fresh")

    elif fruit_color == 'yellow':
        print(f"Sorry {fruit} is ripe but you can Eat")
    elif fruit_color == 'brown':
        print(f" {fruit} is overripe dont Eat")
        
    else:
        print("Its unprdetictable")

else:
    print("I dont have data For any other fruit except banana")