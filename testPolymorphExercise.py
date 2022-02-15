
basicSalary = 3000
class FulltimeEmployee():
    def salary(self):
        print("Fultime Employee Monthly Salary: " , basicSalary + 1500)

class ParttimeEmployee():
    def salary(self):
        print("Parttime Employee Monthly Salary : ", basicSalary)

def CalculateSalary(cal):
    cal.salary()

fulltime = FulltimeEmployee()
parttime = ParttimeEmployee()

CalculateSalary(fulltime)
CalculateSalary(parttime)
