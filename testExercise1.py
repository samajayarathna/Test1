class BaseClassA ():
    def __init__(self,a ,b) :
        self.a = a
        self.b = b

class ChildClassA (BaseClassA):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def display(self):
        print(self.a, self.b, self.c)

class ChildClassB (ChildClassA):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

ojb1 = ChildClassA(100,200,300)
ojb1.display()

ojb2 =ChildClassB(1000,2000,3000,4000)
ojb2.display()