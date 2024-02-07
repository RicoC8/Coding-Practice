MAX_SIZE = 5 #MAX_SIZE is a constant
top = -1 #DECLARE top: INTEGER
stack = [None for i in range(MAX_SIZE)] #DECLARE stack: ARRAY[0:MAX_SIZE-1]

def IsFull():
    if top == MAX_SIZE -1:
        return True
    else: 
        return False

def IsEmpty():
    if top == -1:
        return True
    else: 
        return False

def Push(item: int):
    global top
    if IsFull() == False:
        top = top + 1
        stack[top] = item
    else:
        print("stack is full!")

def Pop():
    global top
    if IsEmpty() == False:
        stack[top] = None
        top = top - 1
    else:
        print("underflow!")

def Peek():
    return stack[top]

Push(1)
Push(2)
Push(3)
Push(4)
Push(5)
Push(6)
Pop()
print(stack)
print(Peek())