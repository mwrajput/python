"""
Problem: Write a function that greets a user. 
If no name is provided, it should greet with a default name.

"""
name = input("Enter Name : ")

def greet(name = "Waqas"):
    return (f"Salam {name}!")

print(greet(name))