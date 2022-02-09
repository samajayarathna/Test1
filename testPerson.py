
class Person ():
    def __init__(self, fname , lname) :
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)

objStu = Student("Mice","Alice", 2021)
objStu.printname()
print("Graduation year : " ,objStu.graduationyear)
obj1 = Person("Sama","Siriwardhanage")
obj1.printname()

objStu.welcome()