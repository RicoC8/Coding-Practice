array = [1,2,3,4,5,6,7,8,9,10]

def binsearch(searchElement, low, high):
    global array
    mid = (high + low)//2
    if high < low:
        return -1
    if array[mid] > searchElement:
        high = mid - 1
        return binsearch(searchElement, low, high)
    elif array[mid] < searchElement:
        low = mid + 1
        return binsearch(searchElement, low, high)
    elif array[mid] == searchElement:
        return mid
    
print(binsearch(33, 0, len(array) - 1))
print(binsearch(10, 0, len(array) - 1))
