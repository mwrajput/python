"""
Employee Salary Calculator


Base Class: Employee

Define a method calculate_salary() that will be overridden in child classes.
The Employee class should have a name and base salary as attributes.
Derived Classes:

FullTimeEmployee: Takes a fixed salary and possibly bonus as input 
and calculates the total salary.

PartTimeEmployee: Takes hourly wage and hours worked as input and calculates the salary.
Polymorphism:

Create a list of Employee objects (FullTimeEmployee and PartTimeEmployee).
Iterate over the list and call the calculate_salary() method on each object 
to get the respective salary.
"""

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        pass  # This will be overridden in the child classes
    
# Derived Class: FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)  # Calling parent class constructor
        self.bonus = bonus
    
    def calculate_salary(self):
        # Full-time salary includes the base salary and bonus
        return f"{self.name}'s Full-Time Salary: {self.base_salary + self.bonus}"

# Derived Class: PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name, 0)  # Part-time employees don't have a base salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        # Part-time salary is calculated based on hourly wage and hours worked
        return f"{self.name}'s Part-Time Salary: {self.hourly_wage * self.hours_worked}"
# Derived Class: PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name, 0)  # Part-time employees don't have a base salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        # Part-time salary is calculated based on hourly wage and hours worked
        return f"{self.name}'s Part-Time Salary: {self.hourly_wage * self.hours_worked}"
    
# Polymorphism example
full_time_employee = FullTimeEmployee("John", 5000, 1000)
part_time_employee = PartTimeEmployee("Alice", 20, 80)

# List of Employee objects
employees = [full_time_employee, part_time_employee]

# Iterate over the list and calculate salary for each employee
for employee in employees:
    print(employee.calculate_salary())