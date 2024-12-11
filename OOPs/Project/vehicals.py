from datetime import datetime

class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage =mileage
    
    def display_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")
        print(f"Mileage: {self.mileage} km/l")
    
    def drive(self, litre):
        distance = self.mileage * litre  # Distance is calculated as mileage per litre multiplied by litres
        print(f"The car can drive {distance} kilometers with {litre} litres of fuel.")

    
    def is_vintage(self):
        current_year = datetime.now().year
        if current_year - self.year > 50 :
            return True
        else:
            return False 
            
car = Car("Toyota", "Corolla", 2020, 15)  # 15 km/l mileage
car.display_info()
car.drive(10) 

"""

Task:
Create a class Car with the following attributes:

make (brand of the car)
model (model of the car)
year (year of manufacture)
mileage (mileage of the car in kilometers)
Methods to implement:

display_info(): Displays the car's details (make, model, year, mileage).
drive(distance): Increases the mileage by the given distance.
is_vintage(): Returns True if the car is more than 20 years old, otherwise False.
Steps:

Create at least two Car objects with different details.
Display their information using display_info().
Drive each car for a certain distance using the drive() method.
Check if each car is vintage using the is_vintage() method.
"""