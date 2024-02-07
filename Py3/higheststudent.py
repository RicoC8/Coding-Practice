studentNames = ['a','b','z','y']
studentScores = [90,80,70,20]

def highest(list):
    high = list[0]
    highpoint = 0
    for i in range(len(list)):
        if list[i] > high:
            high = list[i]
            highpoint = i
    return studentNames[highpoint]
def lowest(list):
    low = list[0]
    lowpoint = 0
    for i in range(len(list)):
        if list[i] < low:
            low = list[i]
            lowpoint = i
    return studentNames[lowpoint]

print(highest(studentScores))
print(lowest(studentScores))


