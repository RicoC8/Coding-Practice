class Character:
    #self.name = Name
    #self.xpos = Xposition
    #self.ypos = Yposition

    def __init__(self, Name, Xposition, Yposition):
        self.name = Name
        self.xpos = Xposition
        self.ypos = Yposition

    def GetXPosition(self):
        return self.xpos
    
    def GetYPosition(self):
        return self.ypos

    def SetXPosition(self, val):
        newval = self.xpos + val
        if newval > 10000:
            newval = 10000
        if newval < 0:
            newval = 0

        self.xpos = newval

    def SetYPosition(self, val):
        newval = self.ypos + val
        if newval > 10000:
            newval = 10000
        if newval < 0:
            newval = 0

        self.ypos = newval
        

    def Move(self, move):
        if move == "up":
            self.SetYPosition(10)
        elif move == "down":
            self.SetYPosition(-10)
        elif move == "right":
            self.SetXPosition(10)  
        elif move == "left":
            self.SetYPosition(-10) 
                
Jack = Character("Jack", 50, 50)

class BikeCharacter(Character):
    #self.Name = Name
    #self.Xposition = Xposition
    #self.Yposition = Yposition
    def __init__(self, Name, Xposition, Yposition):
        super().__init__(Name, Xposition, Yposition)

    def Move(self):
        

