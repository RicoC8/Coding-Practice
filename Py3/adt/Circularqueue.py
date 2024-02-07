MAX_SIZE = 5 #CONSTANT MAX_SIZE <- 5
lqueue = [None for i in range(MAX_SIZE)] #DECLARE lqueue: ARRAY[0:MAX_SIZE - 1] OF INTEGER
front = 1 #DECLARE front: INTEGER
rear = 4 #DECLARE rear: INTEGER

def IsEmpty():
    if front > rear:
        return True
    else:
        return False

def IsFull():
    if (rear + 1) % MAX_SIZE == front:
        return True
    else:
        return False
    
print(IsFull())