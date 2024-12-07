"""

Concept of Python dictionaries with small tasks. 

A dictionary in Python is a data structure that stores data as 
key-value pairs. 


"""

# Step 1: Creating a Dictionary
programming_languages = {
    "Cpp": "Bjarne Stroustrup",
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "JavaScript": "Brendan Eich",
    "Ruby": "Yukihiro Matsumoto",
    "PHP": "Rasmus Lerdorf",
    "Swift": "Chris Lattner",
}

# Step 2: Accessing Values in a Dictionary
# print(programming_languages["Cpp"])

# Step 3: Adding or Updating Key-Value Pairs

# Adding
# programming_languages["Kotlin"] = "Andrey Breslav"

# Updating
# programming_languages["Cpp"] = "22"


# Step 4: Removing a Key-Value Pair
# del programming_languages["Swift"]
# del programming_languages["PHP"]




#Step 5: Looping Through a Dictionary

# for name,persons in programming_languages.items():
#     print(f"{name} : {persons}")


# Step 6: Checking for a Key
print("Cpp" in programming_languages)