Dict = {
    'name' : 'Muhammad Waqas',
    'class' : 16,
    'description' : 'Hey! Muhammad Waqas'
}

# for x in Dict:
#     print(Dict[x])

# gets keys
# k = Dict.keys()
# print("Keys : \n",k)

# # gets values
# v = Dict.values()
# print("Values : \n" ,v)

# #update dictionary
# Dict['class'] = '16th'
# Dict['name'] = 'Haider'
# print("Updated Dictionary : \n",Dict)

# # remove item
# Dict.pop('description')
# print("Updated Dictionary : \n",Dict)

#get specific value
# print(Dict['name'])
# print(Dict['class'])

# copy Dictionary
# Copy_dic = Dict.copy()
# print("Copied Dictionary : \n",Copy_dic)

# print(Dict)
# print(Copy_dic)


# Copy_dic.pop('description')
# print("Updated Dictionary : \n",Copy_dic)
# print(Dict.clear())



# squared number

squared_number = {x:x**2 for x in range(5) }
print(squared_number)