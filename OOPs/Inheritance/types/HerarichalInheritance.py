# Herarchical inheritance

class Father:
    def father_show(self):
        print('I am father')
        
class Boy(Father):
    def boy_show(self):
        print('I am son')

class Girl(Father):
    def girl_show(self):
        print('I am Girl')
    
    
boy1 =  Boy()
girl1 = Girl()

boy1.father_show()
girl1.father_show()
