StackVowel = [None for i in range(100)] #DECLARE StackVowel: ARRAY[0:99] OF STRING
StackConsonant = [None for i in range(100)] #DECLARE StackConsonant: ARRAY[0:99] OF STRING

VowelTop = 0 #DECLARE VowelTop: INTEGER
ConsonantTop = 0 #DECLARE ConsonantTop: INTEGER

def PushData(letter):
    global VowelTop, ConsonantTop
    vowels = ['a', 'e','i','o','u']
    isVowel = False
    for index in range(5):
        if letter == vowels[index]:
            isVowel = True
    if isVowel == True:
        if VowelTop <= 99:
            StackVowel[VowelTop] = letter
            VowelTop += 1
        else: 
            print("Vowel Stack is FULL!")
    else:
        if ConsonantTop <= 99:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop += 1
        else:
            print("Consonant Stack is Full!")

def ReadData():
    try:
        file = open("Py3/Paper_4_2023_oct_nov_32/StackData.txt", 'r')
    except FileNotFoundError:
        print("File DOES NOT EXIST YET!")
    Lines = file.readlines()
    for letter in Lines:
        PushData(letter[:1])

def PopVowel():
    global VowelTop
    if VowelTop == -1:
        return "No data"
    else:
        Data = StackVowel[VowelTop]
        StackVowel[VowelTop] = None
        StackVowel -= 1
        return Data

def PopConsonant():
    global ConsonantTop
    if ConsonantTop == -1:
        return "No data"
    else:
        Data = StackConsonant[ConsonantTop]
        StackConsonant[ConsonantTop] = None
        StackConsonant -= 1
        return Data
    
if __name__ == '__main__':
    count = 0
    outString = ''
    while count != 5:
        letterType = input("Vowel or Consonant?: ")
        if letterType == 'vowel':
            letter = PopVowel()
            outString = outString 
# ReadData()
# print(StackConsonant)
# print("---")
# print(StackVowel)

    