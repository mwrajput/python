# Initialize the dictionary
studentGrades = {}

# Function to add or update a student
def add_or_update_student():
    name = input("Enter the student's name: ")
    grade = input("Enter the grade: ")
    studentGrades[name] = grade # Convert grade to integer
    print(f"{name}'s grade has been added/updated.")

# Function to delete a student
def delete_student():
    name = input("Enter the student's name to delete: ")
    if name in studentGrades:
        del studentGrades[name]
        print(f"{name} has been removed.")
    else:
        print(f"{name} is not in the records.")

# Function to view all students and grades
def view_grades():
    if studentGrades:
        print("Student Grades:")
        for name, grade in studentGrades.items():
            print(f"{name}: {grade}")
    else:
        print("No books in the library.")

# Function to check if a student exists
def check_student():
    name = input("Enter the student's name to check: ")
    if name in studentGrades:
        print(f"{name} exists with a grade of {studentGrades[name]}.")
    else:
        print(f"{name} does not exist in the records.")

# Main loop for the menu
while True:
    print("\nStudent Grades Manager")
    print("1. Add or Update a Student")
    print("2. Delete a Student")
    print("3. View All Students and Grades")
    print("4. Check if a Student Exists")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_or_update_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        view_grades()
    elif choice == "4":
        check_student()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
