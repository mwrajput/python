# Inheritance

# single Inheritance

class Parent:
    def show(self):
        print ("This is Parent class")
        
class Child(Parent):
    def display(self):
        print ("This is Child class")
        

child = Child()
child.show()
child.display()