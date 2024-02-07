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