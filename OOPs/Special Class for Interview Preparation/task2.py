no_of_student = int(input("Enter Total No Of students :"))
course_credits = []

for i in range(no_of_student):
    credits = int(input("Enter the Course Credit : "))
    course_credits.append(credits) 

enrollment_status = []

for credits in course_credits:
    if credits >= 12:
            enrollment_status.append("full_Time")
    else:
            enrollment_status.append("part_Time")
        
for i in range(no_of_student):
    print(f"Student {i+1} : Entrollment Status - {enrollment_status[i]}")   
    
    