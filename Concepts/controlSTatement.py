# if -elif- else

age = input("Age : ")

age=int(age)

if age >= 18:
    print ("You can vote")
elif age <= 17 and age >= 10:
    print ("You cannot vote")
else:
    print ("drink milk")