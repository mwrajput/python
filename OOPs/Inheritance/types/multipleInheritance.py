# Multiple Inheritance

class Father:
    def fatherShow(self):
        print("I am father")

class Mother:
    def motherShow(self):
        print("I am mother")
        

class Child(Father,Mother):
    def childShow(self):
        print("I am child")


child = Child()

child.fatherShow()
child.motherShow()
child.childShow()