# List

# list = [1,2,3,4,5]
# print(type(list))

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])  
# print(list[4])

# list.append(10)
# print(list)

# Marks = [10,30,70,"please" ,"true"]

# print(Marks)
# Marks.pop()
# print(Marks)
# Marks.append(False)
# print(Marks)

# if 70 in Marks:
#     print("true")
# else:
#     print("false")



# name = 'Muhammad Waqas'# string

# print(name[0])
# print(name[1])
# print(name[2])

# Add "rajput" to the string
#ame = name + " rajput"
#print(name)  # Output: Muhammad Waqas rajput

# Remove "rajput" (case-sensitive)
#name = name.replace("rajput", "")
#print(name)  # Output: Muhammad Waqas

# if 'waqas' in name:
#     print("true")
# else:
#     print("false")


# Define a list named Marks with mixed data types
Marks = [10, 30, 70, "please", "true"]

# Print the entire list
print(Marks)  
# Output: [10, 30, 70, "please", "true"]

# Print every second element using slicing with a step value
print(Marks[0:5:2])  
# Output: [10, 70, 'true']
# Explanation: Start at index 0, go up to index 5 (exclusive), with a step of 2.

# Print every element in reverse order using a negative step
print(Marks[::-1])  
# Output: ['true', 'please', 70, 30, 10]
# Explanation: Start from the end of the list and move backward.

# Print every second element in reverse order
print(Marks[::-2])  
# Output: ['true', 70, 10]
# Explanation: Start from the last element and pick every second element moving backward.

# Print elements starting from index 1, skipping one element at a time
print(Marks[1::2])  
# Output: [30, 'please']
# Explanation: Start at index 1 and take every second element until the end.


squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]


names = ["Alice", "Bob", "Charlie"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)  # Output: ['ALICE', 'BOB', 'CHARLIE']


numbers = [1, 2, 3, 4, 5]
even_odd = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(even_odd)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']


pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
