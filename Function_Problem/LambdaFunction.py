"""

Problem: Create a lambda function to compute the cube of a number.

"""

cube = lambda x,y: (x**3,y**2)

# res = cube(3,2)
# print(f"Cube : {res[0]},Square : {res[1]}")

cube_x, square_y = cube(3, 2)
print(f"Cube of x: {cube_x}, Square of y: {square_y}")