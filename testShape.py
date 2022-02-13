class Shape():
    def area(self, a, b = 0):
        if b > 0 :
            print("Area of rectangle is : ", a * b)
        else:
            print("Area of square is : ", a ** 2)

square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(2, 5)

