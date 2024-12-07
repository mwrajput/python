"""
Basic Class and Object

Create a car with attribute like
Brand and model.

Then Create an instance of the class

""" 

#     Add a method to the car class that displays the full name of the car
#     (brand and model)

# class name must be capital
# __init__ is a constructor
class Car:
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
   
# object Creation
my_car = Car("toyota" , "Corolla")

print(my_car.full_name())