class A ():
    def __init__(self,weight, height):
        self.weight = weight
        self.height = height

class B (A):
    def __init__(self, weight, height,age):
        super().__init__(weight, height)
        self.age = age

obj1 = B(47,145,33)
print(obj1.height,obj1.weight,obj1.age)