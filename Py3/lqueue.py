MAX_SIZE = 5 #CONSTANT MAX_SIZE <- 5
lqueue = [None for i in range(MAX_SIZE)] #DECLARE lqueue: ARRAY[0:MAX_SIZE - 1] OF INTEGER
front = 0 #DECLARE front: INTEGER
rear = -1 #DECLARE rear: INTEGER

def IsEmpty():
    if front > rear:
        return True
    else:
        return False

def IsFull():
    if rear == MAX_SIZE - 1:
        return True
    else:
        return False
def enqueue(item):
    global rear
    if IsFull() != True:   
        rear += 1
        lqueue[rear] = item
    else:
        print("FULL! Item could not be added")

def dequeue():
    global front
    if IsEmpty() is False:
        lqueue[front] = None
        front += 1
    else:
        print("Queue is EMPTY! Nothing to dequeue")

enqueue(1)
# enqueue(2)
# enqueue(3)
# enqueue(4)
# enqueue(5)
print(lqueue)
dequeue()
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
print(lqueue)  
