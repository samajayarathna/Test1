from time import sleep


class Salary:
    def __init__(self, pay, bonus) :
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus) :
        self.name = name
        self.age = age
        self.objSalary = Salary(pay,bonus)
    
    def totalSalary(self):
        return self.objSalary.annualSalary()

empObj = Employee("sama",33, 15000, 1000)
print(empObj.totalSalary())