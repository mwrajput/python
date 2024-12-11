# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)
# else:
#     print("Loop completed without a break.")


# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)
#     if num == 3:
#         print("Breaking the loop.")
#         break
# else:
#     print("Loop completed without a break.")


# numbers = [10, 20, 30, 40]

# for num in numbers:
#     if num == 25:
#         print("25 found!")
#         break
# else:
#     print("25 not found in the list.")


allowed_users = ["Alice", "Bob", "Charlie"]

username = input("Enter your username: ")

for user in allowed_users:
    if user == username:
        print("Access granted.")
        break
else:
    print("Access denied.")
