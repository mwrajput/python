"""
Project: Vehicle Hierarchy

Create a parent class Vehicle:

Attributes: brand, model, year

Method: display_info()

Create child classes Car and Bike:
Add unique attributes like fuel_type (Car) and gear_count (Bike).

Add methods specific to each child class.
Create objects for each type and demonstrate inheritance.

"""
# Project: Vehicle Hierarchy

class Vehicle:
    def __init__(self, brand="Unknown", model="Unknown", year=0):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Brand : {self.brand}\nModel : {self.model}\nYear : {self.year}"

class Car(Vehicle):
    def __init__(self,fuel_type, brand="Unknown", model="Unknown", year=0):
        super().__init__(brand, model, year)  # Call the parent class constructor
        self.fuel_type = fuel_type
    def display_info(self):
        return f"{super().display_info()}\nFuel Type : {self.fuel_type}"
        
class Bike(Vehicle):
    def __init__(self,gear_count, brand="Unknown", model="Unknown", year=0):
        super().__init__(brand, model, year)  # Call the parent class constructor
        self.gear_count = gear_count
    def display_info(self):
        return f"{super().display_info()}\nGear Count : {self.gear_count}"


# Create an instance of Car and Bike
car1 = Car("Petrol", "Honda", "Civic", 2020)
bike1 = Bike(6, "Yamaha", "FZ", 2018)

# Display information for car and bike
print("\nCar Info:\n")
print(car1.display_info())

print("\nBike Info:\n")
print(bike1.display_info())