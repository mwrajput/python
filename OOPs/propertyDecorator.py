"""
Use a property Decorators in the Car Class to make the class
model attribute read-only

"""

class Car:
    def __init__(self, brand, model):
        # making brand private
       self.__brand = brand
       self.__model = model
       
    def get_brand(self):
        return self.__brand + " : Your Car brand "
    def full_name(self):
        return f"{self.__brand} {self.model}"

    @staticmethod
    def general_descriptions():
        return "Cars are  means of transport"
    
    @property
    def model(self):
        return self.__model
class ElectricCar(Car):
    def __init__(self , brand ,model ,battery_size):
        
        super().__init__(brand, model)
        self.battery_size = battery_size 
        super().full_name()
        
my_Tesla = ElectricCar("Tesla" , "model_101_S" ,"85kWH" )
# print(my_Tesla.model)
# print(my_Tesla.full_name())
# print(my_Tesla.get_brand())

my_car = Car("Honda" , "Civic")
my_car.model = "City"
print(my_car.model())
# print(my_car.general_descriptions())
print(Car.general_descriptions())
        