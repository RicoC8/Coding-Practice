import datetime
class Character:
    #self.Charactername string
    #self.DateofBirth date
    #self.Intelligence real
    #self.Speed integer

    def __init__(self, CName, DoB, Intel, Speed):
        self.CharacterName = CName
        self.DateOfBirth = DoB
        self.Intelligence = Intel
        self.Speed = Speed

    def GetIntelligence(self):
        return self.Intelligence

    def GetName(self):
        return self.CharacterName

    def SetIntelligence(self, NewVal):
        self.Intelligence = NewVal

    def Learn(self):
        self.Intelligence = self.Intelligence * 1.1

    def ReturnAge(self):
        return 2023 - self.DateOfBirth.year


FirstCharacter = Character('Royal', datetime.datetime(2019, 1, 1), 70, 30)

FirstCharacter.Learn()
print(FirstCharacter.GetName(), " is ", FirstCharacter.ReturnAge(), " years old, with an intelligence of ", FirstCharacter.GetIntelligence())
    
class MagicCharacter(Character):
    def __init__(self, Element, CharacterName, DateOfBirth, Intelligence, Speed):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.Element = Element

    def Learn(self):
        if self.Element == "fire" or self.Element == "water":
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.1)

FirstMagic = MagicCharacter('fire', 'Light', datetime.datetime(2018, 3, 3), 75, 22)
FirstMagic.Learn()

print(FirstMagic.GetName() ," is ", FirstMagic.ReturnAge(), " years old and has an intelligence of ", FirstMagic.GetIntelligence())