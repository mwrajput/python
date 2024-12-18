"""


Here’s a task to practice Polymorphism in Python:

Task: Shape Area Calculator with Polymorphism
Create a base class called Shape with a method area(). Then, create multiple derived classes like Circle, Rectangle, and Triangle, each overriding the area() method to calculate the area in their specific way.

Instructions:
Base Class: Shape

Define an abstract method area() that will be overridden in child classes.
Derived Classes:

Circle: Takes a radius as input and calculates the area using the formula π * radius².
Rectangle: Takes width and height as input and calculates the area using width * height.
Triangle: Takes base and height as input and calculates the area using 0.5 * base * height.
Polymorphism:

Create a list of Shape objects (Circle, Rectangle, Triangle).
Iterate over the list and call the area() method on each object, which should produce different results based on the object type.
Bonus:
Add a display() method to each class to print the area of the respective shape.


"""


class Shape:
    def area(self):
        print ("I calculate Area")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return f"Circle Area: {3.14 * (self.radius ** 2)}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return f"Rectangle Area: {self.width * self.height}"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return f"Triangle Area: {0.5 * self.base * self.height}"


# Polymorphism example
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4)]

for shape in shapes:
    print(shape.area())  # Different areas based on the object type