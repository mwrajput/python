"""
Grade Calculator

Problem Assign a letter grade based on a student's score:

Grade  Scores
A      (90-100)
B      (80-89)
C      (70-79)
D      (60-69)
F      (below 60)

"""
score = int(input('Enter your score : '))

if score >= 101:
    print ('Please enter Score (1 - 100)')
    exit()

if score >=90 and score <=100:
    print('Your Grade is A')
elif score >=80 and score <=89:
    print('Your Grade is B')
elif score >=70 and score <=79:
    print('Your Grade is C')
elif score >=60 and score <=69:
    print('Your Grade is D')
else:
    print('Your Grade is F')