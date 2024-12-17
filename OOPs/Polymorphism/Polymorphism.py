"""
Polymorphism 
"""

# Polymorphism with function

class Bird:
    def fly(self):
        print ("Bird is flying ")

class Airplane:
    def fly(self):
        print ("Airplane is flying ")
        
        
        
bird = Bird()
aeroplane = Airplane()

bird.fly()
aeroplane.fly()     
