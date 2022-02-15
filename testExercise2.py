class A():
    def __init__(self) :
        self.value = 10
    
class B():
    def __init__(self, val2) :
        self.val2 = val2

    def display  (self):
        print("value is ", + self.val2.value)

a = A()
b = B(a)
b.display()