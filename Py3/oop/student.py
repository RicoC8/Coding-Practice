class Student:
    def __init__(self, Name, Class, Age: int, House):
        self._StudentName = Name
        self.__StudentClass = Class
        self.__StudentAge = Age
        self.__StudentHouse = House

    def displayDetails(self):
        print(f"Student's name is {self._StudentName}")
        print(f"Student's class is {self.__StudentClass}")
        print(f"Student's age is {self.__StudentAge}")
        print(f"Student's house is {self.__StudentHouse}")


student1 = Student("Russell", "JC2Z", 17, "Red")
student1.displayDetails()

class Prefect(Student):
    def __init__(self, Name, Class, Age: int, House, Rank):
        super().__init__(Name, Class, Age, House)
        self.__PrefectRank = Rank

    def displayDetails(self):
        print(self._StudentName)
        super().displayDetails()
        print(f"Student is a Prefect! Their rank is {self.__PrefectRank}")

Prefect1 = Prefect("Emil", "JC1", 17, "Green", "Councillor")
Prefect1.displayDetails()