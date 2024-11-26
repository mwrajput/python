
# # Set Methods in Python

# # 1. add()
# s = {1, 2, 3}
# s.add(4)
# print("add:", s)  # Output: {1, 2, 3, 4}

# # 2. remove()
# s = {1, 2, 3}
# s.remove(2)
# print("remove:", s)  # Output: {1, 3}

# # 3. discard()
# s = {1, 2, 3}
# s.discard(2)
# print("discard:", s)  # Output: {1, 3}
# s.discard(5)  # Does nothing, no error

# # 4. pop()
# s = {1, 2, 3}
# element = s.pop()
# print("pop:", element, s)  # Output: random element and remaining set

# # 5. clear()
# s = {1, 2, 3}
# s.clear()
# print("clear:", s)  # Output: set()

# # 6. copy()
# s = {1, 2, 3}
# copy_set = s.copy()
# print("copy:", copy_set)  # Output: {1, 2, 3}

# # 7. union() or |
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# result = s1.union(s2)
# print("union : ", result)  # Output: {1, 2, 3, 4, 5}
# result = s1 | s2
# print("union with |:", result)  # Output: {1, 2, 3, 4, 5}

# # 8. intersection() or &
# result = s1.intersection(s2)
# print("intersection:", result)  # Output: {3}
# result = s1 & s2
# print("intersection with &: ", result)  # Output: {3}

# # 9. difference() or -
# result = s1.difference(s2)
# print("difference:", result)  # Output: {1, 2}
# result = s1 - s2
# print("difference with -:", result)  # Output: {1, 2}

# # 10. symmetric_difference() or ^
# result = s1.symmetric_difference(s2)
# print("symmetric_difference:", result)  # Output: {1, 2, 4, 5}
# result = s1 ^ s2
# print("symmetric_difference with ^:", result)  # Output: {1, 2, 4, 5}

# # 11. issubset()
# s1 = {1, 2}
# s2 = {1, 2, 3}
# print("issubset:", s1.issubset(s2))  # Output: True
# print("issubset:", s2.issubset(s1))  # Output: False

# # 12. issuperset()
# s1 = {1, 2, 3}
# s2 = {1, 2}
# print("issuperset:", s1.issuperset(s2))  # Output: True
# print("issuperset:", s2.issuperset(s1))  # Output: False

# # 13. isdisjoint()
# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# print("isdisjoint:", s1.isdisjoint(s2))  # Output: True

# s3 = {3, 4}
# print("isdisjoint:", s1.isdisjoint(s3))  # Output: False

# # 14. frozenset()
# fset = frozenset([1, 2, 3])
# print("frozenset:", fset)  # Output: frozenset({1, 2, 3})

# # 15. len()
# s = {1, 2, 3, 4}
# print("len:", len(s))  # Output: 4

# # 16. in
# s = {1, 2, 3}
# print("in:", 2 in s)  # Output: True
# print("in:", 4 in s)  # Output: False


square = ( x**2 for x in range(10))
print(list(square))