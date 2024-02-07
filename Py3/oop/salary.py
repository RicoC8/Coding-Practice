class Salary:
    def __init__(self, pay):
        self.MonthlyPay = pay

    def YearlyPay(self):
        return 12 * self.MonthlyPay
    
class Employee1:
    def __init__(self, name, sal: Salary, bonus):
        self.Name = name
        self.Salary = sal
        self.Bonus = bonus

    def TotalPay(self):
        return self.Salary.YearlyPay() + self.Bonus
    
class Employee2:
    def __init__(self, name, sal, bonus):
        self.Name = name
        self.Salary = Salary(sal)
        self.Bonus = bonus

    def TotalPay(self):
        return self.Salary.YearlyPay() + self.Bonus
    
    def __del__(self):
        print("Class of type Employee2 Deleted!")

Sal = Salary(1000)
emp1 = Employee1("Jo", Sal, 100)
    
    
emp2 = Employee2("Jo Samad", 1000, 200)


print(emp1.TotalPay())
print(emp2.TotalPay())

del(emp1)
del(emp2)




