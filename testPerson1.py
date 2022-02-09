class Person():
    def __init__(self, name):
        self.name= name

    def greet(self):
        return f"Hi,it's a {self.name}"

class Employee(Person):
    def __init__(self, name, jobtitle):
        super().__init__(name)
        self.jobtitle = jobtitle
    
    def display(self):
        print(self.name, self.jobtitle)

obj1 = Employee("sama","Python Developer")
obj1.display()