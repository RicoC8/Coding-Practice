size = 5
llist = [None for i in range(size)] #DECLARE llist[0:3] OF STRING
llpointer = [i+1 for i in range(size)] #DECLARE llpointer[0:3] OF INTEGER
llpointer[size-1] = -1

    

startPointer = -1 #first location. Empty when pointing to -1
heapPointer = 0 #pointing to the next available space. Full when pointing to -1

def IsEmpty():
    if startPointer == -1:
        return True
    else:
        return False

def IsFull():
    if heapPointer == -1:
        return True
    else:
        return False
    
def Add(item):
    global startPointer, heapPointer
    if not IsFull():
        tempPointer = startPointer
        startPointer = heapPointer
        heapPointer = llpointer[heapPointer]
        llist[startPointer] = item
        llpointer[startPointer] = tempPointer


def search(item):
    global startPointer, heapPointer
    found = False
    index = startPointer
    while found == False and index != heapPointer:
        if llist[index] == item:
            found = True
            return index, llpointer[index]
        else:
            index = llpointer[index]
    return index, llpointer[index]

    # for index in range(size):
    #     if llist[index] == item:
    #         return index, llpointer[index]


    
def Delete(item):
    global heapPointer
    delIndex = startPointer
    prev_index = startPointer #finds node connected before the deleted
    found = False
    while found == False and delIndex != heapPointer:
        if llist[delIndex] == item:
            found = True
        else:
            prev_index = delIndex
            delIndex = llpointer[delIndex]
    
    if found == False:
        print("You are not deleting an existing item!")
    else:          
        llpointer[delIndex] = heapPointer
        heapPointer = delIndex   
        nextLink = llpointer[prev_index]
        llpointer[prev_index] = nextLink
        

Add(10)
Add(20)
Add(30)
Add(40)
Add(50)
Delete(30)
Delete(40)


Add(60)

Add(70)

Delete(50)
Add(80)


print(llist, llpointer, heapPointer)

 