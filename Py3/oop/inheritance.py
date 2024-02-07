class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def ShowDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def ShowDetails(self):
        super().ShowDetails()
        print(f"Salary: {self.salary}")

person1 = Person("Jake", 18)
person1.ShowDetails()

teacher1 = Teacher("Lucas", 25, 2000)
teacher1.ShowDetails()


