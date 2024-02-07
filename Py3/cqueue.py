MAX_SIZE = 5 #CONSTANT MAX_SIZE <- 5
lqueue = [None for i in range(MAX_SIZE)] #DECLARE lqueue: ARRAY[0:MAX_SIZE - 1] OF INTEGER
front = -1 #DECLARE front: INTEGER
rear = -1 #DECLARE rear: INTEGER

def IsEmpty():
    if front == -1:
        return True
    else:
        return False

def IsFull():
    if (rear + 1) % MAX_SIZE == front:
        return True
    
    else:
        return False
    
def enqueue(item):
    global rear, front
    if IsFull():
        print("FULL! Item could not be added")
    else:
        rear = (rear + 1) % MAX_SIZE
        lqueue[rear] = item
        if IsEmpty():
            front = 0
        
def dequeue():
    global front, rear
    if IsEmpty():
        print("Queue is EMPTY! Nothing to dequeue")
    else:
        lqueue[front] = None
        if front == rear:
            front = -1
        else:
            front = (front + 1) % MAX_SIZE
        
        

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
enqueue(6)

dequeue()
dequeue()
enqueue(7)
enqueue(8)

print(lqueue)
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()



print(lqueue)