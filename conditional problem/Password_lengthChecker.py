"""
Password length Checker

check if password is
"Weak" , "Medium" ,or "Strong"

Criteria:

<6 chars(weak)
6-10  (strong)
> 10 chars (strong)

"""
password = "Secure@123"
password_length = len(password)

if password_length < 6 :
    strength = "weak"

elif password_length <= 10 :
    strength = 'medium'
else: 
    strength = 'strong'

print("Password Strength is : ", strength)