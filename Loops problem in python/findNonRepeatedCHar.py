"""
Find the First Non-Repeated Character

its just give non repeated character

"""


# MY_str = "Hello kyse hn ap k k"
# MY_str = "Muhammad Waqas "
MY_str = "Python programming is fun!"

for char in MY_str:
    # print(char ," : " ,MY_str.count(char))
    if MY_str.count(char) == 1 :
        print("Char : " , char)
        # as we want only frist character that is not repeated
        break;

