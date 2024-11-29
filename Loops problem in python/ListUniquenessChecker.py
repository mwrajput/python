"""
List Uniqueness Checker 

check if elements in list are unique or not

if not unique exit loop


items = ["apple", "banana", "cherry", "apple", "orange"]

"""

items = ["apple", "banana", "cherry", "apple", "orange"]
    
unique_items = set()


for item in items:
    if item in unique_items:
        print("Duplicate : " ,item)
        break
    
    unique_items.add(item)

print("Unique items : " ,unique_items)