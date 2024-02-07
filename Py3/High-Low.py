def highest(list):
    high = list[0]
    for item in list:
        if item > high:
            high = item

    return high

def lowest(list):
    low = list[0]
    for item in list:
        if item < low:
            low = item

    return low

studentNames = ['a','b','z','y']
studentScores = [90,80,70,20]


