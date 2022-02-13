class book ():
    def __init__(self, pages) :
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

obj1 = book(100)
obj2 = book(100)

print("total no of pages is :" , obj1 + obj2)