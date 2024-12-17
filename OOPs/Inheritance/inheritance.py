"""
Create an Electric Car That inherit 
From the car class and has an addition attributes battery_size

"""

class Car:
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
# inheritnace Concepts
class ElectricCar(Car):
    def __init__(self , brand ,model ,battery_size):
        
        super().__init__(brand, model)
        self.battery_size = battery_size 
        super().full_name()
        
my_Tesla = ElectricCar("Tesla" , "model_101_S" ,"85kWH" )
print(my_Tesla.model)
print(my_Tesla.full_name())
