"""
Basic Class and Object

Create a car with attribute like
Brand and model.

Then Create an instance of the class

""" 
# class name must be capital
# __init__ is a constructor
class Car:
   def __init__(self, brand, model):
       self.brand = brand
       self.model = model
    
   
# object Creation
my_car = Car("toyota" , "Corolla")
print(my_car.brand, my_car.model)