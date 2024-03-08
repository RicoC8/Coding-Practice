class Vehicle:
    #self.__ID string
    #self.__MaxSpeed integer
    #self.__CurrentSpeed integer
    #self.__IncreaseAmount integer
    #self.__HorizontalPosition integer

    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__IncreaseAmount = IncreaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0
        
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def SetCurrentSpeed(self, NewSpeed):
        self.__CurrentSpeed = NewSpeed

    def SetHorizontalPosition(self, NewPos):
        self.__HorizontalPosition = NewPos

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
    
    def ShowDetails(self):
        print(f"Horizontal Position: {self.GetHorizontalPosition()}")
        print(f"Speed: {self.GetCurrentSpeed()}")

class Helicopter(Vehicle):
    #VerticalPosition string
    #VerticalChange integer
    #MaxHeight integer

    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__vpos = 0
        self.__vchange = VerticalChange
        self.__hmax = MaxHeight
    
    def IncreaseSpeed(self):
        self.__vpos = self.__vpos + self.__vchange
        if self.__vpos > self.__hmax:
            self.__vpos = self.__hmax
        self.SetCurrentSpeed(self.GetCurrentSpeed() + self.GetIncreaseAmount())
        self.SetHorizontalPosition(self.GetHorizontalPosition() + self.GetCurrentSpeed())

    def GetVerticalPosition(self):
        return self.__vpos

    def ShowDetails(self):
        print(f"Horizontal Position: {self.GetHorizontalPosition()}")
        print(f"Speed: {self.GetCurrentSpeed()}")
        print(f"Vertical Position: {self.GetVerticalPosition()}")

car = Vehicle("Tiger", 100, 20)
helicopter = Helicopter("Lion", 350, 40, 3, 100)
car.IncreaseSpeed()
car.IncreaseSpeed()
car.ShowDetails()
helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
helicopter.ShowDetails()