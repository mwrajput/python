"""
Project: Movie Collection Tracker

Description:
Create a program to manage a personal collection of movies. 
The program should allow users to:

Add a new movie with details like title, genre, and release year.
View all movies in the collection.
Search for a movie by its title.
Delete a movie from the collection.


"""

# Initialize the movie collection
movie_collection = {}
title = ""
genre = ""
release_Year = ""

def add_movie():
    # Add a new movie to the collection
    title = input("Enter Movie Name: ")
    genre = input("Enter Movie Genre (e.g., Action, Comedy): ")
    release_year = input("Enter Release Year: ")
    
    while not (release_year.isdigit() and len(release_year) == 4):
        print("Invalid year. Please enter a 4-digit number.")
        release_year = input("Enter Release Year: ")

    
    if title in movie_collection:
        print(f"The movie '{title}' already exists in the collection.")
    else:
    # Proceed to add the movie
        movie_collection[title] = {"Genre": genre, "Release Year": release_year}
        print(f"Movie '{title}' has been added to the collection!")

def view_movies():
    # View all movies in the collection
    if not movie_collection:
        print("\nThe collection is empty.")
        return  # Exit the function if no movies are present
    
    print("\nMovies in the Collection:")
    print("-" * 40)
    for title, details in movie_collection.items():
        print(f"Title: {title}")
        print(f"Genre: {details['Genre']}")
        print(f"Release Year: {details['Release Year']}")
        print("-" * 40)
    
def search_movie():
    # Search for a movie by title
    title = input("Enter Movie Name: ")
    print("-" * 40)
    if title in movie_collection:
        print("\nMovie found in the Collection:")
        print(f"Title : {title}")
        print(f"Genre : {movie_collection[title]['Genre']}")
        print(f"Release Year : {movie_collection[title]['Release Year']}")
        print("-" * 40)
    else:
        print(f"\n'{title}' Movie not found in the collection.")

def delete_movie():
    # Delete a movie from the collection
    title = input("Enter Movie Name: ")
    print("-" * 40)
    if title in movie_collection:
        del movie_collection[title]
        print("\nMovie is deleted from Collection")
    else:
        print(f"\n'{title}' Movie not found in the collection.")

# Main Program
while True:
    print("-" * 40)
    print("\nMovie Collection Tracker")
    print("-" * 40)
    print("\n1. Add Movie")
    print("2. View All Movies")
    print("3. Search for a Movie")
    print("4. Delete a Movie")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_movie()
    elif choice == "2":
        view_movies()
    elif choice == "3":
        search_movie()
    elif choice == "4":
        delete_movie()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
