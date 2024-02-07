class Overload:
    def add(self, Num1 = None, Num2 = None):
        if Num1 == None and Num2 == None:
            return Num1
        elif Num1 != None and Num2 == None:
            return Num1
        elif Num1 == None and Num2 != None:
            return Num2
        elif Num1 != None and Num2 != None:
            return Num1 + Num2
        
adding = Overload()
print(adding.add())
print(adding.add(1))
print(adding.add(None, 9))
print(adding.add(1, 9))

def add(Num1, Num2):
    return Num1 + Num2

def add(Num1, Num2, Num3):
    return Num1 + Num2 + Num3

print(add(2, 4, 8))
print(add(2, 4))