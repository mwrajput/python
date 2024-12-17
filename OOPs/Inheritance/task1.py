"""
Task 1: Create a Simple Inheritance Example

Objective: Understand the basics of single inheritance.

Task Description:

Create a Person class with attributes:
name
age

Method display_info() to print the details of a person.

Create a Student class that inherits from Person and adds:
student_id

Method display_student_info() that prints 
the student_id and calls display_info() from the parent class.

Create objects for Person and Student classes, and demonstrate:

Calling methods of both parent and child classes.

"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"{self.name}, {self.age}"

class Student(Person):
    def __init__(self,id,name,age):
        self.id = id
        super().name
        super().age
    def display_student_info(self):
        super().display_info()
        return {self.id}
    
st1 = Student("Ali Haider" , 25)

print(st1.display_info())