"""

Student Class

Attributes: Name, age, grade.

Methods:
Constructor (__init__) to initialize attributes.
A method to display student details (display_details).

Objective: Practice setting and accessing attributes, 
and creating meaningful methods.

"""


class Student:
    def __init__(self , name ,age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    # display method
    def display_details(self):
        return f"{self.name}, {self.age}, {self.grade}"

student_1 = Student("Muhammad Waqas", "25" ,"A")
print(student_1.display_details())