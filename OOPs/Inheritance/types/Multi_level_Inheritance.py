# Multilevel Inheritance

class GrandFather:
    def grand_fatherShow(self):
        print("I am a grand father")

class Father(GrandFather):
    def fatherShow(self):
        print("I am a father")

class Son(Father):
    def sonShow(self):
        print("I am a son")

son = Son()
father = Father()

son.grand_fatherShow()
son.fatherShow()
son.sonShow()

father.grand_fatherShow()