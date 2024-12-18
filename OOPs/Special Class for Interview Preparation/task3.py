num_people = int(input("Enter the number of people : "))
ages = []

for i  in range(num_people):
    user_age = int(input("Enter the user age : "))
    ages.append(user_age)
    # print(ages)
    
collector_Age = []
 
child_count = 0
adult_count = 0
senior_count = 0   

# classifying age group
for age in ages:
    if (age < 18):
        # collector_Age.append("Child")
        child_count += 1
    elif (age >= 18 and age <65 ):
        # collector_Age.append("Adult")
        adult_count += 1
    else:
        # collector_Age.append("Senior")
        senior_count += 1

# for i in range(num_people):
#     print(f"Person  : {i+1} age -- Citizen Status {collector_Age[i]}")

print("Number Of People in each Group : " , (child_count + adult_count + senior_count))
print("Children : " , child_count)
print("Adult : " , adult_count)
print("Senior : " , senior_count)