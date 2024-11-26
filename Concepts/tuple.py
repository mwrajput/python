tuple = (1,2,3,4,5)

print(tuple)

print(tuple + (6,7,8,9,10))

t = (10, 20, 30, 20, 40, 50)

# Count and Index
print(t.count(20))        # Output: 2
print(t.index(30))        # Output: 2

# Access and Slice
print(t[0])               # Output: 10
print(t[-1])              # Output: 50
print(t[1:4])             # Output: (20, 30, 20)

# Concatenation and Repetition
print(t + (60, 70))       # Output: (10, 20, 30, 20, 40, 50, 60, 70)
print(t * 2)              # Output: (10, 20, 30, 20, 40, 50, 10, 20, 30, 20, 40, 50)

# Membership
print(40 in t)            # Output: True
print(100 in t)           # Output: False

# Length, Max, Min
print(len(t))             # Output: 6
print(max(t))             # Output: 50
print(min(t))             # Output: 10


# l = [1, 2, 3]
# my_tuple = tuple(l)  # Built-in tuple() function
# print(my_tuple)  # Output: (1, 2, 3)

# print(type(tuple))  # Should output <class 'type'> if `tuple` is not shadowed
