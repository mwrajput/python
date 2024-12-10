"""
Project: 

Library Book Tracker

Description:
Create a program to manage books in a library. The program should allow you to:

Add new books.
Update the number of copies of a book.
Remove a book from the library.
View all books and their available copies.
Check if a book is available.



Goal
This project will help you practice:

Working with dictionaries to store and manage data.
Using functions to perform specific tasks.
Creating a menu for user interaction.
Validating user input and handling different cases.


"""
# Initialize the dictionary
# key : value pair
book_rack = {}
book_title = ""
book_Subject = ""

def add_book():
    book_title = input("Enter Book Name : ")
    book_Subject = input("Enter Book Subject : ")
    book_rack[book_Subject] = book_title 
    print(f"\nBook '{book_title}' added under subject '{book_Subject}'.")
    
def remove_book():
    book_title = input("Enter the Book's name to delete: ")
    if book_title in book_rack:
        del book_rack[book_title]
        print(f"\n{book_title} has been removed.")
    else:
        print(f"\n{book_title} is not in record")
        
def view_book():
    if book_rack:
        print("\nBooks in the Library:")
        print(f"{'Subject':<20} {'Title'}")
        print("-" * 30)
        for subject, title in book_rack.items():
            print(f"{subject:<20} {title}")
    else:
        print("\nThe library has no books.")


def check_book():
    book_title = input("Which Book to check ? ")
    if book_title in book_rack.values():
        print(f"\n'{book_title}'is available in the Library:")
    else:
        print(f"\n'{book_title}' is not available in the library.")

while True:
    print("\nLibrary Book Tracker")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. View All Books")
    print("4. Check Book Availability")
    print("5. Exit")

    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        view_book()
    elif choice == "4":
        check_book()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    
