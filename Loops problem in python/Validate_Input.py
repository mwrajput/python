"""
keep asking the use for input until user enter number between (1-10)

"""

while True:
    n = int(input("Enter a number (1-10): "))
    if n>=1 and n<=10:
        print (f"Number : {n}")
        # USe can use break or exit
        # exit()
        break
    else:
      print("Invalid Input try again")

        