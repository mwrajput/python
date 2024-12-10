"""
Project: Student Grades Manager
Description: 
Create a program that manages student 
grades using a dictionary. 

The program should allow you to 
add, update, delete, and view 
student grades.

"""

studentGrades = {}  # Start with an empty dictionary

# Adding a new student
# grades["Ali"] = 85

# update grades
studentGrades["Ali"] = 95
studentGrades ["waqas"] = 100
studentGrades["Ahmed"] = 70

# del studentGrades["Ali"] 
# del studentGrades["Ahmed"] 

# while True:
#     # Ask for the student's name
#     name =  input("Enter the student's name (or type 'done' to finish): ")  
#     if name.lower() == "done":
#         break
#     grade = input("Enter the grade : ")
    
#     studentGrades[name] = grade

print(studentGrades)

# for value in grades.values():
#     print(value)

# for keys in grades.keys():
#     print(keys)

# for keys,values in grades.items():
#     print(keys,values)

# print("Ahmed" in studentGrades)

