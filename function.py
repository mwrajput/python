# def hello(g):
#     print(f"hello world {g}")

# hello("pakistan")

# ------function arguments------
def avg(a=10,b=20):
    print(f"avg : ", (a+b)//2)

# avg() # default argument
# avg(b=15,a=25) 

# def average(*number):
#     for i in number:
#         print(i)
#     print(f"avg is {sum(number)//len(number)}")
    
# average(1,2,3,4,5)
    
    
# return statement in function

def hello():
    return "hello world"

print(hello())
