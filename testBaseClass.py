class baseClass():
    def __init__(self, var1, var2) :
        self.var1 = var1
        self.var2 = var2

    def display(self):
        print(self.var1, self.var2)

class childClass(baseClass): 
    pass

ojb1 = childClass("variable1", "variable2")
ojb1.display()