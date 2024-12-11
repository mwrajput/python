from datetime import datetime

class Book:
    def __init__(self, title , author , year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year_published}")

    def update_title(self,new_title):
        self.title = new_title
        print(f"Title updated to: {self.title}")
        
    def is_classic(self):
        current_year = datetime.now().year
        if current_year - self.year_published > 50:  # Check if the book is older than 50 years
            return True
        else:
            return False
    
# Creating two book objects
book_1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
book_2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

# Calling the display_info method for both books
print("\n\nBook 1:")
book_1.display_info()
print("Is Classic?", book_1.is_classic())

print("\n\nBook 2:")
book_2.display_info()
print("Is Classic?", book_2.is_classic())

# Update the title of book_1 and check again
# book_1.update_title("Harry Potter and the Philosopher's Stone")
# book_1.display_info()