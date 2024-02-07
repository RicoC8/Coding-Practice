class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.arr = [None for i in range(max_size)]
        self.top = -1

    def IsEmpty(self):
        if self.top == -1:

            return True
        else:
            return False
        
    def IsFull(self):
        if self.top == self.max_size - 1:
            return True
        else:
            return False
        
    def push(self,item):
        if self.IsFull != True:
            self.top += 1
            self.arr[self.top] = item
        else:
            print("Stack is FULL")
    
    def DisplayStack(self):
        print(self.arr)

mystack = Stack(3)
mystack.push(1)
mystack.push(1)
mystack.push(1)
mystack.DisplayStack()

