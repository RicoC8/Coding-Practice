def binSearch(searchElement, list):
    high = len(list) - 1
    low = 0

    while high >= low:
        mid = (high + low) // 2
 
        if list[mid] == searchElement:
            return mid
        else:
            if list[mid] > searchElement:
                high = mid - 1
            else:
                low = mid + 1

myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(binSearch(5,myList))

def binSearch_recursive(searchEm,mylist,high,low):
    mid = (high+low)//2
    if high < low:
        return -1
    else:
        if searchEm == mylist[mid]:
            return mid
        else:
            if searchEm > mylist[mid]:
                low = mid + 1
                return binSearch_recursive(searchEm,mylist,high,low)
            elif searchEm < mylist[mid]:
                high = mid - 1
                return binSearch_recursive(searchEm,mylist,high,low)
        
output = binSearch_recursive(15,myList,len(myList)-1,0)
print(output)
        
