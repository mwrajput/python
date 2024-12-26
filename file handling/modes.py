file = open('youtube.txt' , 'w')

try:
    file.write("My youtube Manager Project")
finally:
    file.close()

# ==================================================== #
with open('youtube2.txt','w') as file:
    file.write("Hm sekh rhy han python")