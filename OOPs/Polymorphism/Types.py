"""
Runtime Polymorphism - method Overriding


Overriding - 
Method overriding tab hota hai jab child class
apne parent class ke method ko redefine karti hai. 
Yeh ensure karta hai ki child class
ka method call ho jab object child class ka ho.

"""

# Runtime Polymorphism - method Overriding

# parent Class
# class Animal:
#     def make_sounds(self):
#         print("Animal makes sound")

# child Class
# class Dog(Animal):
#     def make_sounds(self):
#         print("Dog barks")

# child class
# class Cat(Animal):
    # def make_sounds(self):
        # print("Cat Meow Meow")
        
# object Creation

# animal = Animal()
# dog = Dog()
# cat = Cat()

# animal.make_sounds()
# dog.make_sounds()
# cat.make_sounds()

# ------------------------------------------------------------------------------------------------------------

# Compile Time Polymorphism - method overloading


# Python me method overloading directly support nahi karta, 
# lekin hum default arguments ka use karke
# ek method ko multiple tarike se use kar sakte hain.

# ------------------------------------------------------------------------------------------------------------

class Calculator:
    def add(self, a,b,c=0):
        print("Sum = " ,a+b+c)

calc = Calculator()        

calc.add(3,4,5)