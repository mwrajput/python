"""
Encapsulation :

Modify a car Class to encapsulate the brand attributes,
making it private and provide a getter method for it.

"""


class Car:
    def __init__(self, brand, model):
        # making brand private
       self.__brand = brand
       self.model = model
       
    def get_brand(self):
        return self.__brand + " : Your Car brand "
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
# inheritnace Concepts
class ElectricCar(Car):
    def __init__(self , brand ,model ,battery_size):
        
        super().__init__(brand, model)
        self.battery_size = battery_size 
        super().full_name()
        
my_Tesla = ElectricCar("Tesla" , "model_101_S" ,"85kWH" )
# print(my_Tesla.model)
# print(my_Tesla.full_name())
print(my_Tesla.get_brand())

