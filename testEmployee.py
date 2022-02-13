class Employee ():
    def __init__(self , name, salary) :
        self.name = name
        self.salary = salary

    def __mul__(self, timesheets):
        print("worked for" , timesheets.days , "days")
        return self.salary * timesheets.days

class Timesheet ():
    def __init__(self, name , days) :
        self.name = name
        self.days = days

obj1 = Employee("sama", 45000)
obj2 = Timesheet("sama", 30)

print("salary is :", obj1 * obj2)