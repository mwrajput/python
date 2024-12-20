class Car:
    
    def __init__(self, name,password):
        self.name = name
        self.__password = password
    
    def getPassword(self):
        return self.__password
    def setPassword(self, password):
        self.__password = password

car1 = Car("Waqas", "asas")

# Accessing and modifying the attributes
print("Car Name:", car1.name)
print("Initial Password:", car1.getPassword())

# Updating the password using the setter method
car1.setPassword("new_password")
print("Updated Password:", car1.getPassword())