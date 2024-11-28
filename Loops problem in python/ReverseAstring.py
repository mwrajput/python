"""
Reverse a String


"""

# string = input("Enter a string : ")

string = "Hi Muhammad Waqas"
reverseString = ""

for char in string:
# for char in reversed(string):
    # print (char)
    reverseString = char+ reverseString  

print(reverseString)